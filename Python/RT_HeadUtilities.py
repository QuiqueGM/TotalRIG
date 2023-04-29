import RiggingTools
import RT_ErrorsHandler as RTeh
import RT_Utils as utils
import RT_GlobalVariables as RTvars
import RT_ChainTools
import maya.cmds as cmds


def createHead():
    utils.printHeader('CREATING HEAD')
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    jointsToMirror = []
    centralJoints = []
    
    for s in sel:
        if utils.getSideFromBone(s) == '':
            centralJoints.append(s)
        else:
            jointsToMirror.append(s)
    
    for j in jointsToMirror:
        RT_ChainTools.createChainSystemWithMirror(j)
        parentJointAndOffset(j)
        
    for c in centralJoints:
        RT_ChainTools.connectChainSystem(c)
        parentJointAndOffset(c)

    try:
        side = '_' + utils.getSideFromBone(jointsToMirror[0])
        newSide = '_R_' if side == '_L_' else '_L_'
    except:
        return
    
    for j in jointsToMirror:
        jnt = j.replace(side, newSide)
        parentJointAndOffset(jnt)
    
    if cmds.checkBox( 'SquashAndStretchCB', q=True, v=True ):
        createSquashAndStretch()
        
    if cmds.checkBox( 'CreateAndConnectEyesCB', q=True, v=True ):
        RT_EyesController.createEyesController()



def parentJointAndOffset(jnt):
    cmds.parent( jnt, 'JNT__Head' )
    cmds.parent( 'OFFSET' + jnt[3:], 'CTRL__Head' )



def createSquashAndStretch():
    cmds.select( 'CTRL__Head' )
    cmds.setAttr( 'CTRL__Head.scaleX', k=False, l=False, cb=False )
    cmds.setAttr( 'CTRL__Head.scaleY', k=False, l=False, cb=False )
    cmds.setAttr( 'CTRL__Head.scaleZ', k=False, l=False, cb=False )
    cmds.addAttr( ln='SquashStretch', nn='Squash and Stretch', at='float', k=True, dv=0, min=-100, max=100 )
    SS_Remap = 'CTRL__Head_SS_Remap'
    cmds.shadingNode( 'remapValue', au=True, n=SS_Remap )
    cmds.setAttr( SS_Remap + '.inputMin', -100 )
    cmds.setAttr( SS_Remap + '.inputMax', 100 )
    cmds.setAttr( SS_Remap + '.outputMin', 0 )
    cmds.setAttr( SS_Remap + '.outputMax', 2 )
    cmds.connectAttr( 'CTRL__Head.SquashStretch', SS_Remap + '.inputValue' )
    cmds.connectAttr( SS_Remap + '.outValue', 'CTRL__Head.scaleY' )
    SS_Reverse = 'CTRL__Head_SS_Reverse'
    cmds.shadingNode( 'reverse', au=True, n=SS_Reverse )
    cmds.connectAttr( SS_Remap + '.outValue', SS_Reverse + '.inputX' )
    SS_PlusMinus = 'CTRL__Head_SS_PlusMinus'
    cmds.shadingNode( 'plusMinusAverage', au=True, n=SS_PlusMinus )
    cmds.setAttr( SS_PlusMinus + '.input1D[0]', 1)
    cmds.connectAttr( SS_Reverse + '.outputX', SS_PlusMinus + '.input1D[1]' )
    cmds.connectAttr( SS_PlusMinus + '.output1D', 'CTRL__Head.scale.scaleX' )
    cmds.connectAttr( SS_PlusMinus + '.output1D', 'CTRL__Head.scale.scaleZ' )
    cmds.select( d=True )



def createEyesController():
    utils.printHeader('CREATING EYES CONTROLLER')
    
    #############################
    utils.printSubheader('Mirroring eyes')
    eyes = []
    distance = cmds.floatSliderGrp( 'EyesControllerDist', q=True, v=True )
    distance = 0.8
    addEye('JNT__L_Eye', eyes)
    cmds.select( eyes[0] )
    cmds.mirrorJoint( myz=True, mb=True, sr=('_L_', '_R_') )
    addEye('JNT__R_Eye', eyes)
    
    cmds.setAttr( 'JNT__R_Eye.jointOrientX', -90 )
    cmds.setAttr( 'JNT__R_Eye.jointOrientY', -90 )

    #############################
    utils.printSubheader('Creating controllers')
    for e in eyes:
        cmds.select( e )
        ctrl = RTctrl.createController('Circle', utils.getColorFromSide(e[0]), getEyesRadius(), 'World', '', '', False, False)
        cmds.select ( ctrl[1] + 'Shape.cv[0:7]' )
        cmds.rotate( 0, '90deg', 0 )
        
    cmds.select( d=True )
    JNT_Eyes = 'JNT__Eyes'
    cmds.duplicate( eyes[0], n=JNT_Eyes, rc=True )
    cmds.setAttr( JNT_Eyes + '.translateX', 0 )
    cmds.select( JNT_Eyes )
    ctrl = RTctrl.createController('Circle', utils.getColorFromSide(JNT_Eyes[0]), getEyesRadius(), 'World', '', '', False, False)
    cmds.select ( ctrl[1] + 'Shape.cv[0:7]' )
    cmds.rotate( 0, '90deg', 0 )
    cmds.scale( 2.65, 1.6, 1 )
    cmds.select( d=True )
    cmds.delete( JNT_Eyes )
    cmds.parent( 'OFFSET__L_Eye', ctrl[1] )
    cmds.parent( 'OFFSET__R_Eye', ctrl[1] )
    cmds.setAttr( ctrl[0] + '.translateZ', distance + cmds.getAttr( 'JNT__L_Eye.translateZ' ) )

    #############################
    utils.printSubheader('Connecting eyes')
    connectingEyes('CTRL__L_Eye', 'LOC__L_Eye', eyes[0])
    connectingEyes('CTRL__R_Eye', 'LOC__R_Eye', eyes[1])
    cmds.parent( 'OFFSET__Eyes', 'CTRL__Master' )
    
    #############################    
    utils.printSubheader('Locking and hidding unused attributes')
    utils.lockAndHideAttribute('CTRL__Eyes', False, True)    
    utils.lockAndHideAttribute('CTRL__L_Eye', False, True)
    utils.lockAndHideAttribute('CTRL__R_Eye', False, True)
    
    RT_SpaceSwitch.createSpaceSwitch('HeadSpace', ctrl[1], 'CTRL__Master', 'CTRL__Head', 'Parent')
    cmds.select( d=True )



def addEye(eye, eyes):
    cmds.select( eye )
    sel = cmds.ls(sl=True)
    eyes.append(sel)



def getEyesRadius():
    return cmds.getAttr( 'JNT__L_Eye.translateX' ) * cmds.floatSliderGrp( 'EyesPupillaryDist', q=True, v=True )


def connectBlendShapes():
    utils.printHeader('CONNECTING BLEND SHAPES')
    connectEyeBlendShape('CTRL__L_Eye', 0, 'L_Eye_Opened', 0, 'L_Eye_Closed', 0)
    connectEyeBlendShape('CTRL__L_Eye', 10, 'L_Eye_Opened', 1, 'L_Eye_Closed', 0)
    connectEyeBlendShape('CTRL__L_Eye', -10, 'L_Eye_Opened', 0, 'L_Eye_Closed', 1)
    connectEyeBlendShape('CTRL__R_Eye', 0, 'R_Eye_Opened', 0, 'R_Eye_Closed', 0)
    connectEyeBlendShape('CTRL__R_Eye', 10, 'R_Eye_Opened', 1, 'R_Eye_Closed', 0)
    connectEyeBlendShape('CTRL__R_Eye', -10, 'R_Eye_Opened', 0, 'R_Eye_Closed', 1)
    cmds.setAttr( 'CTRL__L_Eye.Eye', 0 )
    cmds.setAttr( 'CTRL__R_Eye.Eye', 0 )



def connectEyeBlendShape(eye, attrValue, bs1, bs1Value, bs2, bs2Value):
    cmds.setAttr( eye + '.Eye', attrValue )
    cmds.setAttr( 'BS__Eyes.' + bs1, bs1Value )
    cmds.setAttr( 'BS__Eyes.' + bs2, bs2Value )
    cmds.setDrivenKeyframe( 'BS__Eyes.' + bs1, cd=eye + '.Eye' )
    cmds.setDrivenKeyframe( 'BS__Eyes.' + bs2, cd=eye + '.Eye' )



def connectingEyes(ctrl, loc, eye):
    locator = cmds.spaceLocator( n=loc )
    cmds.editDisplayLayerMembers( 'HELPERS', locator, nr=True )
    utils.setLocalScaleLocators(locator[0])
    cmds.xform( locator[0], m=cmds.xform( eye, q=True, m=True, ws=True ), ws=True )
    cmds.parent( locator, 'CTRL__Head' )
    cmds.aimConstraint( ctrl, eye, n=utils.getConstraint('Aim', eye[0][3:]), mo=False, w=1, aim=(0, 0, 1), u=(0, 1, 0), wut='objectrotation', wu=(0, 1, 0), wuo=locator[0] )
    cmds.pointConstraint( locator, eye, n=utils.getConstraint('Point', eye[0][3:]) )
    cmds.parent( eye, 'JNT__Head' )



def deleteEyesController():
    utils.printHeader('DELETING EYES CONTROLLERS')
    itemToDelete = ['JNT__R_Eye', 'CONST__L_Eye__AIM', 'CONST__L_Eye__POINT', 'OFFSET__Eyes', 'LOC__L_Eye', 'LOC__R_Eye', 'SPSW_PARENT__Eyes_HEAD', 'SPSW_PARENT__Eyes_MASTER']
    for i in itemToDelete:
        try:
            cmds.delete( i )
        except:
            pass

    cmds.parent( 'JNT__L_Eye', w=True )




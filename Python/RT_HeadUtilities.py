import RiggingTools as RT
import RT_ErrorsHandler as RTeh
import RT_Utils as utils
import RT_GlobalVariables as RTvars
import RT_ChainTools
import maya.cmds as cmds



def drawUI():
    RT.toolHeader('headControllerTab', '---------   HEAD CONTROLLER  ---------')
    RT.subHeader(1, 'EYES', 5)
    RT.createFloarSliderGroup('EyesPupillaryDist', 'Radius factor scale      ', 0.85, 0.75, 0.95, 0.01)
    RT.createFloarSliderGroup('EyesControllerDist', 'Distance from Eyes      ', 1.0, 0.01, 1.5, 0.05)       
    RT.subHeader(7, 'OPTIONS', 5)
    RT.createCheckbox(0.1, 'CreateAndConnectEyesCB', 'Create and connect Eyes', enableCreateEyes, True, True)
    RT.createCheckbox(0.1, 'ConnectTongueCB', 'Connect tongue', RT.emptyCallback, True, True)
    RT.createCheckbox(0.1, 'SquashAndStretchCB', 'Create Squash and Stretch', RT.emptyCallback, True, True)
    RT.createCheckbox(0.1, 'BlendShapesCB', 'Create Blend Shapes', enableBlendShapes, True, True)
    RT.createCheckbox(0.2, 'EyesCB', 'Eyes', RT.emptyCallback, True, True)
    RT.verticalSpace(2)
    RT.createButtonAction(10,'', 'Create Head', createHead, False)
    RT.createSpaceForUtilities('---------   UTILITIES  ---------')
    RT.createTwoButtonsAction(7,'cec', 'Create Eyes Controller', createEyesController, 'dec', 'Delete Eyes Controllers', deleteEyesController, False)
    RT.createButtonAction(3,'', 'Create Squash And Stretch', createSquashAndStretch, True)



def enableCreateEyes(*args):
    value = cmds.checkBox( 'CreateAndConnectEyesCB', q=True, v=True )
    cmds.floatSliderGrp( 'EyesPupillaryDist', edit=True, en=value )
    cmds.floatSliderGrp( 'EyesControllerDist', edit=True, en=value )



def enableBlendShapes(*args):
    value = cmds.checkBox( 'BlendShapesCB', q=True, v=True )
    cmds.checkBox( 'EyesCB', edit=True, en=value )



### EYES & HEAD



def connectBlendShapes(*args):
    RT_HeadUtilities.connectBlendShapes()

def createSquashAndStretch(*args):
    RT_HeadUtilities.createSquashAndStretch()







def createHead():
    utils.printHeader('CREATING HEAD')
    chains = RT_ChainTools.createChainSystem(True)
    
    for c in chains:
        cmds.parent( c, 'JNT__Head' )
        offset = 'OFFSET' + c[3:]
        utils.lockAndHideOffset(offset, False)
        cmds.parent( 'OFFSET' + c[3:], 'CTRL__Head' )
        utils.lockAndHideOffset(offset, True)

    if cmds.checkBox( 'ConnectTongueCB', q=True, v=True ):
        connectTongue()

    if cmds.checkBox( 'CreateAndConnectEyesCB', q=True, v=True ):
        RT_EyesController.createEyesController()

    if cmds.checkBox( 'SquashAndStretchCB', q=True, v=True ):
        createSquashAndStretch()

    if cmds.checkBox( 'BlendShapesCB', q=True, v=True ):
        createBlendShapes()





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





### EYES

def createEyesController(*args):
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
        cmds.select ( ctrl[1] + '_Shape.cv[0:7]' )
        cmds.rotate( 0, '90deg', 0 )
        
    cmds.select( d=True )
    JNT_Eyes = 'JNT__Eyes'
    cmds.duplicate( eyes[0], n=JNT_Eyes, rc=True )
    cmds.setAttr( JNT_Eyes + '.translateX', 0 )
    cmds.select( JNT_Eyes )
    ctrl = RTctrl.createController('Circle', utils.getColorFromSide(JNT_Eyes[0]), getEyesRadius(), 'World', '', '', False, False)
    cmds.select ( ctrl[1] + '_Shape.cv[0:7]' )
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



def connectingEyes(ctrl, loc, eye):
    locator = cmds.spaceLocator( n=loc )
    cmds.editDisplayLayerMembers( 'HELPERS', locator, nr=True )
    utils.setLocalScaleLocators(locator[0])
    cmds.xform( locator[0], m=cmds.xform( eye, q=True, m=True, ws=True ), ws=True )
    cmds.parent( locator, 'CTRL__Head' )
    cmds.aimConstraint( ctrl, eye, n=utils.getConstraint('Aim', eye[0][3:]), mo=False, w=1, aim=(0, 0, 1), u=(0, 1, 0), wut='objectrotation', wu=(0, 1, 0), wuo=locator[0] )
    cmds.pointConstraint( locator, eye, n=utils.getConstraint('Point', eye[0][3:]) )
    cmds.parent( eye, 'JNT__Head' )



def deleteEyesController(*args):
    utils.printHeader('DELETING EYES CONTROLLERS')
    itemToDelete = ['JNT__R_Eye', 'CONST__L_Eye__AIM', 'CONST__L_Eye__POINT', 'OFFSET__Eyes', 'LOC__L_Eye', 'LOC__R_Eye', 'SPSW_PARENT__Eyes_HEAD', 'SPSW_PARENT__Eyes_MASTER']
    for i in itemToDelete:
        try:
            cmds.delete( i )
        except:
            pass

    cmds.parent( 'JNT__L_Eye', w=True )

import RiggingTools
import RT_ErrorsHandler as RTeh
import RT_Utils as utils
import RT_GlobalVariables as RTvars
import RT_ChainTools
import maya.cmds as cmds


def createHead():
    utils.printHeader('CREATING HEAD')
    utils.printSubheader('WIP...')



def createEyesController():
    utils.printHeader('CREATING EYES CONTROLLER')
    eyes = []
    ctrlSize = 0.04
    distance = cmds.floatSliderGrp( 'EyesControllerDist', q=True, v=True )
    
    addEye('JNT__L_Eye', eyes)
    cmds.select( eyes[0] )
    cmds.mirrorJoint( myz=True, mb=True, sr=('_L_', '_R_') )
    addEye('JNT__R_Eye', eyes)

    cmds.setAttr( 'JNT__R_Eye.jointOrientX', -90 )
    cmds.setAttr( 'JNT__R_Eye.jointOrientY', -90 )
    
    for e in eyes:
        cmds.select( e )
        ctrl = RTctrl.createController('Circle', utils.getColorFromSide(e), ctrlSize, 'World', '', '')
        cmds.select ( ctrl[1] )
        cmds.addAttr( ln='Eye', at="float", k=True, dv=0, min=-10, max=10 )
        cmds.select ( ctrl[1] + 'Shape.cv[0:7]' )
        cmds.rotate( 0, '90deg', 0 )
    
    cmds.select( d=True )
    JNT_Eyes = 'JNT__Eyes'
    cmds.duplicate( eyes[0], n=JNT_Eyes, rc=True )
    cmds.setAttr( JNT_Eyes + '.translateX', 0 )
    cmds.select( JNT_Eyes )
    ctrl = RTctrl.createController('Circle', utils.getColorFromSide(JNT_Eyes), ctrlSize, 'World', '', '')
    cmds.select ( ctrl[1] + 'Shape.cv[0:7]' )
    cmds.rotate( 0, '90deg', 0 )
    cmds.scale( 2.65, 1.6, 1 )
    cmds.select( d=True )
    cmds.delete( JNT_Eyes )
    cmds.parent( 'OFFSET__L_Eye', ctrl[1] )
    cmds.parent( 'OFFSET__R_Eye', ctrl[1] )
    cmds.setAttr( ctrl[0] + '.translateZ', distance )
    
    connectingEyes('CTRL__L_Eye', 'LOC__L_Eye', eyes[0])
    connectingEyes('CTRL__R_Eye', 'LOC__R_Eye', eyes[1])
    
    if cmds.checkBox( 'UseBlendShapesCB', q=True, v=True ):
        connectBlendShapes()
        
    if cmds.checkBox( 'UseHeadSpaceSwitchCB', q=True, v=True ):
        RT_SpaceSwitch.createSpaceSwitch('HeadSpace', ctrl[1], 'CTRL__Master', 'CTRL__Head')
    
    cmds.select( d=True )



def addEye(eye, eyes):
    cmds.select( eye )
    sel = cmds.ls(sl=True)
    eyes.append(sel)



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
    utils.setLocalScaleLocators(locator[0])
    cmds.xform( locator[0], m=cmds.xform( eye, q=True, m=True, ws=True ), ws=True )
    cmds.parent( locator, 'JNT__Head' )
    cmds.aimConstraint( ctrl, eye, mo=False, w=1, aim=(0, 0, 1), u=(0, 1, 0), wut='objectrotation', wu=(0, 1, 0), wuo=locator[0] )
    cmds.parent( eye, 'JNT__Head' )
	

def createSquashAndStretch(*args):
    utils.printHeader('createSquashAndStretch')
    utils.printSubheader('WIP...')

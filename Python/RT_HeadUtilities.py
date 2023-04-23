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
    ctrlSize = 0.08
    distance = cmds.floatSliderGrp( 'EyesControllerDist', q=True, v=True )
    
	cmds.select( 'JNT__L_Eye' )
    sel = cmds.ls(sl=True)
    eyes.append(sel)

    cmds.select( eyes[0] )
    cmds.mirrorJoint( myz=True, mb=True, sr=('_L_', '_R_') )
	
	cmds.select( 'JNT__R_Eye' )
    sel = cmds.ls(sl=True)
    eyes.append(sel)

    cmds.setAttr( 'JNT__R_Eye.jointOrientX', 90 )
    cmds.setAttr( 'JNT__R_Eye.jointOrientY', 90 )
    
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
    cmds.select ( ctrl[1] + 'Shape.cv[0:6]' )
    cmds.rotate( 0, '90deg', 0 )
    cmds.scale( 2, 1.5, 1 )
    cmds.select( d=True )
    cmds.delete( JNT_Eyes )
    cmds.parent( 'OFFSET__L_Eye', ctrl[1] )
    cmds.parent( 'OFFSET__R_Eye', ctrl[1] )
    cmds.setAttr( ctrl[0] + '.translateZ', distance )

    locator = cmds.spaceLocator( n='LOC__L_Eye' )
    utils.setLocalScaleLocators(locator[0])
    cmds.xform( locator[0], m=cmds.xform( eye, q=True, m=True, ws=True ), ws=True )
    cmds.parent( locator, 'JNT__Head' )
    cmds.aimConstraint( 'CTRL__L_Eye', eyes[0], mo=False, w=1, aim=(0, 0, 1), u=(0, 1, 0), wut='objectrotation', wu=(0, 1, 0), wuo=locator[0] )
    cmds.parent( eye, 'JNT__Head' )
	
	locator = cmds.spaceLocator( n='LOC__L_Eye' )
    utils.setLocalScaleLocators(locator[0])
    cmds.xform( locator[0], m=cmds.xform( eye, q=True, m=True, ws=True ), ws=True )
    cmds.parent( locator, 'JNT__Head' )
    cmds.aimConstraint( 'CTRL__L_Eye', eyes[0], mo=False, w=1, aim=(0, 0, 1), u=(0, 1, 0), wut='objectrotation', wu=(0, 1, 0), wuo=locator[0] )
    cmds.parent( eye, 'JNT__Head' )
	
    cmds.select( d=True )



def createBlendShapes(*args):
    utils.printHeader('createBlendShapes')
    utils.printSubheader('WIP...')

def connectBlendShapes(*args):
    utils.printHeader('connectBlendShapes')
    utils.printSubheader('WIP...')

def createSquashAndStretch(*args):
    utils.printHeader('createSquashAndStretch')
    utils.printSubheader('WIP...')

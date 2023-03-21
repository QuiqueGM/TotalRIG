import RiggingTools
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Controllers as RTctrl
import RT_Utils as utils
import RT_ChainTools
import RT_SpaceSwitch
import maya.cmds as cmds
import maya.mel as mel
import RT_Rename


def createSimpleJoint(orientation, name):
    sel = cmds.ls(sl=True)
    newJoint = cmds.joint( n=name, p=(0, 0, 0) )
    
    if len(sel) > 0:
        cmds.setAttr( newJoint + '.translateX', 0 )
        cmds.setAttr( newJoint + '.translateY', 0 )
        cmds.setAttr( newJoint + '.translateZ', 0 )
        cmds.parent( newJoint, w=True )
    if orientation=='ZUp':
        cmds.setAttr( newJoint + '.rotateX', -90 )
        cmds.setAttr( newJoint + '.rotateY', -90 )
        
    cmds.setAttr( newJoint + '.radius', 2 )
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.editDisplayLayerMembers( 'JOINTS', newJoint, nr=True )
        


def rotateAndOrientSimpleChainZUp():
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return

    for s in sel:
        cmds.setAttr( s + '.rotateX', -90 )
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        endJoint = cmds.listRelatives( s, c=True)
        cmds.setAttr( endJoint[0] + '.jointOrientX', 0 )
        cmds.setAttr( endJoint[0] + '.jointOrientY', 0 )
        cmds.setAttr( endJoint[0] + '.jointOrientZ', 0 )   



def orientSimpleChain():
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    for s in sel:
        cmds.select( s )
        cmds.makeIdentity( apply=True )
        cmds.joint (e=True, oj='xzy', sao='zup', ch=True, zso=True)
        last_jnt = cmds.listRelatives(allDescendents=True, type='joint')[0]
        cmds.joint (last_jnt, e=True, oj='none', ch=True, zso=True)



def orientEndJoint():
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    for s in sel:
        cmds.select( s )
        last_jnt = cmds.listRelatives( ad=True, type='joint')[0]
        cmds.joint (last_jnt, e=True, oj='none', ch=True, zso=True)



def localRotationAxes():
    sel = cmds.listRelatives( ad=True, type='joint')
    try:
        sel.extend(cmds.ls(sl=True))        
    except:
        sel = cmds.ls( sl=True )

    for i in sel:
        value = (cmds.getAttr( i + '.displayLocalAxis') + 1) % 2
        cmds.setAttr( i + '.displayLocalAxis', value )



def jointSize(size):
    s = cmds.jointDisplayScale( q=True )
    s += size
    cmds.jointDisplayScale( s )



def handleOffset(state):
    sel = cmds.ls(sl=True)
    for s in sel:
        cmds.select( s )
        utils.lockAndHideOffset('null', state, True)
        cmds.select( d=True )



def convertIKtoObject():
    utils.printHeader('CHANGING IK WORLD TO OBJECT')
    utils.printSubheader('WIP...')      
    


def IKFKSnap():
    utils.printHeader('SNAP IK /FK')
    utils.printSubheader('WIP...')
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



def createRibbonJoints():
    for x in range(4):
        name = 'JNT__' + RTvars.bodyBones[x]
        newJoint = cmds.joint( n = name, p=(0, 0, 0) )
        cmds.select( d=True )
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



def createRoot():
    utils.printHeader('CREATING ROOT')
    cmds.select( 'JNT__Spine' )
    root = RTctrl.createController('Circle', (0, 0.5, 1), 1, 'Object', 'Spine', 'Root')
    cmds.select( root[1] + '_Shape.cv[0:7]' )
    cmds.rotate(  0, '90deg', 0 )
    cmds.select( d=True )
    cmds.parent( 'OFFSET__Spine', 'OFFSET__Chest', 'CTRL__Root' )
    cmds.parent( 'OFFSET__Spine_Chest__CENTRAL', 'GRP_LOC__Spine_Chest', 'CTRL__Root' )

    cmds.parent( 'OFFSET__Root', 'CTRL__Master' )
    cmds.select( 'CTRL__Master' )
    
    for n in RTvars.attributes:
        cmds.setAttr( 'CTRL__Master' + n, k=True, l=False )
        
    cmds.select( d=True )
   


def connectLegs():
    utils.printHeader('CONNECTING LEGS')

    if getTypeOfLimb('OFFSET__L_HipHead'):
        parentLimbs('HipHead', 'Spine')
    else:
        parentLimbs('Hip', 'Spine')
                
    createSideGroup('LEG__L', '__L_', RTvars.sideGroupLegs)
    createSideGroup('LEG__R', '__R_', RTvars.sideGroupLegs)

    result = cmds.confirmDialog( t='Space Switch', m='Do you want to create an <b>Point/Orient</b> space switch between both <b>Back Legs</b> and the <b>Spine</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName )
    if result == 'Yes':
        if getTypeOfLimb('JNT__L_HipHead'):
            switchSpaceLimbs('Hip', 'HipHead', 'SpineSpace')
        else:
            switchSpaceLimbs('UpperLeg', 'Hip', 'SpineSpace')             
    
    cmds.select( d=True )



def parentLimbs(child, source):
    for side in RTvars.sides:
        utils.lockAndHideOffset('OFFSET__' + side + child, False)
        cmds.parent('OFFSET__' + side + child, 'CTRL__' + source)
        cmds.parent('JNT__' + side + child, 'JNT__' + source)



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
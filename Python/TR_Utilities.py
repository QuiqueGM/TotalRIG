import TotalRig as TR
import TR_GlobalVariables as TRvars
import TR_ErrorsHandler as TReh
import TR_Controllers as TRctrl
import TR_Utils as utils
import TR_ChainTools
import TR_SpaceSwitch
import maya.cmds as cmds
import maya.mel as mel
import TR_Rename
from functools import partial


def drawUI():
    TR.toolHeader('utilitiesTab', '---------   UTILITIES  ---------')
    TR.verticalSpace(5)
    w = TR.winWidth*0.9
    h = 30
    TR.createFourButtonUtility('Joint - World', partial(createSimpleJoint, 'World', ''), 'Joint - Z Up', partial(createSimpleJoint, 'ZUp', ''), 'Ribbon joints', createRibbonJoints, ' -- EMPTY -- ', TR.emptyCallback, w, h)
    TR.createFourButtonUtility('Orient Simple Chain', rotateAndOrientSimpleChainZUp, 'Orient Chain', orientSimpleChain, 'Orient End Joint', orientEndJoint, ' Show/Hide LRA ', localRotationAxes, w, h)
    TR.createFourButtonUtility('Create Root', createRoot, 'Connect Legs', connectLegs, 'Connect Arms', connectArms, 'Connect Wings', connectWings, w, h)
    TR.createDoubleButtonUtility('Delete References', deleteReferences, 'Delete Blend Shape Targets', deleteBSTargets, w, h)
    TR.createDoubleButtonUtility('Bind skin', bindSkinMesh, 'Remove END influences', removeInfluences, w, h)
    TR.createSpaceForUtilities('---------   UTILITIES  ---------')
    TR.verticalSpace(5)
    TR.createDoubleButtonUtility('Decrease Joint Size', partial(jointSize, -0.2), 'Increase Joint Size', partial(jointSize, 0.2), w, h)
    TR.createFourButtonUtility('Reset controllers', resetControllers, 'Rename Chains', renameChains, 'Unlock OFFSET', partial(handleOffset, False), 'Lock OFFSET', partial(handleOffset, True), w, h)



def createSimpleJoint(orientation, name, *args):
    sel = cmds.ls(sl=True)
    if name == '':
        name = getRandomName()
        
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



def createRibbonJoints(*args):
    for x in range(4):
        name = 'JNT__' + TRvars.bodyBones[x]
        newJoint = cmds.joint( n = name, p=(0, 0, 0) )
        cmds.select( d=True )
        cmds.editDisplayLayerMembers( 'JOINTS', newJoint, nr=True )
        


def rotateAndOrientSimpleChainZUp(*args):
    sel = cmds.ls(sl=True)
    if TReh.GetNoSelectionException(sel): return

    for s in sel:
        cmds.setAttr( s + '.rotateX', -90 )
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        endJoint = cmds.listRelatives( s, c=True)
        cmds.setAttr( endJoint[0] + '.jointOrientX', 0 )
        cmds.setAttr( endJoint[0] + '.jointOrientY', 0 )
        cmds.setAttr( endJoint[0] + '.jointOrientZ', 0 )   



def orientSimpleChain(*args):
    sel = cmds.ls(sl=True)
    if TReh.GetNoSelectionException(sel): return
    
    for s in sel:
        cmds.select( s )
        cmds.makeIdentity( apply=True )
        cmds.joint (e=True, oj='xzy', sao='zup', ch=True, zso=True)
        last_jnt = cmds.listRelatives(allDescendents=True, type='joint')[0]
        cmds.joint (last_jnt, e=True, oj='none', ch=True, zso=True)



def orientEndJoint(*args):
    sel = cmds.ls(sl=True)
    if TReh.GetNoSelectionException(sel): return
    
    for s in sel:
        cmds.select( s )
        last_jnt = cmds.listRelatives( ad=True, type='joint')[0]
        cmds.joint (last_jnt, e=True, oj='none', ch=True, zso=True)



def localRotationAxes(*args):
    sel = cmds.listRelatives( ad=True, type='joint')
    try:
        sel.extend(cmds.ls(sl=True))        
    except:
        sel = cmds.ls( sl=True )

    for i in sel:
        value = (cmds.getAttr( i + '.displayLocalAxis') + 1) % 2
        cmds.setAttr( i + '.displayLocalAxis', value )



def createRoot(*args):
    utils.printHeader('CREATING ROOT')
    cmds.select( 'JNT__Spine' )
    root = TRctrl.createController('Circle', (0, 0.5, 1), 1, 'Object', 'Spine', 'Root')
    cmds.select( root[1] + '_Shape.cv[0:7]' )
    cmds.rotate(  0, '90deg', 0 )
    cmds.select( d=True )
    cmds.parent( 'OFFSET__Spine', 'OFFSET__Chest', 'CTRL__Root' )
    cmds.parent( 'OFFSET__Spine_Chest__CENTRAL', 'GRP_LOC__Spine_Chest', 'CTRL__Root' )

    cmds.parent( 'OFFSET__Root', 'CTRL__Master' )
    cmds.select( 'CTRL__Master' )
    
    for n in TRvars.attributes:
        cmds.setAttr( 'CTRL__Master' + n, k=True, l=False )
        
    cmds.select( d=True )
   


def connectLegs(*args):
    utils.printHeader('CONNECTING LEGS')

    if getTypeOfLimb('OFFSET__L_HipHead'):
        parentLimbs('HipHead', 'Spine')
    else:
        parentLimbs('Hip', 'Spine')
                
    createSideGroup('LEG__L', '__L_', TRvars.sideGroupLegs)
    createSideGroup('LEG__R', '__R_', TRvars.sideGroupLegs)

    result = cmds.confirmDialog( t='Space Switch', m='Do you want to create an <b>Point/Orient</b> space switch between both <b>Back Legs</b> and the <b>Spine</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=TRvars.winName )
    if result == 'Yes':
        if getTypeOfLimb('JNT__L_HipHead'):
            switchSpaceLimbs('Hip', 'HipHead', 'SpineSpace')
        else:
            switchSpaceLimbs('UpperLeg', 'Hip', 'SpineSpace')             
    
    cmds.select( d=True )



def connectArms(*args):
    utils.printHeader('CONNECTING ARMS')
    
    if getTypeOfLimb('OFFSET__L_ClavicleHead'):
        parentLimbs('ClavicleHead', 'Chest')
    else:
        parentLimbs('Clavicle', 'Chest')
            
    createSideGroup('ARM__L', '__L_', TRvars.sideGroupArms)
    createSideGroup('ARM__R', '__R_', TRvars.sideGroupArms)

    result = cmds.confirmDialog( t='Space Switch', m='Do you want to create an <b>Point/Orient</b> space switch between both <b>Front Legs / Arms</b> and the <b>Chest</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=TRvars.winName )
    if result == 'Yes':
        if getTypeOfLimb('JNT__L_ClavicleHead'):
            switchSpaceLimbs('Clavicle', 'ClavicleHead', 'ChestSpace')
        else:
            switchSpaceLimbs('Arm', 'Clavicle', 'ChestSpace')

    cmds.select( d=True )



def parentLimbs(child, source):
    for side in TRvars.sides:
        utils.lockAndHideOffset('OFFSET__' + side + child, False)
        cmds.parent('OFFSET__' + side + child, 'CTRL__' + source)
        cmds.parent('JNT__' + side + child, 'JNT__' + source)



def switchSpaceLimbs(ctrl, jnt, nameSpace):
    for side in TRvars.sides:
        utils.lockAndHideOffset('OFFSET__' + side + ctrl, False)
        TR_SpaceSwitch.createSpaceSwitch(nameSpace, 'CTRL__' + side + ctrl, 'CTRL__Master', 'JNT__' + side + jnt, 'PointOrient')
        utils.lockAndHideOffset('OFFSET__' + side + jnt, True)



def getTypeOfLimb(ctrl):
    try:
        cmds.select( ctrl )
        return True
    except:
        return False



def createSideGroup(name, side, offsets):
    sGroup = cmds.group( n=name, em=1 )
    utils.hideAttributes(sGroup, 1)
    
    for o in offsets:
        try:
            cmds.parent( 'OFFSET' + side + o, sGroup )
        except:
            pass
        
    cmds.parent( sGroup, 'CTRL__Master' )



def connectWings(*args):
    utils.printHeader('CONNECTING WINGS')
    
    offsets = getWingRoot(cmds.ls('OFFSET__L*_Wing*', 'OFFSET__R*_Wing*'))
    for o in offsets:
        utils.lockAndHideOffset(o, False)
        cmds.parent(o, 'CTRL__Chest')
        
    joints = getWingRoot(cmds.ls('JNT__L*_Wing*', 'JNT__R*_Wing*'))
    for j in joints:
        cmds.parent(j, 'JNT__Chest')

    result = cmds.confirmDialog( t='Space Switch', m='Do you want yo create an <b>Point/Orient</b> space switch between the <b>Wings</b> and the <b>Chest</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=TRvars.winName )
    if result == 'Yes':
        try:
            for o in offsets:
                TR_SpaceSwitch.createSpaceSwitch('ChestSpace', 'CTRL' + o[6:], 'CTRL__Master', 'CTRL__Chest', 'PointOrient')
        except:
            print ('It has not been possible to create the space switch. Probably the name of the winds don\'t match with a standard name')
    
    cmds.select( d=True )



def getWingRoot(list):
    roots = []
    for o in list:
        if cmds.listRelatives( o, p=True ) == None:
            roots.append(o)
    
    return roots



def deleteReferences(*args):
    utils.printHeader('DELETING REFERENCES and UNUSED LAYERS')
    toDelete = [ 'JointsReference', 'JOINTS_REF', 'Back_Up_Limbs' ]
    for n in toDelete:
        try:
            cmds.delete( n )
        except:
            pass



def deleteBSTargets(*args):
    utils.printHeader('DELETING BLEND SHAPES')
    for n in TRvars.blendShapesEyes:
        try:
            cmds.delete( n )
        except:
            pass



def bindSkinMesh(*args):
    utils.printHeader('BINDING SKIN')
    resetControllers()
    mel.eval('SelectAllJoints;')
    sel = cmds.ls(sl=True, type='joint')
    cmds.skinCluster( sel, 'Mesh', n=TRvars.skinCluster, tsb=True, bm=0, nw=1, mi=4, omi=True, dr=4, rui=True )
    cmds.select( d=True )



def removeInfluences(*args):
    utils.printHeader('REMOVING UNNECESSARY INFLUENCES')
    cmds.select( 'END_*', 'JNT_RBN__*1', 'JNT_RBN__*5', 'JNT_RBN__*_CENTRAL', 'JNT_RBN__*_BOTTOM', 'JNT_RBN__*_TOP', 'STRJNT__*', 'REV_JNT__*' )
    sel = cmds.ls(sl=True, type='joint')
    cmds.select( d=True )
    for s in sel:
        try:
            cmds.skinCluster( TRvars.skinCluster, e=True, ri=s )
        except:
            pass
            
    cmds.select( d=True )



def jointSize(size, *args):
    s = cmds.jointDisplayScale( q=True )
    s += size
    cmds.jointDisplayScale( s )



def resetControllers(*args):
    mel.eval('SelectAllNURBSCurves;')
    sel = cmds.ls(sl=True)
    
    attr = ['.translateX','.translateY','.translateZ','.rotateX','.rotateY','.rotateZ','.scaleX','.scaleY','.scaleZ']
    values = [0,0,0,0,0,0,1,1,1]
    
    for s in sel:
        for a in range(len(attr)):
            try:
                cmds.setAttr( s + attr[a], values[a] )
            except:
                pass
            
    cmds.select( d=True )



def renameChains(*args):
    sel = cmds.ls(sl=True)
    if TReh.GetSelectionException(sel): return

    sel = cmds.listRelatives( cmds.ls(sl=True), ad=True )
    sel.append( cmds.ls(sl=True)[0] )
    for s in sel:
        cmds.refresh()
        cmds.select( s )
        cmds.rename( getRandomName() )



def getRandomName():
    from random import seed
    from random import randint
    from datetime import datetime
    seed(datetime.now())
    return 'joint_' + str(randint(10000000, 9999999999))



def handleOffset(state, *args):
    sel = cmds.ls(sl=True)
    for s in sel:
        cmds.select( s )
        utils.lockAndHideOffset('null', state, True)
        cmds.select( d=True )

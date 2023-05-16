import RiggingTools as RT
import RT_Controllers as RTctrl
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils as utils
import RT_SpaceSwitch
import maya.cmds as cmds
from pymel.core import language,PyNode
import maya.mel as mel
from functools import partial


def drawUI():
    RT.toolHeader('ribbonSystemTab', '---------   RIBBON SYSTEM  ---------')
    RT.subHeader(1, 'JOINTS', 5)
    RT.createTextFieldButtonGrp('RBBottomJoint', 'Top Joint', partial(RT.addObject, 'RBBottomJoint'), True)    
    RT.createTextFieldButtonGrp('RBTopJoint', 'Bottom  Joint', partial(RT.addObject, 'RBTopJoint'), True)
    RT.subHeader(7, 'OPTIONS', 5)
    winWidth = RT.winWidth
    rowWidth = [winWidth*0.1, winWidth*0.42, winWidth*0.42]
    colWidth = [rowWidth[1]*0.3, rowWidth[1]*0.25, rowWidth[1]*0.3]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.intSliderGrp( 'RBSpawns', l='Spawns', min=3, max=20, f=True, value=5, s=2, adj=1, cal=(1, "left"), cw3=colWidth )
    cmds.floatSliderGrp( 'RBRWidth', l='Width   ', f=True, min=0.05, max=0.5, v=0.10, s=0.05, cal=(1, "right"), cw3=colWidth )
    cmds.setParent( '..' )
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.floatSliderGrp( 'RBSizeBottom', l='Bottom Size   ', f=True, min=0.05, max=0.5, v=0.30, s=0.01, cal=(1, "right"), cw3=colWidth )
    cmds.floatSliderGrp( 'RBSizeTop', l='Top Size', f=True, min=0.05, max=0.5, v=0.30, s=0.01, cal=(1, "left"), cw3=colWidth )
    cmds.setParent( '..' )
    RT.verticalSpace(3)
    RT.createButtonAction(10,'', 'Create Ribbon System', createRibbonSystem, False)
    RT.createSpaceForUtilities('---------   UTILITIES  ---------')
    RT.createTwoButtonsAction(3,'dwl', 'Delete whole ribbon', partial(deleteRibbon, False), 'dls', 'Delete but keep controllers', partial(deleteRibbon, True), True)



def createRibbonSystem(*args):
    utils.printHeader('CREATING RIBBON SYSTEM')
    
    
    #############################
    utils.printSubheader('Deleting unused nodes')
    mel.eval('MLdeleteUnused;')
    
    #############################
    utils.printSubheader('Defining and declaring variables')
    topJoint = cmds.textFieldGrp( 'RBTopJoint', q=True, tx=True )
    bottomJoint = cmds.textFieldGrp( 'RBBottomJoint', q=True, tx=True )
    spawns = cmds.intSliderGrp( 'RBSpawns', q=True, v=True )
    width = cmds.floatSliderGrp( 'RBRWidth', q=True, v=True )
    name1 = utils.getNameControl(5, topJoint, 'lower') + utils.getNameControl(5, bottomJoint, 'lower')
    name = '_' + utils.getNameControl(5, topJoint, 'lower') + utils.getNameControl(5, bottomJoint, 'lower')
    ribbonName = 'RBN' + name
    dist = utils.getDistance(topJoint, bottomJoint)
    dist = dist + (dist/spawns)
    ratio = dist / width

    #############################
    utils.printSubheader('Creating nurb surface')
    cmds.nurbsPlane( n=ribbonName, w=width, lr=ratio ,d=3, u=1, v=spawns, ax=[0,1,0], p=[0,0,0], ch=0 )
    cmds.rebuildSurface( ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=1, du=1, sv=spawns, dv=3, tol=0, fr=0, dir=2)
    cmds.select( ribbonName )
    cmds.setAttr( ribbonName + '.rotateY', 180 )
    angle = cmds.angleBetween( v1=utils.getVector(topJoint, bottomJoint), v2=(0, 0, 1) )[3]
    angle *= 1 if cmds.getAttr( bottomJoint + '.translateY' ) > cmds.getAttr( topJoint + '.translateY' ) else -1
    cmds.setAttr( ribbonName + '.rotateX', angle )
    cmds.refresh()
    cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0 )
    cmds.editDisplayLayerMembers( 'HELPERS', ribbonName, nr=True )
    cmds.parent( ribbonName, 'Helpers' )

    #############################
    utils.printSubheader('Creating follicles')
    ch = "createHair 1 " + str(spawns) + " 5 0 0 0 0 5 0 1 1 1;"
    language.Mel.eval( ch )
    hairSystem = PyNode("hairSystem1")
    cmds.delete( 'hairSystem1' )
    cmds.delete( 'pfxHair1' )
    cmds.delete( 'nucleus1' )
    cmds.select( 'hairSystem1Follicles', r=True )
    hairSystemFollicle =  'HSF' + name
    cmds.rename( 'hairSystem1Follicles', hairSystemFollicle )
    curvesGroup = cmds.listRelatives( hairSystemFollicle, ad=True )
    cmds.parent( hairSystemFollicle, 'Rig' )
    cmds.editDisplayLayerMembers( 'JOINTS', hairSystemFollicle, nr=True )

    #############################
    utils.printSubheader('Creating ribbon joints')    
    x = 1
    jointsRibbon = []
    
    for i in curvesGroup:
        if i==('curve' + str(x)):
            cmds.select( i )
            p = cmds.listRelatives( i, p=True )
            cmds.rename( p, 'FLC' + name + '_' + str(x) )
            cmds.rename( i, 'CRV' + name + '_' + str(x) )
            bone = cmds.joint( n='JNT_RBN' + name + '_' + str(x) )
            jointsRibbon.append(bone)
            cmds.setAttr( bone + '.rz', 90 )
            cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0 ) 
            x += 1
    x -= 1

    #############################
    utils.printSubheader('Creating controllers')      
    influences = []
    influences.append(createBoneController(jointsRibbon[0], name + '__TOP'))
    influences.append(createBoneController(jointsRibbon[x//2], name + '__CENTRAL'))   
    influences.append(createBoneController(jointsRibbon[-1], name + '__BOTTOM'))
    
    skinCluster = cmds.skinCluster( influences, ribbonName, n='SKCL' + name, tsb=True, bindMethod=0, skinMethod=0, normalizeWeights=1, mi=2 )[0]
    
    locatorTop = createLocator(influences[0])
    locatorCentral = createLocator(influences[1])
    locatorBottom = createLocator(influences[2])
    
    offset = cmds.group( n = 'OFFSET' + locatorCentral[1][3:], em=1 )
    cmds.xform( offset, m=locatorCentral[0], ws=True)
    cmds.parent( locatorCentral[1], offset )

    #############################
    utils.printSubheader('Orienting central controller')
    locOrientTop = 'LOC' + name + '__TOP_ORIENT'
    locOrientBottom = 'LOC' + name + '__BOTTOM_ORIENT'
    ctrlOrientCentral = 'GRP_LOC' + name
    
    locatorOriTop = cmds.spaceLocator( n=locOrientTop )
    locatorOriBottom = cmds.spaceLocator( n=locOrientBottom )
    cmds.editDisplayLayerMembers( 'HELPERS', locOrientTop, nr=True )
    cmds.editDisplayLayerMembers( 'HELPERS', locOrientBottom, nr=True )
    utils.setLocalScaleLocators( locatorOriTop[0] )
    utils.setLocalScaleLocators( locatorOriBottom[0] )
    ctrlOffsetOriLocators = cmds.group( n=ctrlOrientCentral, em=1 )
    cmds.parent( locOrientTop, ctrlOrientCentral )
    cmds.parent( locOrientBottom, ctrlOrientCentral )
    
    cmds.xform( ctrlOffsetOriLocators, m=locatorCentral[0], ws=True )
    cmds.pointConstraint( locatorTop[1], locatorBottom[1], ctrlOrientCentral, n=utils.getConstraint('Point', ctrlOrientCentral[7:]), mo=True)
    cmds.aimConstraint( locatorTop[1], locOrientTop, n=utils.getConstraint('Aim', locOrientTop[3:]), mo=False, wut='object', wuo=locatorTop[1], aim=[-1,0,0], u=[0,0,1] )
    cmds.aimConstraint( locatorBottom[1], locOrientBottom, n=utils.getConstraint('Aim', locOrientBottom[3:]), mo=False, wut="object", wuo=locatorBottom[1], aim=[1,0,0], u=[0,0,1] )
    cmds.parentConstraint( locOrientTop, locOrientBottom, offset, n=utils.getConstraint('Parent', locOrientBottom[3:]), mo=True )
    cmds.select(d=True)

    #############################
    utils.printSubheader('Creating distance dimension and helpers')
    topLoc = cmds.xform( locatorTop[1], q=True, m=True, ws=True )
    bottomLoc = cmds.xform( locatorBottom[1], q=True, m=True, ws=True )
    distance = utils.createDistanceMeasure(name, name + '__DIST_TOP', name + '__DIST_BOTTOM')
    cmds.xform( distance[1], m=topLoc, ws=True )
    cmds.xform( distance[2], m=bottomLoc, ws=True )

    #############################
    utils.printSubheader('Setting Distance Dimension connections')
    RBMultDivStretch = utils.createShadingNode('multiplyDivide', locatorTop[1] + '_MultDivStretch')    
    distValue = cmds.getAttr( distance[0] + '.distance' )
    cmds.setAttr( RBMultDivStretch + '.input2X', distValue )
    cmds.setAttr( RBMultDivStretch + '.operation', 2 )
    cmds.connectAttr( distance[0] + '.distance', RBMultDivStretch + '.input1X')
    
    #############################
    utils.printSubheader('Setting Stretch System')
    cmds.select( locatorTop[1] )
    cmds.addAttr( ln='Stretch', at="float", k=True, dv=0, min=0, max=1 )
    
    RBPower = utils.createShadingNode('multiplyDivide', name[2:] + '_Power')
    cmds.setAttr( RBPower + '.operation', 3 )
    cmds.connectAttr( locatorTop[1] + '.Stretch', RBPower + '.input2.input2X')
    cmds.connectAttr( RBMultDivStretch + '.outputX', RBPower + '.input1.input1X')
    
    RBDivide = utils.createShadingNode('multiplyDivide', name[2:] + '_Divide')
    cmds.setAttr( RBDivide + '.input1X', 1 )
    cmds.setAttr( RBDivide + '.operation', 2 )
    cmds.connectAttr( RBPower + '.outputX', RBDivide + '.input2.input2X')

        
    #############################
    utils.printSubheader('Connecting scales')
    for j in range(len(jointsRibbon)-1):
        cmds.connectAttr( RBDivide + '.outputX', jointsRibbon[j] + '.scaleY')
        cmds.connectAttr( RBDivide + '.outputX', jointsRibbon[j] + '.scaleZ')
            
    cmds.pointConstraint( jointsRibbon[0], distance[1], n=utils.getConstraint('Point', distance[1][3:]), mo=True )
    cmds.pointConstraint( jointsRibbon[-1], distance[2], n=utils.getConstraint('Point', distance[2][3:]), mo=True )
    
    topJointPos = cmds.xform( topJoint, q=True, t=True, ws=True )
    bottomJointPos = cmds.xform( bottomJoint, q=True, t=True, ws=True )
    cmds.xform( locatorTop[1], t=topJointPos, ws=True )
    cmds.xform( locatorBottom[1], t=bottomJointPos, ws=True )

    #############################
    utils.printSubheader('Parenting locators and setting constraints')
    controlTop = createRibbonJointConnection(locatorTop[1], topJoint)
    controlBottom = createRibbonJointConnection(locatorBottom[1], bottomJoint)
    centralJointRibbon = 'JNT_RBN' + name + '__CENTRAL'
    cmds.select( centralJointRibbon )
    ctrl = RTctrl.createController('Circle', (1, 1, 0), 0.3, 'Object', 'OFFSET', 'AUX')
    cmds.parent( ctrl[1], offset )
    utils.setTransformAndRotationToZero(ctrl[1]) 
    cmds.parent( locatorCentral[1], ctrl[1] )
    cmds.delete( ctrl[0] )
    cmds.parent( topJoint, bottomJoint, 'Rig' )

    #############################
    utils.printSubheader('Connecting stretch system')
    cmds.select( controlTop )
    utils.addAttrSeparator(controlTop, 'StretchSeparator', 'STRETCH  VOLUME')
    cmds.addAttr( ln='Stretch', nn='Influence', at="float", k=True, dv=0, min=0, max=1 )
    cmds.connectAttr( controlTop + '.Stretch', locatorTop[1] + '.Stretch' )
    cmds.parent( 'OFFSET' + topJoint[3:], 'OFFSET' + bottomJoint[3:], 'OFFSET' + name + '__CENTRAL', 'CTRL__Master' )
    cmds.parent('GRP_LOC' + name, 'CTRL' + topJoint[3:] )

    #############################
    cmds.refresh()
    if name.find('Head') > -1 and len(cmds.ls('CTRL__Neck')) == 1:
        result = cmds.confirmDialog( t='Space Switch', m='Do you want to create an <b>Point/Orient</b> space switch between the <b>Head</b> and the <b>Neck</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName )
        if result == 'Yes':
            RT_SpaceSwitch.createSpaceSwitch('NeckSpace', 'CTRL__Head', 'CTRL__Master', 'CTRL__Neck', 'PointOrient')

    if name.find('Neck') > -1 and len(cmds.ls('CTRL__Chest')) == 1:
        result = cmds.confirmDialog( t='Space Switch', m='Do you want to create an <b>Point/Orient</b> space switch between the <b>Neck</b> and the <b>Chest</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName )
        if result == 'Yes':
            RT_SpaceSwitch.createSpaceSwitch('ChestSpace', 'CTRL__Neck', 'CTRL__Master', 'CTRL__Chest', 'PointOrient')

    #############################
    utils.printSubheader('Locking and hidding unused attributes')
    utils.lockAndHideAttribute(controlTop, False, False)
    utils.lockAndHideAttribute(ctrl[1], False, False)
    utils.lockAndHideAttribute(controlBottom, False, False)
    ctrlName = ctrl[1].replace('CTRL_RBN__', 'CTRL__')
    cmds.rename( ctrl[1], ctrlName )



def createRibbonJointConnection(locCtrl, bone):
    cmds.parent( locCtrl, bone )
    cmds.select( bone )
    ctrl =  RTctrl.createController('Mesh', (1, 1, 0), 0.35, 'World', '', '')
    cmds.parentConstraint( ctrl[1], bone, n=utils.getConstraint('Parent', bone[3:]), mo=True )
    return ctrl[1]



def createBoneController(bone, pName):
    ctrlName = 'JNT_RBN' + pName
    ctrl = cmds.duplicate( bone )    
    cmds.rename( ctrl, ctrlName )
    cmds.select( ctrlName ) 
    cmds.parent( w=True )
    cmds.setAttr( ctrlName + '.radius', 1.5 )
    return ctrlName



def createLocator(influence):
    print influence
    name = 'LOC' + influence[7:]
    print name
    locator = cmds.spaceLocator( n='LOC' + influence[7:] )
    sel = cmds.xform( influence, q=True, m=True, ws=True )
    cmds.xform( locator, m=sel, ws=True )
    cmds.parent( influence, locator )
    utils.setLocalScaleLocators(locator[0])
    cmds.editDisplayLayerMembers( 'HELPERS', locator, nr=True )
    return [sel, locator[0]]



def deleteRibbonKeepControllers():
    utils.printHeader('DELETING RIBBON SYSTEM...')
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    ribbon = sel[0][5:]
    topJoint = sel[0][5:].split('_')[0]
    btmJoint = sel[0][5:].split('_')[1]
    
    utils.printSubheader('Deleting helpers...')
    cmds.delete( 'LOC__' + ribbon + '*' )
    cmds.delete( sel )
    
    utils.printSubheader('Deleting rig connections...')
    cmds.delete( 'HSF__' + ribbon )
    cmds.delete( 'JNT__' + topJoint )
    cmds.delete( 'JNT__' + btmJoint )
    
    utils.printSubheader('Deleting controllers...')
    cmds.delete( 'OFFSET__' + ribbon + '__CENTRAL' )
    cmds.delete( 'GRP_LOC__' + ribbon )
    cmds.delete( 'OFFSET__' + topJoint )
    cmds.delete( 'OFFSET__' + btmJoint )
    
    utils.printSubheader('Deleting unused nodes...') 
    mel.eval('MLdeleteUnused;')


def deleteRibbon(*args):
    utils.printHeader('DELETING WHOLE RIBBON...')
    deleteRibbonKeepControllers()
    print 'WIP - deleteRibbon'
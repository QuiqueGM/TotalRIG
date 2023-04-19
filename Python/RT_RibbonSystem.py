import RT_Controllers as RTctrl
import RT_Utils as utils
import maya.cmds as cmds
from pymel.core import language,PyNode
import maya.mel as mel


def createRibbonSystem():
    utils.printHeader('CREATING RIBBON SYSTEM')
    mel.eval('MLdeleteUnused;')
    topJoint = cmds.textFieldGrp( 'RBTopJoint', q=True, tx=True )
    bottomJoint = cmds.textFieldGrp( 'RBBottomJoint', q=True, tx=True )
    spawns = cmds.intSliderGrp( 'RBSpawns', q=True, v=True )
    width = cmds.floatSliderGrp( 'RBRWidth', q=True, v=True )
    name = '__' + utils.getNameControl(5, topJoint, 'lower') + utils.getNameControl(5, bottomJoint, 'lower') 
    ribbonName = 'RBN' + name
    dist = utils.getDistance(topJoint, bottomJoint)
    dist = dist + (dist/spawns)
    ratio = dist / width
    
    # Create una superficie nurbs a partir de la distancia dels ossos i un nombre de divisions
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
    
    #Crea els follicles i posa un os a cada Follicle
    ch = "createHair 1 " + str(spawns) + " 5 0 0 0 0 5 0 1 1 1;"
    language.Mel.eval( ch )
    hairSystem = PyNode("hairSystem1")
    cmds.delete( 'hairSystem1' )
    cmds.delete( 'pfxHair1' )
    cmds.delete( 'nucleus1' )
    cmds.select( 'hairSystem1Follicles', r=True )
    cmds.rename( 'hairSystem1Follicles', 'HSF' + name )
    curvesGroup = cmds.listRelatives( 'HSF' + name, ad=True )
    
    x = 1
    jointsRibbon = []
    
    for i in curvesGroup:
        if i==('curve' + str(x)):
            cmds.select( i )
            cmds.rename( i, 'CRV' + name + '_' + str(x) )
            bone = cmds.joint( n='JNT_RBN' + name + '_' + str(x) )
            jointsRibbon.append(bone)
            cmds.setAttr( bone + '.rz', 90 )
            cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0 ) 
            x += 1
    x -= 1
    
    influences = []
    influences.append(createBoneController(jointsRibbon[0], name + '_TOP'))
    influences.append(createBoneController(jointsRibbon[x//2], name + '_CENTRAL'))
    influences.append(createBoneController(jointsRibbon[-1], name + '_BOTTOM'))
    
    skinCluster = cmds.skinCluster( influences, ribbonName, n='SKCL' + name, tsb=True, bindMethod=0, skinMethod=0, normalizeWeights=1, mi=2 )[0]
    
    locatorTop = createLocator(influences[0])
    locatorCentral = createLocator(influences[1])
    locatorBottom = createLocator(influences[2])
    
    offset = cmds.group( n = 'OFFSET' + locatorCentral[1][3:], em=1 )
    cmds.xform( offset, m=locatorCentral[0], ws=True)
    cmds.parent( locatorCentral[1], offset )
    
    #Orientacio del control central
    locOrientTop = 'LOC' + name + '_TOP_ORIENTATION'
    locOrientBottom = 'LOC' + name + '_BOTTOM_ORIENTATION'
    ctrlOrientCentral = 'GRP_CTRL_LOCATORS' + name
    
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
    cmds.pointConstraint( locatorTop[1], locatorBottom[1], ctrlOrientCentral, mo=True)
    cmds.aimConstraint( locatorTop[1], locOrientTop, mo=False, wut='object', wuo=locatorTop[1], aim=[-1,0,0], u=[0,0,1] )
    cmds.aimConstraint( locatorBottom[1], locOrientBottom, mo=False, wut="object", wuo=locatorBottom[1], aim=[1,0,0], u=[0,0,1] )
    cmds.parentConstraint( locOrientTop, locOrientBottom, offset, mo=True )
    cmds.select(d=True)
    
    # Crea locators i distance dimension i els posiciona als extrems del ribbon
    topLoc = cmds.xform( locatorTop[1], q=True, m=True, ws=True )
    bottomLoc = cmds.xform( locatorBottom[1], q=True, m=True, ws=True )
    distance = utils.createDistanceMeasure(name, name + '_DIST_TOP', name + '_DIST_BOTTOM')
    cmds.xform( distance[1], m=topLoc, ws=True )
    cmds.xform( distance[2], m=bottomLoc, ws=True )
    
    #Conectarem el parametre distance del DistanceDimension a un multiplyDivide.
    RBMultDivStretch = locatorTop[1] + '_MultiplyDivideStretch'
    cmds.shadingNode( 'multiplyDivide', au=True, n=RBMultDivStretch )
    cmds.connectAttr( distance[0] + '.distance', RBMultDivStretch + '.input1X')
    distValue = cmds.getAttr( distance[0] + '.distance' )
    cmds.setAttr( RBMultDivStretch + '.input2X', distValue )
    cmds.setAttr( RBMultDivStretch + '.operation', 2 )
    
    #Crearem un BlendColors i el sistema Stretch
    RBBlendCol = locatorTop[1] + '_BlendColor'
    RBClamp = locatorTop[1] + '_Clamp'
    cmds.select( locatorTop[1] )
    cmds.addAttr( ln='Stretch', at="float", k=True, dv=0, min=0, max=1 )
    cmds.shadingNode( 'blendColors', au=True, n=RBBlendCol )
    cmds.connectAttr( locatorTop[1] + '.Stretch', RBBlendCol + '.blender')
    cmds.shadingNode( 'clamp', au=True, n=RBClamp )
    cmds.connectAttr( RBBlendCol + '.outputR', RBClamp + '.inputR' )
    cmds.setAttr( RBClamp + '.minR', 1 )
    cmds.setAttr( RBClamp + '.maxR', 999 )
    cmds.connectAttr( RBMultDivStretch + '.outputX', RBBlendCol + '.color1R')
    
    #Crearem un node MultiplyDivide per controlar la escala Y i Z
    RBMultDivStretch2 = name[2:] + '_MultiplyDivideStretch2'
    cmds.shadingNode( 'multiplyDivide', au=True, n=RBMultDivStretch2 )
    cmds.connectAttr( RBClamp + '.outputR', RBMultDivStretch2 + '.input2X' )
    cmds.setAttr( RBMultDivStretch2 + '.input1X', 1 )
    cmds.setAttr( RBMultDivStretch2 + '.operation', 2 )
        
    #Connetem amb les escales
    for j in range(len(jointsRibbon)-1):
        cmds.connectAttr( RBMultDivStretch2 + '.outputX', jointsRibbon[j] + '.scaleY')
        cmds.connectAttr( RBMultDivStretch2 + '.outputX', jointsRibbon[j] + '.scaleZ')
            
    cmds.pointConstraint( jointsRibbon[0], distance[1], mo=True )
    cmds.pointConstraint( jointsRibbon[-1], distance[2], mo=True )
    
    topJointPos = cmds.xform( topJoint, q=True, t=True, ws=True )
    bottomJointPos = cmds.xform( bottomJoint, q=True, t=True, ws=True )
    cmds.xform( locatorTop[1], t=topJointPos, ws=True )
    cmds.xform( locatorBottom[1], t=bottomJointPos, ws=True )
    
    #Emparentem els locators amb els joints i creem els constraints i fem els constraints
    controlTop = createRibbonJointConnection(locatorTop[1], topJoint)
    createRibbonJointConnection(locatorBottom[1], bottomJoint)
    centralJointRibbon = 'RBNJNT' + name + '_CENTRAL'
    cmds.select( centralJointRibbon )
    cmds.rename ( centralJointRibbon, centralJointRibbon[3:] )
    ctrl = RTctrl.createController('Circle', (1, 1, 0), 0.3, 'Object', '', '')
    cmds.parent( ctrl[1], offset )
    cmds.parent( locatorCentral[1], ctrl[1] )
    cmds.delete( ctrl[0] + '1' )
    cmds.select(d=True)
    
    #Connectem l'stretch del locatorTop amb el controlador Top
    cmds.select( controlTop )
    cmds.addAttr( ln='Stretch', at="float", k=True, dv=0, min=0, max=1 )
    cmds.connectAttr( controlTop + '.Stretch', locatorTop[1] + '.Stretch' )
    
    

def createRibbonJointConnection(locCtrl, bone):
    cmds.parent( locCtrl, bone )
    cmds.select( bone )
    ctrl =  RTctrl.createController('Box', (1, 1, 0), 0.35, 'World', '', '')
    cmds.parentConstraint( ctrl[1], bone, mo=True )
    return ctrl[1]



def createBoneController(bone, pName):
    ctrlName = 'RBNJNT' + pName
    ctrl = cmds.duplicate( bone )    
    cmds.rename( ctrl, ctrlName )
    cmds.select( ctrlName ) 
    cmds.parent( w=True )
    cmds.setAttr( ctrlName + '.radius', 1.5 )
    return ctrlName



def createLocator(influence):
    locator = cmds.spaceLocator( n='LOC' + influence[6:] )
    sel = cmds.xform( influence, q=True, m=True, ws=True )
    cmds.xform( locator, m=sel, ws=True )
    cmds.parent( influence, locator )
    utils.setLocalScaleLocators(locator[0])
    cmds.editDisplayLayerMembers( 'HELPERS', locator, nr=True )
    return [sel, locator[0]]
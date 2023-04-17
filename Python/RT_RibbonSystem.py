import RT_Utils as utils
import maya.cmds as cmds


def createRibbonSystem():
    utils.printHeader('CREATING RIBBON SYSTEM')
    
    topJoint = cmds.textFieldGrp( 'RBTopJoint', q=True, tx=True )
    bottomJoint = cmds.textFieldGrp( 'RBBottomJoint', q=True, tx=True )
    spawns = cmds.intSliderGrp( 'RBSpawns', q=True, v=True )
    width = cmds.floatSliderGrp( 'RBRWidth', q=True, v=True )
    name = '__' + utils.getNameControl(5, topJoint, 'lower') + utils.getNameControl(5, bottomJoint, 'lower') 
    dist = utils.getDistance(topJoint, bottomJoint)
    dist = dist + (dist/spawns)
    ratio = dist / width
    
    # Create una superficie nurbs a partir de la distancia dels ossos i un nombre de divisions
    cmds.nurbsPlane( n=ribbonName, w=width, lr=ratio ,d=3, u=1, v=spawns, ax=[0,1,0], p=[0,0,0], ch=0 )
    cmds.rebuildSurface( ch=0, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=1, du=1, sv=spawns, dv=3, tol=0, fr=0, dir=2)
    cmds.select( ribbonName )
    cmds.setAttr( ribbonName + '.rotateY', 90)
    angle = cmds.angleBetween( v1=utils.getVector(topJoint, bottomJoint), v2=(1, 0, 0) )[3]
    angle *= 1 if cmds.getAttr( bottomJoint + '.translateY' ) > cmds.getAttr( topJoint + '.translateY' ) else -1
    cmds.setAttr( ribbonName + '.rotateX', angle )
    cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0 )
    
    #Crea els follicles i posa un os a cada Follicle
    ch = "createHair 1 " + str(spawns) + " 5 0 0 0 0 5 0 1 1 1;"
    language.Mel.eval( ch )
    hairSystem = PyNode("hairSystem1")
    cmds.delete( 'hairSystem1' )
    cmds.delete( 'pfxHair1' )
    cmds.delete( 'nucleus1' )
    curvesGroup = cmds.listRelatives( 'HSF' + name, ad=False )
    
    x = 1
    jointsRibbon = []
    
    for i in curvesGroup:
        if i==('curve' + str(x)):
            cmds.select( i )
            cmds.rename( i, 'CRV' + name + '_' + str(x) )
            bone = cmds.joint( n='JNT_RBN' + name + '_' + str(x) )
            jointsRibbon.append(bone)
            cmds.setAttr( bone + '.rz', -90 )
            cmds.makeIdentity( apply=True, t=0, r=1, s=1, n=1 ) 
            x += 1
    x -= 1
    
    influences = []
    influences.append(createBoneController(jointsRibbon[0], name + '_TOP'))
    influences.append(createBoneController(jointsRibbon[x//2], name + '_CENTRAL'))
    influences.append(createBoneController(jointsRibbon[-1], name + '_BOTTOM'))   
    
    #Orientacio del control central
    locOrientTop = 'LOC' + name + '_TOP_ORIENTATION'
    locOrientBottom = 'LOC' + name + '_BOTTOM_ORIENTATION'
    ctrlOrientCentral = 'GRP_CTRL_LOCATORS' + name
    
    utils.setLocalScaleLocators([0] )
    utils.setLocalScaleLocators( cmds.spaceLocator( n=locOrientBottom )[0] )
    ctrlOffsetOriLocators = cmds.group( n=ctrlOrientCentral, em=1 )
    cmds.parent( cmds.spaceLocator( n=locOrientTop ), ctrlOrientCentral )
    cmds.parent( cmds.spaceLocator( n=locOrientBottom ), ctrlOrientCentral )
    
    cmds.xform( ctrlOffsetOriLocators, m=locatorCentral[0], ws=True )
    cmds.pointConstraint( locatorTop[1], locatorBottom[1], ctrlOrientCentral, mo=True)
    cmds.aimConstraint( locatorTop[1], locOrientTop, mo=False, wut='object', wuo=locatorTop[1], aim=[-1,0,0], u=[0,0,1] )
    cmds.aimConstraint( locatorBottom[1], locOrientBottom, mo=False, wut="object", wuo=locatorBottom[1], aim=[1,0,0], u=[0,0,1] )
    cmds.parentConstraint( locOrientTop, locOrientBottom, offset, mo=True )

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
    cmds.addAttr( ln='Stretch', at="int", k=False, dv=0, min=0, max=)
    cmds.shadingNode( 'blendColors', au=True, n=RBBlendCol )
    cmds.connectAttr( RBBlendCol + '.outputR', RBClamp + '.inputR' )
    cmds.setAttr( RBClamp + '.minR', 0 )
    cmds.setAttr( RBClamp + '.maxR', 10000 )
    cmds.connectAttr( RBMultDivStretch + '.outputX', RBBlendCol + '.color1R')
    
    
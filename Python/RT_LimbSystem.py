import RiggingTools
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Controllers as RTctrl
import RT_Utils as utils
import RT_FillTools
import RT_Utilities
import RT_SpaceSwitch
import RT_Rename
import maya.cmds as cmds
import maya.mel as mel

def assignVariables():
    global limbBones, offsetsLimb, ctrlLimbBones, reverseFoot, sidePos
    global JNT_ClavHip, JNT_UpperLimb, JNT_LowerLimb, JNT_WristAnkle, JNT_HandFoot, JNT_FingToeInd, JNT_FingToeMid, JNT_FingToeRing, JNT_FingToeThumb, JNT_FingToePinky
    global CTRL_ClavHip, CTRL_ClavHip_IK, CTRL_UpperLimb, CTRL_LowerLimb, CTRL_WristAnkle, CTRL_HandFoot
    global CTRL_FingToeInd, CTRL_FingToeMid, CTRL_FingToeRing, CTRL_FingToeThumb, CTRL_FingToePinky, CTRL_WristAnkle_IK, CTRL_UpperLimbPV, CTRL_LowerLimbPV, CTRL_LowerLimbIK, CTRL_LimbSwitch_FKIK
    global REV_Orient, REV_Heel, REV_Ext, REV_Int, REV_Tip, REV_Ball, REV_WristAnkle, REV_JNT_WristAnkle, IKH_LowerLimb, IKH_WristAnkle, PV_UpperLine, PV_LowerLine
    global snapGroups
    
    cmds.select( RTvars.limbStartingBone )
    sel = cmds.ls(sl=True)[0]
    RT_FillTools.autofillFromSelection()
    sidePos = '__' + utils.getSideFromBone(sel) + utils.getPositionFromBone(sel)

    if utils.getHierarchy() == 'Leg':
        if utils.getIKSystem() == 'HingeLimb':
            offsetsLimb = RTvars.offsetsHingeLeg
            snapGroups = RTvars.snapHingeLeg
            CTRL_UpperLimbPV = 'CTRL' + sidePos + 'UpperLeg_PV'
            PV_UpperLine = 'LINE' + sidePos + 'UpperLeg_PV'
            CTRL_LowerLimbIK = 'CTRL' + sidePos + 'LowerLeg_IK'
            IKH_LowerLimb = 'IKH' + sidePos + 'LowerLeg'
        else:
            offsetsLimb = RTvars.offsetsLeg
            snapGroups = RTvars.snapLeg
                               
        limbBones = RTvars.legBones
        reverseFoot = RTvars.reverseFoot
        JNT_ClavHip = cmds.textFieldGrp( 'Hip' ,q=True, tx=True )
        JNT_UpperLimb = cmds.textFieldGrp( 'UpperLeg' ,q=True, tx=True )
        JNT_LowerLimb = cmds.textFieldGrp( 'LowerLeg' ,q=True, tx=True )
        JNT_WristAnkle = cmds.textFieldGrp( 'Ankle' ,q=True, tx=True )
        JNT_HandFoot = cmds.textFieldGrp( 'Foot' ,q=True, tx=True )
        JNT_FingToeRing = cmds.textFieldGrp( 'ToeRing' ,q=True, tx=True )
        JNT_FingToeMid = cmds.textFieldGrp( 'ToeMid' ,q=True, tx=True )
        JNT_FingToeInd = cmds.textFieldGrp( 'ToeIndex' ,q=True, tx=True )
        JNT_FingToeThumb = cmds.textFieldGrp( 'ToeThumb' ,q=True, tx=True )
        JNT_FingToePinky = cmds.textFieldGrp( 'ToePinky' ,q=True, tx=True )
        
        CTRL_LowerLimbPV = 'CTRL' + sidePos + 'LowerLeg_PV'
        PV_LowerLine = 'LINE' + sidePos + 'LowerLeg_PV'
        CTRL_LimbSwitch_FKIK = 'CTRL' + sidePos + 'LegSwitch_FKIK'
        REV_WristAnkle = 'REV' + sidePos + 'Ankle'
        REV_JNT_WristAnkle = 'REV_JNT' + sidePos + 'Ankle'
        IKH_LowerLimb = 'IKH' + sidePos + 'LowerLeg'
        IKH_WristAnkle = 'IKH' + sidePos + 'Ankle'
        
    else:
        if utils.getIKSystem() == 'HingeLimb':
            offsetsLimb = RTvars.offsetsHingeArm
            snapGroups = RTvars.snapHingeArm
            CTRL_UpperLimbPV = 'CTRL' + sidePos + 'Arm_PV'
            PV_UpperLine = 'LINE' + sidePos + 'Arm_PV'
            CTRL_LowerLimbIK = 'CTRL' + sidePos + 'Forearm_IK'
            IKH_LowerLimb = 'IKH' + sidePos + 'Forearm'
        else:
            offsetsLimb = RTvars.offsetsArm
            snapGroups = RTvars.snapArm
            
        limbBones = RTvars.armBones
        reverseFoot = RTvars.reverseHand
        JNT_ClavHip = cmds.textFieldGrp( 'Clavicle' ,q=True, tx=True ) 
        JNT_UpperLimb = cmds.textFieldGrp( 'Arm' ,q=True, tx=True )
        JNT_LowerLimb = cmds.textFieldGrp( 'Forearm' ,q=True, tx=True )
        JNT_WristAnkle = cmds.textFieldGrp( 'Wrist' ,q=True, tx=True )
        JNT_HandFoot = cmds.textFieldGrp( 'Hand' ,q=True, tx=True )
        JNT_FingToeRing = cmds.textFieldGrp( 'FingerRing' ,q=True, tx=True )
        JNT_FingToeMid = cmds.textFieldGrp( 'FingerMid' ,q=True, tx=True )
        JNT_FingToeInd = cmds.textFieldGrp( 'FingerIndex' ,q=True, tx=True )
        JNT_FingToeThumb = cmds.textFieldGrp( 'FingerThumb' ,q=True, tx=True )
        JNT_FingToePinky = cmds.textFieldGrp( 'FingerPinky' ,q=True, tx=True )
        
        CTRL_LowerLimbPV = 'CTRL' + sidePos + 'Forearm_PV'
        PV_LowerLine = 'LINE' + sidePos + 'Forearm_PV'
        CTRL_LimbSwitch_FKIK = 'CTRL' + sidePos + 'ArmSwitch_FKIK'
        REV_WristAnkle = 'REV' + sidePos + 'Wrist'
        REV_JNT_WristAnkle = 'REV_JNT' + sidePos + 'Wrist'
        IKH_WristAnkle = 'IKH' + sidePos + 'Wrist'

    if utils.getIKSystem() == 'HingeLimb':
        ctrlLimbBones = [[limbBones[0], 'Circle', 0.1, 'World', offsetsLimb[0]], [limbBones[0], 'Circle', 0.1, 'Object', ''], [limbBones[1], 'Circle', 0.14, 'Object', ''], [limbBones[1], 'Diamond', 0.035, 'World', offsetsLimb[3]], [limbBones[2], 'Circle', 0.13, 'Object', ''], [limbBones[2], 'Diamond', 0.035, 'World', offsetsLimb[5]], [limbBones[2], 'DoubleArrow', 0.1, 'World', offsetsLimb[6]], [limbBones[3], 'Circle', 0.1, 'Object', ''], [limbBones[3], 'Box', 0.15, 'World', offsetsLimb[8]], [limbBones[3], 'Box', 0.03, 'World', offsetsLimb[9]], [limbBones[4], 'Box', 0.125, 'World', ''], [limbBones[5], 'Circle', 0.04, 'Object', ''], [limbBones[6], 'Circle', 0.04, 'Object', ''], [limbBones[7], 'Circle', 0.04, 'Object', ''], [limbBones[8], 'Circle', 0.04, 'Object', ''], [limbBones[9], 'Circle', 0.04, 'Object', '']]
    else:
        ctrlLimbBones = [[limbBones[0], 'Circle', 0.1, 'World', ''], [limbBones[1], 'Circle', 0.14, 'Object', ''], [limbBones[2], 'Circle', 0.13, 'Object', ''], [limbBones[2], 'Diamond', 0.035, 'World', offsetsLimb[3]], [limbBones[3], 'Circle', 0.1, 'Object', ''], [limbBones[3], 'Box', 0.15, 'World', offsetsLimb[5]], [limbBones[3], 'Box', 0.03, 'World', offsetsLimb[6]], [limbBones[4], 'Box', 0.125, 'World', ''], [limbBones[5], 'Circle', 0.04, 'Object', ''], [limbBones[6], 'Circle', 0.04, 'Object', ''], [limbBones[7], 'Circle', 0.04, 'Object', ''], [limbBones[8], 'Circle', 0.04, 'Object', ''], [limbBones[9], 'Circle', 0.04, 'Object', '']]
    
    CTRL_ClavHip = 'CTRL' + JNT_ClavHip[3:]
    CTRL_UpperLimb = 'CTRL' + JNT_UpperLimb[3:]
    CTRL_LowerLimb = 'CTRL' + JNT_LowerLimb[3:]
    CTRL_WristAnkle = 'CTRL' + JNT_WristAnkle[3:]
    CTRL_HandFoot = 'CTRL' + JNT_HandFoot[3:]
    CTRL_FingToeRing = 'CTRL' + JNT_FingToeRing[3:]
    CTRL_FingToeMid = 'CTRL' + JNT_FingToeMid[3:]
    CTRL_FingToeInd = 'CTRL' + JNT_FingToeInd[3:]
    CTRL_FingToeThumb = 'CTRL' + JNT_FingToeThumb[3:]
    CTRL_FingToePinky = 'CTRL' + JNT_FingToePinky[3:]
    CTRL_ClavHip_IK = 'CTRL' + JNT_ClavHip[3:] + '_IK'
    CTRL_WristAnkle_IK = CTRL_WristAnkle + '_IK'
    
    REV_Heel = 'REV' + sidePos + reverseFoot[0]
    REV_Ext = 'REV' + sidePos + reverseFoot[1]
    REV_Int = 'REV' + sidePos + reverseFoot[2]
    REV_Tip = 'REV' + sidePos + reverseFoot[3]
    REV_Ball = 'REV' + sidePos + reverseFoot[4]
    
    ctrlLimbBones = utils.createLimbArray(ctrlLimbBones)
    offsetsLimb = utils.createLimbArray(offsetsLimb)
    limbBones = utils.createLimbArray(limbBones)



def createLimbControllers():
    RT_Rename.autorenameLimb()
    assignVariables()
    utils.printHeader('CREATING LIMB CONTROLLERS')
    
    
    cmds.select( RTvars.limbStartingBone )
    cmds.refresh()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    
    for b in range(len(ctrlLimbBones)): 
        utils.printSubheader('Creating controller --> ' + offsetsLimb[b])
        cmds.select( cmds.textFieldGrp( ctrlLimbBones[b][0], q=True, tx=True ))
        sel = cmds.ls(sl=True)
        ctrl = RTctrl.createController( ctrlLimbBones[b][1], utils.getColorFromSide(sel[0]), ctrlLimbBones[b][2], ctrlLimbBones[b][3], ctrlLimbBones[b][0], ctrlLimbBones[b][4] )[1]
        
    ctrls = getListControllers()
    createShape()

    if utils.getFootReverse() == 'Yes':
        if utils.getIKSystem() == 'HingeLimb':
            createReverseFootSetUp(ctrls[8])
        else:
            createReverseFootSetUp(ctrls[5])
    else:
        grp = cmds.group( em=True, n=REV_WristAnkle )
        cmds.parent( grp, cmds.textFieldGrp( limbBones[3], q=True, tx=True ) )
        utils.setTransformAndRotationToZero(grp)
        cmds.parent( grp, CTRL_WristAnkle_IK )
        utils.setTransformAndRotationToZero(grp)
        
    relocateControllers(ctrls)
    utils.lockControllers(ctrls, True)



def createShape():
    hip = cmds.xform( JNT_ClavHip, query=True, t=True, ws=True )
    upper = cmds.xform( JNT_UpperLimb, query=True, t=True, ws=True, a=True)
    lower = cmds.xform( JNT_LowerLimb, query=True, t=True, ws=True )
    wrist = cmds.xform( JNT_WristAnkle, query=True, t=True, ws=True )
    
    cmds.polyCreateFacet( p=[(upper[0]*100, upper[1]*100, upper[2]*100), (lower[0]*100, lower[1]*100, lower[2]*100), (wrist[0]*100, wrist[1]*100, wrist[2]*100)] )
    if utils.getIKSystem() == 'HingeLimb':
        cmds.polyCreateFacet( p=[(hip[0]*100, hip[1]*100, hip[2]*100), (upper[0]*100, upper[1]*100, upper[2]*100), (lower[0]*100, lower[1]*100, lower[2]*100)] )   



def relocateControllers(ctrls):
    if (utils.getIKSystem() == 'SimpleLimb' and utils.getFootReverse() == 'Yes') or utils.getIKSystem() == 'HingeLimb':
        cmds.select( ctrls[0] + 'Shape.cv[0:7]' )
        cmds.move( 0.2, 0, 0, r=True, os=True, wd=True)
        cmds.select( d=True )
 
        
    if utils.getIKSystem() == 'HingeLimb':
        cmds.select( ctrls[9] + '_Shape.cv[0:16]' )
    else:
        cmds.select( ctrls[6] + '_Shape.cv[0:16]' )

    cmds.move( 0, -0.05, -0.17, r=True, os=True, wd=True)

    for n in range(cmds.intSliderGrp( 'NumFingerToes', q=True, v=True )):
        if utils.getIKSystem() == 'HingeLimb':
            rotateToeController(ctrls[11 + n])     
        else:
            rotateToeController(ctrls[8 + n])



def rotateToeController(toeName):
    cmds.select( toeName )
    cmds.select( toeName + 'Shape.cv[0:7]' )
    cmds.rotate(  0, '90deg', 0 )
    cmds.move( 0.035, 0, 0, r=True, os=True, wd=True)
    cmds.scale( 1.25, 1, 1 )
    cmds.select( d=True )



def getListControllers():
    assignVariables()
    side = utils.getSideFromBone( JNT_ClavHip )
    position = utils.getPositionFromBone( JNT_ClavHip )
    ctrls = []
    for o in offsetsLimb:
        ctrl = 'CTRL__' + side + position + o
        ctrls.append( ctrl )

    return ctrls



def createReverseFootSetUp(wristAnkleIK):
    global rev
    rev = []
    
    for x in range(6):
        name = 'REV' + sidePos + reverseFoot[x]
        grp = cmds.group( em=True, n=name )
        rev.append(grp)
    
    cmds.parent( rev[5], rev[4] )
    cmds.parent( rev[4], rev[3] )
    cmds.parent( rev[3], rev[2] )
    cmds.parent( rev[2], rev[1] )
    cmds.parent( rev[1], rev[0] )
    cmds.parent( rev[0], wristAnkleIK )  
    
    ball = cmds.xform(JNT_HandFoot, ws=True, t=True, q=True)
    cmds.move( ball[0], ball[1], ball[2], rev[4]+'.scalePivot', rev[4]+'.rotatePivot', a=True )
    wristAnkle = cmds.xform(wristAnkleIK, ws=True, t=True, q=True)
    cmds.move( wristAnkle[0], wristAnkle[1], wristAnkle[2], rev[5]+'.scalePivot', rev[5]+'.rotatePivot', a=True )



def createLimbSystem():
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    RTvars.limbStartingBone = sel[0]
    utils.printHeader('CREATING LIMB SYSYEM')
    mel.eval('MLdeleteUnused;')
    
    if utils.getFootReverse() == 'Yes':
        if not checkIfFootReverseIsSet():
            result = cmds.confirmDialog( t='Foot reverse Setup', m='Something in the Reverse Foot is not set properly.\nMaybe you forgot to move some anchor. Do you want to continue?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName )
            if result == 'No':
                return
    
    utils.lockControllers(getListControllers(), False)
    if cmds.checkBox( 'UseMirrorCB', q=True, v=True ):
        createMirror()
        connectLimb()
        RT_FillTools.reloadMirror(limbBones)
        connectLimb()
    else:
        connectLimb()



def checkIfFootReverseIsSet():
    assignVariables()
    pos = cmds.xform(REV_Ext, q=True, sp=True )
    add = 0
    for p in pos:
        add += p;
    
    if getWorldScalePivotInfo(REV_Ext)==0 or getWorldScalePivotInfo(REV_Int)==0 or getWorldScalePivotInfo(REV_Tip)==0:
        return False
    else:
        return True



def createPoleVectorHelpers(JNT_PV, CTRL_PV, PV_LINE):
    utils.printHeader('CRETTING HELPERS FOR POLE VECTOR')
         
    p1 = cmds.xform( JNT_PV, query=True, t=True, ws=True )
    p2 = cmds.xform( CTRL_PV, query=True, t=True, ws=True )
    
    cmds.curve( n=PV_LINE, d=1, p=[(p1[0], p1[1], p1[2]), (p2[0], p2[1], p2[2])], k=[0,1] )
    cmds.parent( PV_LINE, 'Helpers' )
    cmds.editDisplayLayerMembers( 'CONTROLLERS', PV_LINE, nr=True )
    PVLineShape = cmds.listRelatives(PV_LINE, s=True)
    cmds.select( PVLineShape )
    cmds.rename( PVLineShape[0], PV_LINE + '_Shape' )
    col = (1, 0, 0) if utils.getSideFromBone(PV_LINE) == 'L_' else (0, 1, 0)
    RTctrl.overrideColor(PV_LINE + '_Shape', col)
    
    iniCluster = createClusters(PV_LINE, JNT_PV[3:], '0')
    endCluster = createClusters(PV_LINE, CTRL_PV[4:], '1')
    cmds.pointConstraint( JNT_PV, iniCluster, n=utils.getConstraint('Point', iniCluster[4:][:-7]) )
    cmds.pointConstraint( CTRL_PV, endCluster, n=utils.getConstraint('Point', endCluster[4:][:-7]) )
    
    utils.lockAndHideAttribute(PV_LINE, True, True)



def createClusters(line, name, index):
    cmds.select( line + '_Shape.cv[' + index + ']' )
    clusterName = 'CLST' + name + '_'
    cmds.cluster( n=clusterName )
    clh = clusterName + 'Handle'
    cmds.parent( clh, 'Helpers' )
    cmds.editDisplayLayerMembers( 'HELPERS', clh, nr=True )
    return clh



def mirrorControllers():
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    RTvars.limbStartingBone = sel[0]
    mel.eval('MLdeleteUnused;')
    utils.lockControllers(getListControllers(), False)
    createMirror()



def createMirror():
    assignVariables()
    utils.printHeader('MIRRORING LIMB')
    side = '__' + utils.getSideFromBone(RTvars.limbStartingBone)
    newSide = '__R_' if side == '__L_' else '__L_'
    cmds.select( RTvars.limbStartingBone )
    utils.printSubheader('Mirroring joint hierarchy')
    cmds.mirrorJoint( myz=True, mb=True, sr=(side, newSide) )
    createMirrorControllers(side, newSide)


side = '__L_'
newSide = '__R_' if side == '__L_' else '__L_'
o = 'OFFSET__L_HipHead'

def createMirrorControllers(side, newSide):
    offsets = []
    for o in offsetsLimb:
        offset = 'OFFSET' + sidePos + o
        offsets.append(offset)

    for o, s in zip(offsets, ctrlLimbBones):
        utils.printSubheader('Mirroring controller --> ' + o)
        nameMirror = o.replace(side, newSide)
        mirror = cmds.duplicate( o, n=nameMirror, rc=True )
        mirrorGrp = cmds.group( em=True, n='MIRROR_GRP', w=True )
        cmds.parent( mirror[0], mirrorGrp )
        cmds.select( mirrorGrp )
        cmds.setAttr( mirrorGrp + '.scaleX', -1 )
        
        if s[3] == 'Object':
            cmds.refresh()
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            tempGrp = cmds.group( em=True, n='TMP_GRP', w=True )
            cmds.parent( tempGrp, 'JNT' + mirror[0][6:] )
            utils.setTransformAndRotationToZero(tempGrp)
            cmds.parent( tempGrp, w=True )
            cmds.parent( mirror[0], tempGrp )
            cmds.refresh()
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            cmds.parent( mirror[0], w=True )
            cmds.delete( tempGrp, mirrorGrp )
            
        else:
            if o.find('Clavicle') > -1 or o.find('HipHead') > -1:
                cmds.refresh()
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                tempGrp = cmds.group( em=True, n='TMP_GRP', w=True )
                cmds.setAttr( tempGrp + '.rotateX', 180 )
                pConstTmpGrp = cmds.pointConstraint( mirror[0], tempGrp, mo=False )
                cmds.delete( pConstTmpGrp )
                cmds.parent( mirror[0], tempGrp )
                cmds.refresh()
                cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
                cmds.parent( mirror[0], w=True )
                cmds.delete( tempGrp, mirrorGrp )
            else:
                cmds.parent( mirror[0], w=True )
                cmds.refresh()
                cmds.makeIdentity(apply=True, r=1, s=1, n=0)
                cmds.delete( mirrorGrp )
        
        if (nameMirror.find('_Hand') > -1) or (nameMirror.find('_Foot') > -1): 
            cmds.setAttr( nameMirror + '.rotateX', 0 )
        
        for n in cmds.listRelatives( mirror[0], ad=True, s=False ):
            newName = n.replace(side, newSide)[:-1]
            cmds.rename( n, newName )
            col = (0, 1, 0) if side == '__L_' else (1, 0, 0)
            RTctrl.overrideColor(newName, col)



def getWorldScalePivotInfo(rev):
    pos = cmds.xform(rev, q=True, sp=True )
    magnitude = 0
    for p in pos:
        magnitude += p;
    
    return magnitude



def createReverseJoint():
    utils.printHeader('Create Reverse Joint')
    cmds.select( d=True )
    revJnt = 'REV_JNT' + sidePos + reverseFoot[5]
    RT_Utilities.createSimpleJoint('World', revJnt)
    cmds.editDisplayLayerMembers( 'defaultLayer', revJnt, nr=True )
    RTvars.ctrlColor = utils.getColorFromSide(revJnt)
    RTctrl.colorizeController()
    cmds.parent( revJnt, CTRL_WristAnkle )
    utils.setTransformAndRotationToZero(revJnt)
    utils.hideAttributes(revJnt, 0)



def connectLimb():
    utils.printHeader('CONNECTINC LIMB')
    assignVariables()
    createReverseJoint()
    createPoleVectorHelpers(JNT_LowerLimb, CTRL_LowerLimbPV, PV_LowerLine)
    if utils.getIKSystem() == 'HingeLimb':
        createPoleVectorHelpers(JNT_UpperLimb, CTRL_UpperLimbPV, PV_UpperLine)
    createSnapHelpers()
    
    cmds.editDisplayLayerMembers( 'JOINTS', JNT_ClavHip, nr=True )   

    #############################
    utils.printSubheader('Setting IK System')
    if utils.getIKSystem() == 'HingeLimb':
        createIKHandlerWithGroup(JNT_ClavHip, JNT_LowerLimb)
        createIKHandlerWithGroup(JNT_UpperLimb, JNT_WristAnkle)
        groupIKHs = 'OFFSET_IKH' + sidePos + 'HingeLeg'
        cmds.group( em=True, n=groupIKHs )
        cmds.parent( getOffset(IKH_LowerLimb), getOffset(IKH_WristAnkle), groupIKHs )
        posIKH = cmds.xform( IKH_WristAnkle , ws=True, t=True, q=True)
        cmds.move( posIKH[0], posIKH[1], posIKH[2], groupIKHs + '.scalePivot', groupIKHs + '.rotatePivot', a=True )
        cmds.poleVectorConstraint( CTRL_UpperLimbPV, IKH_LowerLimb, n=utils.getConstraint('PoleVector', IKH_LowerLimb[3:]) )
        cmds.poleVectorConstraint( CTRL_LowerLimbPV, IKH_WristAnkle, n=utils.getConstraint('PoleVector', IKH_WristAnkle[3:]) )
        cmds.pointConstraint( REV_WristAnkle, groupIKHs, n=utils.getConstraint('Point', groupIKHs[10:]), mo=True )
        cmds.pointConstraint( REV_WristAnkle, 'IKH' + JNT_LowerLimb[3:], n=utils.getConstraint('Point', JNT_LowerLimb[3:]), mo=True )
        cmds.pointConstraint( REV_WristAnkle, 'IKH' + JNT_WristAnkle[3:], n=utils.getConstraint('Point', JNT_WristAnkle[3:]), mo=True )
        cmds.pointConstraint( CTRL_LowerLimbIK, 'IKH' + JNT_LowerLimb[3:], n=utils.getConstraint('Point', JNT_LowerLimb[3:]), mo=True )
        cmds.pointConstraint( CTRL_WristAnkle_IK, 'OFFSET' + CTRL_LowerLimbIK[4:], n=utils.getConstraint('Point', CTRL_LowerLimbIK[4:]), mo=True )
        
        cmds.parent( groupIKHs, 'Helpers' )
        cmds.editDisplayLayerMembers( 'HELPERS', groupIKHs, nr=True )
    else:
        createIKHandler(JNT_UpperLimb, JNT_WristAnkle)
        cmds.poleVectorConstraint( CTRL_LowerLimbPV, IKH_WristAnkle, n=utils.getConstraint('PoleVector', IKH_WristAnkle[3:]) )
        cmds.pointConstraint( REV_WristAnkle, IKH_WristAnkle, n=utils.getConstraint('Point', IKH_WristAnkle[3:]), mo=True )
        cmds.parent( IKH_WristAnkle, 'Helpers' )
        cmds.editDisplayLayerMembers( 'HELPERS', IKH_WristAnkle, nr=True )
    
   #############################
    utils.printSubheader('Creating FK Constraints of the Limb')
    if utils.getIKSystem() == 'HingeLimb':
        cmds.orientConstraint( CTRL_ClavHip, JNT_ClavHip, n=utils.getConstraint('Orient', JNT_ClavHip[3:]), mo=True )
    else:
        cmds.parentConstraint( CTRL_ClavHip, JNT_ClavHip, n=utils.getConstraint('Parent', JNT_ClavHip[3:]), mo=True )
    cmds.orientConstraint( CTRL_UpperLimb, JNT_UpperLimb, n=utils.getConstraint('Orient', JNT_UpperLimb[3:]), mo=True )
    cmds.orientConstraint( CTRL_LowerLimb, JNT_LowerLimb, n=utils.getConstraint('Orient', JNT_LowerLimb[3:]), mo=True )
    cmds.orientConstraint( CTRL_HandFoot, JNT_HandFoot, n=utils.getConstraint('Orient', JNT_HandFoot[3:]), mo=True )
    
    #############################
    utils.printSubheader('Creating FK Constraints of the Foot')
    fingToeJoints = [ JNT_FingToeRing, JNT_FingToeMid, JNT_FingToeInd, JNT_FingToeThumb, JNT_FingToePinky ]
    fingToeControllers = [ CTRL_FingToeRing, CTRL_FingToeMid, CTRL_FingToeInd, CTRL_FingToeThumb, CTRL_FingToePinky ]
    
    for n in range(cmds.intSliderGrp( 'NumFingerToes', q=True, v=True )):
        cmds.orientConstraint( fingToeControllers[n], fingToeJoints[n], n=utils.getConstraint('Orient', fingToeJoints[n][3:]), mo=True )
        cmds.parent( getOffset(fingToeControllers[n]), CTRL_HandFoot )

    offsetConst = utils.getConstraint('Parent', CTRL_HandFoot[4:])
    cmds.parentConstraint( REV_WristAnkle if utils.getFootReverse() == 'No' else REV_Tip, REV_JNT_WristAnkle, getOffset(CTRL_HandFoot), n=offsetConst, mo=True )
    cmds.setAttr( offsetConst + '.interpType', 2)

    #############################
    utils.printSubheader('Creating Double Constraints for FKIK')
    offsetConst = utils.getConstraint('Orient', JNT_WristAnkle[3:])
    cmds.orientConstraint( REV_WristAnkle, REV_JNT_WristAnkle, JNT_WristAnkle, mo=True, n=offsetConst )
    cmds.setAttr( offsetConst + '.interpType', 2)

    #############################
    utils.printSubheader('Creating the Ankle/Wrist connections for FKIK')
    cmds.parentConstraint( JNT_WristAnkle, getOffset(CTRL_LimbSwitch_FKIK), n=utils.getConstraint('Parent', CTRL_LimbSwitch_FKIK[4:]), mo=True)
    addAttribute(CTRL_LimbSwitch_FKIK, 'FKIK', 'Switch FK/IK', 0, 0, 1)
    if utils.getIKSystem() == 'HingeLimb':
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', IKH_LowerLimb + '.ikb') 
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', IKH_WristAnkle + '.ikb')
    reverseAnkle = utils.createShadingNode('reverse', CTRL_LimbSwitch_FKIK + '_Reverse')
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', reverseAnkle + '.inputX')
    cmds.connectAttr( reverseAnkle + '.outputX', utils.getConstraint('Parent', CTRL_HandFoot[4:]) + '.' + REV_JNT_WristAnkle + 'W1' )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', utils.getConstraint('Parent', CTRL_HandFoot[4:]) + '.' + (REV_WristAnkle if utils.getFootReverse() == 'No' else REV_Tip) + 'W0' )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', reverseAnkle + '.inputY')
    cmds.connectAttr( reverseAnkle + '.outputY', utils.getConstraint('Orient', JNT_WristAnkle[3:]) + '.' + REV_JNT_WristAnkle + 'W1' )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', utils.getConstraint('Orient', JNT_WristAnkle[3:]) + '.' + REV_WristAnkle + 'W0' )  

    ############################# 
    if utils.getIKSystem() == 'HingeLimb':
        utils.printSubheader('Creating Double Constraint for Hip/Clavivle')
        cmds.pointConstraint( CTRL_ClavHip_IK, CTRL_ClavHip, JNT_ClavHip, n=utils.getConstraint('Point', JNT_ClavHip[3:]), mo=True )
        reverseHip = utils.createShadingNode('reverse', CTRL_ClavHip + '_Reverse')
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', utils.getConstraint('Point', JNT_ClavHip[3:]) + '.' + CTRL_ClavHip_IK + 'W0' )
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', reverseHip + '.inputX')
        cmds.connectAttr( reverseHip + '.outputX', utils.getConstraint('Point', JNT_ClavHip[3:]) + '.' + CTRL_ClavHip + 'W1' )

    #############################
    utils.printSubheader('Connecting the FK hierarchy')
    cmds.parent( getOffset(CTRL_WristAnkle), CTRL_LowerLimb )
    cmds.parent( getOffset(CTRL_LowerLimb), CTRL_UpperLimb )
    cmds.parent( getOffset(CTRL_UpperLimb), CTRL_ClavHip )
    
    #############################
    utils.printSubheader('Setting the toggle visiblity for the controllers')
    if utils.getIKSystem() == 'HingeLimb':
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_ClavHip_IK + '.visibility', f=True )
        cmds.connectAttr( reverseAnkle + '.outputY', CTRL_ClavHip + '.visibility', f=True )
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_UpperLimbPV + '.visibility', f=True )
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', PV_UpperLine + '.visibility', f=True )
        cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_LowerLimbIK + '.visibility', f=True )

    cmds.connectAttr( reverseAnkle + '.outputY', CTRL_UpperLimb + '.visibility', f=True )
    cmds.connectAttr( reverseAnkle + '.outputY', CTRL_LowerLimb + '.visibility', f=True )
    cmds.connectAttr( reverseAnkle + '.outputY', CTRL_WristAnkle + '.visibility', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_WristAnkle_IK + '.visibility', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_LowerLimbPV + '.visibility', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', PV_LowerLine + '.visibility', f=True )
    
    if utils.getFootReverse() == 'Yes':
        createFootReverseSystem()
    else:
        if cmds.checkBox( 'UseDeleteHandFootCB', q=True, v=True ):
            for n in range(cmds.intSliderGrp( 'NumFingerToes', q=True, v=True )):
                cmds.parent( fingToeJoints[n], JNT_WristAnkle )
                cmds.parent( getOffset(fingToeControllers[n]), getOffset(CTRL_HandFoot) )
            cmds.delete( JNT_HandFoot, CTRL_HandFoot )

    if cmds.checkBox( 'UseStretchCB', q=True, v=True ):
        createStretchSystem()

    RT_SpaceSwitch.createSpaceSwitch('LimbSpace', CTRL_LowerLimbPV, 'CTRL__Master', CTRL_WristAnkle_IK, 'Parent')
    if utils.getIKSystem() == 'HingeLimb':
        RT_SpaceSwitch.createSpaceSwitch('LimbSpace', CTRL_UpperLimbPV, 'CTRL__Master', CTRL_WristAnkle_IK, 'Parent')

    #############################
    utils.printSubheader('Locking and hidding unused attributes')
    utils.lockAndHideAttribute(CTRL_ClavHip, False, False)
    utils.lockAndHideAttribute(CTRL_UpperLimb, True, False)
    utils.lockAndHideAttribute(CTRL_LowerLimb, True, False)
    utils.lockAndHideAttribute(CTRL_WristAnkle, True, False)
    if utils.getFootReverse() == 'Yes' or not cmds.checkBox( 'UseDeleteHandFootCB', q=True, v=True ):
        utils.lockAndHideAttribute(CTRL_HandFoot, True, False)
    for n in range(cmds.intSliderGrp( 'NumFingerToes', q=True, v=True )): 
        utils.lockAndHideAttribute(fingToeControllers[n], True, False)
    utils.lockAndHideAttribute(CTRL_WristAnkle_IK, False, False)
    if utils.getIKSystem() == 'HingeLimb':
        utils.lockAndHideAttribute(CTRL_ClavHip_IK, False, True)
        utils.lockAndHideAttribute(CTRL_UpperLimbPV, False, True)
        utils.lockAndHideAttribute(CTRL_LowerLimbIK, False, True)
        cmds.setAttr( CTRL_LowerLimbIK + '.translateX', k=False, l=True, cb=False )
        cmds.setAttr( CTRL_LowerLimbIK + '.translateY', k=False, l=True, cb=False )  
    utils.lockAndHideAttribute(CTRL_LowerLimbPV, False, True)
    utils.lockAndHideAttribute(CTRL_LimbSwitch_FKIK, True, True)

    cmds.select( d=True )



def addAttribute(ctrl, name, niceName, defaultV, minV, maxV):
    if niceName=='':
        niceName=name
    cmds.addAttr( ctrl, ln=name, nn=niceName, at='float',  k=True, dv=defaultV, min=minV, max=maxV )



def getOffset(ctrl):
    return cmds.listRelatives( ctrl, p=True )



def createFootReverseSystem():
    utils.printHeader('ADDING REVERSE FOOT')
    
    #############################
    utils.printSubheader('Adding attributes')
    utils.addAttrSeparator(CTRL_WristAnkle_IK, 'RevFootSeparator', 'REVERSE  FOOT')
    addAttribute(CTRL_WristAnkle_IK, 'FootRoll', 'Roll', 0, -80, 80)
    addAttribute(CTRL_WristAnkle_IK, 'FootRollWeight', 'Roll Weight', 0, 0, 1)
    addAttribute(CTRL_WristAnkle_IK, 'FootBalance', 'Balance', 0, -80, 80)
    
    #############################
    utils.printSubheader('Setting Foot Roll connections')
    conditionRoll = utils.createShadingNode('condition', CTRL_WristAnkle_IK + '_ConditionRoll')
    cmds.setAttr( conditionRoll + '.operation', 4 )
    cmds.setAttr( conditionRoll + '.colorIfFalseR', 0 )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRoll', conditionRoll + '.colorIfFalseG' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRoll', conditionRoll + '.colorIfTrueR' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRoll', conditionRoll + '.firstTerm' )
    cmds.connectAttr( conditionRoll + '.outColorR', REV_Heel + '.rotateX')
    
    #############################
    utils.printSubheader('Setting Foot Roll Weight connections')
    blendColorFootWeight = utils.createShadingNode('blendColors', CTRL_WristAnkle_IK + '_BlendColorFootWeight')
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRollWeight', blendColorFootWeight + '.blender')
    cmds.connectAttr( conditionRoll + '.outColorG', blendColorFootWeight + '.color1R')
    cmds.connectAttr( conditionRoll + '.outColorG', blendColorFootWeight + '.color2G')
    cmds.connectAttr( blendColorFootWeight + '.outputR', REV_Tip + '.rotateX')
    cmds.connectAttr( blendColorFootWeight + '.outputG', REV_Ball + '.rotateX')
    
    #############################
    utils.printSubheader('Setting Foot Balance connections')
    conditionBalance = utils.createShadingNode('condition', CTRL_WristAnkle_IK + '_ConditionBalance')
    cmds.setAttr( conditionBalance + '.operation', 2 )
    cmds.setAttr( conditionBalance + '.colorIfFalseR', 0 )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootBalance', conditionBalance + '.colorIfFalseG' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootBalance', conditionBalance + '.colorIfTrueR' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootBalance', conditionBalance + '.firstTerm' )
    multDivReverse = utils.createShadingNode('multiplyDivide', CTRL_WristAnkle_IK + '_MultDivReverse')
    cmds.setAttr( multDivReverse + '.input2X', -1 )
    cmds.setAttr( multDivReverse + '.input2Y', -1 )
    cmds.connectAttr( conditionBalance + '.outColorR', multDivReverse + '.input1X' )
    cmds.connectAttr( conditionBalance + '.outColorG', multDivReverse + '.input1Y' )
    cmds.connectAttr( multDivReverse + '.outputX', REV_Ext + '.rotateZ' )
    cmds.connectAttr( multDivReverse + '.outputY', REV_Int + '.rotateZ' )



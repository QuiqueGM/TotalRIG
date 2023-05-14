import RiggingTools as RT
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_HandsSetup as RThands
import RT_Controllers as RTctrl
import RT_ChainTools
import RT_Utils as utils
import RT_Utilities
import RT_SpaceSwitch
import RT_Rename
import maya.cmds as cmds
import maya.mel as mel
from functools import partial



def drawUI():
    RT.toolHeader('limbSystemTab', '---------   LIMB SYSTEM  ---------')
    RT.subHeader(1, 'TYPE OF LIMB', 5)
    RT.createLegOption('Hierarchy', 'FrontLimb', 'Front Leg / Arm', True, 'BackLimb', 'Back Leg / Leg', False)
    winWidth = RT.winWidth
    rowWidth = [winWidth*0.05, winWidth*0.25, winWidth*0.3, winWidth*0.3]
    
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l='IK System', w=rowWidth[1], al='left')
    cmds.radioButton( 'SimpleLeg', l='Simple IK', al='center', w=rowWidth[2], sl=True )
    cmds.radioButton( 'HindLeg', l='Hind Leg', al='center', w=rowWidth[2], sl=False )
    cmds.setParent( '..' )
    
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l='Foot Reverse', w=rowWidth[1], al='left')
    cmds.radioButton( 'FootReverseYes', l='Yes', al='center', w=rowWidth[2], sl=True, onc=partial(enableDeleteHandFoot, False) )
    cmds.radioButton( 'FootReverseNo', l='No', al='center', w=rowWidth[2], sl=False, onc=partial(enableDeleteHandFoot, True) )
    cmds.setParent( '..' )
    
    RT.createTwoButtonsAction(7,'cc', 'Create controllers', createLimbControllers, 'mc', 'Mirror controllers', mirrorControllers, False)
    RT.subHeader(7, 'OPTIONS', 5)
    RT.createCheckbox(0.1, 'UseDeleteHandFootCB', 'Remove Hand/Foot', RT.emptyCallback, True, False)
    RT.createCheckbox(0.1, 'UseMirrorCB', 'Actvate mirror', RT.emptyCallback, True, True)
    RT.createCheckbox(0.1, 'UseStretchCB', 'Create stretch system', RT.emptyCallback, True, True)
    createLimbFields()
    RT.createButtonAction(10,'', 'Create Limb System', createLimbSystem, False)
    RT.createSpaceForUtilities('---------   UTILITIES  ---------')
    RT.createButtonAction(3,'', 'Convert IK World to IK Object', convertIKtoObject, False)
    RT.createTwoButtonsAction(3,'dwl', 'Delete whole limb', deleteLimb, 'dls', 'Delete limb system', deleteLimbSystem, True)



def enableDeleteHandFoot(value, *args):
    cmds.checkBox( 'UseDeleteHandFootCB', edit=True, en=value )



def createLimbFields():
    bones = []
    bones.extend(RTvars.bonesHindArm)
    bones.extend(RTvars.simpleHand)
    bones.extend(RTvars.hand)
    bones.extend(RTvars.bonesHindLeg)
    bones.extend(RTvars.simpleFoot)
    bones.extend(RTvars.foot)
    
    winWidth = RT.winWidth
    rowWidth = [winWidth*0.2, winWidth*0.60, winWidth*0.3]
    for b in range(len(bones)):
        cmds.textFieldButtonGrp( bones[b], l=bones[b], vis=False, ed=False, cw3=rowWidth, cl3=('left', 'left', 'left'), bl='  Add  ', bc=partial(RT.addObject, bones[b]), h=20 )



'''
### LIMB SYSTEM

def createLimbControllers(*args):
    RT_LimbSystem.createLimbControllers()

def mirrorControllers(*args):
    RT_LimbSystem.mirrorControllers()

def createLimbSystem(*args):
    RT_LimbSystem.createLimbSystem()

def convertIKtoObject(*args):
    RT_LimbSystem.convertIKtoObject()

def deleteLimb(*args):
    RT_LimbSystem.deleteLimb()

def deleteLimbSystem(*args):
    RT_LimbSystem.deleteLimbSystem()

def createStretchSystem(*args):
    RT_LimbSystem.createStretchSystem(*args)

def createSSforPoleVector(*args):
    RT_LimbSystem.createSSforPoleVector()
'''




def assignVariables(autoFill = True):
    global limbBones, newLimbBones, offsetsLimb, ctrlLimbBones, reverseFoot, sidePos
    global JNT_ClavHipHead, JNT_ClavHip, JNT_UpperLimb, JNT_LowerLimb, JNT_WristAnkle, JNT_HandFoot, JNT_FingToeIndex, JNT_FingToeMiddle, JNT_FingToeRing, JNT_FingToeThumb, JNT_FingToePinky
    global CTRL_ClavHipHead, CTRL_ClavHip, CTRL_UpperLimb, CTRL_LowerLimb, CTRL_WristAnkle, CTRL_HandFoot
    global CTRL_WristAnkle_IK, CTRL_UpperLimbPV, CTRL_LowerLimbPV, CTRL_LowerLimbIK, CTRL_LimbSwitch_FKIK
    global REV_Orient, REV_Heel, REV_Ext, REV_Int, REV_Tip, REV_Ball, REV_WristAnkle, REV_JNT_WristAnkle, IKH_Group, IKH_LowerLimb, IKH_WristAnkle, PV_UpperLine, PV_LowerLine
    global snapGroups
    global mirror
    
    cmds.select( RTvars.limbStartingBone )
    sel = cmds.ls(sl=True)[0]
    if autoFill: autofillFromSelection()
    sidePos = '__' + utils.getSideFromBone(sel) + utils.getPositionFromBone(sel)

    if utils.getHierarchy() == 'Leg':
        if utils.getIKSystem() == 'HindLimb':
            limbBones = RTvars.bonesHindLeg
            offsetsLimb = RTvars.offsetsHindLeg
            snapGroups = RTvars.snapHindLeg
            CTRL_UpperLimbPV = 'CTRL' + sidePos + 'UpperLeg_PV'
            PV_UpperLine = 'LINE' + sidePos + 'UpperLeg_PV'
            CTRL_LowerLimbIK = 'CTRL' + sidePos + 'LowerLeg_IK'
            IKH_LowerLimb = 'IKH' + sidePos + 'LowerLeg'
        else:
            limbBones = RTvars.legBones
            offsetsLimb = RTvars.offsetsLeg
            snapGroups = RTvars.snapLeg
                                 
        reverseFoot = RTvars.reverseFoot
        JNT_ClavHipHead = cmds.textFieldGrp( 'HipHead' ,q=True, tx=True )
        JNT_ClavHip = cmds.textFieldGrp( 'Hip' ,q=True, tx=True )
        JNT_UpperLimb = cmds.textFieldGrp( 'UpperLeg' ,q=True, tx=True )
        JNT_LowerLimb = cmds.textFieldGrp( 'LowerLeg' ,q=True, tx=True )
        JNT_WristAnkle = cmds.textFieldGrp( 'Ankle' ,q=True, tx=True )
        JNT_HandFoot = cmds.textFieldGrp( 'Foot' ,q=True, tx=True )

        CTRL_LowerLimbPV = 'CTRL' + sidePos + 'LowerLeg_PV'
        PV_LowerLine = 'LINE' + sidePos + 'LowerLeg_PV'
        CTRL_LimbSwitch_FKIK = 'CTRL' + sidePos + 'LegSwitch_FKIK'
        REV_WristAnkle = 'REV' + sidePos + 'Ankle'
        REV_JNT_WristAnkle = 'REV_JNT' + sidePos + 'Ankle'
        IKH_Group = 'IKH_SYSTEM' + sidePos + 'Ankle'
        IKH_LowerLimb = 'IKH' + sidePos + 'LowerLeg'
        IKH_WristAnkle = 'IKH' + sidePos + 'Ankle'
        
    else:
        if utils.getIKSystem() == 'HindLimb':
            limbBones = RTvars.bonesHindArm
            offsetsLimb = RTvars.offsetsHindArm
            snapGroups = RTvars.snapHindArm
            CTRL_UpperLimbPV = 'CTRL' + sidePos + 'Arm_PV'
            PV_UpperLine = 'LINE' + sidePos + 'Arm_PV'
            CTRL_LowerLimbIK = 'CTRL' + sidePos + 'Forearm_IK'
            IKH_LowerLimb = 'IKH' + sidePos + 'Forearm'
        else:
            limbBones = RTvars.armBones
            offsetsLimb = RTvars.offsetsArm
            snapGroups = RTvars.snapArm
            
        reverseFoot = RTvars.reverseHand
        JNT_ClavHipHead = cmds.textFieldGrp( 'ClavicleHead' ,q=True, tx=True ) 
        JNT_ClavHip = cmds.textFieldGrp( 'Clavicle' ,q=True, tx=True ) 
        JNT_UpperLimb = cmds.textFieldGrp( 'Arm' ,q=True, tx=True )
        JNT_LowerLimb = cmds.textFieldGrp( 'Forearm' ,q=True, tx=True )
        JNT_WristAnkle = cmds.textFieldGrp( 'Wrist' ,q=True, tx=True )
        JNT_HandFoot = cmds.textFieldGrp( 'Hand' ,q=True, tx=True )
        
        CTRL_LowerLimbPV = 'CTRL' + sidePos + 'Forearm_PV'
        PV_LowerLine = 'LINE' + sidePos + 'Forearm_PV'
        CTRL_LimbSwitch_FKIK = 'CTRL' + sidePos + 'ArmSwitch_FKIK'
        REV_WristAnkle = 'REV' + sidePos + 'Wrist'
        REV_JNT_WristAnkle = 'REV_JNT' + sidePos + 'Wrist'
        IKH_Group = 'IKH_SYSTEM' + sidePos + 'Wrist'
        IKH_WristAnkle = 'IKH' + sidePos + 'Wrist'

    if utils.getIKSystem() == 'HindLimb':
        ctrlLimbBones = [[limbBones[0], 'Circle', 0.1, 'Object', offsetsLimb[0]], [limbBones[1], 'Circle', 0.1, 'Object', ''], [limbBones[2], 'Circle', 0.14, 'Object', ''], [limbBones[2], 'Diamond', 0.035, 'World', offsetsLimb[3]], [limbBones[3], 'Circle', 0.13, 'Object', ''], [limbBones[3], 'Diamond', 0.035, 'World', offsetsLimb[5]], [limbBones[3], 'DoubleArrow', 0.1, 'World', offsetsLimb[6]], [limbBones[4], 'Circle', 0.1, 'Object', ''], [limbBones[4], 'Box', 0.15, 'World', offsetsLimb[8]], [limbBones[4], 'Box', 0.03, 'World', offsetsLimb[9]], [limbBones[5], 'Box', 0.125, 'World', '']]#, [limbBones[6], 'Circle', 0.04, 'Object', ''], [limbBones[7], 'Circle', 0.04, 'Object', ''], [limbBones[8], 'Circle', 0.04, 'Object', ''], [limbBones[9], 'Circle', 0.04, 'Object', ''], [limbBones[10], 'Circle', 0.04, 'Object', '']]
    else:
        ctrlLimbBones = [[limbBones[0], 'Circle', 0.1, 'World', ''], [limbBones[1], 'Circle', 0.14, 'Object', ''], [limbBones[2], 'Circle', 0.13, 'Object', ''], [limbBones[2], 'Diamond', 0.035, 'World', offsetsLimb[3]], [limbBones[3], 'Circle', 0.1, 'Object', ''], [limbBones[3], 'Box', 0.15, 'World', offsetsLimb[5]], [limbBones[3], 'Box', 0.03, 'World', offsetsLimb[6]], [limbBones[4], 'Box', 0.125, 'World', '']]#, [limbBones[5], 'Circle', 0.04, 'Object', ''], [limbBones[6], 'Circle', 0.04, 'Object', ''], [limbBones[7], 'Circle', 0.04, 'Object', ''], [limbBones[8], 'Circle', 0.04, 'Object', ''], [limbBones[9], 'Circle', 0.04, 'Object', '']]
    
    CTRL_ClavHipHead = 'CTRL' + JNT_ClavHipHead[3:]
    CTRL_ClavHip = 'CTRL' + JNT_ClavHip[3:]
    CTRL_UpperLimb = 'CTRL' + JNT_UpperLimb[3:]
    CTRL_LowerLimb = 'CTRL' + JNT_LowerLimb[3:]
    CTRL_WristAnkle = 'CTRL' + JNT_WristAnkle[3:]
    CTRL_HandFoot = 'CTRL' + JNT_HandFoot[3:]
    CTRL_WristAnkle_IK = CTRL_WristAnkle + '_IK'
    
    REV_Heel = 'REV' + sidePos + reverseFoot[0]
    REV_Ext = 'REV' + sidePos + reverseFoot[1]
    REV_Int = 'REV' + sidePos + reverseFoot[2]
    REV_Tip = 'REV' + sidePos + reverseFoot[3]
    REV_Ball = 'REV' + sidePos + reverseFoot[4]
    
    offsetsLimb = utils.createLimbArray(offsetsLimb)
    newLimbBones = utils.createLimbArray(limbBones)
    
    for n in range(len(limbBones), len(newLimbBones)):
        ctrl = [newLimbBones[n], 'Circle', RThands.getFingerSizeController(), 'Object', '']
        ctrlLimbBones.append(ctrl)



def autofillFromSelection():
    utils.printHeader('AUTOFILL LIMB')

    bones = utils.createLimbArray(RTvars.bonesHindArm if utils.getHierarchy() == 'Arm' else RTvars.bonesHindLeg)
    bones = utils.getLimbBones(bones)
    sel = cmds.listRelatives( cmds.ls(sl=True), ad=True )
    sel.append( cmds.ls(sl=True)[0] )

    for s in sel:
        res = s.find('END')
        if (res > -1):
            sel.remove(s)
       
    for s in sel:
        cmds.select(s)
        for b in bones:
            res = s.find(b)
            if (res > -1):
                utils.addObject(b)
                break



def createLimbControllers(*args):
    RT_Rename.autorenameLimb()
    createLimbBackUp(RTvars.limbStartingBone)
    assignVariables()
    
    utils.printHeader('CREATING LIMB CONTROLLERS')
    numFingers = len(newLimbBones) - len(limbBones)
    
    for b in range(len(ctrlLimbBones)): 
        utils.printSubheader('Creating controller --> ' + offsetsLimb[b])
        cmds.select( cmds.textFieldGrp( ctrlLimbBones[b][0], q=True, tx=True ))
        sel = cmds.ls(sl=True)
        
        doubleOffset = True if b >= len(ctrlLimbBones)-numFingers else False
        hideAndLockOffset = False if ctrlLimbBones[b][4].find('_PV') > -1 else True
        ctrl = RTctrl.createController( ctrlLimbBones[b][1], utils.getColorFromSide(sel[0]), ctrlLimbBones[b][2], ctrlLimbBones[b][3], ctrlLimbBones[b][0], ctrlLimbBones[b][4], doubleOffset, hideAndLockOffset )[1]
        
    ctrls = getListControllers()
    createShape()

    if utils.getFootReverse() == 'Yes':
        if utils.getIKSystem() == 'HindLimb':
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



def createLimbBackUp(limb):
    utils.printHeader('CREATING LIMB BACK-UP')
    nameBackUpLimp = limb + '_BACK_UP'
    backUpLimp = cmds.duplicate( limb, n=nameBackUpLimp, rc=True )
    
    backUpGroup = 'Back_Up_Limbs'
    try:
        grp = cmds.select( backUpGroup )
    except:
        cmds.group( em=True, n=backUpGroup )
    
    cmds.parent( backUpLimp[0], backUpGroup, rm=False )
    cmds.setAttr( backUpGroup + '.visibility', 0 )   



def createShape():
    hip = cmds.xform( JNT_ClavHip, query=True, t=True, ws=True )
    upper = cmds.xform( JNT_UpperLimb, query=True, t=True, ws=True, a=True)
    lower = cmds.xform( JNT_LowerLimb, query=True, t=True, ws=True )
    wrist = cmds.xform( JNT_WristAnkle, query=True, t=True, ws=True )
    
    cmds.polyCreateFacet( p=[(upper[0]*100, upper[1]*100, upper[2]*100), (lower[0]*100, lower[1]*100, lower[2]*100), (wrist[0]*100, wrist[1]*100, wrist[2]*100)] )
    if utils.getIKSystem() == 'HindLimb':
        cmds.polyCreateFacet( p=[(hip[0]*100, hip[1]*100, hip[2]*100), (upper[0]*100, upper[1]*100, upper[2]*100), (lower[0]*100, lower[1]*100, lower[2]*100)] )   



def relocateControllers(ctrls):
    if (utils.getIKSystem() == 'SimpleLimb' and utils.getFootReverse() == 'Yes') or utils.getIKSystem() == 'HindLimb':
        cmds.select( ctrls[0] + '_Shape.cv[0:7]' )
        cmds.move( 0.2, 0, 0, r=True, os=True, wd=True)
        cmds.select( d=True )
    
    if utils.getIKSystem() == 'HindLimb':
        cmds.select( ctrls[9] + '_Shape.cv[0:16]' )
    else:
        cmds.select( ctrls[6] + '_Shape.cv[0:16]' )

    cmds.move( 0, -0.05, -0.17, r=True, os=True, wd=True)
    
    if cmds.checkBox( 'ControllersAlongBonesCB', q=True, v=True ):
        controlsToRelocate = len(newLimbBones) - len(limbBones)
        for n in range(len(ctrls)-controlsToRelocate, len(ctrls)):
            rotateToeController(ctrls[n])     

    cmds.select( d=True )



def rotateToeController(toeName):
    cmds.select( toeName )
    cmds.select( toeName + '_Shape.cv[0:7]' )
    cmds.rotate(  0, '90deg', 0 )
    cmds.move( RThands.getFingerSizeController() * 0.9, 0, 0, r=True, os=True, wd=True)
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
    
    for rf in reverseFoot:
        rev = 'REV' + sidePos + rf
        utils.lockAndHideOffset(rev, True)



def createLimbSystem(*args):
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
        connectLimb(False)
        utils.reloadMirror(limbBones)
        connectLimb(True)
    else:
        connectLimb(False)



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



def createSnapHelpers():
    utils.printHeader('CREATING SNAP HELPERS')
    
    for sg in snapGroups:
        snapName = 'SNAP' + sidePos + sg
        snapGrp = cmds.group( em=True, n=snapName )
        cmds.parentConstraint( 'CTRL' + snapName[4:], snapGrp, n='TempSnapConstraint', mo=False )
        cmds.delete( 'TempSnapConstraint' )
        try:
            cmds.parent( snapGrp, 'JNT' + snapGrp[4:] )
        except:
            cmds.parent( snapGrp, 'JNT' + snapGrp[4:][:-3] )
        
        utils.hideAttributes(snapName, 0)
    
    if utils.getHierarchy() == 'Arm':
        snapHelperPV('Forearm', JNT_UpperLimb, JNT_WristAnkle, JNT_LowerLimb)
        if utils.getIKSystem() == 'HindLimb':
            snapHelperPV('Arm', JNT_ClavHip, JNT_LowerLimb, JNT_UpperLimb)
    else:
        snapHelperPV('LowerLeg', JNT_UpperLimb, JNT_WristAnkle, JNT_LowerLimb)
        if utils.getIKSystem() == 'HindLimb':
            snapHelperPV('UpperLeg', JNT_ClavHip, JNT_LowerLimb, JNT_UpperLimb)



def snapHelperPV(limb, JNT_PointUp, JNT_PointDown, JNT_PointMid):
    vectorPV = 'VECTOR' + sidePos + limb
    vector = cmds.polyCube( w=0.002, h=0.002, d=0.5, n=vectorPV )
    cmds.setAttr( vectorPV + '.translateZ', -0.25 )
    cmds.refresh()
    cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0 ) 
    cmds.move( 0, 0, 0, vectorPV + '.scalePivot', vectorPV + '.rotatePivot', a=True )
    
    snapPV = 'SNAP' + sidePos + limb + '_PV'
    snap = cmds.group( em=True, n=snapPV )
    cmds.setAttr( snap + '.translateZ', -0.4 )
    cmds.parent( snap, vectorPV )
    cmds.pointConstraint( JNT_PointUp, JNT_PointDown, vectorPV, mo=False, n=utils.getConstraint('Point', vectorPV[6:]) )
    cmds.aimConstraint( JNT_PointMid, vectorPV, n=utils.getConstraint('Aim', vectorPV[6:]), mo=False, w=1, aim=(0, 0, -1), u=(0, 1, 0), wut='vector', wu=(0, 1, 0) )       
    cmds.parent( vectorPV, 'Helpers' )
    cmds.editDisplayLayerMembers( 'HELPERS', vectorPV, nr=True )
    utils.hideAttributes(vectorPV, 0)



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



def mirrorControllers(*args):
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
    createLimbBackUp(cmds.ls(sl=True)[0])
    createMirrorControllers(side, newSide)



def createMirrorControllers(side, newSide):
    offsets = utils.getOffsetsLimb(offsetsLimb, sidePos)
    for o, s in zip(offsets, ctrlLimbBones):
        utils.printSubheader('Mirroring controller --> ' + o)
        utils.lockAndHideOffset(o, False)
        if utils.getFootReverse() == 'Yes':
            for rf in reverseFoot:
                rev = 'REV' + sidePos + rf
                utils.lockAndHideOffset(rev, False)
        
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
            if ((o.find('Clavicle') > -1 or o.find('Hip') > -1) and utils.getIKSystem() == 'SimpleLimb') or o.find('Head') > -1:
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
            try:
                RTctrl.overrideColor(newName, col)
            except:
                pass



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



def createControllersBackUp():
    utils.printHeader('CREATING CONTROLLERS BACK-UP')
    offsets = utils.getOffsetsLimb(offsetsLimb, sidePos)
    for o in offsets:
        utils.lockAndHideOffset(o, True)
        nameOffset = o + '_BACK_UP'
        backUpCtrl = cmds.duplicate( o, n=nameOffset, rc=True )
        cmds.parent( backUpCtrl[0], 'Back_Up_Limbs', rm=False )



def connectLimb(isMirror):
    utils.printHeader('CONNECTINC LIMB')
    
    assignVariables()
    createControllersBackUp()        
    createReverseJoint()
    createPoleVectorHelpers(JNT_LowerLimb, CTRL_LowerLimbPV, PV_LowerLine)
    if utils.getIKSystem() == 'HindLimb':
        createPoleVectorHelpers(JNT_UpperLimb, CTRL_UpperLimbPV, PV_UpperLine)
    createSnapHelpers()
    
    offsets = utils.getOffsetsLimb(offsetsLimb, sidePos)
    for o in offsets:
        utils.lockAndHideOffset(o, False)
        
    cmds.editDisplayLayerMembers( 'JOINTS', JNT_ClavHip, nr=True )   
    
    #############################
    utils.printSubheader('Setting IK System')
    
    cmds.group( em=True, n=IKH_Group )
    
    if utils.getIKSystem() == 'HindLimb':
        createIKHandlerWithGroup(JNT_ClavHip, JNT_LowerLimb)
        createIKHandlerWithGroup(JNT_UpperLimb, JNT_WristAnkle)
        cmds.parent( getOffset(IKH_LowerLimb), getOffset(IKH_WristAnkle), IKH_Group )
        posIKH = cmds.xform( IKH_WristAnkle , ws=True, t=True, q=True)
        cmds.move( posIKH[0], posIKH[1], posIKH[2], IKH_Group + '.scalePivot', IKH_Group + '.rotatePivot', a=True )
        cmds.poleVectorConstraint( CTRL_UpperLimbPV, IKH_LowerLimb, n=utils.getConstraint('PoleVector', IKH_LowerLimb[3:]) )
        cmds.poleVectorConstraint( CTRL_LowerLimbPV, IKH_WristAnkle, n=utils.getConstraint('PoleVector', IKH_WristAnkle[3:]) )
        cmds.pointConstraint( REV_WristAnkle, IKH_Group, n=utils.getConstraint('Point', IKH_Group[10:]), mo=True )
        cmds.pointConstraint( REV_WristAnkle, 'IKH' + JNT_LowerLimb[3:], n=utils.getConstraint('Point', JNT_LowerLimb[3:]), mo=True )
        cmds.pointConstraint( REV_WristAnkle, 'IKH' + JNT_WristAnkle[3:], n=utils.getConstraint('Point', JNT_WristAnkle[3:]), mo=True )
        cmds.pointConstraint( CTRL_LowerLimbIK, 'IKH' + JNT_LowerLimb[3:], n=utils.getConstraint('Point', JNT_LowerLimb[3:]), mo=True )
        cmds.pointConstraint( CTRL_WristAnkle_IK, 'OFFSET' + CTRL_LowerLimbIK[4:], n=utils.getConstraint('Point', CTRL_LowerLimbIK[4:]), mo=True )
    else:
        createIKHandlerWithGroup(JNT_UpperLimb, JNT_WristAnkle)
        cmds.parent( getOffset(IKH_WristAnkle), IKH_Group )
        posIKH = cmds.xform( IKH_WristAnkle , ws=True, t=True, q=True)
        cmds.move( posIKH[0], posIKH[1], posIKH[2], IKH_Group + '.scalePivot', IKH_Group + '.rotatePivot', a=True )
        cmds.poleVectorConstraint( CTRL_LowerLimbPV, IKH_WristAnkle, n=utils.getConstraint('PoleVector', IKH_WristAnkle[3:]) )
        cmds.pointConstraint( REV_WristAnkle, IKH_Group, n=utils.getConstraint('Point', IKH_Group[10:]), mo=True )
        cmds.pointConstraint( REV_WristAnkle, 'IKH' + JNT_WristAnkle[3:], n=utils.getConstraint('Point', JNT_WristAnkle[3:]), mo=True )

    cmds.parent( IKH_Group, 'Helpers' )
    cmds.editDisplayLayerMembers( 'HELPERS', IKH_Group, nr=True )
    
    #############################
    utils.printSubheader('Creating FK Constraints of the Limb')
    if utils.getIKSystem() == 'HindLimb':
        cmds.orientConstraint( CTRL_ClavHip, JNT_ClavHip, n=utils.getConstraint('Orient', JNT_ClavHip[3:]), mo=True )
    else:
        cmds.parentConstraint( CTRL_ClavHip, JNT_ClavHip, n=utils.getConstraint('Parent', JNT_ClavHip[3:]), mo=True )
    cmds.orientConstraint( CTRL_UpperLimb, JNT_UpperLimb, n=utils.getConstraint('Orient', JNT_UpperLimb[3:]), mo=True )
    cmds.orientConstraint( CTRL_LowerLimb, JNT_LowerLimb, n=utils.getConstraint('Orient', JNT_LowerLimb[3:]), mo=True )
    cmds.orientConstraint( CTRL_HandFoot, JNT_HandFoot, n=utils.getConstraint('Orient', JNT_HandFoot[3:]), mo=True )
    
    #############################
    utils.printSubheader('Creating FK Constraints of the Foot')
    handFoot = RThands.getHandFootHierarchy()
    handFoot.reverse()
    for f in handFoot:
        for p in f:
            ctrl = 'CTRL' + sidePos + p
            jnt = 'JNT' + sidePos + p
            if (cmds.radioButton( 'HandsParentConst', q=True, sl=True )):
                cmds.parentConstraint( ctrl, jnt, n=utils.getConstraint('Parent', sidePos + p), mo=True )
                utils.lockAndHideAttribute(ctrl, False, False)
            elif (cmds.radioButton( 'HandsOrientConst', q=True, sl=True )):
                cmds.orientConstraint( ctrl, jnt, n=utils.getConstraint('Orient', sidePos + p), mo=True )
                utils.lockAndHideAttribute(ctrl, True, False)
            else:
                cmds.pointConstraint( ctrl, jnt, n=utils.getConstraint('Point', sidePos + p), mo=True )
                utils.lockAndHideAttribute(ctrl, False, True)
    
    for f in handFoot:
        for p in range(len(f)):
            try:
                cmds.parent( 'OFFSET' + sidePos + f[p], 'CTRL' + sidePos + f[p+1] )
            except:
                cmds.parent( 'OFFSET' + sidePos + f[p], CTRL_HandFoot )
            
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
    if utils.getIKSystem() == 'HindLimb':
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
    if utils.getIKSystem() == 'HindLimb':
        utils.printSubheader('Creating Hip/Clavivle Head connections')
        cmds.parentConstraint( CTRL_ClavHipHead, JNT_ClavHipHead, n=utils.getConstraint('Parent', CTRL_ClavHipHead[4:]), mo=True)
        cmds.parent( getOffset(CTRL_ClavHip), CTRL_ClavHipHead )

    #############################
    utils.printSubheader('Connecting the FK hierarchy')
    cmds.parent( getOffset(CTRL_WristAnkle), CTRL_LowerLimb )
    cmds.parent( getOffset(CTRL_LowerLimb), CTRL_UpperLimb )
    cmds.parent( getOffset(CTRL_UpperLimb), CTRL_ClavHip )
    
    #############################
    utils.printSubheader('Setting the toggle visiblity for the controllers')
    if utils.getIKSystem() == 'HindLimb':
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
        createFootReverseSystem(isMirror)
    else:
        if cmds.checkBox( 'UseDeleteHandFootCB', q=True, v=True ):
            for f in handFoot:
                f.reverse()
                cmds.parent( 'JNT' + sidePos + f[0], JNT_WristAnkle )
                cmds.parent( 'OFFSET' + sidePos + f[0], getOffset(CTRL_HandFoot) )

            cmds.delete( JNT_HandFoot, CTRL_HandFoot )

    if cmds.checkBox( 'UseStretchCB', q=True, v=True ):
        createStretchSystem()

    #if cmds.checkBox( 'NonRollCB', q=True, v=True ) and utils.getIKSystem() == 'SimpleLimb':
    #    addNonRollSystem()
        
    RT_SpaceSwitch.createSpaceSwitch('LimbSpace', CTRL_LowerLimbPV, 'CTRL__Master', CTRL_WristAnkle_IK, 'Parent')
    if utils.getIKSystem() == 'HindLimb':
        RT_SpaceSwitch.createSpaceSwitch('LimbSpace', CTRL_UpperLimbPV, 'CTRL__Master', CTRL_WristAnkle_IK, 'Parent')

    #############################
    utils.printSubheader('Locking and hidding unused attributes')
    utils.lockAndHideAttribute(CTRL_ClavHip, False, False)
    utils.lockAndHideAttribute(CTRL_UpperLimb, True, False)
    utils.lockAndHideAttribute(CTRL_LowerLimb, True, False)
    utils.lockAndHideAttribute(CTRL_WristAnkle, True, False)
    if utils.getFootReverse() == 'Yes' or not cmds.checkBox( 'UseDeleteHandFootCB', q=True, v=True ):
        utils.lockAndHideAttribute(CTRL_HandFoot, True, False)
    '''
    for f in handFoot:
        for p in f:
            utils.lockAndHideAttribute('CTRL' + sidePos + p, True, False)
    '''
    utils.lockAndHideAttribute(CTRL_WristAnkle_IK, False, False)
    if utils.getIKSystem() == 'HindLimb':
        utils.lockAndHideAttribute(CTRL_ClavHipHead, False, False)
        utils.lockAndHideAttribute(CTRL_ClavHip, True, False)
        utils.lockAndHideAttribute(CTRL_UpperLimbPV, False, True)
        utils.lockAndHideAttribute(CTRL_LowerLimbIK, False, True)
        cmds.setAttr( CTRL_LowerLimbIK + '.translateX', k=False, l=True, cb=False )
        cmds.setAttr( CTRL_LowerLimbIK + '.translateY', k=False, l=True, cb=False )  
    utils.lockAndHideAttribute(CTRL_LowerLimbPV, False, True)
    utils.lockAndHideAttribute(CTRL_LimbSwitch_FKIK, True, True)
    
    for o in offsets:
        utils.lockAndHideOffset(o, True)
        
    cmds.select( d=True )


def createIKHandler(initJoint, endJoint):
    limbIKH = 'IKH_' + endJoint[4:]
    cmds.ikHandle( n=limbIKH, sj=initJoint, ee=endJoint, sol='ikRPsolver', ap=False )
    eff = cmds.ikHandle( limbIKH, q=True, ee=True )
    cmds.rename( eff, 'EFF' + limbIKH[3:] )
    cmds.setAttr( limbIKH + '.ikBlend', 0)
    return limbIKH




def createIKHandlerWithGroup(initJoint, endJoint):
    limbIKH = createIKHandler(initJoint, endJoint)
    groupLimbIKH = 'OFFSET_' + limbIKH
    cmds.group( em=True, n=groupLimbIKH )
    cmds.parent( limbIKH, groupLimbIKH )
    posIKH = cmds.xform(limbIKH, ws=True, t=True, q=True)
    cmds.move( posIKH[0], posIKH[1], posIKH[2], groupLimbIKH + '.scalePivot', groupLimbIKH + '.rotatePivot', a=True )



def addAttribute(ctrl, name, niceName, defaultV, minV, maxV):
    if niceName=='':
        niceName=name
    cmds.addAttr( ctrl, ln=name, nn=niceName, at='float',  k=True, dv=defaultV, min=minV, max=maxV )



def getOffset(ctrl):
    return cmds.listRelatives( ctrl, p=True )



def createFootReverseSystem(isMirror):
    utils.printHeader('ADDING REVERSE FOOT')
    
    #############################
    utils.printSubheader('Unlocking attributes')
    for rf in reverseFoot:
        rev = 'REV' + sidePos + rf
        utils.lockAndHideOffset(rev, False)
    
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

    #############################
    if isMirror:
        utils.printSubheader('Swaping int and ext pivots')
        posExt = cmds.xform( REV_Ext , ws=True, piv=True, q=True)
        posInt = cmds.xform( REV_Int , ws=True, piv=True, q=True)
        cmds.move( posExt[0], posExt[1], posExt[2], REV_Int + '.scalePivot', REV_Int + '.rotatePivot', a=True )
        cmds.move( posInt[0], posInt[1], posInt[2], REV_Ext + '.scalePivot', REV_Ext + '.rotatePivot', a=True )
        tmpExt = REV_Ext + 'tmp'
        cmds.rename( REV_Ext, tmpExt )
        cmds.rename( REV_Int, REV_Ext )
        cmds.rename( tmpExt, REV_Int )
        cmds.select(d=True)

    #############################
    utils.printSubheader('Locking and hidding unused attributes')
    for rf in reverseFoot:
        rev = 'REV' + sidePos + rf
        cmds.setAttr( rev + '.visibility', 0 )
        utils.lockAndHideOffset(rev, True)



def createStretchSystem(*args):
    utils.printHeader('ADDING STRETCH SYSTEM')
    
    #############################
    utils.printSubheader('Creating attributes and variables')
    utils.addAttrSeparator(CTRL_WristAnkle_IK, 'StretchSeparator', 'STRETCH  SYSTEM')
    addAttribute(CTRL_WristAnkle_IK, 'Stretch', '', 0, 0, 1)
    addAttribute(CTRL_WristAnkle_IK, 'StretchCompensation', 'Compensation', 0, 0, 1000)
    addAttribute(CTRL_WristAnkle_IK, 'StretchVolume', 'Volume', 0, 0, 1)
    if utils.getIKSystem() == 'HindLimb':
        joints = [JNT_ClavHip, JNT_UpperLimb, JNT_LowerLimb, JNT_WristAnkle]
    else:
        joints = [JNT_UpperLimb, JNT_LowerLimb, JNT_WristAnkle]
    
    #############################
    utils.printSubheader('Creating and connect stretch distance')
    upperBone = cmds.xform( joints[0], q=True, m=True, ws=True )
    lowerBone = cmds.xform( JNT_WristAnkle, q=True, m=True, ws=True )
    upper = utils.getNameControl(6, CTRL_ClavHip if utils.getIKSystem() == 'HindLimb' else CTRL_UpperLimb, 'n')[1:]
    lower = utils.getNameControl(6, CTRL_WristAnkle, 'n')
    distance = utils.createDistanceMeasure(sidePos + upper + lower, joints[0][3:], JNT_WristAnkle[3:])
    cmds.xform( distance[1], m=upperBone, ws=True )
    cmds.xform( distance[2], m=lowerBone, ws=True )
    cmds.pointConstraint( joints[0], distance[1], n=utils.getConstraint('Point', distance[1][3:]), mo=True )
    cmds.pointConstraint( IKH_Group, distance[2], n=utils.getConstraint('Point', distance[2][3:]), mo=True )
    
    #############################
    utils.printSubheader('Setting MultipleDivide node')
    multDivStretch = utils.createShadingNode('multiplyDivide', JNT_UpperLimb + '_MultDivStretch')
    stretchComp = CTRL_WristAnkle_IK + '.StretchCompensation'
    cmds.setAttr( multDivStretch + '.operation', 2 )
    value = cmds.getAttr( distance[0] + '.distance' )
    cmds.setAttr( stretchComp, value )
    cmds.connectAttr( distance[0] + '.distance', multDivStretch + '.input1X' )
    cmds.connectAttr( stretchComp, multDivStretch + '.input2X' )
        
    #############################
    utils.printSubheader('Setting Condition node')
    condStretch = utils.createShadingNode('condition', CTRL_WristAnkle_IK + '_ConditionStretch')
    cmds.setAttr( condStretch + '.operation', 2 )
    cmds.connectAttr( distance[0] + '.distance', condStretch + '.firstTerm' )
    cmds.connectAttr( stretchComp, condStretch + '.secondTerm')
    cmds.connectAttr( multDivStretch + '.outputX', condStretch + '.colorIfTrueR' )
    
    #############################
    utils.printSubheader('Setting Conditions to remove Stretch when switching to FK')
    condFirst = utils.createShadingNode('condition', CTRL_LimbSwitch_FKIK + '_FirstCondition')
    cmds.setAttr( condFirst + '.colorIfTrueR', 1 )
    cmds.setAttr( condFirst + '.colorIfFalseR', 0 )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', condFirst + '.firstTerm' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.Stretch', condFirst + '.secondTerm' )
    condSecond = utils.createShadingNode('condition', CTRL_LimbSwitch_FKIK + '_SecondCondition')
    cmds.setAttr( condSecond + '.colorIfFalseR', 0 )
    cmds.connectAttr( condFirst + '.outColor.outColorR', condSecond + '.colorIfTrue.colorIfTrueR' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.Stretch', condSecond + '.firstTerm' )
    cmds.connectAttr( condFirst + '.outColor.outColorR', condSecond + '.secondTerm' )
    
    #############################
    utils.printSubheader('Setting Blend Color node')
    blendColTwist = utils.createShadingNode('blendColors', joints[0] + '_BlendColorStretch')
    cmds.connectAttr( condStretch + '.outColorR', blendColTwist + '.color1R' )
    cmds.connectAttr( condSecond + '.outColor.outColorR', blendColTwist + '.blender')
    
    #############################
    utils.printSubheader('Setting Clamp node and Connecting the joints')
    clampTwist = utils.createShadingNode('clamp', joints[0] + '_ClampTwist')
    cmds.setAttr( clampTwist + '.minR', 1 )
    cmds.setAttr( clampTwist + '.maxR', 999 )
    cmds.connectAttr( blendColTwist + '.outputR', clampTwist + '.inputR')
    if utils.getIKSystem() == 'HindLimb':
        cmds.connectAttr( clampTwist + '.outputR', JNT_ClavHip + '.scaleX' )
    cmds.connectAttr( clampTwist + '.outputR', JNT_UpperLimb + '.scaleX' )
    cmds.connectAttr( clampTwist + '.outputR', JNT_LowerLimb + '.scaleX' )
    
    #############################
    utils.printSubheader('Creating non-stretch joints')  
    for j in joints:
        radius = cmds.getAttr( j + '.radius' )
        strechJoint = j.replace( 'JNT', 'STRJNT' )
        cmds.rename( j, strechJoint )
        cmds.select( cl=True )
        newJoint = cmds.joint( p=(0, 0, 0), n=j, rad=radius*2 )
        cmds.editDisplayLayerMembers( 'JOINTS', newJoint, nr=True )
        cmds.parent( newJoint, 'Rig' )
        cmds.parentConstraint( strechJoint, newJoint, n=utils.getConstraint('Parent', newJoint[3:]), mo=False )
    
    #############################
    utils.printSubheader('Setting connections for the volume')  
    multDivVolume = utils.createShadingNode('multiplyDivide', 'STR' + JNT_LowerLimb + '_MultDivVolume')
    cmds.setAttr( multDivVolume + '.operation', 2 )
    cmds.setAttr( multDivVolume + '.input1X', 1 )
    cmds.connectAttr( clampTwist + '.output.outputR', multDivVolume + '.input2.input2X' )
        
    remapVolume = utils.createShadingNode('remapValue', CTRL_WristAnkle_IK + '_RemapVolume')
    cmds.setAttr( remapVolume + '.outputMin', 1 )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.StretchVolume', remapVolume + '.inputValue' )
    cmds.connectAttr( multDivVolume + '.outputX', remapVolume + '.outputMax' )
    
    for j in range(len(joints)-1):
        cmds.connectAttr( remapVolume + '.outValue', joints[j] + '.scale.scaleY' )
        cmds.connectAttr( remapVolume + '.outValue', joints[j] + '.scale.scaleZ' )

    #############################
    utils.printSubheader('Parenting the Hand/Foot with the Wrist/Ankle')
    if utils.getFootReverse() == 'Yes' or not cmds.checkBox( 'UseDeleteHandFootCB', q=True, v=True ):
        cmds.parent( JNT_HandFoot, JNT_WristAnkle )
    else:
        handFoot = RThands.getHandFootHierarchy()
        for f in handFoot:
            f.reverse()
            cmds.parent( 'JNT' + sidePos + f[0], JNT_WristAnkle )

    #############################
    utils.printSubheader('Calculating stretch compensation') 
    cmds.setAttr( CTRL_LimbSwitch_FKIK + '.FKIK', 1 )
    cmds.setAttr( CTRL_WristAnkle_IK + '.Stretch', 1 )
    cmds.setAttr( CTRL_WristAnkle_IK + '.StretchCompensation', 1000 )
    
    angDiff = 90
    oldAngle = angDiff
    n = 0
    inc = 0.0001
    
    while angDiff > 0.05:
        n = n - inc
        cmds.setAttr( CTRL_WristAnkle_IK + '.translateY', n )
        angle = cmds.angleBetween( v1=(utils.getVector(JNT_UpperLimb, JNT_LowerLimb)), v2=(utils.getVector(JNT_LowerLimb, JNT_WristAnkle)) )[3]
        angDiff = abs(oldAngle - angle)
        oldAngle = angle

    strComp = cmds.getAttr( distance[0] + '.distance' )
    cmds.setAttr( CTRL_WristAnkle_IK + '.StretchCompensation', strComp, k=False, cb=False ) 
    cmds.setAttr( CTRL_WristAnkle_IK + '.translateY', 0 )
    cmds.setAttr( CTRL_LimbSwitch_FKIK + '.FKIK', 0 )
    cmds.setAttr( CTRL_WristAnkle_IK + '.Stretch', 0 )


def convertIKtoObject(*args):
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    utils.printHeader('CHANGING IK WORLD TO OBJECT')
    utils.printSubheader('Defining variables...')
    CTRL_Wrist_IK = sel[0]
    OFFSET_Wrist_IK = 'OFFSET' + CTRL_Wrist_IK[4:]
    CTRL_Wrist_O = CTRL_Wrist_IK[:-3]
    OFFSET_Wrist_O = 'OFFSET' + CTRL_Wrist_O[4:]
    CTRL_Wrist_IK_World = CTRL_Wrist_IK + '_World'
    OFFSET_Wrist_IK_World = OFFSET_Wrist_IK + '_World'
    SNAP_Wrist_IK_World = 'SNAP' + CTRL_Wrist_IK[4:]
    
    utils.printSubheader('Creating new Object controller...')
    cmds.rename( OFFSET_Wrist_IK, OFFSET_Wrist_IK_World)
    cmds.rename( CTRL_Wrist_IK, CTRL_Wrist_IK_World)
    
    cmds.duplicate( OFFSET_Wrist_O, n=OFFSET_Wrist_IK, rc=True )
    cmds.parent( OFFSET_Wrist_IK, w=True )
    chld = cmds.listRelatives( OFFSET_Wrist_IK, ad=True )
    cmds.delete( chld )
    cmds.duplicate( CTRL_Wrist_IK_World, n=CTRL_Wrist_IK, rc=True )
    chld = cmds.listRelatives( CTRL_Wrist_IK, ad=True )
    
    for c in range(len(chld)):
        if c==0:
            pass
        else: 
            cmds.delete( chld[c] )
    
    cmds.parent( CTRL_Wrist_IK, OFFSET_Wrist_IK )
    cmds.refresh()
    cmds.makeIdentity(apply=True, t=1, r=1, n=0)
    cmds.parent( OFFSET_Wrist_IK_World, CTRL_Wrist_IK )
    cmds.select( CTRL_Wrist_IK_World + '_Shape.cv[0:16]' )
    cmds.scale( 0.001, 0.001, 0.001 )
    
    utils.printSubheader('Setting connections with the IK controller...')
    cmds.connectAttr( CTRL_Wrist_IK + '.Stretch', CTRL_Wrist_IK_World + '.Stretch' )
    cmds.connectAttr( CTRL_Wrist_IK + '.StretchVolume', CTRL_Wrist_IK_World + '.StretchVolume' )
    cmds.connectAttr( CTRL_Wrist_IK_World + '.visibility', CTRL_Wrist_IK + '.visibility' )
    
    utils.printSubheader('Setting new snap...')
    cmds.delete( SNAP_Wrist_IK_World )
    cmds.duplicate( 'SNAP' + CTRL_Wrist_O[4:], n=SNAP_Wrist_IK_World )
    
    cmds.select( CTRL_Wrist_IK )



def deleteLimbSystem(*args):
    utils.printHeader('DELETING LIMB SYSTEM...')
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return

    RTvars.limbStartingBone = sel[0]
    assignVariables(False)

    utils.printSubheader('Deleting helpers...')
    cmds.delete( 'VECTOR' + sidePos + offsetsLimb[2] )
    
    
    if utils.getIKSystem() == 'SimpleLimb':
        cmds.delete( 'IKH_SYSTEM' + sidePos + offsetsLimb[4] )
    else:
        cmds.delete( 'VECTOR' + sidePos + offsetsLimb[4] )
        cmds.delete( 'IKH_SYSTEM' + sidePos + offsetsLimb[7] )
        
    utils.printSubheader('Deleting PV...')
    PV = sidePos + offsetsLimb[3]
    cmds.delete( 'LINE' + PV )
    cmds.delete( 'CLST' + sidePos + offsetsLimb[2] + '_Handle' )
    cmds.delete( 'CLST' + PV + '_Handle' )
    cmds.delete( 'SPSW_PARENT' + PV + '_MASTER' )
    
    if utils.getIKSystem() == 'HindLimb':
        PV = sidePos + offsetsLimb[5]
        cmds.delete( 'LINE' + PV )
        cmds.delete( 'CLST' + sidePos + offsetsLimb[4] + '_Handle' )
        cmds.delete( 'CLST' + PV + '_Handle' )
        cmds.delete( 'SPSW_PARENT' + PV + '_MASTER' )
        
    utils.printSubheader('Deleting limb...')
    cmds.delete( RTvars.limbStartingBone )
    
    try:
        cmds.delete( 'LOC' + sidePos + offsetsLimb[1] )
        cmds.delete( 'LOC' + sidePos + offsetsLimb[4 if utils.getIKSystem() == 'SimpleLimb' else 7] )
        
        for n in range(0, 5):
            try:
                cmds.delete( 'JNT' + sidePos + limbBones[n] )
            except:
                pass
    except:
        print ('No stretch system found...')

    utils.printSubheader('Deleting controllers...')
    for o in offsetsLimb:
        try:
            cmds.delete( 'OFFSET' + sidePos + o )
        except:
            pass
    
    utils.printSubheader('Deleting unused nodes...') 
    mel.eval('MLdeleteUnused;')
    
    utils.printSubheader('Restoring joint hierarchy...')
    cmds.parent( RTvars.limbStartingBone + '_BACK_UP', w=True )
    cmds.refresh()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.rename( RTvars.limbStartingBone + '_BACK_UP', RTvars.limbStartingBone )
    
    createLimbBackUp(RTvars.limbStartingBone)
    for n in cmds.listRelatives( RTvars.limbStartingBone, ad=True, s=False ):
        cmds.rename( n, n[:-1] )
            
    utils.printSubheader('Restoring controllers hierarchy...')
    for o in offsetsLimb:
        name = 'OFFSET' + sidePos + o
        backUp = name + '_BACK_UP'
        cmds.parent( backUp, w=True )
        cmds.rename( backUp, name )
        for n in cmds.listRelatives( name, ad=True, s=False ):
            cmds.rename( n, n[:-1] )

    utils.printSubheader('Deleting groups...')
    try:
        if utils.getHierarchy() == 'Arm':
            cmds.delete( 'SPSW_ORIENT' + sidePos + 'Arm_MASTER' )
            cmds.delete( 'ARM' + sidePos[:-1] )
        else:
            cmds.delete( 'SPSW_ORIENT' + sidePos + 'Hip_MASTER' )
            cmds.delete( 'LEG' + sidePos[:-1] )
    except:
        print ('No groups found')


def deleteLimb(*args):
    utils.printHeader('DELETING WHOLE LIMB...')
    deleteLimbSystem()
    
    cmds.delete( RTvars.limbStartingBone + '_BACK_UP' )
    cmds.select( RTvars.limbStartingBone )
    RT_Utilities.renameLimb()
    utils.printSubheader('Deleting Controllers...')
    for o in offsetsLimb:
        cmds.delete( 'OFFSET' + sidePos + o )
    
    
    

    
    

JNT_ClavHip = 'JNT__L_Hip'
JNT_UpperLimb = 'JNT__L_UpperLeg'
JNT_LowerLimb = 'JNT__L_LowerLeg'
JNT_WristAnkle = 'JNT__L_Ankle'
JNT_HandFoot = 'JNT__L_Foot'
JNT_FingToeIndex = 'JNT__L_ToeIndex'
JNT_FingToeMiddle = 'JNT__L_ToeMiddle'
JNT_FingToeRing = 'JNT__L_ToeRing'

CTRL_ClavHip = 'CTRL__L_Hip'
CTRL_UpperLimb = 'CTRL__L_UpperLeg'
CTRL_LowerLimbPV = 'CTRL__L_Leg_PV'
CTRL_LowerLimb = 'CTRL__L_LowerLeg'
CTRL_WristAnkle = 'CTRL__L_Ankle'
CTRL_HandFoot = 'CTRL__L_Foot'
CTRL_FingToeIndex = 'CTRL__L_ToeIndex'
CTRL_FingToeMiddle = 'CTRL__L_ToeMiddle'
CTRL_FingToeRing = 'CTRL__L_ToeRing'
CTRL_LimbSwitch_FKIK = 'CTRL__L_LegSwitch_FKIK'
CTRL_WristAnkle_IK = 'CTRL__L_Ankle_IK'

REV_Heel = 'REV__L_FootHeel'
REV_Ext = 'REV__L_FootExt'
REV_Int = 'REV__L_FootInt'
REV_Ball = 'REV__L_FootBall'
REV_WristAnkle = 'REV__L_Ankle'
REV_Tip = 'REV__L_Toetip'
REV_JNT_WristAnkle = 'REV_JNT__L_Ankle'

IKH_LowerLimb = 'IKH__L_LowerLeg'
IKH_WristAnkle = 'IKH__L_Ankle'



sidePos = '__L_'
JNT_ClavHip = 'JNT__L_Clavicle'
JNT_UpperLimb = 'JNT__L_Arm'
JNT_LowerLimb = 'JNT__L_Forearm'
JNT_WristAnkle = 'JNT__L_Wrist'
JNT_HandFoot = 'JNT__L_Hand'
JNT_FingToeIndex = 'JNT__L_FingerRing'
JNT_FingToeMiddle = 'JNT__L_FingerMiddle'
JNT_FingToeRing = 'JNT__L_FingerIndex'

CTRL_ClavHip = 'CTRL__L_Clavicle'
CTRL_UpperLimb = 'CTRL__L_Arm'
CTRL_LowerLimb = 'CTRL__L_Forearm'
CTRL_LowerLimbPV = 'CTRL__L_Forearm_PV'
CTRL_WristAnkle = 'CTRL__L_Wrist'
CTRL_HandFoot = 'CTRL__L_Hand'
CTRL_FingToeIndex = 'CTRL__L_FingerIndex'
CTRL_FingToeMiddle = 'CTRL__L_FingerMiddle'
CTRL_FingToeRing = 'CTRL__L_FingerRing'
CTRL_LimbSwitch_FKIK = 'CTRL__L_ArmSwitch_FKIK'
CTRL_WristAnkle_IK = 'CTRL__L_Wrist_IK'

REV_Heel = 'REV__L_HandHeel'
REV_Ext = 'REV__L_HandExt'
REV_Int = 'REV__L_HandInt'
REV_Ball = 'REV__L_HandBall'
REV_WristAnkle = 'REV__L_Wrist'
REV_Tip = 'REV__L_Fingertip'
REV_JNT_WristAnkle = 'REV_JNT__L_Wrist'

IKH_WristAnkle = 'IKH__L_Wrist'



JNT_ClavHip = 'JNT__R_Hip'
JNT_UpperLimb = 'JNT__R_UpperLeg'
JNT_LowerLimb = 'JNT__R_LowerLeg'
JNT_WristAnkle = 'JNT__R_Ankle'
JNT_HandFoot = 'JNT__R_Foot'
JNT_FingToeIndex = 'JNT__R_ToeIndex'
JNT_FingToeMiddle = 'JNT__R_ToeMiddle'
JNT_FingToeRing = 'JNT__R_ToeRing'

CTRL_ClavHip = 'CTRL__R_Hip'
CTRL_UpperLimb = 'CTRL__R_UpperLeg'
CTRL_LowerLimbPV = 'CTRL__R_Leg_PV'
CTRL_LowerLimb = 'CTRL__R_LowerLeg'
CTRL_WristAnkle = 'CTRL__R_Ankle'
CTRL_HandFoot = 'CTRL__R_Foot'
CTRL_FingToeIndex = 'CTRL__R_ToeIndex'
CTRL_FingToeMiddle = 'CTRL__R_ToeMiddle'
CTRL_FingToeRing = 'CTRL__R_ToeRing'
CTRL_LimbSwitch_FKIK = 'CTRL__R_LegSwitch_FKIK'
CTRL_WristAnkle_IK = 'CTRL__R_Ankle_IK'

REV_Heel = 'REV__R_FootHeel'
REV_Ext = 'REV__R_FootExt'
REV_Int = 'REV__R_FootInt'
REV_Ball = 'REV__R_FootBall'
REV_WristAnkle = 'REV__R_Ankle'
REV_Tip = 'REV__R_Toetip'
REV_JNT_WristAnkle = 'REV_JNT__R_Ankle'

IKH_LowerLimb = 'IKH__R_LowerLeg'
IKH_WristAnkle = 'IKH__R_Ankle'


JNT_ClavHip = 'JNT__R_Clavicle'
JNT_UpperLimb = 'JNT__R_Arm'
JNT_LowerLimb = 'JNT__R_Forearm'
JNT_WristAnkle = 'JNT__R_Wrist'
JNT_HandFoot = 'JNT__R_Hand'
JNT_FingToeIndex = 'JNT__R_FingerRing'
JNT_FingToeMiddle = 'JNT__R_FingerMiddle'
JNT_FingToeRing = 'JNT__R_FingerIndex'

CTRL_ClavHip = 'CTRL__R_Clavicle'
CTRL_UpperLimb = 'CTRL__R_Arm'
CTRL_LowerLimb = 'CTRL__R_Forearm'
CTRL_LowerLimbPV = 'CTRL__R_Arm_PV'
CTRL_WristAnkle = 'CTRL__R_Wrist'
CTRL_HandFoot = 'CTRL__R_Hand'
CTRL_FingToeIndex = 'CTRL__R_FingerIndex'
CTRL_FingToeMiddle = 'CTRL__R_FingerMiddle'
CTRL_FingToeRing = 'CTRL__R_FingerRing'
CTRL_LimbSwitch_FKIK = 'CTRL__R_ArmSwitch_FKIK'
CTRL_WristAnkle_IK = 'CTRL__R_Wrist_IK'

REV_Heel = 'REV__R_HandHeel'
REV_Ext = 'REV__R_HandExt'
REV_Int = 'REV__R_HandInt'
REV_Ball = 'REV__R_HandBall'
REV_WristAnkle = 'REV__R_Wrist'
REV_Tip = 'REV__R_Fingertip'
REV_JNT_WristAnkle = 'REV_JNT__R_Wrist'

IKH_WristAnkle = 'IKH__R_Wrist'
  
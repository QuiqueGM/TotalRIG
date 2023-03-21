import RT_GlobalVariables as RTvars
import RT_Controllers as RTctrl
import RT_Utils as utils
import RT_FillTools
import RT_Utilities
import RT_SpaceSwitch
import maya.cmds as cmds
import maya.mel as mel

def assignVariables():
    global typeOfLimb, limbBones, offsetsLimb, ctrlLimbBones, reverseFoot, sideAndPosition
    global JNT_ClavHip, JNT_UpperLimb, JNT_LowerLimb, JNT_WristAnkle, JNT_HandFoot, JNT_FingToeInd, JNT_FingToeMid, JNT_FingToeRing
    global CTRL_ClavHip, CTRL_UpperLimb, CTRL_LowerLimb, CTRL_WristAnkle, CTRL_HandFoot, CTRL_FingToeExt, CTRL_FingToeMid, CTRL_FingToeInt, CTRL_WristAnkle_IK, CTRL_LimbPV, CTRL_LimbSwitch_FKIK
    global REV_Orient, REV_Heel, REV_Ext, REV_Int, REV_Tip, REV_Ball, REV_WristAnkle
    
    typeOfLimb = utils.getTypeOfLimb(cmds.textFieldButtonGrp( 'LimbStartingBone', q=True, tx=True ))
    
    if typeOfLimb == 'Hip':
        limbBones = RTvars.legBones
        offsetsLimb = RTvars.offsetsLeg
        reverseFoot = RTvars.reverseFoot
        ctrlLimbBones = [[limbBones[0], 'Circle', 0.1, 'World', ''], [limbBones[1], 'Circle', 0.14, 'Object', ''], [limbBones[2], 'Circle', 0.13, 'Object', ''], [limbBones[2], 'Arrow', 0.1, 'World', offsetsLimb[3]], [limbBones[3], 'Circle', 0.1, 'Object', ''], [limbBones[3], 'Box', 0.15, 'World', offsetsLimb[5]], [limbBones[3], 'Box', 0.03, 'World', offsetsLimb[6]], [limbBones[4], 'Box', 0.125, 'World', ''], [limbBones[5], 'Circle', 0.04, 'Object', ''], [limbBones[6], 'Circle', 0.04, 'Object', ''], [limbBones[7], 'Circle', 0.04, 'Object', '']]
        JNT_ClavHip = cmds.textFieldGrp( 'Hip' ,q=True, tx=True ) 
        JNT_UpperLimb = cmds.textFieldGrp( 'UpperLeg' ,q=True, tx=True )
        JNT_LowerLimb = cmds.textFieldGrp( 'LowerLeg' ,q=True, tx=True )
        JNT_WristAnkle = cmds.textFieldGrp( 'Ankle' ,q=True, tx=True )
        JNT_HandFoot = cmds.textFieldGrp( 'Foot' ,q=True, tx=True )
        JNT_FingToeInd = cmds.textFieldGrp( 'ToeIndex' ,q=True, tx=True )
        JNT_FingToeMid = cmds.textFieldGrp( 'ToeMid' ,q=True, tx=True )
        JNT_FingToeRing = cmds.textFieldGrp( 'ToeRing' ,q=True, tx=True )

    elif typeOfLimb == 'Clavicle':
        limbBones = RTvars.armBones
        offsetsLimb = RTvars.offsetsArm
        reverseFoot = RTvars.reverseHand
        ctrlLimbBones = [[limbBones[0], 'Circle', 0.1, 'World', ''], [limbBones[1], 'Circle', 0.14, 'Object', ''], [limbBones[2], 'Circle', 0.13, 'Object', ''], [limbBones[2], 'Arrow', 0.1, 'World', offsetsLimb[3]], [limbBones[3], 'Circle', 0.1, 'Object', ''], [limbBones[3], 'Box', 0.15, 'World', offsetsLimb[5]], [limbBones[3], 'Box', 0.03, 'World', offsetsLimb[6]], [limbBones[4], 'Box', 0.125, 'World', ''], [limbBones[5], 'Circle', 0.04, 'Object', ''], [limbBones[6], 'Circle', 0.04, 'Object', ''], [limbBones[7], 'Circle', 0.04, 'Object', '']]        
        JNT_ClavHip = cmds.textFieldGrp( 'Clavicle' ,q=True, tx=True ) 
        JNT_UpperLimb = cmds.textFieldGrp( 'Arm' ,q=True, tx=True )
        JNT_LowerLimb = cmds.textFieldGrp( 'Forearm' ,q=True, tx=True )
        JNT_WristAnkle = cmds.textFieldGrp( 'Wrist' ,q=True, tx=True )
        JNT_HandFoot = cmds.textFieldGrp( 'Hand' ,q=True, tx=True )
        JNT_FingToeInd = cmds.textFieldGrp( 'FingerIndex' ,q=True, tx=True )
        JNT_FingToeMid = cmds.textFieldGrp( 'FingerMid' ,q=True, tx=True )
        JNT_FingToeRing = cmds.textFieldGrp( 'FingerRing' ,q=True, tx=True )
        
    CTRL_ClavHip = 'CTRL' + JNT_ClavHip[3:]
    CTRL_UpperLimb = 'CTRL' + JNT_UpperLimb[3:]
    CTRL_LowerLimb = 'CTRL' + JNT_LowerLimb[3:]
    CTRL_WristAnkle = 'CTRL' + JNT_WristAnkle[3:]
    CTRL_HandFoot = 'CTRL' + JNT_HandFoot[3:]
    CTRL_FingToeExt = 'CTRL' + JNT_FingToeInd[3:]
    CTRL_FingToeMid = 'CTRL' + JNT_FingToeMid[3:]
    CTRL_FingToeInt = 'CTRL' + JNT_FingToeRing[3:]
    CTRL_WristAnkle_IK = CTRL_WristAnkle + '_IK'

    sideAndPosition = '__' + utils.getSideFromBone(JNT_ClavHip) + utils.getPositionFromBone(JNT_ClavHip)
    CTRL_LimbPV = 'CTRL' + sideAndPosition + ('Leg_PV' if typeOfLimb == 'Hip' else 'Arm_PV')
    CTRL_LimbSwitch_FKIK = 'CTRL' + sideAndPosition + ('LegSwitch_FKIK' if typeOfLimb == 'Hip' else 'ArmSwitch_FKIK')
    REV_Heel = 'REV' + sideAndPosition + reverseFoot[0]
    REV_Ext = 'REV' + sideAndPosition + reverseFoot[1]
    REV_Int = 'REV' + sideAndPosition + reverseFoot[2]
    REV_Tip = 'REV' + sideAndPosition + reverseFoot[3]
    REV_Ball = 'REV' + sideAndPosition + reverseFoot[4]
    REV_WristAnkle = 'REV' + sideAndPosition + ('Ankle' if typeOfLimb == 'Hip' else 'Wrist')



def createLimbControllers():
    assignVariables()       
    utils.printHeader('CREATING LIMB CONTROLLERS')
    cmds.refresh()
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    
    for b in ctrlLimbBones:
        cmds.select( cmds.textFieldGrp( b[0], q=True, tx=True ))
        sel = cmds.ls(sl=True)
        ctrl = RTctrl.createController( b[1], utils.getColorFromSide(sel), b[2], b[3], b[0], b[4] )[1]
    
    if not cmds.checkBox( 'UseCreateReverseFoot', q=True, v=True ):
        cmds.setAttr( CTRL_HandFoot + '.visibility', cmds.checkBox( 'UseShowHandFoot', q=True, v=True ) )
        
    ctrls = getListControllers()
    
    if cmds.checkBox( 'UseCreateReverseFoot', q=True, v=True ):
        createReverseFootGroups(ctrls[5])
    else:
        grp = cmds.group( em=True, n='REV__' + utils.getSideFromBone(CTRL_WristAnkle_IK) + utils.getPositionFromBone(CTRL_WristAnkle_IK) + limbBones[3] )
        cmds.parent( grp, cmds.textFieldGrp( limbBones[3], q=True, tx=True ) )
        utils.setTransformAndRotationToZero(grp)
        cmds.parent( grp, CTRL_WristAnkle_IK )
        
    relocateControllers(ctrls)
    utils.lockControllers(ctrls, True)



def relocateControllers(ctrls):
    cmds.select( ctrls[0] )
    cmds.select( ctrls[0] + 'Shape.cv[0:7]' )
    cmds.move( 0.2, 0, 0, r=True, os=True, wd=True)
    cmds.select( d=True )
    
    cmds.select( ctrls[6] )
    cmds.select( ctrls[6] + '_Shape.cv[0:16]' )
    cmds.move( 0, -0.085, -0.17, r=True, os=True, wd=True)
    cmds.select( d=True )
    
    rotateToeController(ctrls[8])
    rotateToeController(ctrls[9])
    rotateToeController(ctrls[10])



def rotateToeController(toeName):
    cmds.select( toeName )
    cmds.select( toeName + 'Shape.cv[0:7]' )
    cmds.rotate(  0, '90deg', 0 )
    cmds.move( 0.035, 0, 0, r=True, os=True, wd=True)
    cmds.scale( 1.25, 1, 1 )
    cmds.select( d=True )



def getListControllers():
    side = utils.getSideFromBone( cmds.textFieldGrp( typeOfLimb ,q=True, tx=True ) )
    position = utils.getPositionFromBone( cmds.textFieldGrp( typeOfLimb ,q=True, tx=True ) )
    ctrls = []
    for o in offsetsLimb:
        ctrl = 'CTRL__' + side + position + o
        ctrls.append( ctrl )

    return ctrls



def createReverseFootGroups(wristAnkleIK):
    global rev
    rev = []
    
    for x in range(5):
        name = 'REV' + sideAndPosition + reverseFoot[x]
        grp = cmds.group( em=True, n=name )
        rev.append(grp)
    
    cmds.parent( rev[4], cmds.textFieldGrp( limbBones[4], q=True, tx=True ) )
    utils.setTransformAndRotationToZero(rev[4])
    grp = cmds.group( rev[4], n='OFFSET' + rev[4][3:] )
    rev.append(grp)
    cmds.parent( rev[5], w=True )
    grp = cmds.group( em=True, n='REV' + sideAndPosition + limbBones[3] )
    rev.append(grp)
    cmds.parent( rev[6], cmds.textFieldGrp( limbBones[3], q=True, tx=True ) )
    utils.setTransformAndRotationToZero(rev[6])
    
    cmds.parent( rev[6], w=True )
    cmds.parent( rev[6], rev[4] )
    cmds.parent( rev[5], rev[3] )
    cmds.parent( rev[3], rev[2] )
    cmds.parent( rev[2], rev[1] )
    cmds.parent( rev[1], rev[0] )
    cmds.parent( rev[0], wristAnkleIK )  



def createLimbSystem():
    utils.printHeader('CREATING LIMB SYSYEM')
    mel.eval('MLdeleteUnused;')
    
    if cmds.checkBox( 'UseCreateReverseFoot', q=True, v=True ):
        if not checkIfFootReverseIsSet():
            result = cmds.confirmDialog( t='Foot reverse', m='Something in the Foot Reverse is not set properly. Maybe you forgot to move some anchor. Do you want to continue?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName )
            if result == 'No':
                return
     
    if cmds.checkBox( 'UseMirrorCB', q=True, v=True ):
        createMirror()
        connectLimbSystem()
        RT_FillTools.reloadMirror(limbBones)
        connectLimbSystem()
        RT_FillTools.reloadMirror(limbBones)
    else:
        connectLimbSystem()



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



def getWorldScalePivotInfo(rev):
    pos = cmds.xform(rev, q=True, sp=True )
    magnitude = 0
    for p in pos:
        magnitude += p;
    
    return magnitude



def connectLimbSystem():
    assignVariables()
    utils.printHeader('CONNECTINC LIMB SYSYEM')
    utils.lockControllers(getListControllers(), False)
    cmds.editDisplayLayerMembers( 'JOINTS', JNT_ClavHip, nr=True )
    
    #Crearem un IKRPSolver del upperleg al ankle l'emparentem amb el control del peu i fem un poleVector amb el controlador ik del genoll
    footIKH = 'IKH' + CTRL_WristAnkle_IK[4:]
    cmds.ikHandle( n=footIKH, sj=JNT_UpperLimb, ee=JNT_WristAnkle, sol='ikRPsolver', ap=False )
    cmds.parent( footIKH, REV_WristAnkle )
    cmds.poleVectorConstraint( CTRL_LimbPV, footIKH )
       
    #Connectarem el SwitchFKIK amb l'os foot i li crearem l'atribut FKIK i despres ho connectarem amb l'IKBlend de tots els IKHandles    
    cmds.parentConstraint( JNT_WristAnkle, cmds.listRelatives( CTRL_LimbSwitch_FKIK, p=True ), mo=True)
    cmds.select( CTRL_LimbSwitch_FKIK )
    cmds.addAttr( ln='FKIK', at="float", k=True, dv=0, min=0, max=1 )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', footIKH + '.ikb')
    
    #Fem els constraints de orient de FK amb la cadena JNT i el constraint de parent amb la clavicula
    cmds.parentConstraint( CTRL_ClavHip, JNT_ClavHip, mo=True )
    cmds.orientConstraint( CTRL_UpperLimb, JNT_UpperLimb, mo=True )
    cmds.orientConstraint( CTRL_LowerLimb, JNT_LowerLimb, mo=True )
    cmds.orientConstraint( CTRL_WristAnkle, JNT_WristAnkle, mo=True )
    cmds.orientConstraint( CTRL_HandFoot, JNT_HandFoot, mo=True )            

    #Apliquem el doble constraint a l'os de l'ankle i al grup de l'os del Foot
    cmds.orientConstraint( REV_WristAnkle, JNT_WristAnkle, mo=True)
    cmds.parentConstraint( REV_Tip if cmds.checkBox( 'UseCreateReverseFoot', q=True, v=True ) else REV_WristAnkle, cmds.listRelatives( CTRL_HandFoot, p=True ), mo=True )
    cmds.parentConstraint( CTRL_WristAnkle, cmds.listRelatives( CTRL_HandFoot, p=True ), mo=True )
    
	#Fem els constraints dels dits dels peus i emparentem amb el peu
    cmds.orientConstraint( CTRL_FingToeExt, JNT_FingToeInd, mo=True)
    cmds.orientConstraint( CTRL_FingToeMid, JNT_FingToeMid, mo=True)
    cmds.orientConstraint( CTRL_FingToeInt, JNT_FingToeRing, mo=True)
     
    if cmds.checkBox( 'UseCreateReverseFoot', q=True, v=True ):
        cmds.parent( 'OFFSET' + CTRL_FingToeExt[4:], CTRL_HandFoot )
        cmds.parent( 'OFFSET' + CTRL_FingToeMid[4:], CTRL_HandFoot )
        cmds.parent( 'OFFSET' + CTRL_FingToeInt[4:], CTRL_HandFoot )
    else:
        cmds.parentConstraint( JNT_WristAnkle, 'OFFSET' + CTRL_FingToeExt[4:], mo=True)
        cmds.parentConstraint( JNT_WristAnkle, 'OFFSET' + CTRL_FingToeMid[4:], mo=True)
        cmds.parentConstraint( JNT_WristAnkle, 'OFFSET' + CTRL_FingToeInt[4:], mo=True)

    #Crearem un altre node Reverse
    cmds.shadingNode( 'reverse', au=True, n=CTRL_UpperLimb + '_Reverse' )
    
    #Amaga i visualitza els controladors de IK i FK.
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_WristAnkle_IK +'.visibility', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_LimbPV +'.visibility', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_UpperLimb + '_Reverse.input.inputY', f=True )
    cmds.connectAttr( CTRL_UpperLimb + '_Reverse.output.outputY', CTRL_UpperLimb + '.visibility', f=True )
    cmds.connectAttr( CTRL_UpperLimb + '_Reverse.output.outputY', CTRL_LowerLimb + '.visibility', f=True )
    cmds.connectAttr( CTRL_UpperLimb + '_Reverse.output.outputY', CTRL_WristAnkle + '.visibility', f=True )
    
    #Posarem les curves de FK en jerarquia
    cmds.parent( 'OFFSET' + CTRL_WristAnkle[4:], CTRL_LowerLimb )
    cmds.parent( 'OFFSET' + CTRL_LowerLimb[4:], CTRL_UpperLimb )
    cmds.parent( 'OFFSET' + CTRL_UpperLimb[4:], CTRL_ClavHip )
    
    #Crearem un altre node Reverse pels constraints dobles de l'ankle i el foot
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_UpperLimb + '_Reverse.input.inputX', f=True )
    cmds.connectAttr( CTRL_UpperLimb + '_Reverse.output.outputX', JNT_WristAnkle + '_orientConstraint1.w0', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', JNT_WristAnkle + '_orientConstraint1.w1', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', CTRL_UpperLimb + '_Reverse.input.inputZ', f=True )
    cmds.connectAttr( CTRL_UpperLimb + '_Reverse.output.outputZ', 'OFFSET' + CTRL_HandFoot[4:] + '_parentConstraint1.w1', f=True )
    cmds.connectAttr( CTRL_LimbSwitch_FKIK + '.FKIK', 'OFFSET' + CTRL_HandFoot[4:] + '_parentConstraint1.w0', f=True )

    #Fem el foot reverse
    if cmds.checkBox( 'UseCreateReverseFoot', q=True, v=True ):
        createFootReverseSystem()
        
    #Fem l'stretch de la cama
    if cmds.checkBox( 'UseStretchCB', q=True, v=True ):
        createStretchSystem()

    #Fem els space switch dels Pole Vectors
    if cmds.checkBox( 'UseSSPoleVectorCB', q=True, v=True ):
        createSSforPoleVector
        RT_SpaceSwitch.createSpaceSwitch('LimbSpace', CTRL_LimbPV, 'CTRL__Master', CTRL_WristAnkle_IK, 'Parent')

    #Bloquejem i amaguem attributs dels controladors
    utils.lockAndHideAttribute(CTRL_ClavHip, False, False)
    utils.lockAndHideAttribute(CTRL_UpperLimb, True, False)
    utils.lockAndHideAttribute(CTRL_LowerLimb, True, False)
    utils.lockAndHideAttribute(CTRL_WristAnkle, True, False)
    utils.lockAndHideAttribute(CTRL_HandFoot, True, False)
    utils.lockAndHideAttribute(CTRL_FingToeExt, True, False)
    utils.lockAndHideAttribute(CTRL_FingToeMid, True, False)
    utils.lockAndHideAttribute(CTRL_FingToeInt, True, False)
    utils.lockAndHideAttribute(CTRL_WristAnkle_IK, False, False)
    utils.lockAndHideAttribute(CTRL_LimbPV, False, True)
    utils.lockAndHideAttribute(CTRL_LimbSwitch_FKIK, True, True)



def createFootReverseSystem():
    utils.printHeader('ADDING FOOT REVERSE')
    #Crearem els atributs necessaris al controlador del peu per les connexions del FootReverse
    addCtrlAnkleIKAttribute(CTRL_WristAnkle_IK, 'FootRoll', 0, -80, 80)
    addCtrlAnkleIKAttribute(CTRL_WristAnkle_IK, 'FootRollWeight', 0, 0, 1)
    addCtrlAnkleIKAttribute(CTRL_WristAnkle_IK, 'FootBalance', 0, -80, 80)  
    cmds.shadingNode( 'condition', au=True, n=CTRL_WristAnkle_IK + '_ConditionBalance' )
    cmds.shadingNode( 'condition', au=True, n=CTRL_WristAnkle_IK + '_ConditionRoll' )
    cmds.shadingNode( 'multiplyDivide', au=True, n=CTRL_WristAnkle_IK + '_MultiplyReverse' )

    #Comencarem a fer les connexions.
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRoll', CTRL_WristAnkle_IK + '_ConditionRoll.colorIfFalseG' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRoll', CTRL_WristAnkle_IK + '_ConditionRoll.colorIfTrueR' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRoll', CTRL_WristAnkle_IK + '_ConditionRoll.firstTerm' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootBalance', CTRL_WristAnkle_IK + '_ConditionBalance.colorIfFalseG' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootBalance', CTRL_WristAnkle_IK + '_ConditionBalance.colorIfTrueR' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootBalance', CTRL_WristAnkle_IK + '_ConditionBalance.firstTerm' )

    #Connexions per fer funcionar el Foot Balance
    cmds.setAttr( CTRL_WristAnkle_IK + '_ConditionBalance.operation', 2 )
    cmds.setAttr( CTRL_WristAnkle_IK + '_ConditionBalance.colorIfFalseR',0 )
    cmds.connectAttr( CTRL_WristAnkle_IK + '_ConditionBalance.outColorR', CTRL_WristAnkle_IK + '_MultiplyReverse.input1X' )
    cmds.setAttr( CTRL_WristAnkle_IK + '_MultiplyReverse.input2X',-1 )
    cmds.setAttr( CTRL_WristAnkle_IK + '_MultiplyReverse.input2Y',-1 )
    cmds.connectAttr( CTRL_WristAnkle_IK + '_MultiplyReverse.outputX', REV_Ext + '.rotateZ' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '_ConditionBalance.outColorG', CTRL_WristAnkle_IK + '_MultiplyReverse.input1Y' )
    cmds.connectAttr( CTRL_WristAnkle_IK + '_MultiplyReverse.outputY', REV_Int + '.rotateZ' )
    
    #Ara farem les connexions del FootRoll
    cmds.setAttr( CTRL_WristAnkle_IK + '_ConditionRoll.operation', 4 )
    cmds.setAttr( CTRL_WristAnkle_IK + '_ConditionRoll.colorIfFalseR', 0 )
    cmds.connectAttr( CTRL_WristAnkle_IK + '_ConditionRoll.outColorR', REV_Heel + '.rotateX')
    cmds.shadingNode( 'blendColors', au=True, n=CTRL_WristAnkle_IK + '_bc_Weight')
    cmds.connectAttr( CTRL_WristAnkle_IK + '.FootRollWeight', CTRL_WristAnkle_IK + '_bc_Weight.blender')
    cmds.connectAttr( CTRL_WristAnkle_IK + '_ConditionRoll.outColorG', CTRL_WristAnkle_IK + '_bc_Weight.color1R')
    cmds.connectAttr( CTRL_WristAnkle_IK + '_ConditionRoll.outColorG', CTRL_WristAnkle_IK + '_bc_Weight.color2G')
    cmds.connectAttr( CTRL_WristAnkle_IK + '_bc_Weight.outputR', REV_Tip + '.rotateX')
    cmds.connectAttr( CTRL_WristAnkle_IK + '_bc_Weight.outputG', REV_Ball + '.rotateY')



def addCtrlAnkleIKAttribute(CTRL_WristAnkle_IK, name, defaultV, minV, maxV):
    cmds.select( CTRL_WristAnkle_IK )
    cmds.addAttr( ln=name, at='float', k=True, dv=defaultV, min=minV, max=maxV )



def createMirror():
    assignVariables()
    utils.printHeader('CREATING LIMB MIRROR')
    side = utils.getSideFromBone( cmds.textFieldGrp( 'LimbStartingBone' ,q=True, tx=True ) )
    position = utils.getPositionFromBone( cmds.textFieldGrp( 'LimbStartingBone' ,q=True, tx=True ) )
    newSide = 'R_' if side == 'L_' else 'L_'
    if cmds.checkBox( 'BonesCB', q=True, v=True ):
        cmds.select( cmds.textFieldGrp( 'LimbStartingBone' ,q=True, tx=True ) )
        cmds.mirrorJoint( myz=True, mb=True, sr=(side, newSide) )
        createMirrorControllers(side, position)
        return

    if cmds.checkBox( 'ControllersCB', q=True, v=True ):
        createMirrorControllers(side, position)



def createMirrorControllers(side, position):
    utils.printHeader('CREATING CONTROLLERS MIRROR')
    offsets = []
    for o in offsetsLimb:
        offset = 'OFFSET__' + side + position + o
        offsets.append(offset)
        
    cmds.select( offsets )
    sel = cmds.ls(sl=True)
    limb = 'LEG_' if typeOfLimb == 'Hip' else 'ARM_'
    oldGroup = limb + side + position[:1]    
    sideGroup = cmds.group( em=True, n=oldGroup, w=True )
    for s in sel:
        cmds.parent( s, sideGroup )

    newSide = 'R_' if side == 'L_' else 'L_'
    newGroup = limb + newSide + position[:1]
    
    cmds.duplicate( sideGroup, n=newGroup, rc=True )
    sel = cmds.listRelatives( newGroup, ad=True, s=False )
    side = '_' + side
    newSide = '_' + newSide
    for s in sel:
        name = s.replace(side, newSide)[:-1]
        cmds.rename( s, name )

    sel = cmds.listRelatives( newGroup, c=True )
    for s in sel:
        ctrl = cmds.listRelatives( s, c=True )
        col = (0, 1, 0) if side[1:] == 'L_' else (1, 0, 0)
        RTctrl.overrideColor(ctrl[0], col)

    cmds.setAttr( newGroup + '.scaleX', -1 )
    cmds.parent( newGroup, oldGroup, 'CTRL__Master' )



def createSSforPoleVector():
    assignVariables()
    RT_SpaceSwitch.createSpaceSwitch('LimbSpace', CTRL_LimbPV, 'CTRL__Master', CTRL_WristAnkle_IK, 'Parent')
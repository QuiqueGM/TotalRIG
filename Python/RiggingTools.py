import sys
sys.path.append(r'C:/QGM/UOC/Semestres/2022-23_S1/P3 - Projecte 3. Aplicació interactiva/PAC3/AutoRig/scripts/')

import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils
import RT_Rename
import RT_Controllers
import RT_ChainTools
import RT_SpaceSwitch
import RT_RibbonSystem
import RT_LimbSystem
import RT_HandsSetup
import RT_HeadUtilities
import RT_Utilities
import maya.cmds as cmds
from functools import partial
from importlib import reload

reload(RTvars)
reload(RTeh)
reload(RT_Utils)
reload(RT_Rename)
reload(RT_Controllers)
reload(RT_ChainTools)
reload(RT_SpaceSwitch)
reload(RT_RibbonSystem)
reload(RT_LimbSystem)
reload(RT_HandsSetup)
reload(RT_HeadUtilities)
reload(RT_Utilities)

winWidth = 560
winHeight = 360
margin = 10

def AutorigUI():
    if cmds.window( RTvars.winName, exists=True ):
        cmds.deleteUI( RTvars.winName, window=True )
    elif cmds.windowPref( RTvars.winName, exists=True ):
        cmds.windowPref( RTvars.winName, remove=True )
    
    cmds.window( RTvars.winName, wh=(winWidth+margin, winHeight), s=False, mnb=False, mxb=False, title='AUTORIG ' + RTvars.version )
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    ########################################################################    
    toolHeader('renameBonesTab', '---------   RENAME BONES   ---------')
    subHeader(1, 'SIDE AND POSITION', 1)
    createThreeRadioCollection('LeftSide', 'Left', True, 'RightSide', 'Right', False, 'CenterSide', 'Center', False)
    createThreeRadioCollection('FrontPos', 'Front', False, 'BackPos', 'Back', False, 'NonePose', 'None', True)
    verticalSpace(5)
    subHeader(1, 'PREDEFINED NAMES', 5)
    rowWidth = [winWidth*0.08, winWidth*0.35, winWidth*0.1, winWidth*0.35]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.text( l='', w=rowWidth[0])
    cmds.optionMenu( 'AreaOM', w=rowWidth[1], l='Area   ', cc=fillAreas)
    cmds.menuItem( l='Body' )
    cmds.menuItem( l='Head' )
    cmds.menuItem( l='Arm' )    
    cmds.menuItem( l='Leg' )    
    cmds.text( l='', w=rowWidth[2])
    cmds.optionMenu( 'JointOM', w=rowWidth[3], l='Joint   ', cc=returnBone )
    fillAreas()
    verticalSpace(5)
    rowWidth = [winWidth*0.15, winWidth*0.3, winWidth*0.25]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( 'UseOtherCB', l='Use other', w=rowWidth[1], cc = enableFields )
    cmds.textField( 'AlternativeName' , en=False, w=rowWidth[2] )
    cmds.setParent( '..' )
    rowWidth = [winWidth*0.15, winWidth*0.3, winWidth*0.25, winWidth*0.05, winWidth*0.05]
    cmds.rowLayout( nc=5, cw5=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( 'UseAddNumberCB', l='Add number', w=rowWidth[1], cc=changeIntField )
    cmds.intField( 'AddNumber', en=False, min=1, max=100, w=rowWidth[2], v=1 )
    cmds.button( 'IncButton', en=False, l='+', c=incrementNumber, w=rowWidth[3] )
    cmds.button( 'ResetButton', en=False, l='R', c=resetNumber, w=rowWidth[4] )
    cmds.setParent( '..' )
    verticalSpace(2)
    rowWidth = [winWidth*0.15, winWidth*0.7]
    createButtonAction(10, '', 'Rename', partial(renameBone, ''), False)
    createButtonAction(3,'', 'Autorename Chain', autorenameSimpleChain, False)
    createButtonAction(3,'', 'Autorename Limb', autorenameLimb, True)

    ########################################################################
    toolHeader('limbSystemTab', '---------   LIMB SYSTEM  ---------')
    subHeader(1, 'TYPE OF LIMB', 5)
    createLegOption('Hierarchy', 'FrontLimb', 'Front Leg / Arm', True, 'BackLimb', 'Back Leg / Leg', False)
    rowWidth = [winWidth*0.05, winWidth*0.25, winWidth*0.3, winWidth*0.3]
    
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l='IK System', w=rowWidth[1], al='left')
    cmds.radioButton( 'SimpleLeg', l='Simple IK', al='center', w=rowWidth[2], sl=True, onc=emptyCallback )
    cmds.radioButton( 'HindLeg', l='Hind Leg', al='center', w=rowWidth[2], sl=False, onc=emptyCallback )
    cmds.setParent( '..' )
    
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l='Foot Reverse', w=rowWidth[1], al='left')
    cmds.radioButton( 'FootReverseYes', l='Yes', al='center', w=rowWidth[2], sl=True, onc=emptyCallback )
    cmds.radioButton( 'FootReverseNo', l='No', al='center', w=rowWidth[2], sl=False, onc=emptyCallback )
    cmds.setParent( '..' )
    
    createButtonAction(7,'cc', 'Create controllers', createLimbControllers, False)
    subHeader(7, 'OPTIONS', 5)
    createCheckbox(0.1, 'UseMirrorCB', 'Actvate mirror', emptyCallback, True, True)
    createCheckbox(0.1, 'UseStretchCB', 'Create stretch system', emptyCallback, True, True)
    createCheckbox(0.1, 'UseTwistCB', 'Create twist system', emptyCallback, True, True)
    createCheckbox(0.1, 'UseBendingCB', 'Create bending system', emptyCallback, True, True)
    createCheckbox(0.1, 'UseBoneRollCB', 'Create bone rolls', emptyCallback, True, True)
    createLimbFields()
    createButtonAction(10,'', 'Create Limb System', createLimbSystem, True)


    ########################################################################      
    toolHeader('handsSetupTab', '---------   HANDS SET-UP  ---------')
    mainCL = cmds.columnLayout() 
    colsWidth = [winWidth*0.4, winWidth*0.05, winWidth*0.55] 
    cmds.rowLayout(w=winWidth, nc=3, cw3=colsWidth, rowAttach=(3, 'top', 0))
    cmds.columnLayout(w=colsWidth[0])
    subHeader(1, 'PRESSETS', 3)
    pressetButton(colsWidth[0], 'Basic hand (3)', simple3Layout)
    pressetButton(colsWidth[0], 'Basic hand (4)', simple4Layout)        
    pressetButton(colsWidth[0], 'Simple hand (4/1/1)', simpleHandLayout)
    pressetButton(colsWidth[0], 'Full hand (5/1/1)', fullHandLayout)  
    cmds.setParent('..')
    cmds.columnLayout(w=colsWidth[1])
    cmds.setParent('..')
    cmds.columnLayout(w=colsWidth[2])
    subHeader(1, 'LAYOUT', 3)
    cmds.text(label='          Proximal           Middle              Distal', w=colsWidth[2])
    verticalSpace(7)
    layoutFinger(colsWidth[2], 'Thumb', False)
    layoutFinger(colsWidth[2], 'Index', True)
    layoutFinger(colsWidth[2], 'Middle', True)
    layoutFinger(colsWidth[2], 'Ring', True)
    layoutFinger(colsWidth[2], 'Pinky', True)
    cmds.setParent(mainCL)
    subHeader(7, 'OPTIONS', 5)
    createThreeRadioCollection('HandsParentConst', 'Parent constraint', False, 'HandsOrientConst', 'Orient constraint', True, 'HandsPointConst', 'Point constraint', False, 0.1)
    verticalSpace(1)
    createCheckbox(0.2, 'CreateDoubleOffsetCB', 'Create double offset in fingers / toes', emptyCallback, False, True)
    createCheckbox(0.2, 'ControllersAlongBonesCB', 'Orient controllers along the bones', emptyCallback, True, True)
    rowWidth = [winWidth*0.2, winWidth*0.3, winWidth*.3 ]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( 'OverideFingerControllerSizeCB', l='Override controller size', w=rowWidth[1], cc=enableOverrideSize, v=False, en=True )          
    cmds.floatSliderGrp( 'OverrideControllerSize', min=0.001, max=0.05, s=0.005, field=True, value=0.015, adj=1, cal=(1, "left"), w=rowWidth[2], en=False )
    cmds.setParent( '..' )
    cmds.setParent('..')
    createButtonAction(7,'createHandFoot', 'Create Hand / Foot', createHandFoot, True)
    
    
    ######################################################################## 
    toolHeader('ribbonSystemTab', '---------   RIBBON SYSTEM  ---------')
    subHeader(1, 'JOINTS', 5)
    createTextFieldButtonGrp('RBBottomJoint', 'Top Joint', partial(addObject, 'RBBottomJoint'), True)    
    createTextFieldButtonGrp('RBTopJoint', 'Bottom  Joint', partial(addObject, 'RBTopJoint'), True)
    subHeader(7, 'OPTIONS', 5)
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
    cmds.floatSliderGrp( 'RBSizeTop', l='      Top Size', f=True, min=0.05, max=0.5, v=0.30, s=0.01, cal=(1, "left"), cw3=colWidth )
    cmds.setParent( '..' )
    verticalSpace(3)
    createButtonAction(10,'', 'Create Ribbon System', createRibbonSystem, True)
    
    
    ######################################################################## 
    toolHeader('chainToolsTab', '---------   CHAIN TOOLS  ---------')
    subHeader(1, 'REDEFINE CHAIN', 5)
    rowWidth = [winWidth*0.1, winWidth*0.65]
    cmds.rowLayout( nc=2, cw2=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.intSliderGrp( 'NumBones', l='Number of bones', min=2, max=10, field=True, value=5, adj=1, cal=(1, "left"), w=rowWidth[1] )
    cmds.setParent( '..' ) 
    createCheckbox(0.1, 'DeleteChainCB', 'Delete source chain', emptyCallback, True, True)
    createCheckbox(0.1, 'ControllersAndConnectCB', 'Create controllers and connect', emptyCallback, False, True) 
    createButtonAction(10,'', 'Redefine Chain', redefineChain, False)
    subHeader(7, 'CONTROLLERS', 5)
    createFloarSliderGroup('CtrlSimpleScaleChain', 'Controllers scale          ', 0.15, 0.01, 1.0, 0.05)
    createButtonAction(3,'', 'Create Chain Controllers', createChainControllers, False)
    subHeader(7, 'OPTIONS', 5)
    createCheckbox(0.1, 'UseMirrorChainCB', 'Activate mirror', emptyCallback, True, True)
    createThreeRadioCollection('ParentConst', 'Parent constraint', True, 'OrientConst', 'Orient constraint', False, 'PointConst', 'Point constraint', False, 0.1)
    createButtonAction(10,'', 'Create Chain System', createChainSystem, True)
    

    ######################################################################## 
    toolHeader('headControllerTab', '---------   HEAD CONTROLLER  ---------')
    subHeader(1, 'EYES', 5)
    createFloarSliderGroup('EyesPupillaryDist', 'Radius factor scale      ', 0.85, 0.75, 0.95, 0.01)
    createFloarSliderGroup('EyesControllerDist', 'Distance from Eyes      ', 1.0, 0.01, 1.5, 0.05)       
    subHeader(7, 'OPTIONS', 5)
    createCheckbox(0.1, 'CreateAndConnectEyesCB', 'Create and connect Eyes', emptyCallback, True, True)
    createCheckbox(0.1, 'ConnectTongueCB', 'Connect tongue', emptyCallback, True, True)
    createCheckbox(0.1, 'SquashAndStretchCB', 'Create Squash and Stretch', emptyCallback, True, True)
    createCheckbox(0.1, 'BlendShapesCB', 'Create Blend Shapes', emptyCallback, True, True)
    verticalSpace(2)
    createButtonAction(10,'', 'Create Head', createHead, True)
    
    
    ########################################################################
    toolHeader('spaceSwitchTab', '---------   SPACE SWITCH  ---------')
    subHeader(1, 'TARGET', 1)
    rowWidth = [winWidth*0.1, winWidth*0.165, winWidth*0.2]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l='Attribute', al='left', w=rowWidth[1] )
    cmds.textField( 'SSAttribute' , en=True, w=rowWidth[2] )
    cmds.setParent( '..' )
    createTextFieldButtonGrp('SSController', 'Controller', partial(addObject, 'SSController'), True)
    subHeader(5, 'SPACE SWITCH', 7)
    createTextFieldButtonGrp('SSFrom0', 'From (0)', partial(addObject, 'SSFrom0'), True)
    createTextFieldButtonGrp('SSTo1', 'To (1)', partial(addObject, 'SSTo1'), True)
    subHeader(5, 'CONSTRAINT TYPE', 7)
    createRadioCollection('SpaceSwitchParent', 'Parent space switch', 'SpaceSwitchAimOrient', 'Point/Orient space switch')    
    createButtonAction(10,'', 'Create Space Switch', partial(createSpaceSwitch, '', '', '', '', ''), True)
    
    
    ########################################################################
    toolHeader('controllersTab', '---------   CREATE CONTROLLERS  ---------')
    subHeader(1, 'SCALE AND COLOR', 1)
    rowWidth = [winWidth*0.5, winWidth*0.05, winWidth*0.45]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.floatSliderGrp( 'ctrlScale', l='Scale    ', f=True, min=0.05, max=1.0, v=0.25, s=0.05, cw=[1,75] )
    cmds.text( l='', w=rowWidth[1] )    
    cmds.gridLayout( nc=5, cwh=(rowWidth[2]/6, rowWidth[2]/10) )
    cols = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (0.5, 1, 0.5), (1, 0.5, 0), (0, 0.5, 1), (1, 0.5, 1)]
    for cl in cols:
        cmds.button( l='', c=partial(assignColor, cl), bgc=cl )
    cmds.setParent( 'controllersTab' )
    subHeader(5, 'SHAPE', 7)
    rowWidth = [winWidth*0.1, winWidth*0.2, winWidth*0.2, winWidth*0.2, winWidth*0.2]
    cmds.rowLayout( nc=5, cw5=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )     
    cmds.radioButton( 'CircleCtrl', l='Circle', w=rowWidth[1], sl=True )
    cmds.radioButton( 'BoxCtrl', l='Box', w=rowWidth[2] )
    cmds.radioButton( 'MeshCtrl', l='Mesh', w=rowWidth[3] )
    cmds.radioButton( 'DiamondCtrl', l='Diamond', w=rowWidth[3] )
    cmds.setParent( '..' )
    subHeader(5, 'ORIENTATION', 9)
    createRadioCollection('ObjectCtrl', 'Object', 'WorldCtrl', 'World')
    createButtonAction(3, '', 'Create Controller', partial(createController, '', '', '', '', '', ''), False)
    createTwoButtonsAction(3, 'colorizeCtrl', 'Colorize Controller', partial(colorizeController), 'changeCtrl', 'Change Controller', partial(changeController), False)
    createTwoButtonsAction(3, 'copyCtrl', 'Copy CV Controller', partial(copyController), 'resetCtrl', 'Reset Controllers', resetControllers, True)


    ########################################################################
    toolHeader('utilitiesTab', '---------   UTILITIES  ---------')
    verticalSpace(5)
    w = winWidth*0.9
    h = 30
    
    createDoubleButtonUtility('Joint - World', partial(createSimpleJoint, 'World'), 'Joint - Z Up', partial(createSimpleJoint, 'ZUp'), w, h)
    createDoubleButtonUtility('Decrease Joint Size', partial(jointSize, -0.2), 'Increase Joint Size', partial(jointSize, 0.2), w, h)
    createDoubleButtonUtility('Orient Simple Chain', rotateAndOrientSimpleChainZUp, 'Orient Chain', orientSimpleChain, w, h)
    createDoubleButtonUtility('Orient End Joint', orientEndJoint, ' Show/Hide LRA ', localRotationAxes, w, h)
    createDoubleButtonUtility('Unlock OFFSET', unlockOffset, 'Lock OFFSET', lockOffset, w, h)
    createDoubleButtonUtility('IK / FK Convertion', convertIKtoObject, 'IK / FK Snap', IKFKSnap, w, h)


    cmds.tabLayout( tabs, edit=True, tabLabel=(('renameBonesTab', 'Rename'), ('limbSystemTab', 'Limbs'), ('handsSetupTab', 'Hands'), ('ribbonSystemTab', 'Ribbons'), ('chainToolsTab', 'Chains'), ('headControllerTab', 'Head'), ('spaceSwitchTab', 'S. Switch'), ('utilitiesTab', 'Utilities'), ('controllersTab', 'Controllers')), sti=1 )
    cmds.showWindow(RTvars.winName)
    RT_HandsSetup.simple3Layout()
    return



####################################### UI SNIPPETS #####################################

def createThreeRadioCollection(name1, label1, state1, name2, label2, state2, name3, label3, state3, initPos=0.15):
    rowWidth = [winWidth*initPos, winWidth*0.3, winWidth*0.3, winWidth*0.3]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )
    cmds.radioButton( name1, l=label1, al='center', w=rowWidth[1], sl=state1 )
    cmds.radioButton( name2, l=label2, al='center', w=rowWidth[2], sl=state2 )
    cmds.radioButton( name3, l=label3, al='center', w=rowWidth[3], sl=state3 )
    cmds.setParent( '..' )



def createLegOption(label, name1, label1, state1, name2, label2, state2):
    rowWidth = [winWidth*0.05, winWidth*0.25, winWidth*0.3, winWidth*0.3]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l=label, w=rowWidth[1], al='left')
    cmds.radioButton( name1, l=label1, al='center', w=rowWidth[2], sl=state1 )
    cmds.radioButton( name2, l=label2, al='center', w=rowWidth[3], sl=state2 )
    cmds.setParent( '..' )



def createDoubleButtonUtility(labelBtn1, callbackBtn1, labelBtn2, callbackBtn2, buttonWidth, buttonHeight):
    rowWidth = [(winWidth-buttonWidth-margin)/2, buttonWidth/2, buttonWidth/2,(winWidth-buttonWidth-margin)/2]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.button( l=labelBtn1, c=callbackBtn1 , w=rowWidth[1], h=buttonHeight )
    cmds.button( l=labelBtn2, c=callbackBtn2 , w=rowWidth[2], h=buttonHeight )
    cmds.text( l='', w=rowWidth[3] )
    cmds.setParent( '..' )
    verticalSpace(2)



def createButtonAction(space, name, label, callback, endOfTab):
    verticalSpace(space)
    rowWidth = [winWidth*0.2, winWidth*0.6, winWidth*0.2]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.button( name, l=label, c=callback , w=rowWidth[1], h=30)
    cmds.text( l='', w=rowWidth[2] )
    cmds.setParent( '..' )
    if endOfTab:
        cmds.setParent( '..' )



def createTwoButtonsAction(space, nameBtn1, labelBtn1, callbackBtn1, nameBtn2, labelBtn2, callbackBtn2, endOfTab):
    verticalSpace(space)
    rowWidth = [winWidth*0.2, winWidth*0.295, winWidth*0.005, winWidth*0.295, winWidth*0.2]
    cmds.rowLayout( nc=5, cw5=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.button( nameBtn1, l=labelBtn1, c=callbackBtn1 , w=rowWidth[1], h=30)
    cmds.text( l='', w=rowWidth[2] )
    cmds.button( nameBtn2, l=labelBtn2, c=callbackBtn2 , w=rowWidth[3], h=30)
    cmds.text( l='', w=rowWidth[4] )
    cmds.setParent( '..' )
    if endOfTab:
        cmds.setParent( '..' )



def createCheckbox(width, name, label, callback, value, enable):
    rowWidth = [winWidth*width, winWidth*0.65]
    cmds.rowLayout( nc=2, cw2=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( name, l=label, w=rowWidth[1], cc=callback, v=value, en=enable )
    cmds.setParent( '..' )    



def createFloarSliderGroup(name, label, defValue, min, max, step):
    rowWidth = [winWidth*0.1, winWidth*0.9]
    cmds.rowLayout( nc=2, cw2=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.floatSliderGrp( name, l=label, f=True, min=min, max=max, v=defValue, s=step, cw=[1,115] )
    cmds.setParent( '..' )



def createRadioCollection(name1, label1, name2, label2):
    rowWidth = [winWidth*0.1, winWidth*0.45, winWidth*0.45]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.radioCollection()
    cmds.text( l='', w=rowWidth[0] )     
    cmds.radioButton( name1, l=label1, w=rowWidth[1], sl=True )
    cmds.radioButton( name2, l=label2, w=rowWidth[2] )
    cmds.setParent( '..' )



def createTextFieldButtonGrp(name, label, callback, visible):
    rowWidth = [winWidth*0.1, winWidth*0.8]
    cmds.rowLayout( nc=2, cw2=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.textFieldButtonGrp( name, l=label, w=rowWidth[1], vis=visible, ed=False, cw3=(rowWidth[1]*0.2, rowWidth[1]*0.60, rowWidth[1]*0.3), cl3=('left', 'left', 'left'), bl='  Add  ', bc=callback )
    cmds.setParent( '..' )



def pressetButton(column, labelButton, callback):
    rowWidth = [column*0.1, column*0.9]
    cmds.rowLayout( nc=2, cw2=rowWidth )
    cmds.text(label='', w=rowWidth[0])
    cmds.button( l=labelButton, c=callback, w=rowWidth[1], h=24 )
    cmds.setParent('..')



def layoutFinger(column, finger, value):
    rowWidth = [column*0.28, column*0.24, column*0.24, column*0.24]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.text(label=finger + '          ', w=rowWidth[0], al='right')
    cmds.checkBox( finger + 'ProximalCB', l='', w=rowWidth[1], onc=emptyCallback, ofc=emptyCallback, v=True, en=True )
    cmds.checkBox( finger + 'MiddleCB', l='', w=rowWidth[2], onc=emptyCallback, ofc=emptyCallback, v=value, en=True )
    cmds.checkBox( finger + 'DistalCB', l='', w=rowWidth[3], onc=emptyCallback, ofc=emptyCallback , v=True, en=True )  
    cmds.setParent('..')
    verticalSpace(7)



def toolHeader(tabName, textHeader):
    cmds.columnLayout(tabName, columnAttach=('both', margin), cw=winWidth )
    verticalSpace(5)



def subHeader(spaceBefore, subHeader, spaceAfter):
    verticalSpace(spaceBefore)
    cmds.text( l=subHeader, al='left', fn='boldLabelFont')
    verticalSpace(spaceAfter)



def verticalSpace(space):
    cmds.text( l='', h=space )    



def fillAreas(*args):
    currentValue = cmds.optionMenu( 'AreaOM', q=True, v=True )
    joints = cmds.optionMenu( 'JointOM', q=True, ill=True )
    
    if joints: cmds.deleteUI( joints )
    
    if currentValue == 'Head': fillArea(RTvars.headBones)
    elif currentValue == 'Leg': fillArea(RTvars.legBones)
    elif currentValue == 'Arm': fillArea(RTvars.armBones)      
    elif currentValue == 'Body': fillArea(RTvars.bodyBones)
        
    cmds.setParent( '..' )



def fillArea(bones):
    for b in bones:
        cmds.menuItem( p='JointOM', l=b )
    RTvars.bone = bones[0]



def createLimbFields():
    bones = []
    bones.extend(RTvars.bonesHindArm)
    bones.extend(RTvars.simpleHand)
    bones.extend(RTvars.hand)
    bones.extend(RTvars.bonesHindLeg)
    bones.extend(RTvars.simpleFoot)
    bones.extend(RTvars.foot)

    rowWidth = [winWidth*0.2, winWidth*0.60, winWidth*0.3]
    for b in range(len(bones)):
        cmds.textFieldButtonGrp( bones[b], l=bones[b], vis=False, ed=False, cw3=rowWidth, cl3=('left', 'left', 'left'), bl='  Add  ', bc=partial(addObject, bones[b]), h=20 )


####################################### VALIDATORS #####################################

def changeIntField(*args):
    value = cmds.checkBox( 'UseAddNumberCB', q=True, v=True )
    cmds.intField( 'AddNumber', edit=True, en=value )
    cmds.button( 'IncButton', edit=True, en=value )
    cmds.button( 'ResetButton', edit=True, en=value )


def enableFields(*args):
    value = cmds.checkBox( 'UseOtherCB', q=True, v=True )
    cmds.optionMenu( 'AreaOM', edit=True, en=not value )
    cmds.optionMenu( 'JointOM', edit=True, en=not value )
    cmds.textField( 'AlternativeName', edit=True, en=value )


def enableOverrideSize(*args):
    value = cmds.checkBox( 'OverideFingerControllerSizeCB', q=True, v=True )
    cmds.floatSliderGrp( 'OverrideControllerSize', edit=True, en=value )


def enableCreateEyes(*args):
    value = cmds.checkBox( 'CreateAndConnectEyesCB', q=True, v=True )
    cmds.floatSliderGrp( 'EyesPupillaryDist', edit=True, en=value )
    cmds.floatSliderGrp( 'EyesControllerDist', edit=True, en=value )


def enableBlendShapes(*args):
    value = cmds.checkBox( 'BlendShapesCB', q=True, v=True )
    cmds.checkBox( 'FacialExpressionsCB', edit=True, en=value )
    cmds.checkBox( 'EyesCB', edit=True, en=value )


####################################### CALLBACKS #####################################

### GLOBAL VARIABLES & UTILS

def emptyCallback(*args):
    print ('Empty callback')

def returnBone(item):
    RTvars.bone = item

def addObject(nameBone, *args):
    RT_Utils.addObject(nameBone)


### RENAME

def incrementNumber(*args):
    RT_Rename.incrementNumber()

def resetNumber(*args):
    RT_Rename.resetNumber()

def renameBone(add, *args):
    RT_Rename.renameBone(add)

def autorenameLimb(*args):
    RT_Rename.autorenameLimb()

def autorenameSimpleChain(*args):
    RT_Rename.autorenameSimpleChain()
    

### LIMB SYSTEM

def createLimbControllers(*args):
    RT_LimbSystem.createLimbControllers()

def createLimbSystem(*args):
    RT_LimbSystem.createLimbSystem()


### HANDS

def simple3Layout(*args):
    RT_HandsSetup.simple3Layout()

def simple4Layout(*args):
    RT_HandsSetup.simple4Layout()

def simpleHandLayout(*args):
    RT_HandsSetup.simpleHandLayout()

def fullHandLayout(*args):
    RT_HandsSetup.fullHandLayout()
    
def createHandFoot(*args):
    RT_HandsSetup.createHandFoot()


### RIBBON

def createRibbonSystem(*args):
    RT_RibbonSystem.createRibbonSystem()


### CHAINS

def redefineChain(*args):
    RT_ChainTools.redefineChain(False, True, False)

def createChainControllers(*args):
    RT_ChainTools.createChainControllers(False)

def createChainSystem(*args):
    RT_ChainTools.createChainSystem(False)


### EYES & HEAD

def createHead(*args):
    RT_HeadUtilities.createHead()


### SPACE SWITCH

def createSpaceSwitch(pName, pCtrl, pFrom0, pTo1, type, *args):
    RT_SpaceSwitch.createSpaceSwitch(pName, pCtrl, pFrom0, pTo1, type)


### CONTROLLERS

def createController(sh, col, scl, ori, lblFrom, lblTo, *args):
    RT_Controllers.createController(sh, col, scl, ori, lblFrom, lblTo)
    
def assignColor(col, *args):
    RT_Controllers.assignColor(col)

def colorizeController(*args):
    RT_Controllers.colorizeController()

def changeController(*args):
    RT_Controllers.changeController()

def copyController(*args):
    RT_Controllers.copyController()

def resetControllers(*args):
    RT_Controllers.resetControllers()
    

### UTILITIES

def createSimpleJoint(orientation, *args):
    RT_Utilities.createSimpleJoint(orientation, '')

def jointSize(size, *args):
    RT_Utilities.jointSize(size)
    
def rotateAndOrientSimpleChainZUp(*args):
    RT_Utilities.rotateAndOrientSimpleChainZUp()

def orientSimpleChain(*args):
    RT_Utilities.orientSimpleChain()

def orientEndJoint(*args):
    RT_Utilities.orientEndJoint()

def localRotationAxes(*args):
    RT_Utilities.localRotationAxes()

def lockOffset(*args):
    RT_Utilities.handleOffset(True)

def unlockOffset(*args):
    RT_Utilities.handleOffset(False)

def convertIKtoObject(*args):
    RT_Utilities.convertIKtoObject(); 

def IKFKSnap(*args):
    RT_Utilities.IKFKSnap();


AutorigUI()

import sys
sys.path.append(r'D:/UOC/Semestres/2022-23_S2/TFG - Videojocs/TotalRIG/Python/')

import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils
import RT_Rename
import RT_Controllers
import RT_LimbSystem
import RT_HandsSetup
import RT_ChainTools
import RT_SpaceSwitch
import RT_RibbonSystem
import RT_HeadUtilities
import RT_Utilities
import maya.cmds as cmds
from functools import partial
#from importlib import reload

reload(RTvars)
reload(RTeh)
reload(RT_Utils)
reload(RT_RibbonSystem)
reload(RT_LimbSystem)
reload(RT_HandsSetup)
reload(RT_RibbonSystem)
reload(RT_ChainTools)
reload(RT_Controllers)
reload(RT_HeadUtilities)
reload(RT_SpaceSwitch)
reload(RT_Utilities)
reload(RT_Rename)

winWidth = 560
winHeight = 440
margin = 10

def rigginToolsUI():
    if cmds.window( RTvars.winName, exists=True ):
        cmds.deleteUI( RTvars.winName, window=True )
    elif cmds.windowPref( RTvars.winName, exists=True ):
        cmds.windowPref( RTvars.winName, remove=True )
    
    cmds.window( RTvars.winName, wh=(winWidth+margin, winHeight), s=False, mnb=False, mxb=False, title=RTvars.winName + ' ' + RTvars.version )
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    RT_Rename.drawUI()
    RT_LimbSystem.drawUI()
    RT_HandsSetup.drawUI()
    RT_RibbonSystem.drawUI()
    RT_ChainTools.drawUI()
    RT_HeadUtilities.drawUI()

    
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
    createButtonAction(10,'', 'Create Space Switch', partial(createSpaceSwitch, '', '', '', '', ''), False)
    createSpaceForUtilities('---------   UTILITIES  ---------')
    createButtonAction(3,'', 'Create Point/Orient Space Switch for Head', createSpaceSwitchForHead, False)
    createButtonAction(3,'', 'Create Point/Orient Space Switch for Tail', createSpaceSwitchForTail, True)
    
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
    createSpaceForUtilities('---------   UTILITIES  ---------')
    createButtonAction(3, 'colorizeCtrl', 'Colorize Controller', partial(colorizeController), False)
    createButtonAction(3, 'changeCtrl', 'Change Controller', partial(changeController), False)
    createButtonAction(3, 'copyCtrl', 'Copy CV Controller', partial(copyController), True)

    toolHeader('utilitiesTab', '---------   UTILITIES  ---------')
    verticalSpace(5)
    w = winWidth*0.9
    h = 30
    createFourButtonUtility('Joint - World', partial(createSimpleJoint, 'World'), 'Joint - Z Up', partial(createSimpleJoint, 'ZUp'), 'Ribbon joints', createRibbonJoints, ' -- EMPTY -- ', emptyCallback, w, h)
    createFourButtonUtility('Orient Simple Chain', rotateAndOrientSimpleChainZUp, 'Orient Chain', orientSimpleChain, 'Orient End Joint', orientEndJoint, ' Show/Hide LRA ', localRotationAxes, w, h)
    createFourButtonUtility('Create Root', createRoot, 'Connect Legs', connectLegs, 'Connect Arms', connectArms, 'Connect Wings', connectWings, w, h)
    createDoubleButtonUtility('Delete References', deleteReferences, 'Delete Blend Shape Targets', deleteBSTargets, w, h)
    createDoubleButtonUtility('Bind skin', bindSkinMesh, 'Remove END influences', removeInfluences, w, h)
    createSpaceForUtilities('---------   UTILITIES  ---------')
    createDoubleButtonUtility('Decrease Joint Size', partial(jointSize, -0.2), 'Increase Joint Size', partial(jointSize, 0.2), w, h)
    createFourButtonUtility('Reset controllers', resetControllers, 'Rename Limb', renameLimb, 'Unlock OFFSET', unlockOffset, 'Lock OFFSET', lockOffset, w, h)
            
    cmds.tabLayout( tabs, edit=True, tabLabel=(('renameBonesTab', 'Rename'), ('limbSystemTab', 'Limbs'), ('handsSetupTab', 'Hands'), ('ribbonSystemTab', 'Ribbons'), ('chainToolsTab', 'Chains'), ('headControllerTab', 'Head'), ('spaceSwitchTab', 'S. Switch'), ('utilitiesTab', 'Utilities'), ('controllersTab', 'Controllers')), sti=1 )
    cmds.showWindow(RTvars.winName)
    RT_HandsSetup.simple3Layout()
    return



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



def createButtonUtility(label, callback, buttonWidth, buttonHeight):
    rowWidth = [(winWidth-buttonWidth-margin)/2, buttonWidth, (winWidth-buttonWidth-margin)/2]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.button( l=label, c=callback , w=rowWidth[1], h=buttonHeight )
    cmds.setParent( '..' )
    verticalSpace(2)



def createDoubleButtonUtility(labelBtn1, callbackBtn1, labelBtn2, callbackBtn2, buttonWidth, buttonHeight):
    rowWidth = [(winWidth-buttonWidth-margin)/2, buttonWidth/2, buttonWidth/2,(winWidth-buttonWidth-margin)/2]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.button( l=labelBtn1, c=callbackBtn1 , w=rowWidth[1], h=buttonHeight )
    cmds.button( l=labelBtn2, c=callbackBtn2 , w=rowWidth[2], h=buttonHeight )
    cmds.text( l='', w=rowWidth[3] )
    cmds.setParent( '..' )
    verticalSpace(2)


def createFourButtonUtility(labelBtn1, callbackBtn1, labelBtn2, callbackBtn2, labelBtn3, callbackBtn3, labelBtn4, callbackBtn4, buttonWidth, buttonHeight):
    sp = 1
    rowWidth = [(winWidth-buttonWidth-margin)/2, buttonWidth/4-sp, buttonWidth/4-sp, buttonWidth/4-sp, buttonWidth/4-sp,(winWidth-buttonWidth-margin)/2]
    cmds.rowLayout( nc=6, cw6=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.button( l=labelBtn1, c=callbackBtn1 , w=rowWidth[1], h=buttonHeight )
    cmds.button( l=labelBtn2, c=callbackBtn2 , w=rowWidth[2], h=buttonHeight )
    cmds.button( l=labelBtn3, c=callbackBtn3 , w=rowWidth[3], h=buttonHeight )
    cmds.button( l=labelBtn4, c=callbackBtn4 , w=rowWidth[4], h=buttonHeight )    
    cmds.text( l='', w=rowWidth[5] )
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



def createFourButtonsAction(space, nameBtn1, labelBtn1, callbackBtn1, nameBtn2, labelBtn2, callbackBtn2, nameBtn3, labelBtn3, callbackBtn3, nameBtn4, labelBtn4, callbackBtn4, endOfTab):
    verticalSpace(space)
    sp = 1
    rowWidth = [(winWidth-margin)/4.1 ,(winWidth-margin)/4.1, (winWidth-margin)/4.1, (winWidth-margin)/4.1]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.button( nameBtn1, l=labelBtn1, c=callbackBtn1 , w=rowWidth[0], h=30 )
    cmds.button( nameBtn2, l=labelBtn2, c=callbackBtn2 , w=rowWidth[1], h=30 )
    cmds.button( nameBtn3, l=labelBtn3, c=callbackBtn3 , w=rowWidth[2], h=30 )
    cmds.button( nameBtn4, l=labelBtn4, c=callbackBtn4 , w=rowWidth[3], h=30 )
  
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



def toolHeader(tabName, textHeader):
    cmds.columnLayout(tabName, columnAttach=('both', margin), cw=winWidth )
    verticalSpace(5)



def subHeader(spaceBefore, subHeader, spaceAfter):
    verticalSpace(spaceBefore)
    cmds.text( l=subHeader, al='left', fn='boldLabelFont')
    verticalSpace(spaceAfter)



def verticalSpace(space):
    cmds.text( l='', h=space )    



def createSpaceForUtilities(utilities):
    verticalSpace(10)
    cmds.separator()
    cmds.separator()   
    verticalSpace(5)



####################################### CALLBACKS #####################################

### GLOBAL VARIABLES & UTILS

def emptyCallback(*args):
    print ('Empty callback')

def returnBone(item):
    RTvars.bone = item

def addObject(nameBone, *args):
    RT_Utils.addObject(nameBone)


### SPACE SWITCH

def createSpaceSwitch(pName, pCtrl, pFrom0, pTo1, type, *args):
    RT_SpaceSwitch.createSpaceSwitch(pName, pCtrl, pFrom0, pTo1, type)

def createSpaceSwitchForHead(*args):
    RT_SpaceSwitch.createSpaceSwitchForHead()

def createSpaceSwitchForTail(*args):
    RT_SpaceSwitch.createSpaceSwitchForTail()


### CONTROLLERS

def assignColor(col, *args):
    RT_Controllers.assignColor(col)

def colorizeController(*args):
    RT_Controllers.colorizeController()

def changeController(*args):
    RT_Controllers.changeController()

def copyController(*args):
    RT_Controllers.copyController()


def createController(sh, col, scl, ori, lblFrom, lblTo, *args):
    RT_Controllers.createController(sh, col, scl, ori, lblFrom, lblTo)


### UTILITIES

def createSimpleJoint(orientation, *args):
    RT_Utilities.createSimpleJoint(orientation, '')

def rotateAndOrientSimpleChainZUp(*args):
    RT_Utilities.rotateAndOrientSimpleChainZUp()

def createRibbonJoints(*args):
    RT_Utilities.createRibbonJoints()

def orientSimpleChain(*args):
    RT_Utilities.orientSimpleChain()

def orientEndJoint(*args):
    RT_Utilities.orientEndJoint()

def localRotationAxes(*args):
    RT_Utilities.localRotationAxes()

def createRoot(*args):
    RT_Utilities.createRoot()

def connectLegs(*args):
    RT_Utilities.connectLegs()

def connectArms(*args):
    RT_Utilities.connectArms()

def connectWings(*args):
    RT_Utilities.connectWings()

def connectBodyToCtrlMaster(*args):
    RT_Utilities.connectBodyToCtrlMaster()

def deleteReferences(*args):
    RT_Utilities.deleteReferences()

def deleteBSTargets(*args):
    RT_Utilities.deleteBSTargets()

def bindSkinMesh(*args):
    RT_Utilities.bindSkinMesh()

def removeInfluences(*args):
    RT_Utilities.removeInfluences()

def jointSize(size, *args):
    RT_Utilities.jointSize(size)

def resetControllers(*args):
    RT_Utilities.resetControllers()

def renameLimb(*args):
    RT_Utilities.renameLimb()

def unlockOffset(*args):
    RT_Utilities.handleOffset(False)

def lockOffset(*args):
    RT_Utilities.handleOffset(True)
    


rigginToolsUI()

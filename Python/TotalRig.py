import sys
sys.path.append(r'D:/UOC/Semestres/2022-23_S2/TFG - Videojocs/TotalRIG/Python/')

import TR_GlobalVariables as TRvars
import TR_ErrorsHandler as TReh
import TR_Utils
import TR_Rename
import TR_Controllers
import TR_LimbSystem
import TR_HandsSetup
import TR_ChainTools
import TR_SpaceSwitch
import TR_RibbonSystem
import TR_HeadUtilities
import TR_Utilities
import maya.cmds as cmds
from functools import partial
#from importlib import reload

reload(TRvars)
reload(TReh)
reload(TR_Utils)
reload(TR_RibbonSystem)
reload(TR_LimbSystem)
reload(TR_HandsSetup)
reload(TR_RibbonSystem)
reload(TR_ChainTools)
reload(TR_Controllers)
reload(TR_HeadUtilities)
reload(TR_SpaceSwitch)
reload(TR_Utilities)
reload(TR_Rename)

winWidth = 560
winHeight = 440
margin = 10

def totalRigUI():
    if cmds.window( TRvars.winName, exists=True ):
        cmds.deleteUI( TRvars.winName, window=True )
    elif cmds.windowPref( TRvars.winName, exists=True ):
        cmds.windowPref( TRvars.winName, remove=True )
    
    cmds.window( TRvars.winName, wh=(winWidth+margin, winHeight), s=False, mnb=False, mxb=False, title=TRvars.winName + ' ' + TRvars.version )
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    TR_Rename.drawUI()
    TR_LimbSystem.drawUI()
    TR_HandsSetup.drawUI()
    TR_RibbonSystem.drawUI()
    TR_ChainTools.drawUI()
    TR_HeadUtilities.drawUI()
    TR_SpaceSwitch.drawUI()
    TR_Controllers.drawUI()
    TR_Utilities.drawUI()
    
    cmds.tabLayout( tabs, edit=True, tabLabel=(('renameBonesTab', 'Rename'), ('limbSystemTab', 'Limbs'), ('handsSetupTab', 'Hands'), ('ribbonSystemTab', 'Ribbons'), ('chainToolsTab', 'Chains'), ('headControllerTab', 'Head'), ('spaceSwitchTab', 'S. Switch'), ('utilitiesTab', 'Utilities'), ('controllersTab', 'Controllers')), sti=1 )
    cmds.showWindow(TRvars.winName)
    TR_HandsSetup.simple3Layout()
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



def emptyCallback(*args):
    print ('Empty callback')



def returnBone(item):
    TRvars.bone = item



def addObject(nameBone, *args):
    TR_Utils.addObject(nameBone)



totalRigUI()
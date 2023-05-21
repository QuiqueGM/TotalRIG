import TotalRig as TR
import TR_GlobalVariables as TRvars
import TR_ErrorsHandler as TReh
import TR_Utils as utils
import maya.cmds as cmds
from functools import partial


def drawUI():
    TR.toolHeader('handsSetupTab', '---------   HANDS SET-UP  ---------')
    mainCL = cmds.columnLayout()
    winWidth = TR.winWidth
    colsWidth = [winWidth*0.4, winWidth*0.05, winWidth*0.55]
    cmds.rowLayout(w=winWidth, nc=3, cw3=colsWidth, rowAttach=(3, 'top', 0))
    cmds.columnLayout(w=colsWidth[0])
    TR.subHeader(1, 'PRESSETS', 3)
    TR.pressetButton(colsWidth[0], 'Basic hand (3)', simple3Layout)
    TR.pressetButton(colsWidth[0], 'Basic hand (4)', simple4Layout)        
    TR.pressetButton(colsWidth[0], 'Dragon (4/1)', dragonLayout)
    TR.pressetButton(colsWidth[0], 'Simple hand (4/1/1)', simpleHandLayout)
    TR.pressetButton(colsWidth[0], 'Full hand (5/1/1)', fullHandLayout)  
    cmds.setParent('..')
    cmds.columnLayout(w=colsWidth[1])
    cmds.setParent('..')
    cmds.columnLayout(w=colsWidth[2])
    TR.subHeader(1, 'LAYOUT', 3)
    cmds.text(label='          Proximal           Middle              Distal', w=colsWidth[2])
    TR.verticalSpace(7)
    layoutFinger(colsWidth[2], 'Thumb', False)
    layoutFinger(colsWidth[2], 'Index', True)
    layoutFinger(colsWidth[2], 'Middle', True)
    layoutFinger(colsWidth[2], 'Ring', True)
    layoutFinger(colsWidth[2], 'Pinky', True)
    cmds.setParent(mainCL)
    TR.subHeader(7, 'OPTIONS', 5)
    TR.createThreeRadioCollection('HandsParentConst', 'Parent constraint', False, 'HandsOrientConst', 'Orient constraint', True, 'HandsPointConst', 'Point constraint', False, 0.1)
    TR.verticalSpace(1)
    TR.createCheckbox(0.2, 'UseSimpleNameCB', 'Use short naming convention', TR.emptyCallback, True, True)
    TR.createCheckbox(0.2, 'CreateDoubleOffsetCB', 'Create double offset in fingers / toes', TR.emptyCallback, False, True)
    TR.createCheckbox(0.2, 'ControllersAlongBonesCB', 'Orient controllers along the bones', TR.emptyCallback, True, True)
    rowWidth = [winWidth*0.2, winWidth*0.3, winWidth*.3 ]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( 'OverideFingerControllerSizeCB', l='Override controller size', w=rowWidth[1], cc=enableOverrideSize, v=False, en=True )          
    cmds.floatSliderGrp( 'OverrideControllerSize', min=0.001, max=0.05, s=0.005, field=True, value=0.015, adj=1, cal=(1, "left"), w=rowWidth[2], en=False )
    cmds.setParent( '..' )
    cmds.setParent('..')
    TR.createSpaceForUtilities('---------   UTILITIES  ---------')
    TR.createTwoButtonsAction(3,'selectDrivenKeys', 'Selecy Driven Key Offsets', partial(selectDrivenKeys, 'DRIVEN_KEY'), 'getHierarchyLayout', 'Get hierarchy layout', getHierarchyLayout, False)
    TR.createTwoButtonsAction(3,'saveClosedHand', 'Save Closed', partial(saveHand, 'CLOSED'), 'saveOpenHand', 'Save Open', partial(saveHand, 'OPEN'),  False)
    TR.createTwoButtonsAction(3,'saveDrivenKeysHand', 'Create Driven Keys', saveDrivenKeysHand, 'mirrorDrivenKeysHand', 'Mirror Driven Keys', mirrorDrivenKeysHand, True)



def layoutFinger(column, finger, value):
    rowWidth = [column*0.28, column*0.24, column*0.24, column*0.24]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.text(label=finger + '          ', w=rowWidth[0], al='right')
    cmds.checkBox( finger + 'ProximalCB', l='', w=rowWidth[1], onc=partial(addHandLayout, 10), ofc=partial(addHandLayout, -10), v=True, en=True )
    cmds.checkBox( finger + 'MiddleCB', l='', w=rowWidth[2], onc=partial(addHandLayout, 100), ofc=partial(addHandLayout, -100), v=value, en=True )
    cmds.checkBox( finger + 'DistalCB', l='', w=rowWidth[3], onc=partial(addHandLayout, 1000), ofc=partial(addHandLayout, -1000) , v=True, en=True )        
    cmds.setParent('..')
    TR.verticalSpace(7)



'''
def enableCtrlScaleChain(*args):
    value = cmds.checkBox( 'UseCreateControllersCB', q=True, v=True )
    cmds.floatSliderGrp( 'CtrlScaleChain', edit=True, en=value )
'''


def enableOverrideSize(*args):
    value = cmds.checkBox( 'OverideFingerControllerSizeCB', q=True, v=True )
    cmds.floatSliderGrp( 'OverrideControllerSize', edit=True, en=value )



def getFullHandFootHierarchy():
    fingerToe = 'Finger' if utils.getHierarchy() == 'Arm' else 'Toe'

    handFoot = []
    for n in TRvars.fingersToes:
        for p in TRvars.phalanges:
            if cmds.checkBox( n + p + 'CB', q=True, v=True ):
                if cmds.checkBox( 'UseSimpleNameCB', q=True, v=True ):
                    handFoot.append( fingerToe + n )
                else:
                    handFoot.append( fingerToe + n + p )
                    
    return handFoot



def getHandFootHierarchy():
    fingerToe = 'Finger' if utils.getHierarchy() == 'Arm' else 'Toe'
    handFoot = []
    fingersToes = []
    for n in TRvars.fingersToes:
        for p in TRvars.phalanges:
            if cmds.checkBox( n + p + 'CB', q=True, v=True ):
                if cmds.checkBox( 'UseSimpleNameCB', q=True, v=True ):
                    fingersToes.append( fingerToe + n )
                else:
                    fingersToes.append( fingerToe + n + p )
                    
        if len(fingersToes) > 0:         
            handFoot.append(fingersToes)
            
        fingersToes = []
    
    for f in handFoot:
        f.reverse()
    
    return handFoot



def addHandLayout(value, reset=False):
    if reset == True:
        TRvars.handLayout = value
    else:
        TRvars.handLayout += value
    
    if TRvars.handLayout <= 50:
        cmds.checkBox( 'UseSimpleNameCB', edit=True, en=True, v=True )
    else:
        cmds.checkBox( 'UseSimpleNameCB', edit=True, en=False, v=False )
        
    if TRvars.handLayout >= 1000:
        cmds.checkBox( 'CreateDoubleOffsetCB', edit=True, en=True, v=True )
        cmds.checkBox( 'OverideFingerControllerSizeCB', edit=True, v=True )
        cmds.floatSliderGrp( 'OverrideControllerSize', edit=True, en=True )
    else:
        cmds.checkBox( 'CreateDoubleOffsetCB', edit=True, en=True, v=False )
        cmds.checkBox( 'OverideFingerControllerSizeCB', edit=True, v=False )
        cmds.floatSliderGrp( 'OverrideControllerSize', edit=True, en=False )



def getFingerSizeController():
        if cmds.checkBox( 'OverideFingerControllerSizeCB', q=True, v=True ):
            return cmds.floatSliderGrp( 'OverrideControllerSize', q=True, v=True )
        else:
            return TRvars.fingerControllerSizeDefault
		


def clearLayout(*args):
    setLayout(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 0)



def simple3Layout(*args):
    setLayout(False, False, False, True, False, False, True, False, False, True, False, False, False, False, False, 30)



def simple4Layout(*args):
    setLayout(True, False, False, True, False, False, True, False, False, True, False, False, False, False, False, 40)



def dragonLayout(*args):
    setLayout(True, False, True, True, False, True, True, False, True, True, False, True, False, False, False, 4040)



def simpleHandLayout(*args):
    setLayout(True, False, True, True, True, True, True, True, True, True, True, True, False, False, False, 4340)



def fullHandLayout(*args):
    setLayout(True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, 5450)



def setLayout(thumbProx, thumbInt, thumbDist, indexProx, indexInt, indexDist, middleProx, middleInt, middleDist, ringProx, ringInt, ringDist, pinkyProx, pinkyInt, pinkyDist, layoutValue):
    cmds.checkBox( 'ThumbProximalCB', edit=True, v=thumbProx )
    cmds.checkBox( 'ThumbMiddleCB', edit=True, v=thumbInt )
    cmds.checkBox( 'ThumbDistalCB', edit=True, v=thumbDist )
    cmds.checkBox( 'IndexProximalCB', edit=True, v=indexProx )
    cmds.checkBox( 'IndexMiddleCB', edit=True, v=indexInt )
    cmds.checkBox( 'IndexDistalCB', edit=True, v=indexDist )
    cmds.checkBox( 'MiddleProximalCB', edit=True, v=middleProx )
    cmds.checkBox( 'MiddleMiddleCB', edit=True, v=middleInt )
    cmds.checkBox( 'MiddleDistalCB', edit=True, v=middleDist )
    cmds.checkBox( 'RingProximalCB', edit=True, v=ringProx )
    cmds.checkBox( 'RingMiddleCB', edit=True, v=ringInt )
    cmds.checkBox( 'RingDistalCB', edit=True, v=ringDist )
    cmds.checkBox( 'PinkyProximalCB', edit=True, v=pinkyProx )
    cmds.checkBox( 'PinkyMiddleCB', edit=True, v=pinkyInt )
    cmds.checkBox( 'PinkyDistalCB', edit=True, v=pinkyDist )                
    addHandLayout(layoutValue, True)



def getHierarchyLayout(*args):
    utils.printHeader('GET HIERARCHY LAYOUT')
    
    sel = cmds.ls(sl=True)
    if TReh.GetSelectionException(sel): return
    
    fingerToe = 'Finger' if sel[0].find('Hand') > -1 else 'Toe'
    pattern = 'OFFSET__' + utils.getSideFromBone(sel[0]) + utils.getPositionFromBone(sel[0]) + fingerToe
            
    dk = getListOfDrivenKeys(pattern)
    
    clearLayout()
    
    for n in TRvars.fingersToes:
        for p in TRvars.phalanges:
            for d in dk:
                if d.find(n + p) > -1:
                    cmds.checkBox( n+p+'CB', edit=True, v=True )



def saveHand(state, *args):
    utils.printHeader('SAVING HAND - ' + state)
    sel = cmds.ls(sl=True)
    if TReh.GetNoSelectionException(sel): return
  
    dks = []
    for s in sel:
        dk = []
        dk.append(s)
        dk.append(cmds.xform( s, query=True, ro=True, os=True ))
        dks.append(dk)

    if state == 'CLOSED':
        TRvars.drivenKeyClosed= dks
    else:
        TRvars.drivenKeyOpen = dks

    utils.printSubheader('Hand ' + state.lower() + ' successfully saved!')



def saveDrivenKeysHand(*args):
    utils.printHeader('CREATING DRIVEN KEYS')
    
    sel = cmds.ls(sl=True)
    if TReh.GetSelectionException(sel): return
    
    handFoot = 'HAND' if sel[0].find('Arm') > -1 else 'FOOT'
    utils.addAttrSeparator(sel[0], 'HandBehaviourSeparator', handFoot)
    cmds.addAttr( ln='Hand', nn='Open / Close', at="long", k=True, dv=0, min=-100, max=100 )
    
    if len(TRvars.drivenKeyClosed) == 0:
        print ('No closed keys saved')
        return
    elif len(TRvars.drivenKeyOpen) == 0:
        print ('No open keys saved')
        return
    
    hand = sel[0] + '.Hand'
    
    for phalange in TRvars.drivenKeyClosed:
        resetDrivenKeyToPhalange(hand, sel, phalange)

    for phalange in TRvars.drivenKeyClosed:
        connectDrivenKeyToPhalange(hand, sel, phalange, 100)

    for phalange in TRvars.drivenKeyOpen:
        connectDrivenKeyToPhalange(hand, sel, phalange, -100)

    cmds.setAttr( hand, 0 )
    utils.printSubheader('Driven keys succesfully created!!')
    


def resetDrivenKeyToPhalange(hand, sel, phalange):
    cmds.setAttr( hand, 0 )
    for r in TRvars.rotAttr:
        cmds.setAttr( phalange[0] + r, 0 )
        cmds.setDrivenKeyframe( phalange[0] + r, cd=hand )    



def connectDrivenKeyToPhalange(hand, sel, phalange, value):
    cmds.setAttr( hand, value )
    cmds.setAttr( phalange[0] + '.rotateX', phalange[1][0] )
    cmds.setAttr( phalange[0] + '.rotateY', phalange[1][1] )
    cmds.setAttr( phalange[0] + '.rotateZ', phalange[1][2] )
    for r in TRvars.rotAttr:
        cmds.setDrivenKeyframe( phalange[0] + r, cd=hand )   



def selectDrivenKeys(pattern, *args):
    dk = getListOfDrivenKeys(pattern)
    cmds.select (dk)



def getListOfDrivenKeys(pattern):
    sel = cmds.ls(sl=True)
    if TReh.GetSelectionException(sel): return
    
    sidePos = utils.getSideFromBone(sel[0])
    children = cmds.listRelatives(ad=True)
    dk = []
    for c in children:
        if c.find(pattern) > -1:
            dk.append(c)

    return dk    



def mirrorDrivenKeysHand(*args):
    utils.printHeader('MIRRORING DRIVEN KEYS')
 
    hand = 'OFFSET__L_Hand.Hand'
    cmds.select( 'OFFSET__L_Hand' )
    selectDrivenKeys('DRIVEN_KEY')
    cmds.setAttr( hand, 100 )
    saveHand('CLOSED')
    cmds.setAttr( hand, -100 )
    saveHand('OPEN')
    
    for phalange in TRvars.drivenKeyClosed:
        phalange[0] = phalange[0].replace('__L_', '__R_')
        
    for phalange in TRvars.drivenKeyOpen:
        phalange[0] = phalange[0].replace('__L_', '__R_')
    
    cmds.select( 'OFFSET__R_Hand' )
    saveDrivenKeysHand()
        
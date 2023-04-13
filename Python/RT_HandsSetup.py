import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils as utils
import maya.cmds as cmds


def getFullHandFootHierarchy():
    fingerToe = 'Finger' if utils.getHierarchy() == 'Arm' else 'Toe'

    handFoot = []
    for n in RTvars.fingersToes:
        for p in RTvars.phalanges:
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
    for n in RTvars.fingersToes:
        for p in RTvars.phalanges:
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
        RTvars.handLayout = value
    else:
        RTvars.handLayout += value
    
    if RTvars.handLayout <= 50:
        cmds.checkBox( 'UseSimpleNameCB', edit=True, en=True, v=True )
    else:
        cmds.checkBox( 'UseSimpleNameCB', edit=True, en=False, v=False )
        
    if RTvars.handLayout >= 1000:
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
            return RTvars.fingerControllerSizeDefault
		


def clearLayout():
    setLayout(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 0)



def simple3Layout():
    setLayout(False, False, False, True, False, False, True, False, False, True, False, False, False, False, False, 30)



def simple4Layout():
    setLayout(True, False, False, True, False, False, True, False, False, True, False, False, False, False, False, 40)



def dragonLayout():
    setLayout(True, False, True, True, False, True, True, False, True, True, False, True, False, False, False, 4040)



def simpleHandLayout():
    setLayout(True, False, True, True, True, True, True, True, True, True, True, True, False, False, False, 4340)



def fullHandLayout():
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



def getHierarchyLayout():
    utils.printHeader('GET HIERARCHY LAYOUT')
    
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    fingerToe = 'Finger' if sel[0].find('Hand') > -1 else 'Toe'
    pattern = 'OFFSET__' + utils.getSideFromBone(sel[0]) + utils.getPositionFromBone(sel[0]) + fingerToe
            
    dk = getListOfDrivenKeys(pattern)
    
    clearLayout()
    
    for n in RTvars.fingersToes:
        for p in RTvars.phalanges:
            for d in dk:
                if d.find(n + p) > -1:
                    cmds.checkBox( n+p+'CB', edit=True, v=True )
					

def saveHand(state):
    dks = []
    for s in sel:
        dk = []
        dk.append(s)
        dk.append(cmds.xform( s, query=True, ro=True, os=True ))
        dks.append(dk)

    if state == 'CLOSED':
        RTvars.drivenKeyClosed= dks
    else:
        RTvars.drivenKeyOpen = dks



def saveDrivenKeysHand():    
    handFoot = 'HAND' if sel[0].find('Arm') > -1 else 'FOOT'
    utils.addAttrSeparator(sel[0], 'HandBehaviourSeparator', handFoot)
    cmds.addAttr( ln='Hand', nn='Open / Close', at="long", k=True, dv=0, min=-100, max=100 )
    hand = sel[0] + '.Hand'
    
    for phalange in RTvars.drivenKeyClosed:
        resetDrivenKeyToPhalange(hand, sel, phalange)

    for phalange in RTvars.drivenKeyClosed:
        connectDrivenKeyToPhalange(hand, sel, phalange, 100)

    for phalange in RTvars.drivenKeyOpen:
        connectDrivenKeyToPhalange(hand, sel, phalange, -100)

    cmds.setAttr( hand, 0 )

    


def resetDrivenKeyToPhalange(hand, sel, phalange):
    cmds.setAttr( hand, 0 )
    for r in RTvars.rotAttr:
        cmds.setAttr( phalange[0] + r, 0 )
        cmds.setDrivenKeyframe( phalange[0] + r, cd=hand )    



def connectDrivenKeyToPhalange(hand, sel, phalange, value):
    cmds.setAttr( hand, value )
    cmds.setAttr( phalange[0] + '.rotateX', phalange[1][0] )
    cmds.setAttr( phalange[0] + '.rotateY', phalange[1][1] )
    cmds.setAttr( phalange[0] + '.rotateZ', phalange[1][2] )
    for r in RTvars.rotAttr:
        cmds.setDrivenKeyframe( phalange[0] + r, cd=hand )   


def getListOfDrivenKeys(pattern):  
    sidePos = utils.getSideFromBone(sel[0])
    children = cmds.listRelatives(ad=True)
    dk = []
    for c in children:
        if c.find(pattern) > -1:
            dk.append(c)

    return dk    



def mirrorDrivenKeysHand():
    hand = 'CTRL__L_ArmSwitch_FKIK.Hand'
    cmds.setAttr( hand, 100 )
    cmds.select( 'OFFSET__L_Hand' )
    selectDrivenKeys('DRIVEN_KEY')
    
    saveHand('CLOSED')
    cmds.setAttr( hand, -100 )
    saveHand('OPEN')
    
    for phalange in RTvars.drivenKeyClosed:
        phalange[0] = phalange[0].replace('__L_', '__R_')
    
    cmds.select( 'CTRL__R_ArmSwitch_FKIK' )
        					
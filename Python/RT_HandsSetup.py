import RT_Utils as utils
import maya.cmds as cmds



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



def createHandFoot():
    utils.printHeader('CREATE HAND / FOOT')
    utils.printSubheader('WIP...')
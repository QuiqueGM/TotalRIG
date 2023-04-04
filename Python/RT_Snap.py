import maya.cmds as cmds
from functools import partial

winName = 'Snap'
winWidth = 200
winHeight = 95
margin = 10

CTRL = 'CTRL__'
SNAP = 'SNAP__'
PV = '_PV'
IK = '_IK'
switchFKIK = 'Switch_FKIK.FKIK'
armBones = ['Arm', 'Forearm', 'Wrist']
legBones = ['Hip', 'UpperLeg', 'LowerLeg', 'Ankle']

def snapTool():
    if cmds.window( winName, exists=True ):
        cmds.deleteUI( winName, window=True )
    elif cmds.windowPref( winName, exists=True ):
        cmds.windowPref( winName, remove=True )
    
    cmds.window( winName, wh=(winWidth+margin, winHeight), s=False, mnb=False, mxb=False, title='SNAP FK/IK' )
    mainCL = cmds.columnLayout()
    rowWidth = [winWidth*0.2, winWidth*0.4, winWidth*0.4]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0], h=25 )
    cmds.text( l='Left', al='center', w=rowWidth[1], h=25 )
    cmds.text( l='Right', al='center', w=rowWidth[2], h=25 )
    cmds.setParent( '..' )
    
    btn1 = getButtonProperties('CTRL__L_ArmSwitch_FKIK.FKIK')
    btn2 = getButtonProperties('CTRL__R_ArmSwitch_FKIK.FKIK') 
    createTwoButtonsAction('Arm', btn1, partial(snapFKIK, 'Arm', 'L_', armBones), btn2, partial(snapFKIK, 'Arm', 'R_', armBones), rowWidth, 30)
    
    btn1 = getButtonProperties('CTRL__L_LegSwitch_FKIK.FKIK')
    btn2 = getButtonProperties('CTRL__R_LegSwitch_FKIK.FKIK') 
    createTwoButtonsAction('Leg', btn1, partial(snapFKIK, 'Leg', 'L_', legBones), btn2, partial(snapFKIK, 'Leg', 'R_', legBones), rowWidth, 30)
    
    cmds.showWindow( winName )



def getButtonProperties(ctrl):
    label = 'To IK' if cmds.getAttr( ctrl ) == 0 else 'To FK'
    col = (0, 1, 1) if cmds.getAttr( ctrl ) == 0 else (0.5, 1, 0.5)
    ctrl = 'BTN' + ctrl[4:][:-5]
    return [ctrl, label, col]



def createTwoButtonsAction(label, btn1, callbackBtn1, btn2, callbackBtn2, rowWidth, height):
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l=label, w=rowWidth[0], h=height )
    cmds.button( btn1[0], l=btn1[1], c=callbackBtn1, bgc=btn1[2], w=rowWidth[1], h=height )
    cmds.button( btn2[0], l=btn2[1], c=callbackBtn2, bgc=btn2[2], w=rowWidth[2], h=height )
    cmds.setParent( '..' )



def snapFKIK(limb, side, bones, *args):
    ctrl = CTRL + side + limb + switchFKIK
    if cmds.getAttr( ctrl ) == 1:
        for b in bones:
            rot = cmds.xform( SNAP + side + b, query=True, ro=True, ws=True )
            cmds.xform( CTRL + side + b, ro=[rot[0], rot[1], rot[2]], ws=True )
        cmds.setAttr( ctrl, 0 )
        
    else:
        IKRot = cmds.xform( SNAP + side + bones[-1] + IK, query=True, ro=True, ws=True)
        IKPos = cmds.xform( SNAP + side + bones[-1] + IK, query=True, t=True, ws=True)

        cmds.xform( CTRL + side + bones[-1] + IK , ro=[IKRot[0], IKRot[1], IKRot[2]], ws=True )
        cmds.xform( CTRL + side + bones[-1] + IK , t=[IKPos[0], IKPos[1], IKPos[2]], ws=True )
        
        if bones[0] == 'Arm':
            snapPV('Arm', side)
        else:
            snapPV(bones[1], side)
            snapPV(bones[2], side)
            
        cmds.setAttr( ctrl, 1 )
    
    btn = getButtonProperties(ctrl)
    cmds.button( btn[0], e=True, l=btn[1], bgc=btn[2] )



def snapPV(name, side):
    PVPos = cmds.xform( SNAP + side + name + PV, query=True, t=True, ws=True)
    cmds.xform( CTRL + side + name + PV , t=[PVPos[0], PVPos[1], PVPos[2]], ws=True )


snapTool()
 
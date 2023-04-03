import maya.cmds as cmds
from functools import partial

PV = '_PV'
IK = '_IK'
switchFKIK = 'Switch_FKIK.FKIK'
armBones = ['Arm', 'Forearm', 'Wrist']
legBones = ['Hip', 'UpperLeg', 'LowerLeg', 'Ankle']



def 'SNAP__'FKIK(limb, side, bones, *args):
    'CTRL__' = 'CTRL__' + side + limb + switchFKIK
    if cmds.getAttr( 'CTRL__' ) == 1:
		rot = cmds.xform( 'SNAP__' + side + b, query=True, ro=True, ws=True )
		cmds.xform( 'CTRL__' + side + b, ro=[rot[0], rot[1], rot[2]], ws=True )
        
    else:
        IKRot = cmds.xform( 'SNAP__' + side + bones[-1] + IK, query=True, ro=True, ws=True)
        IKPos = cmds.xform( 'SNAP__' + side + bones[-1] + IK, query=True, t=True, ws=True)

        cmds.xform( 'CTRL__' + side + bones[-1] + IK , ro=[IKRot[0], IKRot[1], IKRot[2]], ws=True )
        cmds.xform( 'CTRL__' + side + bones[-1] + IK , t=[IKPos[0], IKPos[1], IKPos[2]], ws=True )
        
        limb = 'Arm' if bones[0] == 'Arm' else 'Leg'
        PVPos = cmds.xform( 'SNAP__' + side + limb + PV, query=True, t=True, ws=True)
        cmds.xform( 'CTRL__' + side + limb + PV , t=[PVPos[0], PVPos[1], PVPos[2]], ws=True )
            
        cmds.setAttr( 'CTRL__', 1 )
    
    btn = getButtonProperties('CTRL__')
    cmds.button( btn[0], e=True, l=btn[1], bgc=btn[2] )
   
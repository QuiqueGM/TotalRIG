version='0.0.1'
winName = 'AUTORIG'

bone = ''
ctrlColor = (0, 0, 0)
limbStartingBone = ''
chainStartingBone = ''

ClavicleHead = 'ClavicleHead'
Clavicle = 'Clavicle'
Arm = 'Arm'
Arm_PV = 'Arm_PV'
Forearm = 'Forearm'
Forearm_PV = 'Forearm_PV'
Forearm_IK = 'Forearm_IK'
Wrist = 'Wrist'
Wrist_IK = 'Wrist_IK'    
ArmSwitch_FKIK = 'ArmSwitch_FKIK'
Hand = 'Hand'
Finger = 'Finger'

HipHead = 'HipHead'
Hip = 'Hip'
UpperLeg = 'UpperLeg'
UpperLeg_PV = 'UpperLeg_PV'
LowerLeg = 'LowerLeg'
LowerLeg_PV = 'LowerLeg_PV'
LowerLeg_IK = 'LowerLeg_IK'
Ankle = 'Ankle'
Ankle_IK = 'Ankle_IK'
LegSwitch_FKIK = 'LegSwitch_FKIK'
Foot = 'Foot'
Toe = 'Toe'

fingersToes = ['Pinky', 'Ring', 'Middle', 'Index', 'Thumb']
phalanges = ['Proximal', 'Middle', 'Distal']

FingerThumb = Finger + fingersToes[0]
FingerIndex = Finger + fingersToes[1]
FingerMid = Finger + fingersToes[2]
FingerRing = Finger + fingersToes[3]
FingerPinky = Finger + fingersToes[4]

ToeThumb = Toe + fingersToes[0]
ToeIndex = Toe + fingersToes[1]
ToeMid = Toe + fingersToes[2]
ToeRing = Toe + fingersToes[3]
ToePinky = Toe + fingersToes[4]

armBones = [ Clavicle, Arm, Forearm, Wrist, Hand ]
offsetsArm = [ Clavicle, Arm, Forearm, Forearm_PV, Wrist, Wrist_IK, ArmSwitch_FKIK, Hand ]
bonesHindArm = [ ClavicleHead, Clavicle, Arm, Forearm, Wrist, Hand ]
offsetsHindArm = [ ClavicleHead, Clavicle, Arm, Arm_PV, Forearm, Forearm_PV, Forearm_IK, Wrist, Wrist_IK, ArmSwitch_FKIK, Hand ]
armBones = [ Clavicle, Arm, Forearm, Wrist, Hand, FingerRing, FingerMid, FingerIndex, FingerThumb, FingerPinky ]
offsetsArm = [ Clavicle, Arm, Forearm, Forearm_PV, Wrist, Wrist_IK, ArmSwitch_FKIK, Hand, FingerRing, FingerMid, FingerIndex, FingerThumb, FingerPinky ]
bonesHindArm = [ ClavicleHead, Clavicle, Arm, Forearm, Wrist, Hand, FingerRing, FingerMid, FingerIndex, FingerThumb, FingerPinky ]
offsetsHindArm = [ ClavicleHead, Clavicle, Arm, Arm_PV, Forearm, Forearm_PV, Forearm_IK, Wrist, Wrist_IK, ArmSwitch_FKIK, Hand, FingerRing, FingerMid, FingerIndex, FingerThumb, FingerPinky ]
snapArm = [ Arm, Forearm, Wrist, Wrist_IK ]
snapHindArm = [ Clavicle, Arm, Forearm, Wrist, Wrist_IK ]

legBones = [ Hip, UpperLeg, LowerLeg, Ankle, Foot, ToeRing, ToeMid, ToeIndex, ToeThumb, ToePinky ]
offsetsLeg = [ Hip, UpperLeg, LowerLeg, LowerLeg_PV, Ankle, Ankle_IK, LegSwitch_FKIK, Foot, ToeRing, ToeMid, ToeIndex, ToeThumb, ToePinky ]
bonesHindLeg = [ HipHead, Hip, UpperLeg, LowerLeg, Ankle, Foot, ToeRing, ToeMid, ToeIndex, ToeThumb, ToePinky ]
offsetsHindLeg = [ HipHead, Hip, UpperLeg, UpperLeg_PV, LowerLeg, LowerLeg_PV, LowerLeg_IK, Ankle, Ankle_IK, LegSwitch_FKIK, Foot, ToeRing, ToeMid, ToeIndex, ToeThumb, ToePinky ]
snapLeg = [ UpperLeg, LowerLeg, Ankle, Ankle_IK]
snapHingeLeg = [ Hip, UpperLeg, LowerLeg, Ankle, Ankle_IK]

headBones = ['Head', 'Eye', 'Nose', 'Tongue', 'Jaw', 'Ear', 'Hair', 'Horn', 'Antler', 'Fin']
bodyBones = ['Spine', 'Chest', 'Neck', 'Tail', 'Wing', 'Membrane', 'Ribs', 'Fin']
reverseHand = ['HandHeel', 'HandExt', 'HandInt', 'Fingertip', 'HandBall', 'Wrist']
reverseFoot = ['FootHeel', 'FootExt', 'FootInt', 'Toetip', 'FootBall', 'Ankle']
centralBones = ['Head', 'Nose', 'Tongue', 'Jaw', 'Root', 'Neck', 'Chest', 'Spine', 'Tail']

attributes = ['.translateX', '.translateY', '.translateZ', '.rotateX', '.rotateY', '.rotateZ', '.scaleX', '.scaleY', '.scaleZ']
reverseFootAttr = ['RevFootSeparator', 'FootBalance', 'FootRollWeight', 'FootRoll']
stretchAttr = ['StretchSeparator', 'StretchCompensation', 'Stretch', 'StretchVolume']

sideGroupArms = [ Arm_PV, Forearm_PV, Forearm_IK, Wrist_IK, ArmSwitch_FKIK, Hand ]
sideGroupLegs = [ UpperLeg_PV, LowerLeg_PV, LowerLeg_IK, Ankle_IK, LegSwitch_FKIK, Foot ]

CONST = 'CONST'
PARENT = '__PARENT'
POINT = '__POINT'
ORIENT = '__ORIENT'
SCALE = '__SCALE'
AIM = '__AIM'
POLEV = '__POLE_VECTOR'
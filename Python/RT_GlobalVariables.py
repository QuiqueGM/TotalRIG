winName = 'TOTALRIG'
version='0.1.1'

sides = ['L_', 'R_']
bone = ''
handLayout = 30
ctrlColor = (0, 0, 0)
fingerControllerSizeDefault = 0.04
limbStartingBone = ''
chainStartingBone = ''
dragonSkinCluster = 'dragonSkinCluster'
drivenKeyClosed = []
drivenKeyOpen = []

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
snapArm = [ Arm, Forearm, Wrist, Wrist_IK ]
snapHindArm = [ Clavicle, Arm, Forearm, Wrist, Wrist_IK ]

simpleHand = [ FingerThumb, FingerIndex, FingerMid, FingerRing, FingerPinky ]
hand = [ FingerThumb + phalanges[0], FingerThumb + phalanges[1], FingerThumb + phalanges[2], FingerIndex + phalanges[0], FingerIndex + phalanges[1], FingerIndex + phalanges[2], FingerMid + phalanges[0], FingerMid + phalanges[1], FingerMid + phalanges[2], FingerRing + phalanges[0], FingerRing + phalanges[1], FingerRing + phalanges[2], FingerPinky + phalanges[0], FingerPinky + phalanges[1], FingerPinky + phalanges[2] ]

legBones = [ Hip, UpperLeg, LowerLeg, Ankle, Foot ]
offsetsLeg = [ Hip, UpperLeg, LowerLeg, LowerLeg_PV, Ankle, Ankle_IK, LegSwitch_FKIK, Foot ]
bonesHindLeg = [ HipHead, Hip, UpperLeg, LowerLeg, Ankle, Foot ]
offsetsHindLeg = [ HipHead, Hip, UpperLeg, UpperLeg_PV, LowerLeg, LowerLeg_PV, LowerLeg_IK, Ankle, Ankle_IK, LegSwitch_FKIK, Foot ]
snapLeg = [ UpperLeg, LowerLeg, Ankle, Ankle_IK]
snapHindLeg = [ Hip, UpperLeg, LowerLeg, Ankle, Ankle_IK]

simpleFoot = [ ToeThumb, ToeIndex, ToeMid, ToeRing, ToePinky ]
foot = [ ToeThumb + phalanges[0], ToeThumb + phalanges[1], ToeThumb + phalanges[2], ToeIndex + phalanges[0], ToeIndex + phalanges[1], ToeIndex + phalanges[2], ToeMid + phalanges[0], ToeMid + phalanges[1], ToeMid + phalanges[2], ToeRing + phalanges[0], ToeRing + phalanges[1], ToeRing + phalanges[2], ToePinky + phalanges[0], ToePinky + phalanges[1], ToePinky + phalanges[2] ]


headBones = ['Head', 'Eye', 'Nose', 'Tongue', 'Jaw', 'Ear', 'Hair', 'Horn', 'Antler', 'Fin']
bodyBones = ['Spine', 'Chest', 'Neck', 'Head', 'Tail', 'Wing', 'Membrane', 'Claw', 'Ribs', 'Fin']
reverseHand = ['HandHeel', 'HandExt', 'HandInt', 'Fingertip', 'HandBall', 'Wrist']
reverseFoot = ['FootHeel', 'FootExt', 'FootInt', 'Toetip', 'FootBall', 'Ankle']
centralBones = ['Head', 'Nose', 'Tongue', 'Jaw', 'Root', 'Neck', 'Chest', 'Spine', 'Tail']

attributes = ['.translateX', '.translateY', '.translateZ', '.rotateX', '.rotateY', '.rotateZ', '.scaleX', '.scaleY', '.scaleZ']
rotAttr = ['.rotateX', '.rotateY', '.rotateZ']
reverseFootAttr = ['RevFootSeparator', 'FootBalance', 'FootRollWeight', 'FootRoll']
stretchAttr = ['StretchSeparator', 'StretchCompensation', 'Stretch', 'StretchVolume']
blendShapesEyes = ['L_Eye_Closed', 'L_Eye_Open', 'R_Eye_Closed', 'R_Eye_Open']

sideGroupArms = [ Arm_PV, Forearm_PV, Forearm_IK, Wrist_IK, ArmSwitch_FKIK, Hand ]
sideGroupLegs = [ UpperLeg_PV, LowerLeg_PV, LowerLeg_IK, Ankle_IK, LegSwitch_FKIK, Foot ]

CONST = 'CONST'
PARENT = '__PARENT'
POINT = '__POINT'
ORIENT = '__ORIENT'
SCALE = '__SCALE'
AIM = '__AIM'
POLEV = '__POLE_VECTOR'
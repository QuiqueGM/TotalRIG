import RiggingTools
import RT_HandsSetup
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import maya.cmds as cmds
from math import pow,sqrt


def addObject(field):
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return

    cmds.textFieldButtonGrp(field, e=True, tx=''.join(sel))



def removeObject(bone):
    cmds.textFieldButtonGrp( bone, e=True, tx='' )



def reloadMirror(bones):
    replaceBones('L_', 'R_', bones)



def reloadPosition(bones):
    replaceBones('F_', 'B_', bones)



def replaceBones(A, B, bones):
    for b in range(len(bones)):
        boneName = cmds.textFieldButtonGrp( bones[b], q=True, tx=True )
        
        if (boneName.find(A) > -1):
            boneName = boneName.replace(A, B)
        elif (boneName.find(B) > -1):
            boneName = boneName.replace(B, A)
            
        cmds.textFieldButtonGrp(bones[b], e=True, tx=boneName)
        
        if b==0:
            RTvars.limbStartingBone = boneName



def getColorFromSide(sel):
    if (sel.find('_L_') > -1):
        return (1, 0, 0)
    elif (sel.find('_R_') > -1):
        return (0, 1, 0)
    else:
        return (0, 0, 1)



def getSideFromBone(bone):
    if (bone.find('_L_') > -1):
        return 'L_'
    elif (bone.find('_R_') > -1):
        return 'R_'
    else:
        return ''



def getPositionFromBone(bone):
    if (bone.find('_F_') > -1):
        return 'F_'
    elif (bone.find('_B_') > -1):
        return 'B_'
    else:
        return ''



def getTypeOfJoint(selection):
    children = cmds.listRelatives( selection, ad=True )
    try:
        a = len(children)
        return 'JNT__'
    except:
        return 'END__'



def getNameControl(num, ctrl, case):
    name = ctrl.replace('_L_', '_')
    name = name.replace('_R_', '_')
    name = name.replace('_F_', '_')
    name = name.replace('_B_', '_')
    name = name.replace('_U_', '_')
    name = name.replace('_D_', '_')
    name = name[num:].upper() if case == 'upper' else name[num:]
    return '_' + name



def createDistanceMeasure(nameDist, nameLoc1, nameLoc2):
    cmds.distanceDimension( sp=(0,0,1), ep=(0,0,2) )
    distMeasure = cmds.rename( 'distanceDimension1', 'DST' + nameDist )    
    locator1 = cmds.rename( 'locator1', 'LOC' + nameLoc1 )
    locator2 = cmds.rename( 'locator2', 'LOC' + nameLoc2 )
    cmds.parent( locator1, locator2, distMeasure, 'Helpers' )
    setLocalScaleLocators(locator1)
    setLocalScaleLocators(locator2)
    cmds.editDisplayLayerMembers( 'HELPERS', distMeasure, nr=True )
    cmds.editDisplayLayerMembers( 'HELPERS', locator1, nr=True )
    cmds.editDisplayLayerMembers( 'HELPERS', locator2, nr=True )
    return [distMeasure, locator1, locator2]



def setTransformToZero(obj):
    cmds.setAttr( obj + '.translateX', 0 )
    cmds.setAttr( obj + '.translateY', 0 )
    cmds.setAttr( obj + '.translateZ', 0 )



def setRotationToZero(obj):
    cmds.setAttr( obj + '.rotateX', 0 )
    cmds.setAttr( obj + '.rotateY', 0 )
    cmds.setAttr( obj + '.rotateZ', 0 )



def setLocalScaleLocators(obj):
    cmds.setAttr( obj + '.localScaleX', 0.0005 )
    cmds.setAttr( obj + '.localScaleY', 0.0005 )
    cmds.setAttr( obj + '.localScaleZ', 0.0005 )



def setTransformAndRotationToZero(obj):
    setTransformToZero(obj)
    setRotationToZero(obj)



def getVector(jointA, jointB):
    x1 = cmds.getAttr( jointA + '.translateX' )
    y1 = cmds.getAttr( jointA + '.translateY' )
    z1 = cmds.getAttr( jointA + '.translateZ' )
    x2 = cmds.getAttr( jointB + '.translateX' )
    y2 = cmds.getAttr( jointB + '.translateY' )
    z2 = cmds.getAttr( jointB + '.translateZ' )
    return (x2-x1, y2-y1, z2-z1)



def getDistance(objA, objB):
	gObjA = cmds.xform(objA, q=True, t=True, ws=True)
	gObjB = cmds.xform(objB, q=True, t=True, ws=True)
	
	return sqrt(pow(gObjA[0]-gObjB[0],2)+pow(gObjA[1]-gObjB[1],2)+pow(gObjA[2]-gObjB[2],2))



def lockControllers(ctrls, state):
    for c in ctrls:
        for a in RTvars.attributes:
            cmds.setAttr( c + a, l=state )



def lockController(ctrl, state):
    for a in RTvars.attributes:
        cmds.setAttr( ctrl + a, l=state )



def lockAndHideAttribute(ctrl, pos, rot):
    cmds.setAttr( ctrl + '.visibility', k=False, cb=False )
    cmds.setAttr( ctrl + '.scaleX', k=False, l=True, cb=False )
    cmds.setAttr( ctrl + '.scaleY', k=False, l=True, cb=False )
    cmds.setAttr( ctrl + '.scaleZ', k=False, l=True, cb=False )    
    if pos:
        cmds.setAttr( ctrl + '.translateX', k=False, l=True, cb=False )
        cmds.setAttr( ctrl + '.translateY', k=False, l=True, cb=False )
        cmds.setAttr( ctrl + '.translateZ', k=False, l=True, cb=False )  
    if rot:
        cmds.setAttr( ctrl + '.rotateX', k=False, l=True, cb=False )
        cmds.setAttr( ctrl + '.rotateY', k=False, l=True, cb=False )
        cmds.setAttr( ctrl + '.rotateZ', k=False, l=True, cb=False )



def lockAndHideOffset(offset, state, keyable=False):
    if offset=='null':
        offset = cmds.ls(sl=True)
        if RTeh.GetSelectionException(offset): return
        offset = offset[0]

    cmds.setAttr( offset + '.visibility', k=not state, l=state, cb=not state )
    for attribute in RTvars.attributes:
        cmds.setAttr( offset + attribute, k=not state, l=state, cb=not state )
    
    if keyable:
        cmds.setAttr( offset + '.visibility', k=not state )
        for attribute in RTvars.attributes:
            cmds.setAttr( offset + attribute, k=not state )



def hideAttributes(ctrl, vis):
    cmds.setAttr( ctrl + '.visibility', vis, k=False, cb=False )
    for a in RTvars.attributes:
        cmds.setAttr( ctrl + a, k=False, cb=False )



def getConstraint(type, object):
    if type == 'Parent': return RTvars.CONST + object + RTvars.PARENT
    elif type == 'Point': return RTvars.CONST + object + RTvars.POINT
    elif type == 'Orient': return RTvars.CONST + object + RTvars.ORIENT
    elif type == 'Scale': return RTvars.CONST + object + RTvars.SCALE
    elif type == 'Aim': return RTvars.CONST + object + RTvars.AIM
    elif type == 'PoleVector': return RTvars.CONST + object + RTvars.POLEV    



def createShadingNode(node, name):
    cmds.shadingNode( node, au=True, n=name )
    return name



def addAttrSeparator(ctrl, name, niceName):
    cmds.addAttr( ctrl, ln=name, nn=niceName, at='enum', en='--------------:', k=True )



def printHeader(header):
    print ('=================================== ' + header + ' ===================================')



def printSubheader(subheader):
    print ('    ---------> ' + subheader)
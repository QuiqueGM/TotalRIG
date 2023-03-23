import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils
import maya.cmds as cmds

def autofillFromSelection():
    RT_Utils.printHeader('AUTOFILL LIMB')

    bones = RT_Utils.createLimbArray(RTvars.armBones if RT_Utils.getHierarchy() == 'Arm' else RTvars.legBones)
    sel = cmds.listRelatives( cmds.ls(sl=True), ad=True )
    sel.append( cmds.ls(sl=True)[0] )

    for s in sel:
        res = s.find('END')
        if (res > -1):
            sel.remove(s)
       
    for s in sel:
        cmds.select(s)
        for b in bones:
            res = s.find(b)
            if (res > -1):
                RT_Utils.addObject(b)
                break



def clearAllFields():
    for b in RTvars.legBones:
        removeObject(b)



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
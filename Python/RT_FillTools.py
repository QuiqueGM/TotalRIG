import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils
import maya.cmds as cmds


def autofillFromSelection(nameBone):
    RT_Utils.addObject(nameBone)
    sel = cmds.listRelatives( cmds.ls(sl=True), ad=True )
    if (RTeh.GetNoSelectionException(sel)): return
        
    sel.append( cmds.ls(sl=True)[0] )

    for s in sel:
        res = s.find('END')
        if (res > -1):
            sel.remove(s)
       
    for s in sel:
        cmds.select(s)
        for b in RTvars.legBones:
            res = s.find(b)
            if (res > -1):
                RT_Utils.addObject(b)
                break






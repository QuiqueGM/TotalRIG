import TR_GlobalVariables as TRvars
import maya.cmds as cmds

def GetNoSelectionException(sel):

    errorSel = False
    
    if not sel:
        cmds.confirmDialog( t='Selection', m='Nothing selected! Please, select an object.', b=['OK'], p=TRvars.winName )
        errorSel = True
    
    return errorSel



def GetSelectionException(sel):

    errorSel = GetNoSelectionException(sel)
    
    if len(sel) > 1:
        cmds.confirmDialog( t='Selection', m='More than one object selected! Please, select ONLY a single object.', b=['OK'], p=TRvars.winName )
        errorSel = True
    
    return errorSel



def GetTwoSelectionException(sel):

    errorSel = False
    
    if not len(sel) == 2:
        cmds.confirmDialog( t='Selection', m='Please, select ONLY two objects.', b=['OK'], p=TRvars.winName )
        errorSel = True
    
    return errorSel



def GetLimbException():
    raise RuntimeError("The selected object doesn't match with 'Hip' or 'Clavicle'")

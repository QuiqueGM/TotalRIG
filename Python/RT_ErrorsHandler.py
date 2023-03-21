import RT_GlobalVariables as RTvars
import maya.cmds as cmds

def GetNoSelectionException(sel, message = ''):

    errorSel = False
    
    if not sel:
        cmds.confirmDialog( t='Selection', m='Nothing selected! Please, select an object.' + message, b=['OK'], p=RTvars.winName )
        errorSel = True
    
    return errorSel



def GetSelectionException(sel,message = ''):

    errorSel = GetNoSelectionException(sel, message)

    if len(sel) > 1:
        cmds.confirmDialog( t='Selection', m='More than one object selected! Please, select ONLY a single object.' + message, b=['OK'], p=RTvars.winName )
        errorSel = True
    
    return errorSel



def GetTwoSelectionException(sel,message = ''):

    errorSel = False
    
    if not len(sel) == 2:
        cmds.confirmDialog( t='Selection', m='Please, select ONLY two objects.' + message, b=['OK'], p=RTvars.winName )
        errorSel = True
    
    return errorSel
    


def GetLimbException():
    cmds.confirmDialog( t='Selection', m="The selected object doesn't match with 'Hip' or 'Clavicle'", b=['OK'], p=RTvars.winName )


def DestinationIsLocked(offset):
    cmds.confirmDialog( t='Creating controllers', m='Could not add the controller in the object --> ' + offset + '. Check that the destination object --> ' + offset + ' is not locked.', b=['OK'], p=RTvars.winName )
    
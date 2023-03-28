def GetNoSelectionException(sel):

    errorSel = False
    
    if not sel:
        raise RuntimeError("Nothing selected! Please, select an object.")
        errorSel = True
    
    return errorSel



def GetSelectionException(sel):

    errorSel = GetNoSelectionException(sel)
    
    if len(sel) > 1:
        raise RuntimeError("More than one object selected! Please, select only a single object.")
        errorSel = True
    
    return errorSel



def GetLimbException():
    raise RuntimeError("The selected object doesn't match with 'Hip' or 'Clavicle'")

import RiggingTools
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils
import RT_Utilities
import maya.cmds as cmds


def incrementNumber():
    value = cmds.intField( 'AddNumber', q=True, v=True )
    value = value + 1
    cmds.intField( 'AddNumber', edit=True, v=value)



def resetNumber():
    cmds.intField( 'AddNumber', edit=True, v=1)



def renameBone(add):
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return

    getBone()
    typeOfBone = RT_Utils.getTypeOfJoint(sel) if not isAnIsolatedJoint(sel) else 'JNT__'
    name =  typeOfBone + getSide() + getPosition() + RTvars.bone + getNumber()

    if (getSide() != '' or getPosition() != '') and checkIfCentralBone(name):        
        message = 'Are you sure you want to rename the   <b>' + sel[0] + '</b>   joint as   <b>' + name + '</b>  ?'
        if cmds.confirmDialog( t='Rename', m=message, b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName ) == 'No':
            return

    if getSide() == '' and name.find('Eye') > -1:        
        message = 'Are you sure you want to rename the   <b>' + sel[0] + '</b>   joint as   <b>' + name + '</b>  ?'
        if cmds.confirmDialog( t='Rename', m=message, b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName ) == 'No':
            return
            
    if name.find('Nose') > -1 or name.find('Jaw') > -1:
        renameJoint(sel[0], name)
        end = cmds.listRelatives( name, c=True )
        cmds.select(end)
        newName = name.replace('JNT__', 'END__')
        renameJoint(end[0], newName)
    else:
        renameJoint(sel[0], name)



def renameJoint(sel, name):
    RT_Utils.printHeader('RENAMING ' + sel + ' --> ' + name)
    cmds.rename(name)



def getBone():
    if cmds.checkBox( 'UseOtherCB', q=True, v=True ):
        RTvars.bone = cmds.textField( 'AlternativeName', q=True, tx=True )



def getSide():
	if (cmds.radioButton( 'LeftSide', q=True, sl=True )):
		return 'L_'
	elif (cmds.radioButton( 'RightSide', q=True, sl=True )):
		return 'R_'
	else:
	    return ''



def getPosition():
	if (cmds.radioButton( 'FrontPos', q=True, sl=True )):
		return 'F_'
	elif (cmds.radioButton( 'BackPos', q=True, sl=True )):
		return 'B_'
	else:
	    return ''



def getHeight():
	if (cmds.radioButton( 'UpPos', q=True, sl=True )):
		return 'U_'
	elif (cmds.radioButton( 'DownPos', q=True, sl=True )):
		return 'D_'
	else:
	    return ''



def getNumber():
    number = ''
    if cmds.checkBox( 'UseAddNumberCB', q=True, v=True ):
        int = cmds.intField( 'AddNumber', q=True, v=True )
        number = "_{0:0=2d}".format(int)
    return number



def checkIfCentralBone(name):
    for c in RTvars.centralBones:
        if RTvars.bone == c:
            return True

    return False



def isAnIsolatedJoint(sel):
    if cmds.listRelatives( sel, p=True ) == None:
        children = cmds.listRelatives( sel, ad=True )
        try:
            a = len(children)
            return False
        except:
            return True
    else:
        return False



def autorenameLimb():
    RT_Utils.printHeader('AUTORENAME LIMB')
    RT_Utils.printSubheader('WIP...')



def autorenameSimpleChain():
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    RT_Utils.printHeader('AUTORENAME SIMPLE CHAIN')
    chain = cmds.listRelatives( sel, ad=True, type='joint' )
    chain.append(sel)
    chain.reverse()
    n=0
    
    name =  RT_Utils.getTypeOfJoint(sel) + getSide() + getPosition() + RTvars.bone + getNumber()
    if (getSide() != '' or getPosition() != '') and checkIfCentralBone(name):        
        message = 'Are you sure you want to rename the   <b>' + sel[0] + '</b>   joint as   <b>' + name + '</b>  ?'
        if cmds.confirmDialog( t='Rename', m=message, b=['Yes','No'], db='Yes', cb='No', ds='No', p=RTvars.winName ) == 'No':
            return
    
    for c in chain:
        getBone()
        cmds.select( c )
        jnt = cmds.ls( sl=True )
        n+=1
        number = "_{0:0=2d}".format(n)
        name =  RT_Utils.getTypeOfJoint(jnt) + getSide() + getPosition() + RTvars.bone + getNumber() + number
        cmds.rename( jnt, name )
        cmds.select( cl=True )
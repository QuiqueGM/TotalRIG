import RiggingTools as RT
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils
import maya.cmds as cmds
from functools import partial



def drawUI():
    RT.toolHeader('renameBonesTab', '---------   RENAME BONES   ---------')
    RT.subHeader(1, 'SIDE AND POSITION', 1)
    RT.createThreeRadioCollection('LeftSide', 'Left', True, 'RightSide', 'Right', False, 'CenterSide', 'Center', False)
    RT.createThreeRadioCollection('FrontPos', 'Front', False, 'BackPos', 'Back', False, 'NonePose', 'None', True)
    RT.verticalSpace(5)
    RT.subHeader(1, 'PREDEFINED NAMES', 5)
    winWidth = RT.winWidth
    rowWidth = [winWidth*0.08, winWidth*0.35, winWidth*0.1, winWidth*0.35]
    cmds.rowLayout( nc=4, cw4=rowWidth )
    cmds.text( l='', w=rowWidth[0])
    cmds.optionMenu( 'AreaOM', w=rowWidth[1], l='Area   ', cc=fillAreas)
    cmds.menuItem( l='Body' )
    cmds.menuItem( l='Head' )
    cmds.menuItem( l='Arm' )    
    cmds.menuItem( l='Leg' )    
    cmds.text( l='', w=rowWidth[2])
    cmds.optionMenu( 'JointOM', w=rowWidth[3], l='Joint   ', cc=RT.returnBone )
    fillAreas()
    RT.verticalSpace(5)
    rowWidth = [winWidth*0.15, winWidth*0.3, winWidth*0.25]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( 'UseOtherCB', l='Use other', w=rowWidth[1], cc=enableFields )
    cmds.textField( 'AlternativeName' , en=False, w=rowWidth[2] )
    cmds.setParent( '..' )
    rowWidth = [winWidth*0.15, winWidth*0.3, winWidth*0.25, winWidth*0.05, winWidth*0.05]
    cmds.rowLayout( nc=5, cw5=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.checkBox( 'UseAddNumberCB', l='Add number', w=rowWidth[1], cc=changeIntField )
    cmds.intField( 'AddNumber', en=False, min=1, max=100, w=rowWidth[2], v=1 )
    cmds.button( 'IncButton', en=False, l='+', c=incrementNumber, w=rowWidth[3] )
    cmds.button( 'ResetButton', en=False, l='R', c=resetNumber, w=rowWidth[4] )
    cmds.setParent( '..' )
    RT.verticalSpace(2)
    rowWidth = [winWidth*0.15, winWidth*0.7]
    RT.createButtonAction(10, '', 'Rename', partial(renameBone, ''), False)
    
    RT.createSpaceForUtilities('---------   UTILITIES  ---------')
    RT.createButtonAction(3,'', 'Autorename Simple Chain', autorenameSimpleChain, False)
    RT.createButtonAction(3,'', 'Autorename Multiple Chains', autorenameMultChains, True)



def enableFields(*args):
    value = cmds.checkBox( 'UseOtherCB', q=True, v=True )
    cmds.optionMenu( 'AreaOM', edit=True, en=not value )
    cmds.optionMenu( 'JointOM', edit=True, en=not value )
    cmds.textField( 'AlternativeName', edit=True, en=value )



def changeIntField(*args):
    value = cmds.checkBox( 'UseAddNumberCB', q=True, v=True )
    cmds.intField( 'AddNumber', edit=True, en=value )
    cmds.button( 'IncButton', edit=True, en=value )
    cmds.button( 'ResetButton', edit=True, en=value )



def fillAreas(*args):
    currentValue = cmds.optionMenu( 'AreaOM', q=True, v=True )
    joints = cmds.optionMenu( 'JointOM', q=True, ill=True )
    
    if joints: cmds.deleteUI( joints )
    
    if currentValue == 'Head': fillArea(RTvars.headBones)
    elif currentValue == 'Leg': fillArea(RTvars.legBones)
    elif currentValue == 'Arm': fillArea(RTvars.armBones)      
    elif currentValue == 'Body': fillArea(RTvars.bodyBones)
        
    cmds.setParent( '..' )



def fillArea(bones):
    for b in bones:
        cmds.menuItem( p='JointOM', l=b )
    RTvars.bone = bones[0]



def incrementNumber(*args):
    value = cmds.intField( 'AddNumber', q=True, v=True )
    value = value + 1
    cmds.intField( 'AddNumber', edit=True, v=value)



def resetNumber(*args):
    cmds.intField( 'AddNumber', edit=True, v=1)



def renameBone(add, *args):
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
    RT_Utils.printHeader('AUTORENAME LIMB -- ' + RT_Utils.getHierarchy())
    
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    chain = cmds.listRelatives( sel, ad=True, type='joint' )
    chain.append( sel[0] )
    chain.reverse()
    bones = RT_Utils.createLimbArray(RTvars.bonesHindArm if RT_Utils.getHierarchy() == 'Arm' else RTvars.bonesHindLeg)
    bones = RT_Utils.getLimbBones(bones)
    n = -1

    for c in range(len(chain)):
        cmds.select( chain[c] )
        sel = cmds.ls( sl=True )
        typeOfBone = RT_Utils.getTypeOfJoint(sel)
        if typeOfBone == 'JNT__':
            n+=1

        name =  typeOfBone + getSide() + getPosition() + bones[n]
        cmds.rename( sel, name )
        if c==0:
            RTvars.limbStartingBone = name
            
        cmds.select( cl=True )
def autorenameSimpleChain(*args):
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



def autorenameMultChains(*args):
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    RT_Utils.printHeader('AUTORENAME MULTIPLE CHAINS')
    for s in sel:
        chain = cmds.listRelatives( s, ad=True, type='joint' )
        chain.append(s)
        chain.reverse()
        n=0
        jointName = RT_Utils.getNameControl(5, s, 'lower')[1:]
        
        for c in chain:
            cmds.select( c )
            jnt = cmds.ls( sl=True )
            n+=1
            number = "_{0:0=2d}".format(n)
            name =  RT_Utils.getTypeOfJoint(jnt) + getSide() + getPosition() + jointName + number
            cmds.rename( jnt, name )
            cmds.select( cl=True )



def autorenameComplexChain(*args):
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    chain = cmds.listRelatives( sel, ad=True, type='joint' )
    chain.append(sel[0])
    chain.reverse()
    index = []
    n = 0
    
    for c in range(len(chain)):
        n = n + 1
        
        if (chain[c].find('JNT_') > -1):
            n = 1
            currentName = chain[c]
            number = "_{0:0=2d}".format(n)
            name = currentName + number
            cmds.rename( chain[c], name )
            index.append(name)
        else:  
            number = "_{0:0=2d}".format(n)
            name = RT_Utils.getTypeOfJoint(chain[c]) + currentName[5:] + number
            cmds.rename( chain[c], name )
            index[-1] = name
            
            if name.find('END_') > -1:
                index.pop(-1)
                try:
                    num = index[-1][-2:]
                    n = int(num)
                    currentName = index[-1][:-3]
                except:
                    break
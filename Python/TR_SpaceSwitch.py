import TotalRig as TR
import TR_GlobalVariables as TRvars
import TR_Utils as utils
import maya.cmds as cmds
from functools import partial



def drawUI():
    TR.toolHeader('spaceSwitchTab', '---------   SPACE SWITCH  ---------')
    TR.subHeader(1, 'TARGET', 1)
    winWidth = TR.winWidth
    rowWidth = [winWidth*0.1, winWidth*0.165, winWidth*0.2]
    cmds.rowLayout( nc=3, cw3=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.text( l='Attribute', al='left', w=rowWidth[1] )
    cmds.textField( 'SSAttribute' , en=True, w=rowWidth[2] )
    cmds.setParent( '..' )
    TR.createTextFieldButtonGrp('SSController', 'Controller', partial(TR.addObject, 'SSController'), True)
    TR.subHeader(5, 'SPACE SWITCH', 7)
    TR.createTextFieldButtonGrp('SSFrom0', 'From (0)', partial(TR.addObject, 'SSFrom0'), True)
    TR.createTextFieldButtonGrp('SSTo1', 'To (1)', partial(TR.addObject, 'SSTo1'), True)
    TR.subHeader(5, 'CONSTRAINT TYPE', 7)
    TR.createRadioCollection('SpaceSwitchParent', 'Parent space switch', 'SpaceSwitchAimOrient', 'Point/Orient space switch')    
    TR.createButtonAction(10,'', 'Create Space Switch', partial(createSpaceSwitch, '', '', '', '', ''), False)
    TR.createSpaceForUtilities('---------   UTILITIES  ---------')
    TR.createButtonAction(3,'', 'Create Point/Orient Space Switch for Head', createSpaceSwitchForHead, False)
    TR.createButtonAction(3,'', 'Create Point/Orient Space Switch for Tail', createSpaceSwitchForTail, True)



def createSpaceSwitch(pName, pCtrl, pFrom0, pTo1, type, *args):
    utils.printHeader('CREATING SPACE SWITCH FOR ' + pCtrl)
    
    #############################
    utils.printSubheader('Defining and declaring variables')
    if type == '':
        type = typeOfConstraint()
      
    attribute =  cmds.textField('SSAttribute', q=True, tx=True ) if pName == '' else pName
    ctrl = cmds.textFieldGrp('SSController', q=True, tx=True) if pCtrl == '' else pCtrl
    from0 = cmds.textFieldGrp('SSFrom0', q=True, tx=True) if pFrom0 == '' else pFrom0
    to1 = cmds.textFieldGrp('SSTo1', q=True, tx=True) if pTo1 == '' else pTo1
    offset = 'OFFSET' + ctrl[4:]
    
    t = getPrefixLength(to1)
    f = getPrefixLength(from0)

    if type == 'PointOrient':
        ssTo1 = 'SPSW_ORIENT' + ctrl[4:] + utils.getNameControl(t, to1, 'upper')
        ssFrom0 = 'SPSW_ORIENT' + ctrl[4:] + utils.getNameControl(f, from0, 'upper')
        ssPCon = 'SPSW_POINT' + ctrl[4:] + utils.getNameControl(t, to1, 'upper')
    else:
        ssTo1 = 'SPSW_PARENT' + ctrl[4:] + utils.getNameControl(t, to1, 'upper')
        ssFrom0 = 'SPSW_PARENT' + ctrl[4:] + utils.getNameControl(f, from0, 'upper')
        
    #############################
    utils.printSubheader('Adding attributes and duplicating groups')
    cmds.select( ctrl )
    utils.addAttrSeparator(ctrl, 'SpaceSwitchSeparator', 'SPACE  SWITCH')
    cmds.addAttr( ln=attribute, at='float', k=True, dv=0, min=0, max=1 )
    cmds.duplicate( offset, n=ssFrom0, rc=True)
    cmds.duplicate( offset, n=ssTo1, rc=True)
    try:
        cmds.delete( cmds.listRelatives( ssFrom0, c=True ) )
        cmds.delete( cmds.listRelatives( ssTo1, c=True ) )
    except:
        pass

    if type == 'PointOrient':
        cmds.duplicate( offset, n=ssPCon, rc=True)
        try:
            cmds.delete( cmds.listRelatives( ssPCon, c=True ) )
        except:
            pass
        
    #############################
    utils.printSubheader('Creating constraints')
    
    if type == 'PointOrient':
        const = utils.getConstraint('Orient', offset[6:])

        cmds.orientConstraint( ssFrom0, ssTo1, offset, n=const, mo=True )
        cmds.pointConstraint( ssPCon, offset, n=utils.getConstraint('Point', offset[6:]), mo=True )
    else:
        const = utils.getConstraint('Parent', offset[6:])
        cmds.parentConstraint( ssFrom0, ssTo1, offset, n=const, mo=False )
    
    utils.lockAndHideAttribute(offset, True, True)
    
    #############################
    utils.printSubheader('Connecting constraints')
    reverseNode = ctrl + '_Reverse'
    cmds.shadingNode( 'reverse', au=True, n=reverseNode )
    cmds.connectAttr( ctrl + '.' + attribute, reverseNode + '.input.inputX', f=True )
    cmds.connectAttr( reverseNode + '.output.outputX', const + '.' + ssFrom0 + 'W0', f=True )
    cmds.connectAttr( ctrl + '.' + attribute, const + '.' + ssTo1 + 'W1', f=True )        
        
    #############################
    utils.printSubheader('Parenting and hidding space switch attributes')
    parentSpaceSwitches(ssFrom0, from0)
    parentSpaceSwitches(ssTo1, to1)

    if type == 'PointOrient':
        parentSpaceSwitches(ssPCon, to1)



def getPrefixLength(spsw):
    if (spsw.find('CTRL__') > -1): return 6
    elif (spsw.find('JNT__') > -1): return 5
    elif (spsw.find('OFFSET__') > -1): return 8



def parentSpaceSwitches(c, p):
    try:
        cmds.editDisplayLayerMembers( 'defaultLayer', c, nr=True )
        utils.hideAttributes(c, 0)
        cmds.parent( c, p )
    except:
        pass



def typeOfConstraint():
    if (cmds.radioButton('SpaceSwitchParent', q=True, sl=True)):
        return 'Parent'
    else:
        return 'PointOrient'



def createSpaceSwitchForHead(*args):
    utils.printSubheader('WIP')



def createSpaceSwitchForTail(*args):
    utils.printSubheader('WIP')
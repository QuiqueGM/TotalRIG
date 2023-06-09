import TotalRig as TR
import TR_GlobalVariables as TRvars
import TR_ErrorsHandler as TReh
import TR_Controllers as TRctrl
import TR_Utils as utils
import TR_Utilities
import TR_SpaceSwitch
import maya.cmds as cmds
from functools import partial


def drawUI():
    TR.toolHeader('chainToolsTab', '---------   CHAIN TOOLS  ---------')
    TR.subHeader(1, 'REDEFINE CHAIN', 5)
    winWidth = TR.winWidth
    rowWidth = [winWidth*0.1, winWidth*0.65]
    cmds.rowLayout( nc=2, cw2=rowWidth )
    cmds.text( l='', w=rowWidth[0] )
    cmds.intSliderGrp( 'NumBones', l='Number of bones', min=2, max=10, field=True, value=5, adj=1, cal=(1, "left"), w=rowWidth[1] )
    cmds.setParent( '..' ) 
    TR.createCheckbox(0.1, 'DeleteChainCB', 'Delete source chain', TR.emptyCallback, True, True)
    TR.createCheckbox(0.1, 'ControllersAndConnectCB', 'Create controllers and connect', TR.emptyCallback, False, True) 
    TR.createButtonAction(10,'', 'Redefine Chain', partial(redefineChain, False, True, False, ''), False)
    TR.subHeader(7, 'CONTROLLERS', 5)
    TR.createFloarSliderGroup('CtrlSimpleScaleChain', 'Controllers scale          ', 0.15, 0.01, 1.0, 0.05)
    TR.createButtonAction(3,'', 'Create Chain Controllers', partial(createChainControllers, False), False)
    TR.subHeader(7, 'OPTIONS', 5)
    TR.createCheckbox(0.1, 'UseMirrorChainCB', 'Activate mirror', TR.emptyCallback, True, True)
    TR.createThreeRadioCollection('ParentConst', 'Parent constraint', True, 'OrientConst', 'Orient constraint', False, 'PointConst', 'Point constraint', False, 0.1)
    TR.createButtonAction(10,'', 'Create Chain System', partial(createChainSystem, False), True)



def setStartingBone():
    sel = cmds.ls(sl=True)
    if TReh.GetSelectionException(sel): return
    
    TRvars.chainStartingBone = sel[0]



def redefineChain(delChain, connectChain, nonRoll, extra, *args):
    utils.printHeader('REDEFINE CHAIN')
    setStartingBone()
    cv = createCurve(nonRoll)
    bones = []  
    chainName = TRvars.chainStartingBone[3:]
    cmds.select( cv ) 
    curveCVs = cmds.ls( cv + ".cv[0:]",fl=True)
    
    for i, cv in enumerate(curveCVs):
        cvs = cmds.pointPosition( cv )
        number = "_{0:0=2d}".format(i+1)
        typeOfBone = 'JNT' if (i+1) < len(curveCVs) else 'END'
        bone = cmds.joint( n=typeOfBone + chainName + number + extra, p=cvs )
        cmds.editDisplayLayerMembers( 'JOINTS', bone, nr=True )
        bones.append(bone)
        
    
    cmds.select( bones[0] )
    cmds.parent( w=True )
    cmds.select( bones[0] )
    cmds.joint ( bones[0], e=True, oj='xzy', sao='zup', ch=True, zso=True )
    TRvars.twistBones = bones
    
    if cmds.checkBox( 'DeleteChainCB', q=True, v=True ) or delChain:
        cmds.delete( TRvars.chainStartingBone )
    
    cmds.select( bones[0] )
    setStartingBone()
    cmds.select( 'TMP_ChainCurve' )
    cmds.refresh()
    cmds.delete()
    
    if cmds.checkBox( 'ControllersAndConnectCB', q=True, v=True ) and connectChain:
        cmds.select( TRvars.chainStartingBone )
        createChainControllers(True)



def createCurve(nonRoll):
    selTwo = cmds.listRelatives( TRvars.chainStartingBone, c=True )
    cmds.select( TRvars.chainStartingBone, r=True )
    cmds.select( selTwo, add=True )
    sel = cmds.ls(sl=True)
    pos = [cmds.xform( obj, q=True, ws=True, translation=True ) for obj in sel]
    lastPos = pos[-1]
    length = [pos[1][0]-pos[0][0], pos[1][1]-pos[0][1], pos[1][2]-pos[0][2]]
 
    if (nonRoll == False):
        steps = cmds.intSliderGrp( 'NumBones', q=True, v=True )
    else:
        steps = cmds.intSliderGrp( 'NumNonRollJoints', q=True, v=True )
     
    step = [length[0]/steps, length[1]/steps, length[2]/steps]
    pos.pop(-1)
    
    for n in range(1,steps):
        newPos = [pos[0][0] + step[0]*n, pos[0][1] + step[1]*n, pos[0][2] + step[2]*n]
        pos.append(newPos)
    
    pos.append(lastPos)
    cv = cmds.curve( d=1, p=pos, n='TMP_ChainCurve' )

    return cv



def createChainControllers(link, *args):
    if link:
        utils.printHeader('CREATING AND CONNECTING CHAIN CONTROLLERS')
        
        setStartingBone()
        chain = getChain(TRvars.chainStartingBone, True)
        controllersChain = []
        
        cmds.refresh()
        cmds.select(chain[0])
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
        utils.printSubheader('Creating controllers --> ' + TRvars.chainStartingBone)
        for c in chain:
            cmds.select( c )
            sel = cmds.ls(sl=True)
            if sel[0].find('JNT_') > -1:
                ctrl = TRctrl.createController( 'Circle', utils.getColorFromSide(sel[0]), cmds.floatSliderGrp( 'CtrlSimpleScaleChain' ,q=True, v=True ), 'Object', sel[0], '' )
                controllersChain.append(ctrl)

                utils.lockAndHideOffset(ctrl[0], False)
        
                if (cmds.radioButton( 'ParentConst', q=True, sl=True )):
                    cmds.parentConstraint( ctrl[1], sel, n=utils.getConstraint('Parent', sel[0][3:]), mo=True )
                elif (cmds.radioButton( 'OrientConst', q=True, sl=True )):
                    cmds.orientConstraint( ctrl[1], sel, n=utils.getConstraint('Orient', sel[0][3:]), mo=True )
                else:
                    cmds.pointConstraint( ctrl[1], sel, n=utils.getConstraint('Point', sel[0][3:]), mo=True )
                
                utils.lockAndHideAttribute(ctrl[1], False, False)
            else:
                orientJoint(c)
        
        utils.printSubheader('Connecting controllers --> ' + TRvars.chainStartingBone)
        for c in range(len(controllersChain)):
            try:
                cmds.parent( controllersChain[c+1][0], controllersChain[c][1] )
                utils.lockAndHideOffset(controllersChain[c+1][0], True)
            except:
                break
        
        utils.lockAndHideOffset(controllersChain[0][0], True)
        
        setSSTailAndSpine()
    
    else:
        utils.printSubheader('Creating controllers --> ' + TRvars.chainStartingBone)
        
        chains = cmds.ls(sl=True)
        if TReh.GetNoSelectionException(chains): return
        
        for ch in chains:
            cmds.select( ch )
            setStartingBone()
            chain = getChain(TRvars.chainStartingBone, True)
            controllersChain = []
            
            cmds.refresh()
            cmds.select(chain[0])
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            
            for c in chain:
                cmds.select( c )
                sel = cmds.ls(sl=True)
                if (sel[0].find('JNT_') > -1):
                    if sel[0].find('Nose') > -1 or sel[0].find('Jaw') > -1:
                        ctrl = TRctrl.createController( 'Box', utils.getColorFromSide(sel[0]), cmds.floatSliderGrp( 'CtrlSimpleScaleChain' ,q=True, v=True ) * 2, 'Object', sel[0], '' )
                    else:
                        ctrl = TRctrl.createController( 'Circle', utils.getColorFromSide(sel[0]), cmds.floatSliderGrp( 'CtrlSimpleScaleChain' ,q=True, v=True ), 'Object', sel[0], '' )
                    controllersChain.append(ctrl)
                    utils.lockController(ctrl[1], True)

    cmds.select( d=True )



def createChainSystem(forceMirror, *args):
    utils.printHeader('CONNECTING CHAINs')
    chains = cmds.ls(sl=True)
    if TReh.GetNoSelectionException(chains): return

    allChains = mirrorControllers(chains, forceMirror)
    
    for j in chains:
        utils.printHeader('Connecting chain --> ' + j)        
        cmds.select( j )
        setStartingBone()
        jnt = TRvars.chainStartingBone
        cmds.editDisplayLayerMembers( 'JOINTS', jnt, nr=True )
            
        for c in getChain(jnt, False):
            if c.find('JNT_') > -1:
                ctrl = 'CTRL' + c[3:]
                offset = 'OFFSET' + c[3:]
                utils.lockAndHideOffset(offset, False)
                
                if (cmds.radioButton( 'ParentConst', q=True, sl=True )):
                    cmds.parentConstraint( ctrl, c, n=utils.getConstraint('Parent', c[3:]), mo=True )
                    utils.lockAndHideAttribute(ctrl, False, False)
                elif (cmds.radioButton( 'OrientConst', q=True, sl=True )):
                    cmds.orientConstraint( ctrl, c, n=utils.getConstraint('Orient', c[3:]), mo=True )
                    utils.lockAndHideAttribute(ctrl, True, False)
                else:
                    cmds.pointConstraint( ctrl, c, n=utils.getConstraint('Point', c[3:]), mo=True )
                    utils.lockAndHideAttribute(ctrl, False, True)
                
                
                
        chain = getChain(jnt, False)
        
        for c in range(len(chain)):
            try:
                p = cmds.listRelatives( chain[c], p=True )[0]
                offset = 'OFFSET' + chain[c][3:]
                ctrl = 'CTRL' + p[3:]
                cmds.parent( offset, ctrl )
                utils.lockAndHideOffset(offset, True)
            except:
                pass
        
        offset = 'OFFSET' + chain[-1][3:]
        utils.lockAndHideOffset(offset, True)
        
        if j.find('Tail') > -1:
            setSSTailAndSpine()
            
    cmds.select( d=True )
    return allChains



def mirrorControllers(chains, forceMirror):
    chainsMirror = []
    
    for c in chains:
        offsets = getOffsetsFromChain(c)
        for o in offsets:
            utils.lockAndHideOffset(o, False)
            children = cmds.listRelatives( o, c=True, s=False)
            for ch in children:
                utils.lockController(ch, False)
                
    if cmds.checkBox( 'UseMirrorChainCB', q=True, v=True ) or forceMirror:
        for c in chains:
            cmds.select( c )
            side = utils.getSideFromBone(c)
            
            if side == '':
                pass
            else:
                utils.printSubheader('Mirroring joint hierarchy --> ' + c)
                side = '__' + side
                newSide = '__R_' if side == '__L_' else '__L_'
                cmds.mirrorJoint( myz=True, mb=True, sr=(side, newSide) )
                nameMirror = c.replace(side, newSide)
                createMirrorControllers(c, side, newSide)
                chainsMirror.append(nameMirror)
  
    for j in chainsMirror:
        chains.append(j)

    return chains



def createMirrorControllers(startJoint, side, newSide):
    offsets = getOffsetsFromChain(startJoint)
    
    for o in offsets:
        utils.printSubheader('Mirroring controller --> ' + o)
        nameMirror = o.replace(side, newSide)
        mirror = cmds.duplicate( o, n=nameMirror, rc=True )
        left = cmds.listRelatives( o, ad=True, s=False)
        right = cmds.listRelatives( mirror, ad=True, s=False)
        
        for l, r in zip(left, right):
            rightName = l.replace(side, newSide)
            cmds.select( r )
            cmds.rename( r, rightName )
            col = (0, 1, 0) if side == '__L_' else (1, 0, 0)
            TRctrl.overrideColor(rightName, col)
        
        mirrorGrp = cmds.group( em=True, n='MIRROR_GRP', w=True )
        cmds.parent( mirror[0], mirrorGrp )
        cmds.select( mirrorGrp )
        cmds.setAttr( mirrorGrp + '.scaleX', -1 )
        cmds.refresh()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        
        tempGrp = cmds.group( em=True, n='TMP_GRP', w=True )
        cmds.parent( tempGrp, 'JNT' + mirror[0][6:] )
        utils.setTransformAndRotationToZero(tempGrp)
        cmds.parent( tempGrp, w=True )
            
        cmds.parent( mirror[0], tempGrp )
        cmds.refresh()
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
        cmds.parent( mirror[0], w=True )
        cmds.delete( tempGrp, mirrorGrp )



def getChain(startJoint, reverse):
    chain = cmds.listRelatives( startJoint, ad=True, type='joint' )
    chain.append( startJoint )
    if reverse:
        chain.reverse()
        
    return chain



def getOffsetsFromChain(startJoint):
    offsets = []
    for c in getChain(startJoint, False):
        if c.find('JNT_') > -1:
            offsets.append( 'OFFSET' + c[3:] )
    
    return offsets



def setSSTailAndSpine():
    try:
        cmds.select( 'JNT__Spine' )
        if TRvars.chainStartingBone.find('Tail') > -1:
            result = cmds.confirmDialog( t='Space Switch', m='Do you want to create an <b>Point/Orient</b> space switch between the <b>Tail</b> and the <b>Spine</b>?', b=['Yes','No'], db='Yes', cb='No', ds='No', p=TRvars.winName )
            if result == 'Yes':
                cmds.parent( TRvars.chainStartingBone, 'JNT__Spine' )
                offset = 'OFFSET' + TRvars.chainStartingBone[3:]
                utils.lockAndHideOffset(offset, False)
                cmds.parent( 'OFFSET' + TRvars.chainStartingBone[3:], 'CTRL__Master' )
                TR_SpaceSwitch.createSpaceSwitch('SpineSpace', 'CTRL' + TRvars.chainStartingBone[3:], 'CTRL__Master', 'CTRL__Spine', 'PointOrient')
                utils.lockAndHideOffset(offset, True)
        else:
            print ('No TAIL has been found!!')
    except:
        print ('No SPINE has been found!!')



def orientJoint(bone):
    cmds.setAttr( bone + '.jointOrientX', 0 )
    cmds.setAttr( bone + '.jointOrientY', 0 )
    cmds.setAttr( bone + '.jointOrientZ', 0 )
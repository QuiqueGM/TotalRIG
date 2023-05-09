import RiggingTools
import RT_GlobalVariables as RTvars
import RT_ErrorsHandler as RTeh
import RT_Utils as utils
import maya.cmds as cmds


def createController(sh, col, scl, ori, lblFrom, lblTo, doubleOffset = False, hideAndLockOffset = True):
    jnt = cmds.ls(sl=True)
    if RTeh.GetSelectionException(jnt): return

    if sh == '':
        sh = getShape()

    if ori == '':
        ori = getOrientation()
    
    if col == '':
        col = RTvars.ctrlColor

    if scl == '':
        scl = cmds.floatSliderGrp('ctrlScale', q=True, v=True)
    
    offsetName = jnt[0].replace('JNT', 'OFFSET')
    ctrlName = jnt[0].replace('JNT', 'CTRL')
    sz = scl * 0.5
    sz2 = sz * 2
    
    if not lblTo == '':
      offsetName = offsetName.replace(lblFrom, lblTo)
      ctrlName = ctrlName.replace(lblFrom, lblTo)
      
    if sh == 'Circle':
        ctrlObject = cmds.circle( n=ctrlName, ch=False, nr=[1,0,0], r=scl )[0]
        
    elif sh == 'Box':
	    ctrlObject = cmds.curve( n=ctrlName, d=1, p=[(sz, sz, sz), (-sz, sz, sz),(-sz, sz, -sz), (sz, sz, -sz), (sz, sz, sz), (sz, -sz, sz), (-sz, -sz, sz), (-sz, sz, sz), (-sz, -sz, sz),(-sz, -sz, -sz),(-sz, sz, -sz),(-sz, -sz, -sz),(sz, -sz, -sz),(sz, sz, -sz),(sz, -sz, -sz),(sz, -sz, sz),(sz, sz, sz)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] )
    elif sh == 'Mesh':
	    ctrlObject = cmds.curve( n=ctrlName, d=1, p=[(sz,-sz,sz), (0,-sz,sz), (-sz,-sz,sz), (-sz,-sz,0), (-sz,-sz,-sz), (0,-sz,-sz), (sz,-sz,-sz), (sz,-sz,0), (sz,-sz,sz), (sz,0,sz), (sz,sz,sz), (0,sz,sz), (-sz,sz,sz), (-sz,0,sz), (-sz,-sz,sz), (-sz,0,sz), (-sz,sz,sz), (-sz,sz,0), (-sz,sz,-sz), (-sz,0,-sz), (-sz,-sz,-sz), (-sz,0,-sz), (-sz,sz,-sz), (0,sz,-sz), (sz,sz,-sz), (sz,0,-sz), (sz,-sz,-sz), (sz,0,-sz), (sz,sz,-sz), (sz,sz,0), (sz,sz,sz) ], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] )
    elif sh == 'Lattice':
        ctrlObject = cmds.curve( n=ctrlName, d=1, p=[(0,-sz,0), (sz,-sz,0), (sz,-sz,sz), (0,-sz,sz), (0,-sz,0), (0,-sz,sz), (-sz,-sz,sz), (-sz,-sz,0), (0,-sz,0), (-sz,-sz,0), (-sz,-sz,-sz), (0,-sz,-sz), (0,-sz,0), (0,-sz,-sz), (sz,-sz,-sz), (sz,-sz,0), (sz,0,0), (sz,0,sz), (sz,-sz,sz), (sz,0,sz), (0,0,sz), (0,-sz,sz), (0,0,sz), (-sz,0,sz), (-sz,-sz,sz), (-sz,0,sz), (-sz,0,0), (-sz,-sz,0), (-sz,0,0), (-sz,0,-sz), (-sz,-sz,-sz), (-sz,0,-sz), (0,0,-sz), (0,-sz,-sz), (0,0,-sz), (sz,0,-sz), (sz,-sz,-sz), (sz,0,-sz), (sz,0,0), (sz,sz,0), (0,sz,0), (sz,sz,0), (sz,sz,sz), (sz,0,sz), (sz,sz,sz), (0,sz,sz), (0,sz,0), (0,sz,sz), (0,0,sz), (0,sz,sz), (-sz,sz,sz), (-sz,0,sz), (-sz,sz,sz), (-sz,sz,0), (0,sz,0), (-sz,sz,0), (-sz,0,0), (-sz,sz,0), (-sz,sz,-sz), (-sz,0,-sz), (-sz,sz,-sz), (0,sz,-sz), (0,sz,0), (0,sz,-sz), (0,0,-sz), (0,sz,-sz), (sz,sz,-sz), (sz,0,-sz), (sz,sz,-sz), (sz,sz,0)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69] )
    elif sh == 'Diamond':
        ctrlObject = cmds.curve( n=ctrlName, d=1, p=[(sz, 0, 0), (0, sz, 0), (0, 0, sz), (sz, 0, 0), (0, -sz, 0), (0, 0, sz), (0, sz, 0), (-sz, 0, 0), (0, 0, sz), (0, -sz, 0), (-sz, 0, 0),  (0, sz, 0), (0, 0, -sz),  (-sz, 0, 0), (0, -sz, 0), (-sz, 0, 0), (0, -sz, 0),(0, 0, -sz), (sz, 0, 0)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17, 18] )
    elif sh == 'DoubleArrow':
        ctrlObject = cmds.curve( n=ctrlName, d=1, p=[(sz, 0, sz2), (sz2, 0, sz2), (0, 0, sz2*2), (-sz2, 0, sz2), (-sz, 0, sz2), (-sz, 0, -sz2), (-sz2, 0, -sz2), (0, 0, -sz2*2), (sz2, 0, -sz2), (sz, 0, -sz2),(sz, 0, sz2)], k=[0,1,2,3,4,5,6,7,8,9,10] )	
    elif sh == 'Arrow':
        ctrlObject = cms.curve( n=ctrlName, d=1, p=[(0, 0, sz2), (0, -sz2, 0), (0, -sz, 0), (0, -sz, -sz2), (0, sz, -sz2), (0, sz, 0), (0, sz2, 0), (0, 0, sz2)], k=[0,1,2,3,4,5,6,7] )
        
    controls = setShape(offsetName, ctrlName, ctrlObject)
    const = offsetName + '_controllerConstraint'
    
    try:
        if ori == 'Object':
            cmds.parentConstraint( jnt, offsetName, n=const, mo=False )
        else:
            cmds.pointConstraint( jnt, offsetName, n=const, mo=False )
    except Exception as e:
        RTeh.DestinationIsLocked(offsetName)
        return
            
    cmds.delete( const )
          
    overrideColor( ctrlObject, col )
    cmds.editDisplayLayerMembers( 'CONTROLLERS', offsetName, nr=True )
    
    if doubleOffset and cmds.checkBox( 'CreateDoubleOffsetCB', q=True, v=True ):
        drivenKeyName = offsetName.replace('OFFSET', 'DRIVEN_KEY')
        drivenKey = cmds.duplicate( offsetName, n=drivenKeyName, rc=True )
        cmds.delete( ctrlName + '1' )
        cmds.parent( drivenKey[0], offsetName)
        cmds.parent( ctrlName, drivenKey[0] )
    
    if (hideAndLockOffset):
        utils.lockAndHideOffset(offsetName, True)      

    return [offsetName, ctrlName]



def setShape(offsetName, ctrlName, ctrlObject):
    boxShape = cmds.listRelatives(ctrlName, s=True)
    cmds.select( boxShape )
    cmds.rename( boxShape[0], ctrlName + '_Shape' )
    return parentControllers(offsetName, ctrlObject)



def getShape():
    if (cmds.radioButton('CircleCtrl', q=True, sl=True)):
        return 'Circle'
    elif (cmds.radioButton('BoxCtrl', q=True, sl=True)):
        return 'Box'
    elif (cmds.radioButton('MeshCtrl', q=True, sl=True)):
        return 'Mesh'
    else:
        return 'Diamond'



def getOrientation():
    if cmds.radioButton('ObjectCtrl', q=True, sl=True):
        return 'Object'
    else:
        return 'World'



def parentControllers(offsetName, ctrlObject):
    ctrlOffset = cmds.group( n=offsetName, em=1 )
    cmds.parent( ctrlObject, ctrlOffset )
    return ctrlOffset



def overrideColor(ctrl, col):
    cmds.setAttr( ctrl + ".overrideEnabled", 1 )
    cmds.setAttr( ctrl + ".overrideRGBColors", 1 )
    
    rgb = ("R","G","B")
    for channel, col in zip(rgb, col):
        cmds.setAttr( ctrl + ".overrideColor%s" %channel, col )



def assignColor(col, *args):
    cmds.button( 'colorizeCtrl', e=True, bgc=col )
    RTvars.ctrlColor = col



def colorizeController():
    sel = cmds.ls(sl=True)
    if RTeh.GetNoSelectionException(sel): return
    
    for s in sel:
        overrideColor(s, RTvars.ctrlColor)



def changeController():
    sel = cmds.ls(sl=True)
    if RTeh.GetSelectionException(sel): return
    
    utils.printHeader('CHANGE CONTROLLER')
    print ('OFFSET' + sel[0][4:])
    cmds.delete( 'OFFSET' + sel[0][4:] )
    jnt = 'JNT' + sel[0][4:]
    cmds.select( jnt )
    createController( getShape(), utils.getColorFromSide(jnt), '', getOrientation(), '', '' )



def copyController():
    sel = cmds.ls(sl=True)
    print (sel)
    if RTeh.GetTwoSelectionException(sel): return
    
    utils.printHeader('COPY CV\'s FROM ONE CONTROLLER TO ANOTHER')
    cvsFrom = cmds.getAttr(sel[1] + '_Shape.spans') + 1
    cvsTo = cmds.getAttr(sel[0] + '_Shape.spans') + 1  
    
    if cvsFrom == cvsTo:
        for cv in range(cvsFrom):
            vFrom = ( sel[0] + '_Shape.cv[' + str(cv) + ']' )
            pos = cmds.xform( vFrom, ws=False, t=True, q=True )
            cmds.select( sel[1] + '_Shape.cv[' + str(cv) + ']' )
            cmds.move( pos[0], pos[1], pos[2], r=False, os=True, wd=True)
    
        cmds.delete( sel[0] )
        cmds.select( d=True )
    else:
        cmds.confirmDialog( t='Copy CV\'s', m='The number of spans from the two selected objects MUST be the same.\nSource controller = ' + str(cvsFrom) + '\nDestination controller = ' + str(cvsTo), b=['OK'], p=RTvars.winName )
    

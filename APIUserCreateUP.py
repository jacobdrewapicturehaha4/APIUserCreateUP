#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)

        defaultInputNumber = "5 mm"
        defaultInputName = "Diameter"
        newInputName = ui.inputBox("Enter a new user parameter name: ", "New User Parameter", defaultInputName)
        newInputNumber = ui.inputBox("Enter a User Parameter Value: ", "New User Parameter",defaultInputNumber)

        unitsMgr = design.unitsManager
        realInputNumber = unitsMgr.evaluateExpression(newInputNumber[0],unitsMgr.defaultLengthUnits)
        
        realValueInput = adsk.core.ValueInput.createByReal(realInputNumber)
        design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')

        #ui.messageBox('Hello script')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

from server import forms
import json
from core.context import running_context

def devices():
    return {"apps": running_context.getApps(), "form":forms.AddNewDeviceForm(), "editDeviceform": forms.EditDeviceForm()}

def settings():
    userForm = forms.userForm()
    choices = [(obj.email, str(obj.email)) for obj in running_context.User.query.all()]
    userForm.username.choices = choices
    addUserForm = forms.addUserForm()
    roles =[(x.name,str(x.name)) for x in running_context.Role.query.all()]
    addUserForm.roles.choices = roles
    return {"systemForm": forms.SettingsForm(), "userForm": userForm, "addUserForm": addUserForm }

def playbook():
    return {"currentWorkflow": "multiactionWorkflow"}

def triggers():
    return {"form": forms.addNewTriggerForm(), "editForm":forms.editTriggerForm()}

def cases():
    return {"currentWorkflow": "multiactionWorkflow"}

def dashboard():
    return {"widgets":[{"app":"HelloWorld", "widget":"testWidget"}]}

def controller():
    return {
        "currentController": str(running_context.controller.name),
        "loadedWorkflows": running_context.controller.get_all_workflows(),
        "schedulerStatus": running_context.controller.scheduler.state
    }

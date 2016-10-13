global modules
modules = {}

global views
views = {}

def add_module(module):
    global modules
    modules[module.module_id] = module

def get_modules():
    global modules
    return modules

def get_module(module_id=None, token=None):
    global modules
    if module_id is not None and module_id in modules:
        return modules[module_id]
    elif token is not None:
        for id in modules:
            if token == modules[id].private_token:
                return modules[id]
    return None

def remove_module(module_id):
    global modules
    if module_id in modules:
        modules.pop(module_id)

def add_view(view):
    global views
    views[view.id] = view

def get_views():
    global views
    return views

def get_view(view_id):
    global views
    if view_id in views:
        return views[view_id]
    return None

def remove_view(view_id):
    global views
    if view_id in views:
        views.pop(view_id)

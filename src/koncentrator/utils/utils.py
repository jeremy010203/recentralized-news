global modules
modules = {}

def add_module(module):
    global modules
    modules[module.module_id] = module

def get_modules():
    global modules
    return modules

def get_module(module_id):
    global modules
    if module_id in modules:
        return modules[module_id]
    else:
        return None

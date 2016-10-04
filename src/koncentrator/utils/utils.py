global modules
modules = {}

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

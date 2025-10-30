name = "mGear"

version = "5.1.0"

authors = [
    "Jeremie Passerin",
    "Miquel Campos",
    "Jeremy Andriambolisoa",
]

description = \
    """
    mGear is a rigging and animation framework for Autodesk Maya. mGear provides a set of convenient modules, tools and c++ solvers to streamline the development of rigging and animation tools.
    """


requires = [
    "python-3+"
]

variants = [["maya-2026"]]

uuid = "mGear-Dev.mGear"

build_command = 'python {root}/build.py {install}'

def commands():
    env.MAYA_MODULE_PATH.append("{root}/mGear/")
    
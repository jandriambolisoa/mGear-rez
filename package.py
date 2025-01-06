name = "mGear"

version = "5.0.0-beta.b59ea6c9eadd65ec1717b25ff2b20e4e025e39c6" # beta from https://github.com/mgear-dev/mgear4/tree/mGear5 06/01/2025

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

variants = [["maya-2025"]]

uuid = "mGear-Dev.mGear"

build_command = 'python {root}/build.py {install}'

def commands():
    env.MAYA_MODULE_PATH.append("{root}/mGear/")
    
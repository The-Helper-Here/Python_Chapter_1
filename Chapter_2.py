'''
Chapter 2 - Getting Fameliar with Python Module and 
            understanding how to download External Modules and Writing our first programme.
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

PYTHON MODULES AND PIP.

What is Module in Python?
                           Module or library is a file that contains definitions of several functions,
classes,variables, etc. which is written by someone else and is in its best from and is ready for us to use.
There are two types of Modules.
1.Built-In Modules: They are the modules which are already installed when we download python in our system.
2.External Modules: They are the modules which are not installed and require and external installation when
                    need to be used.The can be installed using pip.

What is Pip in Python?
                       Pip is a package manager in python which helpes to install external modules. 

------------------------------------------------------------------------------------------------------

HOW TO USE PIP AND IMPORT EXTERNAL MODULES IN OUR PROJECT.

Installing External Module:

       Open your terminal, then type the following command.

       pip install "The name of the module."

       This command will automatically intsall the module you have asked for.

Uninstalling External Module:

       Open your terminal, then type the following command.

       pip uninstall "The name of the module."

       This command will automatically intsall the module you have asked for.

Upgrading Pip:
             
             For Upgrading pip there are the following commands based on your OS.
             
             Windows: py -m pip install -U pip
             MacOS  : python -m pip install -U pip


Importing a module in your project:
 To import a module in our project we can use the "import" function.'''

#Example:
#flask is an external module.
#Install flask using pip
import flask

'''Writing our first programme in python'''
# The "print" command is helps to literally print anything enclosed within it without any changes.
 
print("Hello world")

# The output for the above command will be
# Hello World
'''
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
End of chapter 2
Author: The Helper Here </>
'''

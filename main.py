#!/usr/bin/env python3

# Filename: pycalc.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python.

The application is implemented using the MVC pattern. Views and controllers
are provided for PyQt5, PySide2, wxPython and Tkinter. Every time you run the
app, the view changes alternatively from a framework to another."""

import sys

from pycalc.evaluator import Evaluator
from pycalc.config import PyCalcConfig

__version__ = "1.0"
__author__ = "Leodanis Pozo Ramos"


# Client code
def main():
    """Main function."""
    ui = PyCalcConfig('config.ini').read()
    try:
        globals()[f'{ui}_app']()
    except ModuleNotFoundError as e:
        print(e, file=sys.stderr)


def pyqt5_app():
    """PyQt5 implementation."""
    PyCalcConfig('config.ini').write()

    # Import QApplication from PyQt5.QtWidgets
    from PyQt5.QtWidgets import QApplication

    # Import the view and the controller
    from pycalc.pyqt5_vc.qt_view import PyCalcUi
    from pycalc.pyqt5_vc.qt_controller import PyCalcCtrl

    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)

    # Create the calculator's GUI
    view = PyCalcUi()

    # Create the model
    model = Evaluator()

    # Create the controller and run it
    controller = PyCalcCtrl(model=model, view=view)
    controller.run()

    # Execute calculator's main loop
    sys.exit(pycalc.exec_())


def pyside2_app():
    """PySide2 implementation."""
    PyCalcConfig('config.ini').write()

    # Import QApplication from PySide2.QtWidgets
    from PySide2.QtWidgets import QApplication

    # Import the view and the controller
    from pycalc.pyside2_vc.ps2_view import PyCalcUi
    from pycalc.pyside2_vc.ps2_controller import PyCalcCtrl

    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)

    # Create the calculator's GUI
    view = PyCalcUi()

    # Create the model
    model = Evaluator()

    # Create the controller and run it
    controller = PyCalcCtrl(model=model, view=view)
    controller.run()

    # Execute calculator's main loop
    sys.exit(pycalc.exec_())


def tkinter_app():
    """Tkinter implementation."""
    PyCalcConfig('config.ini').write()

    # Import the view and the controller
    from pycalc.tkinter_vc.tk_view import PyCalcUi
    from pycalc.tkinter_vc.tk_controller import PyCalcCtrl

    # Create the calculator's GUI
    view = PyCalcUi()

    # Create the model
    model = Evaluator()

    # Create the controller and run it
    controller = PyCalcCtrl(model, view)
    controller.run()

    # Execute calculator's main loop
    view.mainloop()


def wxpython_app():
    """wxPython implementation."""
    PyCalcConfig('config.ini').write()
    # Import wx package
    import wx

    # Import the view and the controller
    from pycalc.wxpython_vc.wx_view import PyCalcUi
    from pycalc.wxpython_vc.wx_controller import PyCalcCtrl

    # Create an instance of wx.App
    pycalc = wx.App()

    # Create the calculator's GUI
    view = PyCalcUi()
    pycalc.SetTopWindow(view)

    # Create the model
    model = Evaluator()

    # Create the controller and run it
    controller = PyCalcCtrl(model, view)
    controller.run()

    # Execute calculator's main loop
    pycalc.MainLoop()


if __name__ == "__main__":
    main()
    
    
    
    



Python | Simple GUI calculator using Tkinter

 

k.

 



 















 

# Python program to create a simple GUI 

# calculator using Tkinter 

 

# import everything from tkinter module 

from tkinter import *

 

# globally declare the expression variable 

expression = "" 

 

 

# Function to update expression 

# in the text entry box 

def press(num): 

    # point out the global expression variable 

    global expression 

 

    # concatenation of string 

    expression = expression + str(num) 

 

    # update the expression by using set method 

    equation.set(expression) 

 

 

# Function to evaluate the final expression 

def equalpress(): 

    # Try and except statement is used 

    # for handling the errors like zero 

    # division error etc. 

 

    # Put that code inside the try block 

    # which may generate the error 

    try: 

 

        global expression 

 

        # eval function evaluate the expression 

        # and str function convert the result 

        # into string 

        total = str(eval(expression)) 

 

        equation.set(total) 

 

        # initialize the expression variable 

        # by empty string 

        expression = "" 

 

    # if error is generate then handle 

    # by the except block 

    except: 

 

        equation.set(" error ") 

        expression = "" 

 

 

# Function to clear the contents 

# of text entry box 

def clear(): 

    global expression 

    expression = "" 

    equation.set("") 

 

 

# Driver code 

if __name__ == "__main__": 

    # create a GUI window 

    gui = Tk() 

 

    # set the background colour of GUI window 

    gui.configure(background="light green") 

 

    # set the title of GUI window 

    gui.title("Simple Calculator") 

 

    # set the configuration of GUI window 

    gui.geometry("270x150") 

 

    # StringVar() is the variable class 

    # we create an instance of this class 

    equation = StringVar() 

 

    # create the text entry box for 

    # showing the expression . 

    expression_field = Entry(gui, textvariable=equation) 

 

    # grid method is used for placing 

    # the widgets at respective positions 

    # in table like structure . 

    expression_field.grid(columnspan=4, ipadx=70)

 

    # create a Buttons and place at a particular 

    # location inside the root window . 

    # when user press the button, the command or 

    # function affiliated to that button is executed . 

    button1 = Button(gui, text=' 1 ', fg='black', bg='red', 

                    command=lambda: press(1), height=1, width=7) 

    button1.grid(row=2, column=0) 

 

    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 

                    command=lambda: press(2), height=1, width=7) 

    button2.grid(row=2, column=1) 

 

    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 

                    command=lambda: press(3), height=1, width=7) 

    button3.grid(row=2, column=2) 

 

    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 

                    command=lambda: press(4), height=1, width=7) 

    button4.grid(row=3, column=0) 

 

    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 

                    command=lambda: press(5), height=1, width=7) 

    button5.grid(row=3, column=1) 

 

    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 

                    command=lambda: press(6), height=1, width=7) 

    button6.grid(row=3, column=2) 

 

    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 

                    command=lambda: press(7), height=1, width=7) 

    button7.grid(row=4, column=0) 

 

    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 

                    command=lambda: press(8), height=1, width=7) 

    button8.grid(row=4, column=1) 

 

    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 

                    command=lambda: press(9), height=1, width=7) 

    button9.grid(row=4, column=2) 

 

    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 

                    command=lambda: press(0), height=1, width=7) 

    button0.grid(row=5, column=0) 

 

    plus = Button(gui, text=' + ', fg='black', bg='red', 

                command=lambda: press("+"), height=1, width=7) 

    plus.grid(row=2, column=3) 

 

    minus = Button(gui, text=' - ', fg='black', bg='red', 

                command=lambda: press("-"), height=1, width=7) 

    minus.grid(row=3, column=3) 

 

    multiply = Button(gui, text=' * ', fg='black', bg='red', 

                    command=lambda: press("*"), height=1, width=7) 

    multiply.grid(row=4, column=3) 

 

    divide = Button(gui, text=' / ', fg='black', bg='red', 

                    command=lambda: press("/"), height=1, width=7) 

    divide.grid(row=5, column=3) 

 

    equal = Button(gui, text=' = ', fg='black', bg='red', 

                command=equalpress, height=1, width=7) 

    equal.grid(row=5, column=2) 

 

    clear = Button(gui, text='Clear', fg='black', bg='red', 

                command=clear, height=1, width=7) 

    clear.grid(row=5, column='1') 

 

    Decimal= Button(gui, text='.', fg='black', bg='red', 

                    command=lambda: press('.'), height=1, width=7) 

    Decimal.grid(row=6, column=0) 

    # start the GUI 

    gui.mainloop() 

Output : 

 Attention geek! Strengthen your foundations with the Python Programming Foundation Course and learn the basics.  

To begin with, your interview preparations Enhance your Data Structures concepts with the Python DS Course. And to begin with your Machine Learning Journey, join the Machine Learning – Basic Level Course

Article Tags : ProjectPython Python-tkinter











COMPANY

About Us

Careers

Privacy Policy

Contact Us

LEARN

Algorithms

Data Structures

Languages

CS Subjects

Video Tutorials

PRACTICE

Company-wise

Topic-wise

Contests

Subjective Questions

CONTRIBUTE

Write an Article

GBlog

Videos

    


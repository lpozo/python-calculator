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
app, the views change alternatively from a framework to another."""

import sys

from pycalc.model import PyCalcModel
from pycalc.config import PyCalcConfig

__version__ = "0.1"
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
    from pycalc.qt_view import PyCalcUi
    from pycalc.qt_controller import PyCalcCtrl

    # Create an instance of `QApplication`
    pycalc = QApplication(sys.argv)

    # Create the calculator's GUI
    view = PyCalcUi()

    # Create the model
    model = PyCalcModel()

    # Create the controller and run it
    controller = PyCalcCtrl(model=model, view=view)
    controller.run()

    # Execute calculator's main loop
    sys.exit(pycalc.exec_())


def pyside2_app():
    """PySide2 implementation."""
    PyCalcConfig('config.ini').write()

    # Import QApplication from PyQt5.QtWidgets
    from PySide2.QtWidgets import QApplication

    # Import the view and the controller
    from pycalc.ps2_view import PyCalcUi
    from pycalc.ps2_controller import PyCalcCtrl

    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)

    # Create the calculator's GUI
    view = PyCalcUi()

    # Create the model
    model = PyCalcModel()

    # Create the controller and run it
    controller = PyCalcCtrl(model=model, view=view)
    controller.run()

    # Execute calculator's main loop
    sys.exit(pycalc.exec_())


def tkinter_app():
    """Tkinter implementation."""
    PyCalcConfig('config.ini').write()

    # Import the view and the controller
    from pycalc.tk_view import PyCalcUi
    from pycalc.tk_controller import PyCalcCtrl

    # Create the calculator's GUI
    view = PyCalcUi()

    # Create the model
    model = PyCalcModel()

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
    from pycalc.wx_view import PyCalcUi
    from pycalc.wx_controller import PyCalcCtrl

    # Create an instance of wx.App
    pycalc = wx.App()

    # Create the calculator's GUI
    view = PyCalcUi()
    pycalc.SetTopWindow(view)

    # Create the model
    model = PyCalcModel()

    # Create the controller and run it
    controller = PyCalcCtrl(model, view)
    controller.run()

    # Execute calculator's main loop
    pycalc.MainLoop()


if __name__ == "__main__":
    main()

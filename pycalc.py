#!/usr/bin/env python3

# Filename: pycalc.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys

from pycalc.model import PyCalcModel

__version__ = "0.1"
__author__ = "Leodanis Pozo Ramos"


# Client code
def main():
    """Main function."""


def pyqt_app():
    """PyQt5 implementation."""
    # Import QApplication and the required widgets from PyQt5.QtWidgets
    from PyQt5.QtWidgets import QApplication

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


def tk_app():
    """Tkinter implementation."""
    from pycalc.tk_view import PyCalcUi
    from pycalc.tk_controller import PyCalcCtrl
    from pycalc.model import PyCalcModel

    view = PyCalcUi()
    model = PyCalcModel()
    controller = PyCalcCtrl(model, view)
    controller.run()

if __name__ == "__main__":
    main()

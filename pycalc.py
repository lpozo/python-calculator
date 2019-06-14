#!/usr/bin/env python3

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a Python Calculator with PyQt5."""

import sys
from functools import partial

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

__version__ = '0.1'
__author__ = 'Leodanis Pozo Ramos'

ERROR_MSG = 'ERROR'


class PyCalcCtrl:
    """PyCalc Controller class."""

    def __init__(self, model, view):
        """Controller initializer."""
        super(PyCalcCtrl, self).__init__()
        self._evaluate = model
        self._ui = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._ui.displayText())
        self._ui.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._ui.displayText() == ERROR_MSG:
            self._ui.clearDisplay()

        expression = self._ui.displayText() + sub_exp
        self._ui.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btn_text, btn in self._ui.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btn_text))

        self._ui.buttons['='].clicked.connect(self._calculateResult)
        self._ui.display.returnPressed.connect(self._calculateResult)
        self._ui.buttons['C'].clicked.connect(self._ui.clearDisplay)


class PyCalcUi(QMainWindow):
    """PyCalc View or UI class."""

    def __init__(self):
        """UI initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle("PyCalc")
        self.setFixedSize(235, 235)
        # Create and set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        # Add the display widget to the general layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #     btn_text | position in the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }
        # Create the buttons
        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btn_text], pos[0], pos[1])
        # Add the buttons to the general layout
        self.generalLayout.addLayout(buttonsLayout)


# Model
def evaluateExpression(expression):
    """Evaluate a expression."""
    try:
        result = str(eval(expression, {}, {}))
    except:
        result = ERROR_MSG

    return result


# Client code
def main():
    """Main function."""
    createPyqt5Calculator()


def createPyqt5Calculator():
    # 1. Create the PyQt5 Application
    pycalc = QApplication(sys.argv)
    # 2. Create the View
    view = PyCalcUi()
    # 3. Show the View
    view.show()
    # 4. Create the model, and the controller
    model = evaluateExpression
    controller = PyCalcCtrl(model, view)
    # 5. Run PyQt5 main loop
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    # Run the application's main function
    main()

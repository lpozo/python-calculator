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

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout


class PyCalcCtrl:
    """PyCalc Controller class."""

    def __init__(self):
        """Controller initializer."""
        super(PyCalcCtrl, self).__init__()
        # Application
        self._pycalc = QApplication(sys.argv)
        # GUI
        self._ui = PyCalcUi()

    def runApp(self):
        """Run the application."""
        self._ui.show()
        sys.exit(self._pycalc.exec_())


class PyCalcUi(QMainWindow):
    """PyCalc View or UI class."""

    def __init__(self):
        """UI initializer."""
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)


# Client code
def main():
    """Main function."""
    app_ctrl = PyCalcCtrl()
    app_ctrl.runApp()


if __name__ == '__main__':
    main()

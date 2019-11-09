# Filename: qt_view.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and PyQt5."""

# Import QApplication and the required widgets from PyQt5.QtWidgets
import wx


# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(wx.Frame):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__(parent=None, title="PyCalc")
        self.panel = wx.Panel(self)
        self.generalSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.generalSizer)
        # Set some main window's properties
        self.SetMaxSize((250, 250))
        self.SetMinSize((250, 250))
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()
        self.Show()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        sizer = wx.BoxSizer()
        self.display = wx.TextCtrl(self.panel)
        sizer.Add(self.display)
        # Set some display's properties
        # self.display.setFixedHeight(35)
        # self.display.setAlignment(Qt.AlignRight)
        # self.display.setReadOnly(True)
        # Add the display to the general layout
        self.generalSizer.Add(sizer)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsSizer = wx.GridSizer(5, 4, 4)
        # Button text
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = wx.Button(self.panel, label=btnText, size=(40, 40))
            buttonsSizer.Add(self.buttons[btnText])
        # Add buttonsSizer to the general layout
        self.generalSizer.Add(buttonsSizer)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
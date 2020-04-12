# Filename: wx_view.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and the MVC pattern."""

# Import wx package
import wx


# Create a subclass of wx.Frame to setup the calculator's GUI
class PyCalcUi(wx.Frame):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__(parent=None, title="PyCalc")
        self.panel = wx.Panel(self, size=(248, 248))
        self.generalSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizerAndFit(self.generalSizer)
        self.SetMaxSize((250, 268))
        self.SetMinSize((250, 268))
        # Create the display and the buttons
        self._createDisplay()
        self._createButtons()
        self.Show()

    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        sizer = wx.BoxSizer()
        self.display = wx.TextCtrl(self.panel,
                                   style=wx.TE_READONLY|wx.ALIGN_RIGHT)
        self.display.SetMinSize((242, 35))
        sizer.Add(self.display, flag=wx.ALL, border=4)
        # Add the display to the general sizer
        self.generalSizer.Add(sizer)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsSizer = wx.GridBagSizer(hgap=2, vgap=2)
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
        # Create the buttons and add them to the grid sizer
        for btnText, pos in buttons.items():
            self.buttons[btnText] = wx.Button(self.panel,
                                              label=btnText,
                                              size=(40, 40))
            buttonsSizer.Add(self.buttons[btnText], pos, flag=wx.ALL, border=4)
        # Add buttonsSizer to the general sizer
        self.generalSizer.Add(buttonsSizer)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.SetValue(text)
        self.display.SetFocus()

    def displayText(self):
        """Get display's text."""
        return self.display.GetValue()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")

# Filename: tk_view.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and Tkinter."""

# Import Tkinter classes
from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar


# Create a subclass of Tk to setup the calculator's GUI
class PyCalcUi(Tk):
    """PyCalc's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.title("PyCalc")
        self.maxsize(231, 229)
        self.minsize(231, 229)

    #     # Create the display and the buttons
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """Create the display."""
        # Create the display widget
        self.display = Entry(self, state='readonly', justify='right')
        self.display.grid(row=0, columnspan=5, sticky='we', padx=1, pady=1)
        self.display.focus_set()

    def _create_buttons(self):
        """Create the buttons."""
        self.buttons = {}
        # Button text | position on the grid
        buttons = {
            "7": (1, 0),
            "8": (1, 1),
            "9": (1, 2),
            "/": (1, 3),
            "C": (1, 4),
            "4": (2, 0),
            "5": (2, 1),
            "6": (2, 2),
            "*": (2, 3),
            "(": (2, 4),
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "-": (3, 3),
            ")": (3, 4),
            "0": (4, 0),
            "00": (4, 1),
            ".": (4, 2),
            "+": (4, 3),
            "=": (4, 4),
        }
        # Create the buttons and add them to the grid geometry manager
        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = Button(self, text=btn_text)
            self.buttons[btn_text].config(width=2, height=2)
            self.buttons[btn_text].grid(row=pos[0], column=pos[1],
                                        sticky='NSEW', padx=1, pady=1)

    def set_display_text(self, text):
        """Set display's text."""
        text_var = StringVar()
        text_var.set(text)
        self.display['textvariable'] = text_var
        self.display.focus_set()

    def display_text(self):
        """Get display's text."""
        return self.display.get()

    def clear_display(self):
        """Clear the display."""
        self.set_display_text("")

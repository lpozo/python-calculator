# Filename: wx_controller.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and PyQt5."""

from functools import partial

import wx

from . import ERROR_MSG


# Create a Controller class to connect the GUI and the model
class PyCalcCtrl:
    """PyCalc's Controller."""

    def __init__(self, model, view):
        """Controller initializer."""
        self._model = model
        self._view = view

    def run(self):
        """Run the controller."""
        # Bind events
        self._bindEvents()

    def _calculateResult(self, event):
        """Evaluate expressions."""
        result = self._model.evaluate_expression(self._view.displayText())
        self._view.setDisplayText(result)

    def _clearDisplay(self, event):
        """Clear the display."""
        self._view.clearDisplay()

    def _buildExpression(self, sub_exp, event):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _bindEvents(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                self._view.Bind(wx.EVT_BUTTON,
                                partial(self._buildExpression, btnText),
                                btn)

        self._view.Bind(wx.EVT_BUTTON,
                        self._calculateResult,
                        self._view.buttons["="])
        self._view.Bind(wx.EVT_BUTTON,
                        self._clearDisplay,
                        self._view.buttons["C"])
        self._view.Bind(wx.EVT_COMMAND_ENTER,
                        self._calculateResult,
                        self._view.display)

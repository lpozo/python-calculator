# Filename: tk_controller.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python and PyQt5."""

from functools import partial

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
        # Connect commands
        self._connect_commands()

        self._view.mainloop()

    def _calculate_result(self):
        """Evaluate expressions."""
        result = self._model.evaluate_expression(self._view.display_text())
        self._view.set_display_text(result)

    def _build_expression(self, sub_exp):
        """Build expression."""
        if self._view.display_text() == ERROR_MSG:
            self._view.clear_display()

        expression = self._view.display_text() + sub_exp
        self._view.set_display_text(expression)

    def _connect_commands(self):
        """Connect commands."""
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {"=", "C"}:
                btn.config(command=partial(self._build_expression, btn_text))

        self._view.buttons["="].config(command=self._calculate_result)
        # self._view.display.returnPressed.connect(self._calculate_result)
        self._view.buttons["C"].config(command=self._view.clear_display)

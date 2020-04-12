# -*- coding: utf-8 -*-

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This module provides tests for pycalc.evaluator."""

import pytest
from pytest import param

from pycalc.evaluator import Evaluator


@pytest.mark.parametrize(
    "expression, expected",
    [
        param("5 + 8", str(5 + 8)),
        param("-8 * 9", str(-8 * 9)),
        param("2 - 3 *", "ERROR"),
        param("2 * 5 / (3 + 2", "ERROR")
    ],
)
def test_evaluate(expression, expected):
    assert Evaluator().evaluate(expression) == expected

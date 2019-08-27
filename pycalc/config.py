# Filename: config.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""PyCalc is a simple calculator built using Python."""

import configparser


class PyCalcConfig:
    """PyCalcConfig class."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()

    def write(self):
        """Write config file."""
        if self.read() == 'pyqt5':
            self.config['General']['UI'] = 'tkinter'
        else:
            self.config['General']['UI'] = 'pyqt5'

        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)

    def read(self):
        self.config.read(self.file_path)
        return self.config['General']['UI']

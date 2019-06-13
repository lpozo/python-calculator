## PyCalc

PyCalc is a minimal Python Calculator, which GUI was built using the [PyQt5 library](https://www.riverbankcomputing.com/static/Docs/PyQt5/introduction.html).

## Requirements

For PyCalc to work, you need a proper installation of [Python](https://www.python.org) >= 3.6, and then to install the PyQt5 library, which can be done by using `pip3` as follows:

```console
$ sudo pip3 install -r requirements.txt
```

We don't recommend you to install PyCalc's requirements directly into your system. So, you can use a virtual environment to test PyCalc. To do that, you can run the following:

```console
$ python3 -m venv pycalc
$ source pycalc/bin/activate
$ pip install -r requirements.txt
```

For more information on how to install PyQt5, you can take a look at the related topic on the [project's documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html).

## How to Run PyCalc

To run PyCalc from the your system's command-line, you can execute the following command:

```console
$ python3 pycalc.py
```

## Screenshot

![Screenshot](screenshot.png)

## About the Author

- [Leodanis Pozo Ramos](https://lpozo.github.com/)

## License

PyCalc is released under the [MIT License](https://opensource.org/licenses/MIT).
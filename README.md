```shell
$ pip install PyQt5==5.7.1
$ python app.py
file:///path/to/App.qml:17:14: Unable to assign QJSValue to PyQt_PyObject

```

```shell
$ pip install PyQt5==5.7.0
$ python app.py
“python app.py” terminated by signal SIGSEGV (Address boundary error)
```

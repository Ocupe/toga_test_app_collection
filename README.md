# Toga Test App Collection - TTAC
A collection of small apps that test specific widgets or parts of Toga.

### Add new app to TTAC
You should start with the creation of the basic app structure.
We use the briefcase cookiecutter template for that.
~~~bash
$ pip install cookiecutter
$ cookiecutter https://github.com/pybee/briefcase-template
~~~

> Note
If you get an error running cookiecutter than you maybe have to
define the following.
~~~bash
$ export LC_ALL=de_DE.utf-8
$ export LANG=de_DE.utf-8
~~~
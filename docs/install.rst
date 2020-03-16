Install
=======

`Radar-python` requires Python 3.4 or greater.

Below we assume you have the default Python environment already configured on
your computer and you intend to install ``radar-python`` inside of it.  If you want
to create and work with Python virtual environments, please follow instructions
on `venv <https://docs.python.org/3/library/venv.html>`_ and `virtual
environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.

First, make sure you have the latest version of ``pip`` (the Python package manager)
installed. If you do not, refer to the `Pip documentation
<https://pip.pypa.io/en/stable/installing/>`_ and install ``pip`` first.

Install the released version
----------------------------

The easiest (and best) way to install radar-python is through `pip <http://www.pip-installer.org/>`_::

Install the current release of ``radar-python`` with ``pip``::

    $ pip install radar-python

To upgrade to a newer release use the ``--upgrade`` flag::

    $ pip install --upgrade radar-python

If you do not have permission to install software systemwide, you can
install into your user directory using the ``--user`` flag::

    $ pip install --user radar-python

Alternatively, you can manually download ``radar-python`` from
`GitHub <https://github.com/radarlabs/radar-python/releases>`_  or
`PyPI <https://pypi.python.org/pypi/networkx>`_.
To install one of these versions, unpack it and run the following from the
top-level source directory using the Terminal::

    $ pip install .


Dependencies
------------

Python 3.4+ is required.

- :py:mod:`requests` - `python-requests <http://docs.python-requests.org>`_ library handles HTTP requests.

Installing through :py:mod:`pip` takes care of dependencies for you.
Installation
************

.. note::

    Before installing this library, please note the following:

    * The use of a `virtual environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ is **highly recommended**;
    * This library uses `GDAL <http://www.gdal.org/>`_ for reading and writing vector data and `python-GDAL <https://pypi.python.org/pypi/GDAL/>`_ as a wrapper.

Installing GDAL
===============

First of all, **the GDAL library needs to be installed system-wide**.

Linux
-----

If you are using Linux, the GDAL library is probably already located in one of your distribution's repositories. If so, you can install it using your distribution's package manager, along with the other necessary dependencies.

.. note::

    The names of packages may vary between distributions:

    * Fedora::

        $ sudo dnf install gdal gdal-devel gcc-c++ redhat-rpm-config

Once installed, locate the GDAL's headers and set the *include* path to the CPLUS_INCLUDE_PATH and C_INCLUDE_PATH environment variables::

    $ whereis gdal
    gdal: /usr/include/gdal /usr/share/gdal

    $ export CPLUS_INCLUDE_PATH=/usr/include/gdal/
    $ export C_INCLUDE_PATH=/usr/include/gdal/

After that, you can proceed to installing GDAL in the virtual environment (i.e. `python-GDAL`). Please not that the version of `python-GDAL <https://pypi.python.org/pypi/GDAL/>`_ installed in the virtual environment **should correspond as much as possible** to the version of the system-wide installation as much as possible. For instance, if the system-wide installation is 2.1.4, and there is no matching Python library, feel free to install the closest *minor* version (e.g. 2.1.3)::

    $ gdalinfo --version
    GDAL 2.1.4, released 2017/06/23

    # Activate your virtual environment
    $ pip install GDAL==2.1.3

.. seealso::

    For more info, visit `Stack Exchange <http://gis.stackexchange.com/questions/28966/python-gdal-package-missing-header-file-when-installing-via-pip>`__.

Installing centerline
=====================

You can download and install the package from `PyPI <https://pypi.python.org/pypi/centerline>`_ using `pip <https://pypi.python.org/pypi/pip/>`_:

.. code:: bash

    $ pip install centerline

Development
===========

If you want to contribute to this library, apart from installing GDAL, you have to:

1. fork and clone the repository::

    $ git clone git@github.com:user/centerline.git

2. install the library into its own virtual environment::

    $ pip install -e .[dev,lint,test,docs]

3. run the test suite to make sure everything is in order::

    $ pytest

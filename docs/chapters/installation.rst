************
Installation
************

If you want to use the ``create_centerline`` command-line tool, you need to install `GDAL <https://gdal.org/>`_ and the corresponding `python-GDAL <https://pypi.python.org/pypi/GDAL/>`_ version. ``GDAL`` is a translator library for raster and vector geospatial data formats whose `binary <https://gdal.org/download.html#binaries>`_ needs to be installed system-wide, whereas ``python-GDAL`` should be installed into a `virtual environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.

Installing GDAL
===============

GDAL binary
-----------

Linux
^^^^^

If you are using Linux, the GDAL library is probably already located in one of your distribution's repositories. If so, you can install it using your distribution's package manager, along with the other necessary dependencies.

.. note::

    The names of packages may vary between distributions.

If you are using Fedora, run the following command:

.. code:: bash

    $ sudo dnf install gdal gdal-devel gcc-c++ redhat-rpm-config

.. _python-gdal-binding:

python-GDAL
-----------

Once installed, locate the GDAL's headers and set the *include* path to the ``CPLUS_INCLUDE_PATH`` and ``C_INCLUDE_PATH`` environment variables::

    $ whereis gdal
    gdal: /usr/include/gdal /usr/share/gdal

    $ export CPLUS_INCLUDE_PATH=/usr/include/gdal/
    $ export C_INCLUDE_PATH=/usr/include/gdal/

After that, you can proceed to installing GDAL in the virtual environment (i.e. ``python-GDAL``). Please not that the version of `python-GDAL <https://pypi.python.org/pypi/GDAL/>`_ installed in the virtual environment **should correspond as much as possible** to the version of the system-wide installation as much as possible. For instance, if the system-wide installation is 2.1.4, and there is no matching Python library, feel free to install the closest *minor* version (e.g. 2.1.3)::

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

GDAL can be installed either directly (see :ref:`python-gdal-binding`) or by specifying the ``gdal`` extra dependency:

.. code:: bash

    $ pip install centerline[gdal]

.. warning::

    ``pip install centerline[gdal]`` can be error-prone because multiple GDAL versions are supported and ``pip`` will automatically try to retrieve the latest version which you may or may not have installed system-wide.

Development
===========

If you want to contribute to this library, apart from installing GDAL, you have to:

1. fork and clone the repository:

.. code:: bash

    $ git clone git@github.com:user/centerline.git

2. install the library in develop mode:

.. code:: bash

    $ pip install -e .[dev,gdal,lint,test,docs]

3. run the test suite to make sure everything is in order:

.. code:: bash

    $ tox

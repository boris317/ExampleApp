Example python package using distribute.

After you clone the repo do this from the project root (make sure your virtualenv is active!!)::

    $ pip install -e .
    
This installs the package as "editable" along with all its depedencies (Open setup.py and take a look at how dependencies are defined.)
After this you should be able to drop into a python interpeter and import the package::

    $ python
    >> import exampleapp


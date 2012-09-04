After you clone the repo do this from the project root ::

    $ pip install -e .
    
This installs the app as "editable". This is similar to running ``pyhon setup.py develop``. You can test that the
application runs like so ::

    $ paster serve development.ini
    

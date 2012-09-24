from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='ExampleApp',
      version=version,
      description="Example flask app that can be loaded with paste.deploy",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Shawn Adams',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=["foo.py"],
      install_requires=[
          "flask",
          "sqlalchemy",
          "pastedeploy",
          "pastescript"
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.app_factory]
      main = exampleapp:make_app  	  
      """,
      )

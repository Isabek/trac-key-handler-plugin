from setuptools import setup

PACKAGE = 'TracKeyHandler'
VERSION = '0.1'

setup(name=PACKAGE,
      version=VERSION,
      packages=['keyhandler'],
      entry_points={'trac.plugins': [
          'TracKeyHandler.matcher = keyhandler.matcher'
      ]},
      package_data={
          'tracker': ['htdocs/js/*.js']},
      install_requires=['trac']
)
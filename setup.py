from setuptools import setup

setup(
  name='lendinglibrary',
  packages=['lendinglibrary'],
  include_package_data=True,
  install_requires=[
    'flask',
    'Flask-PyMongo',
    'dnspython',
    'schema'
  ],
)

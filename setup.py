from setuptools import setup

setup(
  name='lendinglibrary',
  packages=['lendinglibrary'],
  include_package_data=True,
  install_requires=[
    'flask==1.1.1',
    'Flask-PyMongo==2.3.0',
    'dnspython==1.16.0',
    'schema==0.7.1'
  ],
)

from setuptools import setup

setup(
    name='api',
    packages=['api'],
    include_package_data=True,
    install_requires=[
        'flask==1.1.1',
        'flask-cors==3.0.8',
        'Flask-PyMongo==2.3.0',
        'dnspython==1.16.0',
        'schema==0.7.1',
        'Flask-JWT-Extended==3.24.1'
    ],
    extras_require={
        'dev': [
            'pytest',
            'autopep8'
        ]
    }
)

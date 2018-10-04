from setuptools import setup

setup(
    name='python-appsflyer',
    version='0.2.0',
    description='AppsFlyer API client library for Python.',
    author='SeongKwang Jin',
    author_email='jinsk44@gmail.com',
    url='https://github.com/jinsk44/python-appsflyer',
    packages=[
        'appsflyer',
    ],
    license='MIT',
    install_requires=[
        'requests',
        'furl',
    ],
)

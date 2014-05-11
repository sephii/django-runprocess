#!/usr/bin/env python
import codecs
import os
from setuptools import find_packages, setup

from runprocess import __version__


def read(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with codecs.open(file_path, encoding='utf-8') as fp:
        return fp.read()

setup(
    name='django_runprocess',
    version=__version__,
    license='MIT',
    description='Runs processes along with runserver',
    long_description=read('README.rst'),
    author='Sylvain Fankhauser',
    author_email='sylvain@fankhauser.name',
    packages=find_packages(),
    url='https://github.com/sephii/django-runprocess',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

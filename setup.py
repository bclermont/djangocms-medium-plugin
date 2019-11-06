import os
from setuptools import setup, find_packages

PKG_NAME = 'cmsmedium'
VERSION = __import__(PKG_NAME).__version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=PKG_NAME,
    version=VERSION,
    author="Bruno Clermont",
    author_email="bruno@robotinfra.com",
    description="A Django CMS plugin to show posts of Medium.",
    license="BSD",
    keywords="django cms plugin medium",
    url="http://github.com/bclermont/" + PKG_NAME,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires=['feedparser', 'python-dateutil', 'Django >= 1.4', 'django-cms >= 3.5.3'],
    long_description=read("README.md"),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

# -*- coding: utf-8 -*-


import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from setuptools import setup, find_packages

packages = [
    'async_bruteforce'
]

requires = [
    'aiohttp'
]

test_requirements = []
setup(
    name='async_bruteforce',
    version='0.0.1',
    description='async bruteforce',
    author='eteamin',
    author_email='aminetesamian1371@gmail.com',
    url='https://github.com/eteamin/async_bruteforce',
    packages=packages,
    install_requires=requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=test_requirements,

)


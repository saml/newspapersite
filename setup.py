# -*- coding: utf-8 -*-

from setuptools import setup

project = 'newspapersite'

setup(
    name=project,
    version='0.1',
    url='https://github.com/saml/newspapersite',
    description='A sample site for newspaper.',
    author='saml',
    packages=['newspapersite'],
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt', 'r').readlines(),
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)

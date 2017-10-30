##############################################################################
#
# Copyright (c) 2009-2012 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os
from setuptools import setup
from setuptools import find_packages


NAME = 'LDAPUserFolder'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(name='Products.%s' % NAME,
      version=read('version.txt').strip(),
      description='A LDAP-enabled Zope 2 user folder',
      long_description=read('README.rst'),
      classifiers=[
        "Development Status :: 6 - Mature",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development",
        "Topic :: System :: Systems Administration ::"
        " Authentication/Directory :: LDAP",
        ],
      keywords='web application server zope zope2 ldap',
      author="Jens Vagelpohl and contributors",
      author_email="jens@dataflake.org",
      url="http://pypi.python.org/pypi/Products.%s" % NAME,
      license="ZPL 2.1 (http://www.zope.org/Resources/License/ZPL-2.1)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      install_requires=[
        'setuptools',
        'six',
        'Zope2 < 4',
        'dataflake.fakeldap < 2',
        'pyldap',
        ],
      extras_require={
          'exportimport': ['Products.GenericSetup >= 1.4.0, < 1.9'],
          },
      entry_points="""
      [zope2.initialize]
      Products.%s = Products.%s:initialize
      """ % (NAME, NAME),
      )

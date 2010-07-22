from setuptools import setup, find_packages
import sys, os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.2'

long_description = (
    read('README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('docs/CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('docs/CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n'
    )

setup(name='collective.transcode.daemon',
      version=version,
      description="Video transcoding daemon",
      long_description=long_description,
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'Intended Audience :: Integrators',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Video :: Conversion',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='video transcoding flv mp4 ogg plone zope twisted',
      author='unweb.me',
      author_email='we@unweb.me',
      url='https://unweb.me',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'pycrypto',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

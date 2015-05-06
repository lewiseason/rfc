from setuptools import setup, find_packages

setup(
  name='rfc',
  version='0.1.0',
  description='View RFCs in the terminal',
  url='https://github.com/lewiseason/rfc',
  author='Lewis Eason',
  author_email='me@lewiseason.co.uk',
  classifiers=[
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
  ],
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'Click',
  ],
  entry_points='''
    [console_scripts]
    rfc=rfc.cli:main
  ''',
)

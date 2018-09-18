from setuptools import find_packages, setup

# Read in the README for the long description on PyPI
def long_description():
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='PyDropbox',
      version='0.1',
      description='Simple Wrapper for Dropbox Python API',
      long_description=long_description(),
      url='https://github.com/j-min/pydropbox',
      author='Jaemin Cho',
      author_email='heythisischo@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)

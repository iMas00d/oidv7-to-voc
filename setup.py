from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(name='oidv7-to-voc',
      version='0.1',
      author='Masood Aslam',
      author_email='masood.aslam85@gmail.com',
      description='Convert Open Images Dataset v7 to PASCAL VOC format.',
      url='https://github.com/iMas00d/oidv7-to-voc',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      install_requires=['Pillow>=6.2.1'],
      entry_points={
          'console_scripts': ['oidv7-to-voc = oidv7_to_voc.__main__:main']
      })

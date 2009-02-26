#!/usr/bin/env python

try:
    from setuptools import setup
    stls=True
except ImportError:
    from distutils.core import setup
    stls=False
    
def get_data_files():
    from glob import glob
    return [e.replace('astropysics/','') for e in  glob('astropysics/data/*')]

setup(name='Astropysics',
      version='0.1',
      description='Astrophysics libraries for Python',
      author='Erik Tollerud',
      author_email='etolleru@uci.edu',
      licence = 'Academic Free License',
      url='http://www.physics.uci.edu/~etolleru/software.html#astropysics',
      requires=['numpy','scipy'],
      provides=['astropysics'],
      long_description="""
      ``astropysics`` contains a variety of utilities and algorithms for processing
      and visualizing astronomical data.
      
      while ``astropysics`` requres only ``numpy`` and ``scipy``, other packages are 
      necessary for some of the functionality.  These include: ``Traits``, ``TraitsGUI``,
      and ``pymc``
      """,
      packages=['astropysics','astropysics.gui'],
      package_data={'astropysics':get_data_files()}
     )
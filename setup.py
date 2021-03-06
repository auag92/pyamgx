import  os
from os.path import join as pjoin
from setuptools import setup, Extension
import subprocess
import numpy

try:
    amgx_dir = os.environ['AMGX_DIR']
except KeyError:
    raise EnvironmentError("AMGX_DIR environment variable not set."
            "Set AMGX_DIR to the "
            "root directory of your AMGX installation.")

from Cython.Build import cythonize
ext = cythonize([
    Extension(
        'pyamgx',
        sources=['pyamgx/pyamgx.pyx'],
        depends=['pyamgx/*.pyx, pyamgx/*.pxi'],
        libraries=['amgxsh'],
        language='c',
        include_dirs = [numpy.get_include(), amgx_dir+'/base/include', amgx_dir+'/core/include'],
        library_dirs = [numpy.get_include(), amgx_dir+'/build'],
        runtime_library_dirs = [numpy.get_include(), amgx_dir+'/build'],
    )])

setup(name='pyamgx',
      author='Ashwin Srinath',
      version='0.1',
      ext_modules = ext,
      zip_safe=False)

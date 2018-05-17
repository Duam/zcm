from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

setup(
    name='zero_cm',
    version='1.0.0',
    url='https://github.com/ZeroCM/zcm',
    license='LGPL',
    packages=find_packages(),
    py_modules='zero_cm',
    ext_modules=cythonize([
        Extension(
            "zero_cm",
            ["zero_cm.pyx"],
            libraries=['zcm']
        )
    ])
)

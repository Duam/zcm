from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

setup(
    name='zerocm',
    version='1.0.0',
    url='https://github.com/ZeroCM/zcm',
    license='LGPL',
    packages=find_packages(),
    py_modules='zerocm',
    ext_modules=cythonize([
        Extension(
            "zerocm",
            ["zerocm.pyx"],
            libraries=['zcm']
        )
    ])
)

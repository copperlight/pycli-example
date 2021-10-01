from setuptools import find_packages, setup

setup(
    name='pycli_example',
    version='1.0',
    description='Minimal example of CLI application packaging for Python.',
    url='https://github.com/copperlight/pycli-example',
    license_files=('LICENSE',),
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ],
    extras_require={
        'test': ['pytest'],
    },
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': ['pycli-example = pycli_example.cmd:main'],
    }
)

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-pySearch',
    version='0.1.0',
    description='A Python package to search on the internet from your code.',
    maintainer='HunerOn',
    maintainer_email='toyoureply@gmail.com',
    author='Huzaifa Asim',
    author_email='huzaifaasim017@outlook.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['python-pySearch'],
    py_modules=['python-pySearch'],
    install_requires=[],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)

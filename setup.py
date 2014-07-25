from setuptools import setup, find_packages
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='stanford-corenlp-python',
    version="1.3.3",
    description="Python wrapper for Stanford University NLP group's Java-based CoreNLP tools",
    long_description=readme,
    author='Dustin Smith',
    author_email='dustin@media.mit.edu',
    url='http://github.com/dasmith/stanford-corenlp-python',
    packages=find_packages(),
    license='GNU General Public License v2 (GPLv2)',
    platforms=["any"],
    py_modules=["corenlp", "client", "jsonrpc"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=["pexpect", "Unidecode", ]
)

#!/usr/bin/env python2.7
import setuptools 
import datetime
import os.path

package_name = "nodejs"
version = datetime.datetime.utcnow().strftime("0.0.dev-%Y-%m-%dT%H%MZ")

setuptools.setup(
    name = package_name,
    version = version,
    
    url = "https://github.com/jeremybanks/node.js.py",
    download_url = "http://pypi.python.org/pypi/{}/{}".format(package_name, version),
    
    description = "A Python bridge to node.js and npm.",
    
    packages = ["nodejs"],
    
    install_requires = ["nodeenv==0.3.5"],
    
    package_dir = {"": "src/"},
    
    long_description = open(os.path.join(os.path.dirname(__file__),
                                         "readme.md")).read(),
    
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    
    author = "Jeremy Banks",
    author_email = "jeremy@jeremybanks.ca"
)

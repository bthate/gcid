# This file is placed in the Public Domain.


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


def uploadlist(dir):
    upl = []
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl


setup(
    name='gcid',
    version='104',
    url='https://github.com/bthate/gcid',
    author='Bart Thate',
    author_email='bthate67@gmail.com', 
    description="Prosecutor. Court. Reonsider OTP-CR-117/19.",
    long_description=read(),
    license='Public Domain',
    packages=["gcid"],
    zip_safe=True,
    include_package_data=True,
    data_files=[
                ("share/gcid", ["gcid.service",]),
                ("share/doc/gcid", uploadlist("docs")),
                ("share/doc/gcid/pdf", uploadlist("docs/pdf")),
                ("share/doc/gcid/_static", uploadlist("docs/_static")),
                ("share/doc/gcid/_templates", uploadlist("docs/_templates")),
               ],
    scripts=["bin/gcid", "bin/gcidcmd", "bin/gcidctl", "bin/gcidd"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)

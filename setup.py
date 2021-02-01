from setuptools import setup

setup(
    name='g3read',
    version='1.0',
    description='Read Gadget2/3 snapshots, large simulations and catalogues',
    url='https://aragagnin.github.io',
    author='Antonio Ragagnin',
    author_email='antonio.ragagnin@inaf.it',
    license='GPLv3+',
    #packages=['g3read'],
    #package_dir={'g3read': '.'},
    data_files = [('', ['g3read.py','g3matcha.py'])], 
    zip_safe=False
)




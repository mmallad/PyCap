from distutils.core import setup, Extension
setup(name='PyCap',version='1.0',author='Dipak Malla',author_email='dpakmalla@gmail.com',description='Python Extended Module in c to capture packets.',ext_modules=[Extension('PyCap',['pycapmodule.c'],libraries=['pcap'])])

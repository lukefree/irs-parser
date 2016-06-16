from distutils.core import setup
import py2exe

setup(console=["C:\Users\kli1\PycharmProjects\irs-parser\irsparser.py"],options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}})

setup(windows=[{"script" : "C:\Users\kli1\PycharmProjects\irs-parser\irsparser.py"}], options={"py2exe" : {"includes" : ["sip"]} {"dll_excludes":["MSVCP90.dll"]}})
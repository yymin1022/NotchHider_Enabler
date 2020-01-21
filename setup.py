from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages=["subprocess"], excludes=[], include_files=["bin"])

exe = [Executable("main.py")]

setup(
    name='Notch Hider',
    version='1.0',
    author="yymin1022",
    description="Hello, World!",
    options=dict(build_exe=buildOptions),
    executables=exe
)
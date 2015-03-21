import sys
from cx_Freeze import setup, Executable
sys.argv.append("build")

setup(
    name = "BotASM Interpreter",
    version = "0.4",
    description = "Interprets BotASM code.",
    executables = [Executable("botASM.py", base = None)])

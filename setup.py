from cx_Freeze import setup, Executable

base = None

executables = [Executable("fatura.py", base=base)]

packages = ["idna", "math", "random" ,"os", "tkinter"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Fatura",
    options = options,
    version = "1.0.0",
    description = 'Faturimi',
    executables = executables
)
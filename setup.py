import cx_Freeze

executables = [cx_Freeze.Executable('Cipher.py')]

cx_Freeze.setup(
    name='Transposition Cipher',
    options={"build_exe": {"packages":["os"], "include_files":["about.txt", "helpfile.txt"]}},

    description="Transposition Cipher",
    executables = executables
    )

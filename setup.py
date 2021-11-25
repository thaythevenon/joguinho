import cx_Freeze

executables = [cx_Freeze.Executable(
    script="jogo.py", icon="jogo/ironIcon.png")]

cx_Freeze.setup(
    name="Sponge Bob",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["jogo"]
                           }},
    executables=executables
)
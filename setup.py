from cx_Freeze import setup, Executable,sys


includefiles=['icon.ico']
excludes=[]
packages=[]
base=None

if sys.platform=="win32":
    base="win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Cafe Billing System",
     "TARGETDIR",
     "[TARGETDIR]\main.py",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut": shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version='0.1',
    description="Cafe Billing System",
    author="Sahil Lokhande",
    name="Cafe Billing Application",
    options={'bulid_exe':{'include_files':includefiles}, 'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico'
        )
    ]
)
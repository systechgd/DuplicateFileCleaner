import sys
from cx_Freeze import setup, Executable

# Define the application name and version
app_name = "FileCleaner"
app_version = "1.0"

# Define the base; this suppresses the console window
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Specify the main Python script
script = "duplicate-finder.py"  # Replace with your script filename

# Define additional options
build_exe_options = {
    "packages": ["os", "hashlib", "tkinter"],  # Include all required packages
    "include_files": ["assets/filecleaner.ico"],  # Include your icon file
}


# Define the executable configuration
executables = [
    Executable(script, base=base, icon="assets/filecleaner.ico", target_name="FileCleaner.exe")
]

# Setup script for building the installer
setup(
    name=app_name,
    version=app_version,
    description="File Cleaner Application",
    options={"build_exe": build_exe_options},
    executables=executables,
)

Vivaldi Workspace Desktop Mover
==================

Finds all open Vivaldi browser windows and moves them to Windows Virtual Desktops based on their workspace.

Why Use This?
-------------

If you are using virtual desktops then it often makes sense to have vivaldi windows open in many of them at the same time.

However whenever vivaldi closes they often don't reopen in the correct desktops, all opening in the current desktop instead e.g. after a crash.

Instead of having to manually go through each window and figure out which desktop to move it to, you can use this tool and the built in workspace feature of vivaldi to automate the process!

It can also be used to create new desktops as you create new workspace windows.

Important Information
---------------------

- This tool only moves windows open on the current desktop - so be sure to run it where all your vivaldi windows are!
  
- By defualt this tool will look for virtual desktops with the same name as the window's workspace, and will create new virtual desktops if it cant find a match - if you wish to change this see the [command-line arguments section](#command-line-arguments).

Installation and Usage
----------------------

### Executable
1. Go to the latest release : https://github.com/DavidGBrett/vivaldi-workspace-desktop-mover/releases/latest
2. Download the `.exe` file, e.g. `VivaldiWorkspaceDesktop-v1.0.1.exe`
3. Go to the virtual desktop which has the unsorted vivaldi windows.
4. Double click on the exe or launch it from the terminal.

### Pip Install from PyPI
1. Install using pip: 
    ```bash
    pip install vivaldi-workspace-desktop-mover
    ```
2. Run as a module: 
    ```bash
    python -m vivaldi_workspace_desktop_mover
    ```

### Python Wheel
1. Go to the latest release : https://github.com/DavidGBrett/vivaldi-workspace-desktop-mover/releases/latest
2. Download the `.whl` file e.g. `vivaldi_workspace_desktop_mover-1.0.0-py3-none-any.whl`
3. Install the wheel:
     ```
     pip install C:\path\to\vivaldi_workspace_desktop_mover‑X.Y.Z‑py3-none-any.whl
     ```
4. Run as a module:
     ```
     python -m vivaldi_workspace_desktop_mover
     ```

Command-line Arguments
----------------------

This project exposes two CLI options:

- --no-create
  - Prevents creation of new virtual desktops. By default the tool will create missing desktops as needed; use this flag to disable that behavior.

- --mapping-file <path>
  - Path to a JSON file that defines workspace -> desktop mappings.
  - The file must contain a JSON object (dictionary). Example:
    ```json
    {
      "Work": "Job",
      "Personal": "Other",
      "Research": "Other"
    }
    ```

Notes & troubleshooting
-----------------------

- Windows Defender/SmartScreen blocks the .exe:
Since this is an unsigned executable, Windows may prevent running it. Click "More info" and then "Run anyway".

- If double‑clicking the exe appears to do nothing, run it from PowerShell or cmd to see error messages and other information.

- The mapping file must be valid JSON and must be a top-level object; the tool will exit with an error if the file is missing or malformed.

License
-------
MIT - See LICENSE file for details.
import pywintypes
from dataclasses import dataclass
import time
from typing import Optional
import uiautomation as uia

class NotVivaldiWindowError(Exception):
    """Raised when an attempt is made to parse a Vivaldi window given a non-Vivaldi window."""

class CannotParseVivaldiWindow(Exception):
    """Failed to correctly parse the sturcture of the vivaldi window."""

@dataclass
class VivaldiWindowInfo:
    window_handle:int
    window_name:str
    workspace_name: Optional[str]

    @property
    def has_workspace(self) -> bool:
        return self.workspace_name is not None

def parse_vivaldi_window(window: uia.Control, retries=3) -> VivaldiWindowInfo:
    for _ in range(retries):
        try:
            return _parse_vivaldi_window_once(window)
        except pywintypes.com_error:
            time.sleep(0.1)
    raise CannotParseVivaldiWindow

def _parse_vivaldi_window_once(window: uia.Control) -> VivaldiWindowInfo:

    if window.ClassName != 'Chrome_WidgetWin_1' or not window.Name.endswith("- Vivaldi"):
        raise NotVivaldiWindowError(f"Not a Vivaldi window: {window.Name}")

    window_handle=window.NativeWindowHandle
    window_name = window.Name

    # Find the workspace button using the accessibility api
    # Tabs -> Tab Bar -> Group -> Button "Workspaces"
    workspace_button = \
        window.ToolBarControl(Name="Tabs")\
        .ToolBarControl(Name="Tab Bar") \
        .GroupControl(Name="") \
        .ButtonControl(Name="Workspaces")
    

    # if we cant find the workspace button, the window might not yet have loaded
    if not workspace_button.Exists(1):
        # we can set the focus to the window to encourage it to load and then try again
        window.SetFocus()
        if not workspace_button.Exists(2):
            raise CannotParseVivaldiWindow

    # if has the defualt "Workspaces" label then this window doesn't have a workspace
    if workspace_button.HelpText == "Workspaces":
        workspace_name = None
    else:
        workspace_name = workspace_button.HelpText
    
    return VivaldiWindowInfo(
        window_handle=window_handle,
        window_name=window_name,
        workspace_name=workspace_name
    )

def get_all_vivaldi_windows(ignore_failed_parses=False) -> list[VivaldiWindowInfo]:

    windows = []

    for w in uia.GetRootControl().GetChildren():
        try:
            windows.append(
                parse_vivaldi_window(w)
            )
        except NotVivaldiWindowError:
            continue
        except CannotParseVivaldiWindow:
            print(f"Failed to parse window '{w.Name}'!")
            if not ignore_failed_parses:
                raise CannotParseVivaldiWindow

    return windows

if __name__ == "__main__":

    for window in get_all_vivaldi_windows():
        print(window.workspace_name)

    
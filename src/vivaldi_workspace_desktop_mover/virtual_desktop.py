from typing import Optional
from pyvda import get_virtual_desktops, VirtualDesktop, AppView

def create_desktop(name: Optional[str] = None) -> VirtualDesktop:
    """Create a new virtual desktop, and optionally give it a name.

    Args:
        name: The name for this new desktop.

    Raises:
        NotImplementedError: If the Windows version is < 19041 and a name is given.

    Returns:
        VirtualDesktop: The created desktop
    """
    new_desktop = VirtualDesktop.create()

    if name:
        new_desktop.rename(name=name)

    return new_desktop

def get_desktop_by_name(name:str) -> Optional[VirtualDesktop]:
    for desktop in get_virtual_desktops():
        if desktop.name == name:
            return desktop


def move_window_to_desktop(window_handle:int, desktop:VirtualDesktop):
    app = AppView(window_handle)
    app.move(desktop)
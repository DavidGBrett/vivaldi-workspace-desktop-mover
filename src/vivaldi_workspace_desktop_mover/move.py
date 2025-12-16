
from .config import Config
from .virtual_desktop import move_window_to_desktop, get_desktop_by_name, create_desktop
from .vivaldi_window import get_all_vivaldi_windows

def move_vivaldi_windows(config: Config):

    vivaldi_windows = get_all_vivaldi_windows(ignore_failed_parses=True)

    succesful_moves = 0

    for window in vivaldi_windows:
        print(f"\nHandling window '{window.window_name}'")

        if not window.has_workspace:
            print(f"Window has no workspace!")
            continue
        assert(window.workspace_name != None)

        if config.workspace_to_desktop:
            target_desktop_name = config.workspace_to_desktop(window.workspace_name)

        elif window.window_name in config.mapping:
            target_desktop_name = config.mapping[window.workspace_name]
        
        else:
            target_desktop_name = window.workspace_name
            
        target_desktop = get_desktop_by_name(target_desktop_name)
        if target_desktop == None:
            try:
                target_desktop = create_desktop(name=target_desktop_name)
            except NotImplementedError:
                print(f"Mapped virtual desktop {target_desktop_name} is missing and cannot be created programmtically on this version of Windows!")
                continue

        move_window_to_desktop(window.window_handle,target_desktop)
        print(f"Moved window to desktop '{target_desktop_name}'.")
        succesful_moves += 1

    print("\n"+"-"*10)
    print(f"Succesfully moved {succesful_moves} out of {len(vivaldi_windows)} found vivaldi windows.")
            

if __name__ == "__main__":
    move_vivaldi_windows(config=Config())
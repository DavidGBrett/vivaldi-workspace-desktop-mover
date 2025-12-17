
from .config import Config
from .virtual_desktop import move_window_to_desktop, get_desktop_by_name, create_desktop
from .vivaldi_window import get_all_vivaldi_windows

def move_vivaldi_windows(config: Config):

    # Get all vivaldi windows, skipping over those that a parsing error
    vivaldi_windows = get_all_vivaldi_windows(ignore_failed_parses=True)

    succesful_moves = 0

    for window in vivaldi_windows:
        print(f"\nHandling window '{window.window_name}'")

        if not window.has_workspace:
            print(f"Window has no workspace!")
            continue
        assert(window.workspace_name != None)

        # Get name of mapped desktop
        if config.workspace_to_desktop:
            target_desktop_name = config.workspace_to_desktop(window.workspace_name)

        elif window.window_name in config.mapping:
            target_desktop_name = config.mapping[window.workspace_name]
        
        else:
            target_desktop_name = window.workspace_name
        
        # Attempt to find the mapped desktop
        target_desktop = get_desktop_by_name(target_desktop_name)

        # See if we can and should create a new desktop if it is missing
        if target_desktop == None:
            if config.create_missing_desktops == False:
                print(f"Mapped virtual desktop {target_desktop_name} is missing, and configuration is set to not create new virtual desktops.")
                continue

            try:
                target_desktop = create_desktop(name=target_desktop_name)
            except NotImplementedError:
                print(f"Mapped virtual desktop {target_desktop_name} is missing and cannot be created programmtically on this version of Windows!")
                continue
        
        # If all went well - move the window to its mapped virtual desktop
        move_window_to_desktop(window.window_handle,target_desktop)
        print(f"Moved window to desktop '{target_desktop_name}'.")

        # count how many of these windows we successfully moved to their mapped desktop
        succesful_moves += 1

    print("\n"+"-"*10)
    print(f"Succesfully moved {succesful_moves} out of {len(vivaldi_windows)} found vivaldi windows.")
            

if __name__ == "__main__":
    move_vivaldi_windows(config=Config())
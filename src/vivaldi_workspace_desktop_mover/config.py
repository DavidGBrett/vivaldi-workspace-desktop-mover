from dataclasses import dataclass, field
from typing import Callable, Optional, Dict

@dataclass
class Config:
    create_missing_desktops: bool = True
    
    # mappings: workspace -> desktop
    # Falls back tp direct 1:1 mapping by name, if workspace not in mapping
    mapping: Dict[str, str] = field(default_factory=dict)  

    # Provide hook: user may supply a function like:
    #    lambda w: "Work" if "Coding" in w else "Misc"
    workspace_to_desktop: Optional[Callable[[str], str]] = None
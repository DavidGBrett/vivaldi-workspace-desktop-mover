import argparse
import json
from pathlib import Path
import sys
from .config import Config
from .move import move_vivaldi_windows

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Move Vivaldi browser windows to Windows virtual desktops "
            "based on their workspace name."
        )
    )

    parser.add_argument("--no-create", action="store_true",
        help="Do not create new virtual desktops")
    
    parser.add_argument("--mapping-file", type=str,
        help="Optional JSON file defining workspace→desktop mappings")

    args = parser.parse_args()

    mapping = {}
    if args.mapping_file:
        p = Path(args.mapping_file)
        if not p.exists():
            print(f"Mapping file not found: {p}", file=sys.stderr)
            sys.exit(2)
        try:
            with p.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            print(f"Failed to read/parse mapping file: {exc}", file=sys.stderr)
            sys.exit(2)

        if not isinstance(data, dict):
            print("Mapping file must contain a JSON object (mapping).", file=sys.stderr)
            sys.exit(2)
        mapping = data
        
    cfg = Config(
        create_missing_desktops = not args.no_create,
        mapping = mapping
    )

    try:
        move_vivaldi_windows(cfg)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)    

if __name__ == "__main__":
    main()

import yaml
from yaml.loader import SafeLoader
from pathlib import Path
import sys

#  from this project
from ui import menu


def main():
    """read in the user supplied yaml data then call the ui object"""

    try:
        filename = sys.argv[1]
    except:
        filename = "default.yml"
    print(filename)

    p = Path(__file__).with_name(filename)

    with p.open("r") as f:
        data = yaml.load(f, Loader=SafeLoader)
    ui = menu(data)


if __name__ == "__main__":
    main()
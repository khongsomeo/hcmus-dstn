"""Utilities for the program

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

import json
import csv
from typing import Dict, List, Tuple
from pathlib import Path
import yaml

# Terminal colors
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def load_config(filename: str) -> Dict[str, str]:
    """Load config from supported config type (.json/.yaml)

    Args:
        filename (str): path to the config file.

    Returns:
        Dict[str, str]: config loaded in Dictionary.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    # Initialize
    config = {}

    # Get config extension for correct parsing.
    config_extension = Path(filename).suffix

    with open(filename, "r+", encoding="utf8") as config_handler:
        # Load JSON config.
        if config_extension == ".json":
            config = json.load(config_handler)

        # Load YAML config.
        elif config_extension in [".yaml", ".yml"]:
            config = yaml.safe_load(config_handler)

    return config


def load_csv(filename: str) -> List[Tuple[str, str]]:
    """Load a CSV file of two columns into a list.

    Args:
        filename (str): path to the csv file.

    Returns:
        List[Tuple[str, str]]: List of tuples - each element as a row in the csv file.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    item_list = []

    # Extract item list from file.
    with open(filename, "r+", encoding="utf8") as csv_handler:
        reader = csv.reader(csv_handler)

        for row in reader:
            if len(row) > 0:
                item_list.append(tuple(row))

    return item_list

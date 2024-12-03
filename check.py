"""A CLI for those who don't want to use official HCMUS graduate information lookup website.
"""

import json
import csv
from argparse import ArgumentParser
from pathlib import Path
import yaml
from src.dstn import DSTNSingleRequest, DSTNListRequest


def main():
    """Main function

    Author:
        - Quan H. Tran <quan@trhgquan.xyz>
        - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    parser = ArgumentParser()
    parser.add_argument("--config", default="configs/config.json",
                        help="Config file (config.json/config.yaml)")

    sub_parsers = parser.add_subparsers(dest="mode", required=True)

    # Single mode
    single = sub_parsers.add_parser("single")
    single.add_argument("--student_name", default=None,
                        help="Student Fullname (in Vietnamese or your Student ID)")
    single.add_argument("--degree_id", default=None,
                        help="Degree ID no.")
    single.add_argument("--language", default="vn", help="Language (en/vn)")

    # Multiple mode
    multiple = sub_parsers.add_parser("multiple")
    multiple.add_argument("--file", default=None,
                          help="Path to the .csv file to check")

    args = parser.parse_args()

    # Load config (with multiple extensions)
    config_extension = Path(args.config).suffix

    # Initialize a new config.
    config = dict()

    with open(args.config, "r+", encoding="utf8") as config_handler:
        # JSON format
        if config_extension == ".json":
            config = json.load(config_handler)

        # YAML format
        elif config_extension == ".yaml":
            config = yaml.load(config_handler, Loader=yaml.SafeLoader)

    # Single mode
    if args.mode == "single":
        # Add student info to parameters
        config.update({
            "student_name": args.student_name,
            "degree_id": args.degree_id,
            "language": args.language
        })

        req = DSTNSingleRequest(**config)

        req.process()

    # Multiple mode
    elif args.mode == "multiple":
        student_list = []

        # Extract student list from file.
        with open(args.file, "r+", encoding="utf8") as csv_handler:
            reader = csv.reader(csv_handler)

            for row in reader:
                if len(row) > 0:
                    student_list.append(tuple(row))

        # Add student list to list of parameters
        config["student_list"] = student_list

        req = DSTNListRequest(**config)

        req.process()


if __name__ == "__main__":
    main()

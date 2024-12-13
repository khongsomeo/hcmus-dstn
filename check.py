"""A CLI for those who don't want to use official HCMUS graduate information lookup website.

Author:
    - Me A. Doge <domyeukemphancam@trhgquan.xyz>
    - Quan H. Tran <quan@trhgquan.xyz>
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

import json
import csv
from argparse import ArgumentParser
from pathlib import Path
from typing import Dict
import yaml
from src.dstn import DSTNSingleRequest, DSTNListRequest


def handle_single_request(config: Dict[str, str], args: Dict[str, str]) -> None:
    """Handling single request

    Args:
        config (dict): config dictionary - retrieved from json/yaml
        args (dict): args get from argparse

    Author:
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    # Add student info to parameters
    config.update({
        "student_name": args.student_name,
        "degree_id": args.degree_id,
        "language": args.language
    })

    req = DSTNSingleRequest(**config)

    record_list = req.process()

    # Print record to file (if required from arguments)
    if args.output_file is not None:
        with open(args.output_file, "w+", encoding="utf8") as output_handler:
            for record in record_list:
                print(record, file=output_handler)

        print(f"Results has been written to {args.output_file}")

    else:
        for record in record_list:
            print(record)


def handle_multiple_request(config: Dict[str, str], args: Dict[str, str]) -> None:
    """Handling multiple check request

    Args:
        config (dict): config dictionary - retrieved from json/yaml
        args (dict): args get from argparse

    Author:
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

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

    record_list = req.process()

    # Print result to csv file.
    if args.output_file is None:
        for record in record_list:
            print(" - ".join(record))

    else:
        with open(args.output_file, "w+", encoding="utf8") as output_handler:
            output_writer = csv.writer(output_handler)
            output_writer.writerow(["Name", "Degree ID", "Status"])
            output_writer.writerows(record_list)

        print(f"Status has been written to {args.output_file}")


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
    parser.add_argument("--output_file", default=None,
                        help="Path to output file (printing to screen by default)")

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
    config = {}

    with open(args.config, "r+", encoding="utf8") as config_handler:
        # JSON format
        if config_extension == ".json":
            config = json.load(config_handler)

        # YAML format
        elif config_extension == ".yaml":
            config = yaml.load(config_handler, Loader=yaml.SafeLoader)

    # Single mode
    if args.mode == "single":
        handle_single_request(config, args)

    # Multiple mode
    elif args.mode == "multiple":
        handle_multiple_request(config, args)


if __name__ == "__main__":
    main()

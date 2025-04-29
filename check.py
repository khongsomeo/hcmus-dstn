"""A CLI for those who don't want to use official HCMUS graduate information lookup website.

Author(s):
    - Me A. Doge <domyeukemphancam@trhgquan.xyz>
    - Quan H. Tran <quan@trhgquan.xyz>
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

import csv
from argparse import ArgumentParser
from typing import Dict
from src.dstn import DSTNSingleRequest, DSTNListRequest
from src.utils import load_config, load_csv, color


def handle_single_request(config: Dict[str, str], args: Dict[str, str]) -> None:
    """Handling single request

    Args:
        config (Dict[str, str]): config dictionary - retrieved from json/yaml
        args (Dict[str, str]): args get from argparse

    Author(s):
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
        config (Dict[str, str]): config dictionary - retrieved from json/yaml
        args (Dict[str, str]): args get from argparse

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    student_list = load_csv(args.file)

    # Add student list to list of parameters
    config["student_list"] = student_list

    req = DSTNListRequest(**config)

    record_list = req.process()

    # Print result to csv file.
    if args.output_file is None:
        for record in record_list:
            record_dict = record.asdict()
            if record_dict["status"]:
                print(f"{color.OKGREEN}\u2714 {record_dict['name']}/{record_dict['degree_id']} - VALID{color.ENDC}")
                
            else:
                print(f"{color.FAIL}\u2718 {record_dict['name']}/{record_dict['degree_id']} - INVALID{color.ENDC}")

    else:
        with open(args.output_file, "w+", encoding="utf8") as output_handler:
            print("Name,Degree ID,Status", file=output_handler)
            for record in record_list:
                print(record, file=output_handler)

        print(f"Status has been written to {args.output_file}")


def main():
    """Main function

    Author(s):
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

    # Load config from file.
    config = load_config(args.config)

    # Single mode
    if args.mode == "single":
        handle_single_request(config, args)

    # Multiple mode
    elif args.mode == "multiple":
        handle_multiple_request(config, args)


if __name__ == "__main__":
    main()

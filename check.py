from argparse import ArgumentParser
from src.dstn import DSTNSingleRequest, DSTNListRequest
from pathlib import Path
import json
import yaml
import csv


def main():
    parser = ArgumentParser()
    parser.add_argument("--config", default="configs/config.json",
                        help="Config file (config.json/config.yaml)")

    sub_parsers = parser.add_subparsers(dest="mode", required=True)

    # Single mode
    single = sub_parsers.add_parser("single")
    single.add_argument("--student_name", default=None,
                        help="Student Name (Vietnamese with/without diacritics; upper/lowercased; or just use your Student ID)")
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
    with open(args.config, "r+", encoding="utf8") as f:
        # JSON format
        if config_extension == ".json":
            config = json.load(f)

        # YAML format
        elif config_extension == ".yaml":
            config = yaml.load(f, Loader=yaml.SafeLoader)

    # Single mode
    if args.mode == "single":
        student_name = args.student_name
        degree_id = args.degree_id
        language = args.language

        req = DSTNSingleRequest(
            base_url=config["api_url"],
            results=config["results"],
            headers=config["headers"],
            student_name=student_name,
            degree_id=degree_id,
            language=language
        )

        req.process()

    # Multiple mode
    elif args.mode == "multiple":
        student_list = []

        with open(args.file, "r+", encoding="utf8") as f:
            reader = csv.reader(f)

            for row in reader:
                if (len(row) > 0):
                    student_list.append(tuple(row))

        req = DSTNListRequest(
            base_url=config["api_url"],
            results=config["results"],
            headers=config["headers"],
            student_list=student_list
        )

        req.process()


if __name__ == "__main__":
    main()

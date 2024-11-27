from argparse import ArgumentParser
from dstn import DSTNRequest
import json


def main():
    parser = ArgumentParser()
    parser.add_argument("--config", default="config.json",
                        help="Config file (config.json)")
    parser.add_argument("--student_name", default=None, help="Student Name (Tiếng Việt có dấu/không dấu, hoa/thường đều được)")
    parser.add_argument("--degree_id", default=None,
                        help="Degree ID no.")
    parser.add_argument("--language", default="vn", help="Language (en/vn)")

    args = parser.parse_args()

    with open(args.config, "r+", encoding="utf8") as f:
        config = json.load(f)

    student_name = args.student_name
    degree_id = args.degree_id
    language = args.language

    req = DSTNRequest(
        base_url=config["api_url"],
        results=config["results"],
        headers=config["headers"],
        student_name=student_name,
        degree_id=degree_id,
        language=language
    )

    req.get()


if __name__ == "__main__":
    main()

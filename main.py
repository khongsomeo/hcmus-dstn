from argparse import ArgumentParser
from dstn import DSTNRequest
import json

def main():
    parser = ArgumentParser()
    parser.add_argument("--config", default="config.json", help="Config file (config.json)")
    parser.add_argument("--student_id", default=None, help="Student ID")
    parser.add_argument("--birthday", default=None, help="Student birthday (dd/MM/YYY)")

    args = parser.parse_args()


    with open(args.config, "r+", encoding="utf8") as f:
        config = json.load(f)
    student_id = args.student_id
    birthday = args.birthday

    req = DSTNRequest(
        base_url=config["api_url"],
        rows=config["rows"],
        page=config["page"],
        sord=config["sord"],
        student_id=student_id,
        birthday=birthday
    )

    req.get()

if __name__ == "__main__":
    main()

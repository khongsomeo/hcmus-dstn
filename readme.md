# HCMUS - DSTN

Graduate information lookup CLI - for those who don't want to use the official HCMUS graduate information lookup website.

[Official HCMUS graduate information lookup website](https://pdt.hcmus.edu.vn/dstn)

## Usage

### Installation

#### Manually - Install required packages

```bash
pip install -r requirements.txt
```

#### Docker image

```bash
docker pull <ghcr link - not available>
```

### Check for a single degree

Usage:

```bash
usage: check.py single [-h] [--student_name STUDENT_NAME] [--degree_id DEGREE_ID] [--language LANGUAGE]

optional arguments:
  -h, --help            show this help message and exit
  --student_name STUDENT_NAME
                        Student Name (Vietnamese with/without diacritics; upper/lowercased; or just use your Student ID)
  --degree_id DEGREE_ID
                        Degree ID no.
  --language LANGUAGE   Language (en/vn)
```

Examples:

```bash
# Python
python check.py single --student_name "nguyen van a" --degree_id "QH123456"
```

```bash
# Docker image
docker run khongsomeo/dstn single --student_name "nguyen van a" --degree_id "QH123456"
```

### Check for multiple degrees

Usage:

```bash
usage: check.py multiple [-h] [--file FILE]

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  Path to the .csv file to check
```

The `.csv` file must follow this format:

```text
name1,degreeid1
name2,degreeid2
...
```

Examples:

```bash
# Python
python check.py multiple --file check.csv
```

```bash
# Docker image
docker run khongsomeo/dstn multiple --file check.csv
```

## Configurations

Configurations can be found in `configs/config.json` and `configs/config.yaml`. By default, the program will use configs from `config.json` (though they have the same content).

`configs/config.json`:

```json
{
    "api_url": "https://example.com/dstn/api", // Official school API
    "headers": {
      "User-Agent": ... // Do not edit the User-Agent
    },
    "results": {
      "rows": 10,                              // Max of results per row
      "page": 1,                               // Show results per page.
      "sord": "desc"                           // Sorting order
    }
}
```

`configs/config.yaml`:

```yml
api_url: https://example.com/dstn/api
headers:
    User-Agent: ... # Do not edit the User-Agent
results:
    rows: 10
    page: 1
    sord: desc
```

## LICENSE

This project is licensed under [THE GNU GPL v3](LICENSE)

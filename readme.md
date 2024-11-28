# HCMUS - DSTN

Graduate information lookup, using official HCMUS API.

[Official HCMUS graduate information lookup website](https://pdt.hcmus.edu.vn/dstn)

## Usage

### Install required packages

```bash
pip install -r requirements.txt
```

### Check for a single degree

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

### Check for multiple degrees

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

## Configurations

Configurations can be found in `config.json`:

```json
{
    "api_url": "https://example.com/dstn/api", // Official school API
    // ... do not edit the User-Agent
    "results": {
      "rows": 10,                              // Max of results per row
      "page": 1,                               // Show results per page.
      "sord": "desc"                           // Sorting order
    }
}
```

## LICENSE

This project is licensed under [THE GNU GPL v3](LICENSE)

# HCMUS - DSTN

Graduate information lookup, using official HCMUS API.

Official HCMUS website: https://pdt.hcmus.edu.vn/dstn

## Usage

1. Install required packages.

```
pip install -r requirements.txt
```

2. Running `main.py` with required arguments.

```python
λ python main.py --h
usage: main.py [-h] [--config CONFIG] [--student_id STUDENT_ID] [--degree_id DEGREE_ID] [--language LANGUAGE]

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Config file (config.json)
  --student_id STUDENT_ID
                        Student Name or Student ID
  --degree_id DEGREE_ID
                        Degree ID no.
  --language LANGUAGE   Language (en/vn)
```

## Configurations

Configurations can be found in `config.json`:

```json
{
    "api_url": "https://example.com/dstn/api", // Official school API
    "rows": 10,                                // Max of results per row
    "page": 1,                                 // Show results per page.
    "sord": "desc"                             // Sorting order
}
```

## LICENSE

This project is licensed under [THE GNU GPL v3](LICENSE)
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
λ python main.py -h
usage: main.py [-h] [--config CONFIG] [--student_id STUDENT_ID]
               [--birthday BIRTHDAY]

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Config file (config.json)
  --student_id STUDENT_ID
                        Student ID
  --birthday BIRTHDAY   Student birthday (dd/MM/YYY) 
```

## LICENSE

This project is licensed under [THE GNU GPL v3](LICENSE)
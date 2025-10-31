# logsteplib

- [Description](#package-description)
- [Usage](#usage)
- [Installation](#installation)
- [Docstring](#docstring)
- [License](#license)

## Package Description

Package containing a standard format for the logging module.

## Usage

From a script:

```python
# Log stuff
from logsteplib.std import LogStep

logger = LogStep(name="my_process").logger
logger.info(msg="Something to log!")
```

```python
# Create metadata
from logsteplib.dq import DQMetadata

metadata = DQMetadata(
    target="my_folder",
    key="customer_20251031",
    input_file_name="raw_customers.csv",
    file_name="clean_customers.csv",
    user_name="Parker, Peter",
    user_email="peter.parker@example.com",
    modify_date="2025-10-31",
    file_size="204800",
    file_row_count="15000",
    status="SUCCESS",
    rejection_reason=None,
    file_web_url="https://lakehouse.company.com/files/clean_customers.parquet"
)
```


## Installation

Install python and pip if you have not already.

Then run:

```bash
pip install pip --upgrade
```

For production:

```bash
pip install logsteplib
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:

```bash
git clone https://github.com/aghuttun/logsteplib.git
cd logsteplib
pip install -e ".[dev]"
```

## Docstring

The script's docstrings follow the numpydoc style.

## License

BSD License (see license file)

[top](#logsteplib)

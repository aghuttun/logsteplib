# logsteplib

- [Description](#package-description)
- [Usage](#usage)
- [Installation](#installation)
- [Docstring](#docstring)
- [License](#license)

## Package Description

Package containing a standard format for the logging module.

## Usage

### Generic Console Logs

From a script:

```python
# Initialise a logger for the process and log an informational message
from logsteplib.std import LogStep

logger = LogStep(name="my_process").logger

logger.info(msg="Something to log!")
```

### Lakehouse DQ Logs

From a SQL script:

```sql
-- Create the Delta lakehouse table for tracking SharePoint file uploads
-- Includes metadata such as file details, user info, and processing status
-- Table: workspace.default.sharepoint_uploader_monitoring_logs
DROP TABLE IF EXISTS workspace.default.sharepoint_uploader_monitoring_logs;
CREATE TABLE workspace.default.sharepoint_uploader_monitoring_logs (
  target STRING,
  key STRING,
  input_file_name STRING,
  file_name STRING,
  user_name STRING,
  user_email STRING,
  modify_date STRING,     -- Should be timestamp
  file_size STRING,       -- Should be INT
  file_row_count STRING,  -- Should be INT
  status STRING,
  rejection_reason STRING,
  file_web_url STRING
)
USING DELTA;
```

From a Python script:

```python
from logsteplib.dq import DQStatusCode

print(DQStatusCode.get_description("SchemaMismatch"))  # DQ FAIL: SCHEMA MISMATCH
print(DQStatusCode.get_description("UnknownCode"))     # UNKNOWN STATUS CODE
```

Status Code Table

| Code                       | Description                             |
| -------------------------- | --------------------------------------- |
| NA                         | NOT APPLICABLE                          |
| EmptyFile                  | DQ FAIL: EMPTY FILE                     |
| SchemaMismatch             | DQ FAIL: SCHEMA MISMATCH                |
| SchemaMismatchAndEmptyFile | DQ FAIL: SCHEMA MISMATCH AND EMPTY FILE |
| InvalidNumericFormat       | DQ FAIL: INVALID NUMERIC FORMAT         |
| InvalidDateFormat          | DQ FAIL: INVALID DATE FORMAT            |

```python
# Create a DQMetadata instance containing metadata about a processed file
# This metadata can be used for logging, auditing, or writing to a lakehouse table
from logsteplib.dq import DQMetadata

metadata = DQMetadata(
    target="my_folder/my_system",
    key="customer_20251031",
    input_file_name="raw_customers.csv",
    file_name="clean_customers.csv",
    user_name="Parker, Peter",
    user_email="peter.parker@example.com",
    modify_date="2025-11-02",
    file_size="204800",
    file_row_count="15000",
    status="FAIL",
    rejection_reason=DQStatusCode.get_description("SchemaMismatch"),
    file_web_url="https://lakehouse.company.com/files/clean_customers.parquet"
)
```

```python
# Write the metadata (DQMetadata) to the lakehouse monitoring table
from logsteplib.dq import DQWriter

monitoring_table = "workspace.default.sharepoint_uploader_monitoring_logs"
dq_writer = DQWriter(table_name=monitoring_table)

dq_writer.write_metadata(metadata=metadata)
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

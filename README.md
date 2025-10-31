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
# Initialise a logger for the process and log an informational message
from logsteplib.std import LogStep

logger = LogStep(name="my_process").logger

logger.info(msg="Something to log!")
```

```python
# Create a DQMetadata instance containing metadata about a processed file
# This metadata can be used for logging, auditing, or writing to a lakehouse table
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

```sql
-- Create the Delta lakehouse table for tracking SharePoint file uploads
-- Includes metadata such as file details, user info, and processing status
-- Table: workspace.default.sharepoint_uploader_monitoring_logs
CREATE TABLE IF NOT EXISTS workspace.default.sharepoint_uploader_monitoring_logs (
  target STRING,
  key STRING,
  input_file_name STRING,
  file_name STRING,
  user_name STRING,
  user_email STRING,
  modify_date STRING,
  file_size STRING,  -- Should be INT
  file_row_count STRING,  -- Should be INT
  status STRING,
  rejection_reason STRING,
  file_web_url STRING
)
USING DELTA;
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

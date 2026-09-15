# AEB Trigger Detection

This project reads vehicle sensor data, computes the time-to-collision (TTC), and flags when an automatic emergency braking (AEB) trigger should occur.

## Overview

The workflow is:

1. Read the CSV input file from `data/vehicle_sensor_data.csv`
2. Parse `speed` and `obstacle_distance` values from each row
3. Calculate TTC using the stationary-obstacle formula
4. Trigger an AEB event when TTC is below 2.0 seconds
5. Write the processed rows to `output/output.csv`

## Files

- `main.py` — entry point for the detection workflow
- `aeb_logic.py` — TTC and AEB decision logic
- `csv_handler.py` — CSV read/write helpers
- `config.py` — input/output file paths
- `data/vehicle_sensor_data.csv` — example sensor data
- `output/output.csv` — generated result file

## Requirements

- Python 3.8+
- Standard library only

## Run

From the project root, execute:

```bash
python main.py
```

The script prints summary metrics such as the total number of AEB events and the closest obstacle detected.

## Output

The output CSV includes the original columns plus an `emergency_brake` column, where:

- `1` = AEB should trigger
- `0` = AEB should not trigger

## Notes

- Invalid or missing numeric values are skipped during processing.
- The AEB rule currently uses the threshold: `TTC < 2.0 seconds`.

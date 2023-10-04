
# Log Analysis System

The Log Analysis System is a practice project designed to enhance proficiency with Linux terminal commands, vital for backend development.

## Overview

This project simulates the generation and analysis of log files, mirroring scenarios where backend engineers utilize various terminal tools.

## Getting Started

1. Navigate to the `scripts/` directory.
2. Run the `log_generator.py` script to generate log files:
bash python3 log_generator.py

3. Logs will be saved in the `logs/` directory.

## Tasks

### Searching with `grep`:
- Identify all logs marked `ERROR`.
- Find logs associated with a particular username.
- Count occurrences of the `DOWNLOAD` action.

### Data Processing with `awk`:
- Isolate all IP addresses from logs.
- Showcase logs from a designated date.

### Text Transformation using `sed`:
- Switch all mentions of `ERROR` to `CRITICAL`.
- Prepend each log entry with a timestamp.

### File Exploration using `head`, `tail`, & `less`:
- Display the initial 10 logs.
- Expose the last 10 logs.
- Peruse logs interactively.

### File Discovery with `find`:
- Detect logs edited within the past day.
- Locate logs surpassing a specific file size.

### Networking with `curl` and `wget`:
- Retrieve a distant log file for storage in the `logs/` directory.
- If available, probe your application's API or endpoint.

### Server Interaction using `ssh`:
- Establish a connection to an external server to retrieve logs. This step presumes a server is ready for access.

### Process Management via `kill`:
- Abort a script or process currently generating logs.

### Domain Investigation with `dig`:
- Examine domains correlating to IP addresses found in logs.

## Contributing

While this is primarily a personal project, contributions in the form of suggestions, optimizations, or bug fixes are welcomed. Kindly fork the repository and create a pull request for any changes.



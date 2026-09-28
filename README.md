# Detection Tool

## Overview
The Detection Tool is a utility designed to analyze and process log files to identify specific patterns, anomalies, or security-related events. It is particularly useful for system administrators, security analysts, and developers who need to monitor and investigate system activities.

## Features
- **Log Analysis**: Processes log files to extract meaningful information.
- **Pattern Matching**: Identifies specific patterns or keywords in log files.
- **Customizable**: Easily extendable to include additional patterns or analysis techniques.

## File Structure
- `v2-basic-log.py`: The main script for processing log files.
- `sample-logs/`: Directory containing sample log files for testing.
  - `auth-1.log`
  - `auth-2.log`
  - `auth-3.log`

## Usage

### Prerequisites
Ensure you have Python installed on your system. This tool is compatible with Python 3.x.

### Running the Tool
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/D-Hamza123/detection-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd detection-tool
   ```
3. Run the main script with the desired log file(s):
   ```bash
   python3 v2-basic-log.py sample-logs/auth-1.log
   ```

## Extending the Tool
To add new patterns or analysis techniques:
1. Open `v2-basic-log.py` in a text editor.
2. Locate the section where patterns are defined or analysis logic is implemented.
3. Add your custom logic.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests on the project's repository.

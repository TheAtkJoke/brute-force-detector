# Brute Force Attack Detector

## Overview
This project is a Python-based brute-force attack detector that monitors authentication logs in real-time. It identifies multiple failed login attempts from the same IP address within a specific time window and flags potential brute-force attacks.

## Features
- Monitors authentication logs for failed login attempts
- Detects brute-force attacks based on a threshold of failed attempts
- Uses real-time log parsing
- Outputs warnings when suspicious activity is detected

## How It Works
1. The script reads log entries from a specified authentication log file (`auth.log`).
2. It extracts failed login attempts along with IP addresses.
3. If the number of failed attempts from a single IP exceeds a defined threshold within a given time window, the script flags the IP as a potential brute-force attacker.
4. The detected incidents are displayed in the console.

## Requirements
- Python 3.x

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/TheAtkJoke/brute-force-detector.git
   cd brute-force-detector
   ```
2. Run the script:
   ```bash
   python brute_force_detector.py
   ```
3. The script will monitor the log file and print alerts if suspicious activity is detected.

## Configuration
- Modify the `LOG_FILE` variable in the script to match your authentication log file path.
- Adjust `THRESHOLD_ATTEMPTS` and `TIME_WINDOW` based on your security needs.

## Example Output
```
Potential brute-force attack detected from IP: 192.168.1.10
```

## License
This project is open-source under the MIT License.

## Author
Brandon Mokeba Itor

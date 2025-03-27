import re
import time
from collections import defaultdict

# Simulated log entries (since we cannot access real log files in this environment)
LOG_ENTRIES = [
    "Failed password for user from 192.168.1.100 port 22",
    "Failed password for user from 192.168.1.100 port 22",
    "Failed password for user from 192.168.1.100 port 22",
    "Failed password for user from 192.168.1.100 port 22",
    "Failed password for user from 192.168.1.100 port 22",
    "Failed password for user from 192.168.1.101 port 22"
]

# Thresholds for brute-force detection
THRESHOLD_ATTEMPTS = 5  # Max failed attempts before flagging
TIME_WINDOW = 60  # Time window in seconds to track attempts

# Dictionary to track failed attempts per IP
failed_attempts = defaultdict(list)

def parse_log_line(line):
    """Extracts IP address and timestamp from log line."""
    match = re.search(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+) port', line)
    if match:
        ip_address = match.group(1)
        timestamp = time.time()  # Use current system time
        return ip_address, timestamp
    return None, None

def detect_brute_force():
    """Simulates monitoring log file for brute-force attack patterns."""
    for line in LOG_ENTRIES:
        ip, timestamp = parse_log_line(line)
        if ip:
            failed_attempts[ip].append(timestamp)
            # Remove old attempts beyond time window
            failed_attempts[ip] = [t for t in failed_attempts[ip] if timestamp - t <= TIME_WINDOW]
            
            if len(failed_attempts[ip]) >= THRESHOLD_ATTEMPTS:
                print(f"Potential brute-force attack detected from IP: {ip}")

# Run the brute-force detection simulation
detect_brute_force()

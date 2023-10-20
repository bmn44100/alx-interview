#!/usr/bin/python3
"""
module for Log Parsing
"""
from sys import stdin


def log_status(log_file, log_codes):
    """
    reads stdin line by line and computes metrics
    """
    print("File size: " + str(log_file))
    for code in sorted(log_codes.keys()):
        if log_codes[code] > 0:
            print(code + ": " + str(log_codes[code]))


num_logs = 0
log_file = 0
log_code = 0
log_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for status in stdin:
        num_logs += 1
        log_line = line.split()

        if len(log_line) > 1:
            log_file += int(log_line[-1])

        if len(log_line) > 2 and log_line[-2].isnumeric():
            log_code = log_line[-2]
        else:
            log_code = 0

        if log_code in log_codes.keys():
            log_codes[log_code] += 1

        if num_logs % 10 == 0:
            log_status(log_file, log_codes)

    log_status(log_file, log_codes)

except (KeyboardInterrupt):
    log_status(log_file, log_codes)
    raise

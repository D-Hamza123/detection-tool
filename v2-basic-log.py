import re
from collections import defaultdict, deque
from datetime import datetime, timedelta

WINDOW = timedelta(seconds=60)
THRESHOLD = 5

pattern = re.compile(
    r"^(\w{3}\s+\d+\s[\d:]{8}) .* Failed password .* from (\d+\.\d+\.\d+\.\d+)"
)
recent = defaultdict(deque)

def parse_time(text):
    return datetime.strptime("2026 " + text,"%Y %b %d %H:%M:%S")


with open("sample-logs/auth-3.log") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            when = parse_time(match.group(1))
            ip = match.group(2)
            recent[ip].append(when)
            cutoff = when - WINDOW

            while recent[ip][0] < cutoff:
                recent[ip].popleft()
            if len(recent[ip]) >= THRESHOLD:
                print(f"Alert: {ip} had {len(recent[ip])} failures within 60s at {when}")


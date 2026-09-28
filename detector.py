import re
import requests
from collections import defaultdict, deque
from datetime import datetime, timedelta

WINDOW = timedelta(seconds=60)
THRESHOLD = 5

cache = {}

pattern = re.compile(
    r"^(\w{3}\s+\d+\s[\d:]{8}) .* Failed password .* from (\d+\.\d+\.\d+\.\d+)"
)
recent = defaultdict(deque)
alerted = set()

def lookup_ip(ip):
    if ip in cache:
        return cache[ip]
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        data = response.json()
        result = {
            "country": data.get("country", "?"),
            "city": data.get("city", "?"),
            "ip": data.get("query", "?"),
            "isp": data.get("isp", "?")
        }
    except requests.RequestException as e:
        result = {"error": str(e)}

    cache[ip] = result
    return result

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
                if ip not in alerted:
                    info = lookup_ip(ip)
                    print(f"Alert: {ip} ({info}) had {len(recent[ip])} failures within 60s at {when}")
                    alerted.add(ip)
            else:
                alerted.discard(ip)



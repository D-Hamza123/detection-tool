import re
from collections import Counter

pattern = re.compile(r"Failed password .* from (\d+\.\d+\.\d+\.\d+)")
# pattern = re.compile(r"from 212.129.2.219 port (\d+)") //for ports

failures = Counter()

with open("sample-logs/auth-1.log") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            failures[match.group(1)] += 1

print(failures.most_common(10))
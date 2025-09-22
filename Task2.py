from collections import defaultdict

counts = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("LOGFILE.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
print(counts)
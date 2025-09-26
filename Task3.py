import time
start = time.time()

from collections import defaultdict

num = 1 #number the ip placed
send = ""
item = 0 #item in the list to check
counts = defaultdict(int)           # Create a dictionary to keep track of IPs

def ip_parse(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None



with open("LOGFILE.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
#print(counts)




def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n] #Line from mark , do not think about it too much

test = top_n(counts, n=5)
#print(test)

print("Top 5 Attacker Ip")
#for i in range(5):
#    print(num , test[i])
#    send = test[i]
#    num = num +1

with open("failed_counts.txt", "w") as out:
    for x,y in test: # as long as there is an x and y value , do the loop
        print(f"{num}.{x} - {y}")
        send = (f"{num}.{x} - {y}")
        out.write(f"{send}" + "\n")
        num = num+1


# run counting
end = time.time()
print("Wrote failed_counts.txt")
print("Elapsed:", round(end-start,5), "seconds")
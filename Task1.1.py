#lab2-2_starter.py

LOGFILE = "LOGFILE.log"  # change filename if needed
line_number = 0               # start counting at 1
list_ips = []
count = 0
unique_list_ips = []

def simple_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            list_ips.append(port.strip())             # strip any trailing punctuation

              
        except (ValueError, IndexError):
            return None
    
    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":
    with open(LOGFILE, "r") as f:
        for line in f:  
            line_number = line_number + 1           # increase counter
            count+=1
            simple_parser(line.strip())


    unique_list_ips=set(list_ips)
    sorted_list = sorted(unique_list_ips)
    count = len(unique_list_ips)
    print(f"The set has {count} elements.")

    ##print("Unique ips " , unique_list_ips)
    print ("Lines read " , line_number)
    print(sorted_list[0:10])
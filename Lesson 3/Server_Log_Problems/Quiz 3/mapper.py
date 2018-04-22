import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip_address, identity, username, datetime, timezone, method, path, proto, status, size = data
        cleaned_path = re.sub(r"^http://www.the-associates.co.uk", '', path)
        print cleaned_path

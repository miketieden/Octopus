#!/usr/bin/env python3
#
# Testing
#
#
import time
from datetime import datetime
f = "%Y-%m-%d %H:%M:%S.%f"
t = datetime.now()
timestamp = t.strftime(f)[:-4]
print(timestamp + " This is a test. This is only a test.")
print(timestamp + " This is another test.")

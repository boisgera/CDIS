#!/usr/bin/env python

# Standard Library
from urllib.request import urlopen

# Third-Party Libraries
from ics import *

# ------------------------------------------------------------------------------

url = "https://calendar.google.com/calendar/ical/ecqbbg9bbqgaqh0rgnsjt4ppvk%40group.calendar.google.com/public/basic.ics"

calendar = Calendar(urlopen(url).read().decode("utf-8"))

assert len(calendar.events) == 60
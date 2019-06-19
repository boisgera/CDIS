#!/usr/bin/env python

# Standard Library
from urllib.request import urlopen

# Third-Party Libraries
from ics import *

# ------------------------------------------------------------------------------

url = "https://calendar.google.com/calendar/ical/ecqbbg9bbqgaqh0rgnsjt4ppvk%40group.calendar.google.com/public/basic.ics"

calendar = Calendar(urlopen(url).read().decode("utf-8"))

assert len(calendar.events) == 60

events = list(calendar.events)
events.sort()

for i, event in enumerate(events):
    print(f"{i+1:2d}) {event.name}")
    assert event.begin.date() == event.end.date()
    assert event.duration.seconds == 1.5 * 3600
    print("    " + event.begin.format("dddd DD MMMM YYYY", locale="fr_FR"), end=", ")
    print(event.begin.format("HH:mm") + "-" + event.end.format("HH:mm") + ".")
    print()
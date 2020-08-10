#!/usr/bin/env python

# Standard Library
from urllib.request import urlopen

# Third-Party Libraries
from ics import *
import pandoc

# ------------------------------------------------------------------------------

url = "https://calendar.google.com/calendar/ical/o1rahvtc75kj2qcc5tmsrfr6e0%40group.calendar.google.com/public/basic.ics"

calendar = Calendar(urlopen(url).read().decode("utf-8"))

# assert len(calendar.events) == 60 
# relax this; we have more slots with the exam of EC2 now.

events = list(calendar.events)
events.sort()

for i, event in enumerate(events):
    print(f"{i+1:2d}) {event.name}")
    assert event.begin.date() == event.end.date()
    #assert event.duration.seconds == 1.5 * 3600
    begin = event.begin.to("Europe/Paris")
    end = event.end.to("Europe/Paris")
    print("    " + begin.format("dddd DD MMMM YYYY", locale="fr_FR"), end=", ")
    print(begin.format("HH:mm") + "-" + end.format("HH:mm") + ".")
    description = event.description
    if event.description:
        doc = pandoc.read(event.description, format="html")
        print(pandoc.write(doc, format="markdown"))
        #description = "\n".join(["    " + line for line in description.splitlines()])
        #description = "    " + description.strip()
        #print(description)
    print()
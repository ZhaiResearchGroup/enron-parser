# enron-parser
Python parser for emails in Enron dataset

## Use
Call `python parse_email.py` on a path name for directory or file
Generates a JSON parse for a single file, generates a list of JSON parses recursively through subdirectories for a directory.

## Returns:
Creates or overwrites the following files:

`threads.json`
```
{"": 0, "Weekly Environmental Activity Report-Roswell Area": 2, "Weekly Activity Report, Roswell Area": 1, "Weekly Environemtnal Activity Report": 6, "Weekly Environmental Acitivity Report Roswell ARea": 10, "weekly environmental activity report-Roswell Area": 4, "Environmental findings, Koch South Texas Records Review": 3, "Riedel's Weekly Information September 7, 2001": 5, "Weekly Activity Report Roswell Area": 7, "Weekly Envoironmental Activity Report": 8, "Weekly Report, Roswell Area": 9}
```

`users.json`
```
{"jim.lynch@enron.com": 5, "larry.campbell@enron.com": 0, "gary.fuller@enron.com": 12, "randy.belyeu@enron.com": 10, "william.kendrick@enron.com": 1, "rich.jolly@enron.com": 3, "joe.richards@enron.com": 11, "rick.loveless@enron.com": 7, "dave.miller@enron.com": 6, "scott.clark@enron.com": 2, "mike.riedel@enron.com": 8, "randy.howard@enron.com": 4, "scott.jones@enron.com": 9}
```

`messages.json`
```
[{"bcc": [], "message": "The annual pollution prevention plans were completed and submitted to the State of Arizona. These plans are requried for the three large quantity generators of hazardous waste in Arizona. Annual hazardous waste fees were paid and submitted to the State of New Mexico for four facilities in New Mexico. A conference call was held with Houston Legal and Environmetnal Affairs to discuss the alleged NOV issued for the P-1 C/S which involved a turbine like for like replacement activity. Data has begun to be collected to substantiate Transwestern's position concerning the proposed action by the State of New Mexico. A field trip was made to the Air Quality Bureau to copy all files relevant to the P-1 C/S and will be delivered to the contract attorney who will be assisting Transwestern with this issue. Copies of the New Mexico EOTT air permits were received. Comparisons will be made with the nearly completed EOTT tank database spreadsheet to determine status of permit compliance with each air permit.", "sender": 0, "thread": 10, "recipient": [7, 8, 9], "cc": [], "time": "Thu, 28 Jun 2001 13:10:00 -0700 (PDT)"}]
```

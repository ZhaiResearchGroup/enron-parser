# enron-parser
Python parser for emails in Enron dataset

## Use
Call `python parse_email.py` on a path name for directory or file
Generates a JSON parse for a single file, generates a list of JSON parses recursively through subdirectories for a directory.

## Returns:
Creates or overwrites the following files:

`threads.json`: Assigns each thread a unique integer ID, based on parsed titles
```
{"": 0, "Weekly Environmental Activity Report-Roswell Area": 2, "Weekly Activity Report, Roswell Area": 1, "Weekly Environemtnal Activity Report": 6, "Weekly Environmental Acitivity Report Roswell ARea": 10, "weekly environmental activity report-Roswell Area": 4, "Environmental findings, Koch South Texas Records Review": 3, "Riedel's Weekly Information September 7, 2001": 5, "Weekly Activity Report Roswell Area": 7, "Weekly Envoironmental Activity Report": 8, "Weekly Report, Roswell Area": 9}
```

`thread-users.json`: For each thread ID, a list of user IDs that are associated with the thread
```
{"0": [0, 1, 2, 3, 4], "1": [0, 5, 6, 7, 8], "2": [0, 5, 8], "3": [0, 5, 6, 9, 10], "4": [0, 5, 9], "5": [0, 5, 8], "6": [0, 5, 6, 8, 9], "7": [0, 7, 8, 9, 10, 11], "8": [0, 5, 6, 7], "9": [0, 1, 771, 5, 7, 8, 9, 11, 12, 13, 14, 15, 1040, 17, 1042, 1043, 22, 792, 282, 797, 33, 18, 504, 38, 39, 1066, 1067, 178, 814, 50, 435, 137, 824, 572, 321, 66, 1383, 609, 584, 329, 842, 334, 81, 853, 88, 1039, 95, 96, 16, 356, 1041, 107, 1170, 111, 881, 72, 124, 1149, 363, 903, 392, 393, 834, 1169, 402, 150, 154, 163, 169, 938, 840, 434, 179, 436, 437, 1353, 1354, 707, 453, 462, 209, 724, 725, 482, 483, 484, 999, 1010, 247, 1272, 506, 509, 85], "10": [0, 9, 16, 17, 18]}
```

`user-threads.json`: For each user ID, a list of thread IDs with which the user is associated
```
{"0": [0, 1, 2, 3, 4, 5, 6, 7], "1": [0, 5], "2": [0, 1, 2, 3, 4, 5, 6, 7], "3": [0], "4": [1, 5], "5": [2, 6], "6": [2], "7": [2, 6], "8": [5], "9": [6], "10": [7], "11": [7]}
```

`users.json`: Assigns each email address a unique integer ID
```
{"jim.lynch@enron.com": 5, "larry.campbell@enron.com": 0, "gary.fuller@enron.com": 12, "randy.belyeu@enron.com": 10, "william.kendrick@enron.com": 1, "rich.jolly@enron.com": 3, "joe.richards@enron.com": 11, "rick.loveless@enron.com": 7, "dave.miller@enron.com": 6, "scott.clark@enron.com": 2, "mike.riedel@enron.com": 8, "randy.howard@enron.com": 4, "scott.jones@enron.com": 9}
```

`messages.json`: Parses emails, and maintains thread, sender, recipient, cc, bcc, time, and message fields
```
[{"bcc": [], "message": "The annual pollution prevention plans were completed and submitted to the State of Arizona. These plans are requried for the three large quantity generators of hazardous waste in Arizona. Annual hazardous waste fees were paid and submitted to the State of New Mexico for four facilities in New Mexico. A conference call was held with Houston Legal and Environmetnal Affairs to discuss the alleged NOV issued for the P-1 C/S which involved a turbine like for like replacement activity. Data has begun to be collected to substantiate Transwestern's position concerning the proposed action by the State of New Mexico. A field trip was made to the Air Quality Bureau to copy all files relevant to the P-1 C/S and will be delivered to the contract attorney who will be assisting Transwestern with this issue. Copies of the New Mexico EOTT air permits were received. Comparisons will be made with the nearly completed EOTT tank database spreadsheet to determine status of permit compliance with each air permit.", "sender": 0, "thread": 10, "recipient": [7, 8, 9], "cc": [], "time": "Thu, 28 Jun 2001 13:10:00 -0700 (PDT)"}]
```

import re
from os import path, listdir
import sys
import logging

#
# Precompiled patterns for performance
#
time_pattern = re.compile("Date: (?P<data>[A-Z][a-z]+\, \d{1,2} [A-Z][a-z]+ \d{4} \d{2}\:\d{2}\:\d{2} \-\d{4} \([A-Z]{3}\))")
subject_pattern = re.compile("Subject: (?P<data>.*)")
sender_pattern = re.compile("X-From: (?P<data>.*)")
recipient_pattern = re.compile("X-To: (?P<data>.*)")
cc_pattern = re.compile("X-cc: (?P<data>.*)")
bcc_pattern = re.compile("X-bcc: (?P<data>.*)")
msg_start_pattern = re.compile("\n\n", re.MULTILINE)
msg_end_pattern = re.compile("\n+.*\n\d+/\d+/\d+ \d+:\d+ [AP]M", re.MULTILINE)

#
# Accepts path as argument, returns parsed data as json
# Returns
#
def parse_email(pathname):
    if path.isdir(pathname):
        print(pathname)
        emails = []
        for child in listdir(pathname):
            # only parse visible files
            if child[0] != ".":
                child_parse = parse_email(path.join(pathname, child))
                if type(child_parse) == list and len(child_parse) > 0:
                     emails += child_parse
                elif type(child_parse) == dict:
                     emails.append(child_parse)
        return emails 
    else:
        print("file %s" % pathname)
        with open(pathname) as TextFile:
            text = TextFile.read()
            try:
                time = time_pattern.search(text).group("data")
                subject = subject_pattern.search(text).group("data")
                sender = sender_pattern.search(text).group("data")
                recipient = recipient_pattern.search(text).group("data").split(", ")
                cc = cc_pattern.search(text).group("data").split(", ")
                bcc = bcc_pattern.search(text).group("data").split(", ")
                msg_start_iter = msg_start_pattern.search(text).end()
                try:
                    msg_end_iter = msg_end_pattern.search(text).start()
                    message = text[msg_start_iter:msg_end_iter]
                except AttributeError: # not a reply
                    message = text[msg_start_iter:]
            except AttributeError:
                logging.error("Failed to parse %s" % pathname) 
                return None

        return {'time': time, 'subject': subject, 'sender': sender, 'recipient': recipient, 'cc': cc, 'bcc': bcc, 'message': message}

print(parse_email(sys.argv[1]))

import re
import sys

#
# Precompiled patterns for performance
#
time_pattern = re.compile("Date: (?P<data>[A-Z][a-z]+\, \d{1,2} [A-Z][a-z]+ \d{4} \d{2}\:\d{2}\:\d{2} \-\d{4} \([A-Z]{3}\))")
subject_pattern = re.compile("Subject: (?P<data>.*)")
from_pattern = re.compile("X-From: (?P<data>.*)")
to_pattern = re.compile("X-To: (?P<data>.*)")
cc_pattern = re.compile("X-cc: (?P<data>.*)")
bcc_pattern = re.compile("X-bcc: (?P<data>.*)")
msg_start_pattern = re.compile("\n\n", re.MULTILINE)
msg_end_pattern = re.compile("\n+.*\n\d+/\d+/\d+ \d+:\d+ [AP]M", re.MULTILINE)

#
# Accepts path as argument, returns parsed data as json
# Returns
#
def parse_email(pathname):
    with open(pathname) as TextFile:
        text = TextFile.read()
        print(text)
        time = time_pattern.search(text).group("data")
        subject = subject_pattern.search(text).group("data")
        from_field = from_pattern.search(text).group("data")
        to_field = to_pattern.search(text).group("data").split(", ")
        cc = cc_pattern.search(text).group("data").split(", ")
        bcc = bcc_pattern.search(text).group("data").split(", ")
        msg_start_iter = msg_start_pattern.search(text).end()
        try:
            msg_end_iter = msg_end_pattern.search(text).start()
            message = text[msg_start_iter:msg_end_iter]
        except AttributeError: # not a reply
            message = text[msg_start_iter:]
   

    return {'time': time, 'subject': subject, 'from_field': from_field, 'to_field': to_field, 'cc': cc, 'bcc': bcc, 'message': message}

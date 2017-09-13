# enron-parser
Python parser for emails in Enron dataset

## Use
Call `parse_email` function on a path name
Generates a JSON parse for a single file, generates a list of JSON parses recursively through subdirectories for a directory.

## Returns:
For a file:
```
{
 'message': 'Thanks Jeff. Mike/Jeff: FYI---all of our people are ...',
 'cc': ['Andrew Makk', 'Mac McClelland', 'Jim Rountree', 'Yaser Tobeh'],
 'time': 'Sun, 8 Oct 2000 18:48:00 -0700 (PDT)',
 'subject': 'Re: Latest developments in Palestine',
 'recipient': ['Jeffrey Hammad', 'Mike McConnell', 'Jeffrey A Shankman@ECT'],
 'sender': 'Rick Bergsieker', 
 'bcc': ['']
}
```

For a directory:
```
[
 {
 'message': 'Thanks Jeff. Mike/Jeff: FYI---all of our people are ...',
 'cc': ['Andrew Makk', 'Mac McClelland', 'Jim Rountree', 'Yaser Tobeh'],
 'time': 'Sun, 8 Oct 2000 18:48:00 -0700 (PDT)',
 'subject': 'Re: Latest developments in Palestine',
 'recipient': ['Jeffrey Hammad', 'Mike McConnell', 'Jeffrey A Shankman@ECT'],
 'sender': 'Rick Bergsieker', 
 'bcc': ['']
 }
]
```

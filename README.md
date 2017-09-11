# enron-parser
Python parser for emails in Enron dataset

## Use
Call `parse_email` function on a path name

## Returns:
```
{
  'message': 'Thanks Jeff. \n\nMike/Jeff:  FYI---all of our people are ...',
  'cc': ['Andrew Makk', 'Mac McClelland', 'Jim Rountree', 'Yaser Tobeh'],
  'time': 'Sun, 8 Oct 2000 18:48:00 -0700 (PDT)',
  'subject': 'Re: Latest developments in Palestine',
  'to_field': ['Jeffrey Hammad', 'Mike McConnell', 'Jeffrey A Shankman@ECT'],
  'from_field': 'Rick Bergsieker', 
  'bcc': ['']
}
```

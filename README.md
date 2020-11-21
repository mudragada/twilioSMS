## twilioSMS

#### Usage
```
➜ python main.py -h
Usage: 	main.py [options]

Options:
  -h, --help            show this help message and exit
  -a ACCT_SID, --acct-sid=ACCT_SID
                        The account SID for your Twilio account.
  -f FILENAME, --filename=FILENAME
                        The filename with phone numbers.
  -m MESSAGE, --message=MESSAGE
                        The body of the SMS you are sending
  -u MEDIAURL, --mediaurl=MEDIAURL
                        Any http or https media URLs as a list
  -s FROM_NUMBER, --sender=FROM_NUMBER
                        The phone number to have the SMS message appear from
  -t ACCT_TOKEN, --acct-token=ACCT_TOKEN
                        The account token for your Twilio account
```


```
python main.py
  -f <filename with phone numbers>
  -a <twilio account id>
  -t <twilio token id>
  -m <message>
  -u <http or https url>
  -s <Sender channel/phone number>
```

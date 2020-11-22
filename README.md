## twilioSMS

#### Features
 - You don't have to store/share the data outside of our local.
 - Can send a media url along with text message.
 - Can break text message post 1600 characters.
 - Any format of phone number given will be cleaned up.
 - SMS services using Twilio.

#### Pre-Requisites
 - A Twilio Upgraded account
 - Money (balance to be used)
 - Python version >= 3.6.2
 - pip install twilio, re, getopt, logging



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

```
Example:
python main.py
  -f phonenums.csv
  -a AC12345678901234567890
  -t ABCD1234EFGH5678IJKL9101112
  -m "Hi, This is a test message"
  -u https://myimage123.io/image.gif
  -s +11234567890
```

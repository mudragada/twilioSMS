 ### Download the helper library from https://www.twilio.com/docs/python/install
import os, sys, getopt, re, logging
from twilio.rest import Client
from optparse import OptionParser


class TwilioMsg:
    def __init__(self, account_sid, auth_token, msg_body, media_url, from_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.msg_body = msg_body
        self.media_url = media_url
        self.from_number = from_number

    def cleanupPhoneNum(self, phoneStr):
        phoneStr = phoneStr.strip()
        phoneStr = re.sub('[-()/*]','',phoneStr)
        if(len(phoneStr) == 12):
            if(phoneStr[0] == '+' and phoneStr[1] == '1'):
                pass
        elif(len(phoneStr) == 10):
            if(phoneStr[0]!='+'):
                phoneStr = "+1" + phoneStr
        return phoneStr

    def checkMessage(self, message):
        if len(message) >= 155:
            message = message[0:152] + '...'
        return message

    def sendMessage(self, phoneNumber):
        message = self.checkMessage(self.msg_body)
        client = Client(self.account_sid, self.auth_token)
        if self.media_url:
            response = client.messages.create(body=message, media_url=self.media_url, from_=self.from_number, to=phoneNumber)
        else:
            response = client.messages.create(body=message, from_=self.from_number, to=phoneNumber)

        logging.info("Sending message to " + phoneNumber + "..." + response.status)

        if(response.status != 'failed'):
            return True
        else:
            return False
        return False

def get_args(opts):
    """parse the arguments from the commandline"""
    usage = "\t%prog [options]"
    o = OptionParser(usage=usage)
    o.add_option("-a", "--acct-sid", dest="acct_sid", default=opts['acct_sid'],
                 help="The account SID for your Twilio account.")
    o.add_option("-f", "--filename", dest="filename", default=opts['filename'],
                     help="The filename with phone numbers.")
    o.add_option("-m", "--message", dest="message", default=opts['message'],
                 help="The body of the SMS you are sending")
    o.add_option("-u", "--mediaurl", dest="mediaurl", default=opts['mediaurl'],
                help="Any http or https media URLs as a list")
    o.add_option("-s", "--sender", dest="from_number",
                 default=opts['from_number'],
                 help="The phone number to have the SMS message appear from")
    o.add_option("-t", "--acct-token", dest="acct_token",
                 default=opts['acct_token'],
                 help="The account token for your Twilio account")

    (opt, args) = o.parse_args()
    return validate_args(opt)

def validate_args(args):
    """validate the arguments passed in"""
    if not len(args.acct_sid) == 34:
        raise ValueError('The APP_SID is not the proper length')
    if args.message is None or len(str(args.message).strip()) < 1:
        raise ValueError('You did not provide a valid message')
    if len(args.from_number) < 12:
        raise ValueError("sending number is not valid ( +1 followed by at least 10 digits)")
    return args

def main(argv):
    opts = {
    "acct_sid": "",
    "acct_token": "",
    "from_number": "",
    "message": "",
    "mediaurl":[],
    "filename":""
}
    logging.getLogger().setLevel(logging.INFO)
    args = get_args(opts)
    tMsg = TwilioMsg(args.acct_sid, args.acct_token, args.message, args.mediaurl, args.from_number)
    with open(args.filename, 'r') as filename:
        phoneNumberDict = {}
        lines = filename.readlines()
        for line in lines:
            phoneNumber = (tMsg.cleanupPhoneNum(line))
            if phoneNumber not in phoneNumberDict.keys():
                phoneNumberDict[phoneNumber] = tMsg.sendMessage(phoneNumber)
            else:
                logging.error("found a duplicate - " + phoneNumber)


if __name__=='__main__':
    main(sys.argv[1:])

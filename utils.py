import re

def cleanupPhoneNum(phone_number):
    phone_number = phone_number.strip()
    phone_number = re.sub('[-()/*]','',phone_number)
    phone_number = re.sub('\n', '', phone_number)
    phone_number_len = len(phone_number)
    if(phone_number[0] == '1' and phone_number_len == 11):
        phone_number = '+' + phone_number
    elif(phone_number[0] == '+' and phone_number_len == 12):
        pass
    elif(phone_number_len == 10):
        phone_number = '+1' + phone_number
    return str(phone_number)

def camelizeWords(s):
    return re.sub(r'\w+', lambda m:m.group(0).capitalize(), s)


from info import kavenegarApi
from kavenegar import *
from random import randint


def confirm_code_generator():
    confirmCode = randint(000000, 999999)
    return int(confirmCode)


def sms_sender(userPhoneNumbers: 'user phoen number', msg: 'your message and confirm code'):
    api = KavenegarAPI(f'{kavenegarApi}')
    params = {
        'sender': '1000596446', 
        'receptor': userPhoneNumbers,
        'message': msg,
    }
    response = api.sms_send(params)

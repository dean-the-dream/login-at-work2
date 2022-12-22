import imaplib
import email
import creds
import time
from datetime import datetime as dt, timezone, timedelta

#create impap library object
my_mail=imaplib.IMAP4_SSL(creds.imap_server)



#retrieve verify code email from inbox
def get_message():

    #select auth code messages from messages
    my_mail.select('Inbox')
    key = 'From'
    value = 'no-reply@globalpayments.com'
    _, msgnums = my_mail.search(None, key, value)

    #retreive data from the emails
    for msgnum in msgnums[0].split():
        _,data = my_mail.fetch(msgnum, '(RFC822)')

    # create an email object with the data
    message = email.message_from_bytes(data[0][1])
    my_mail.close()
    return message

# check message for correct time
def check_message(message, currentTime):

    # get the date and time of the message
    email_time = get_message().get("Date")

    # split the date string into an array
    date_parts = email_time.split()

    # remove the first section of the date array
    date_parts = date_parts[1:]
    timezone = date_parts[-1]

    # if the time zone is pacific standard time subtract 8 hours
    if timezone == "(PST)":
        delta = -8
    # if the time zone is pacific daylight, subtract 7 hours
    else:
        delta = -7

    # remove unneccesary parts of the date array
    date_parts = date_parts[:4]

    # turn the date array into a properly formatted string
    date_string = f"{date_parts[0]} {date_parts[1]} {date_parts[2]} {date_parts[3]}"

    # convert the date string into a date obeject
    datetime_object = dt.strptime(date_string, '%d %b %Y %H:%M:%S')

    # convert the time to GMT
    datetime_object = datetime_object - timedelta(hours = delta)

    #if confirm the time to make sure the message was send after the function was run
    if datetime_object < currentTime:
        return False
    else:
         return True

    # print(datetime_object)
    # print(currentTime)

    # return True

# get the verify code from the email
def get_verify_code():
    # login to email account
    my_mail.login(creds.emailun, creds.imapPW)

    # get the current time as a string
    currentTime = str(dt.now(timezone.utc))[:19]
    currentTime = dt.strptime(currentTime, '%Y-%m-%d %H:%M:%S')
    print(currentTime)

    message = get_message()
    
    # check the inbox every 3 seconds until the correct email is found
    while not check_message(message,currentTime):
        message = get_message()
        time.sleep(3)
        print(message.get("Subject")[24:30])

    # get the verification code from the  subject of the message
    message = get_message()
    code=message.get("Subject")[24:30]
    return code





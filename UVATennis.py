'''
This function handles a Slack slash command and echoes the details back to the user.

Follow these steps to configure the slash command in Slack:

  1. Navigate to https://<your-team-domain>.slack.com/services/new

  2. Search for and select "Slash Commands".

  3. Enter a name for your command and click "Add Slash Command Integration".

  4. Copy the token string from the integration settings and use it in the next section.

  5. After you complete this blueprint, enter the provided API endpoint URL in the URL field.


To encrypt your secrets use the following steps:

  1. Create or use an existing KMS Key - http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html

  2. Click the "Enable Encryption Helpers" checkbox

  3. Paste <COMMAND_TOKEN> into the kmsEncryptedToken environment variable and click encrypt


Follow these steps to complete the configuration of your command API endpoint

  1. When completing the blueprint configuration select "Open" for security
     on the "Configure triggers" page.

  2. Enter a name for your execution role in the "Role name" field.
     Your function's execution role needs kms:Decrypt permissions. We have
     pre-selected the "KMS decryption permissions" policy template that will
     automatically add these permissions.

  3. Update the URL for your Slack slash command with the invocation URL for the
     created API resource in the prod stage.
'''

import boto3
import json
import logging
import os
import aiml
import when_court
import when_court2
import when_court3
import dateutil.parser

bot = aiml.Kernel()
bot.learn("uvatennis.aiml")

from base64 import b64decode
from urlparse import parse_qs


# ENCRYPTED_EXPECTED_TOKEN = os.environ['kmsEncryptedToken']

# kms = boto3.client('kms')
# expected_token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    params = parse_qs(event['body'])
    token = params['token'][0]
    if token != expected_token:
        logger.error("Request token (%s) does not match expected", token)
        return respond(Exception('Invalid request token'))

    user = params['user_name'][0]
    command = params['command'][0]
    channel = params['channel_name'][0]
    command_text = params['text'][0]
     
    resp = bot.respond(command_text)
    question = resp.split(' ')
    reply=bot.respond(command_text)
    #question 1
    if question[0] == "aaa" : 
        time =  dateutil.parser.parse(' '.join(question[4:]))
        # format the time input
        s1=str(question[1])
        s2=str(question[3])
        if (len(s1)==1):
            s1="0"+s1+":00"
        else:
            if (len(s1)==2):
                s1=s1+":00"
            else:
                if (len(s1)==3):
                    s1="0"+s1  
        if (len(s2)==1):
            s2="0"+s2+":00"
        else:
            if (len(s2)==2):
                s2=s2+":00"
            else:
                if (len(s2)==3):
                    s2="0"+s2   
        reply = when_court.accessDatabase(time.year,time.month,time.day,s1,s2)

    #question 2
    if question[0] == "bbb" : 
        time =  dateutil.parser.parse(' '.join(question[2:]))
        reply = when_court2.accessDatabase(time.year,time.month,time.day,question[1])

    #question 3
    if question[0] == "ccc" : 
        time =  dateutil.parser.parse(' '.join(question[2:])) 
        # calculate the date of tomorrow
        d=time.day
        m=time.month
        y=time.year
  
        if ((y % 4==0 and m==2 and d==29) or (y % 4!=0 and m==2 and d==28)):
            d=1
            m=3
        else:
            if (d==31):
                if (m==12):
                    d=1
                    m=1
                    y=y+1
                else:
                    d=1
                    m=m+1
            else:
                if ((d==30) and (m==4 or m==6 or m==9 or m==11)):
                    d=1
                    m=m+1
                else:
                    d=d+1

        reply = when_court3.accessDatabase(y,m,d)

    return respond(None, "%s : %s" % (command_text, reply))


sentence = "What time is it?"
print(sentence)
print bot.respond(sentence)




# sentence2 = "Is there a court open today from 7 to 22?"
# resp = bot.respond(sentence2)
# question = resp.split(' ')
# if question[0] == "aaa" : 
#     time =  dateutil.parser.parse(' '.join(question[4:]))
#     # format the time input
#     s1=str(question[1])
#     s2=str(question[3])
#     if (len(s1)==1):
#         s1="0"+s1+":00"
#     else:
#         if (len(s1)==2):
#             s1=s1+":00"
#         else:
#             if (len(s1)==3):
#                 s1="0"+s1  
#     if (len(s2)==1):
#         s2="0"+s2+":00"
#     else:
#         if (len(s2)==2):
#             s2=s2+":00"
#         else:
#             if (len(s2)==3):
#                 s2="0"+s2   
#     reply = when_court.accessDatabase(time.year,time.month,time.day,s1,s2)
#     print(sentence2)
#     print(reply)
#     print

# sentence3 = "When is Court 5 open today?"
# resp = bot.respond(sentence3)
# question = resp.split(' ')
# if question[0] == "bbb" : 
#     time =  dateutil.parser.parse(' '.join(question[2:]))
#     reply = when_court2.accessDatabase(time.year,time.month,time.day,question[1])
#     print(sentence3)
#     print(reply)
#     print

# sentence4 = "What is one of the earliest available courts tomorrow?"
# resp = bot.respond(sentence4)
# question = resp.split(' ')
# if question[0] == "ccc" : 
#     time =  dateutil.parser.parse(' '.join(question[2:])) 
#     # calculate the date of tomorrow
#     d=time.day
#     m=time.month
#     y=time.year
  
#     if ((y % 4==0 and m==2 and d==29) or (y % 4!=0 and m==2 and d==28)):
#             d=1
#             m=3
#     else:
#         if (d==31):
#             if (m==12):
#                 d=1
#                 m=1
#                 y=y+1
#             else:
#                 d=1
#                 m=m+1
#         else:
#             if ((d==30) and (m==4 or m==6 or m==9 or m==11)):
#                 d=1
#                 m=m+1
#             else:
#                 d=d+1

#     reply = when_court3.accessDatabase(y,m,d)
#     print(sentence4)
#     print(reply)
#     print




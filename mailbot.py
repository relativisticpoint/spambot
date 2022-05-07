from email import message
from mailer import Mailer
import sys

lily = Mailer(email='lilywolf272@gmail.com',
              password='lilydog123')

def spam(mess,rec):

    # mess += "this was sent from the relativisticpointXsamaritan spambot"
    lily.send(receiver=rec,  # Email From Any service Provider
            no_reply='hsami272@gmail.com', # Redirect receiver to another email when try to reply.
            subject='test-bot',
            message= mess)

if __name__ == "__main__":
    mess = ''
    for i in range(1,len(sys.argv)-1):
        mess += sys.argv[i] + " " # to create the message from the input
    rec = sys.argv[len(sys.argv)-1] #the last string the user inputs is the email of the receiver
    # print('sending mail to ',rec)
    spam(mess,rec)
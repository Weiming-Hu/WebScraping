import smtplib
from email.mime.text import MIMEText
from pip._vendor.distlib.compat import raw_input

def sendOutlookEmail():
    print("creating message...")
    msg = MIMEText("The body of the email here...")
    
    msg["Subject"] = "An Email Test"
    # since outlook is using TLS authentication, it is of no use
    # to fake a sender email
    msg["From"] = "nobody@outlook.com"
    msg["To"] = "409498637@qq.com"
    
    print(msg)
    input("press any key to continue...")
    
    print("connecting...")
    s = smtplib.SMTP("smtp-mail.outlook.com", 587)
    s.starttls()
#     s.set_debuglevel(1)
    s.login("cosmos.weiming@outlook.com", "Gavinimmortal")
    print("sending message...")
    s.send_message(msg)
    s.quit()
    print("done!")

if __name__ == '__main__':
    count = 5
    while count:
        count -= 1
        try:
            sendOutlookEmail()
            break
        except TimeoutError:
            print("time out!")
            pass
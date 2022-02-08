from email import message
from http import server
import smtplib
from email.message import EmailMessage
import time

while True:
    def alert_email(subject, body, to):
        message = EmailMessage()
        message.set_content(body)
        message[ "subject"] = subject
        message["to"] = to
        
        user = "emailalertstck@gmail.com"
        message["from"] = user
        password = "ooqlyytujhpxlige"
        
        
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,password)
        server.send_message(message)
        
        server.quit()
        
    if __name__ == "__main__":
        alert_email("Stock", " Your Stock has had an inscrease", " peterbradley994@gmail.com ")
        time.sleep(1.2)

    print("run finish")
    
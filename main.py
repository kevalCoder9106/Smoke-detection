import smtplib
import random

def send_mail(msg,receiver):
    try:
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
            
        # start TLS for security
        s.starttls()
            
        # Authentication
        s.login("actemp22@gmail.com", "atempaccount99")
            
        # message to be sent
        message = msg
            
        # sending the mail
        s.sendmail("actemp22@gmail.com", receiver, msg)
            
        print(f"[+] Successfully sent email to {receiver}")

        # terminating the session
        s.quit()
    except:
        print(f"[-] Error sending email")
        return 0

def get_data():
    # here we will get data (in future from sensor, now its just random)
    return random.randrange(1,601)

if __name__ == "__main__":
    rec_mail = input("Enter you email: ")
    
    while True:
        ppm = get_data()
        
        print(f"[+] {ppm}")
                
        if ppm > 400:
            send_mail("Smoke is too high right now, please do something...",rec_mail)
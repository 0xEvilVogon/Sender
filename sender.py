import smtplib
import getpass

def send_email(to, subject, message):
    user = "ankkumar@student.42newdelhi.com"
    password = getpass.getpass("Input password: ")
    
    sent_from = user
    to = to
    subject = subject
    body = message

    email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (sent_from, ", ".join(to), subject, body)
    
    try:
        server = smtplib.SMTP_SSL("smtp.example.com", 587)
        server.starttls()
        server.login(user, password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print("Successful sending")
    except Exception as e:
        print("Unable to send mail. Error: ", e)
        
if __name__ == "__main__":
    with open("target.txt", "r") as f:
        target = f.readlines()
        target = [d.strip() for d in target]
    
    subject = input("Add Subject: ")
    message = input("Add message: ")
    
    send_email(target, subject, message)

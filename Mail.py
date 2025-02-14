import smtplib
from email.mime.text import MIMEText
def new_mail(reciver,code):
    sender_email = "szymon.beczkowski@gmail.com"
    app_password = "lwjxrydpcssewbbn"  # Wygenerowane hasło aplikacji
    receiver_email = reciver # np. "beczkowski.szymon@gmail.com"

    msg = MIMEText("To jest twój kod weryfikacyjny {}. ".format(code))
    msg["Subject"] = "Kod Weryfikacyjny"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)  # Używamy hasła aplikacji
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("✅ E-mail wysłany!")

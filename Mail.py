import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
sender_em = os.getenv("sender")
app_key = os.getenv("app_key")

def new_mail(reciver,code):
    print(reciver,code)
    sender_email = sender_em
    app_password = app_key  # Wygenerowane hasło aplikacji
    receiver_email = str(reciver) # email do kogo chcemy wysłać

    html_content = """
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2 style="color: #007BFF;">Twój kod weryfikacyjny</h2>
        <p><b>Twój kod:</b> <span style="font-size: 20px; color: red;">{}</span></p>
        <p>Użyj go, aby potwierdzić swoją tożsamość.</p>
        <hr>
        <p style="font-size: 12px; color: gray;">Jeśli to nie Ty prosiłeś o kod, zignoruj tę wiadomość.</p>
      </body>
    </html>
    """.format(code)

    text_content = "To jest twój kod weryfikacyjny: {}. ".format(code)

    msg = MIMEMultipart("alternative")

    # Dodanie wersji tekstowej i HTML
    msg.attach(MIMEText(text_content, "plain"))  # Zwykły tekst
    msg.attach(MIMEText(html_content, "html"))  # HTML

    msg["Subject"] = "Kod Weryfikacyjny"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)  # Używamy hasła aplikacji
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("E-mail wysłany!")

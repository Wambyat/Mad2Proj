import sqlite3
from email.message import EmailMessage
import smtplib
import ssl
from celery import Celery
app = Celery('celSQL', broker = "redis://localhost:6379/0", backend = "redis://localhost:6379/0")

@app.task
def cSQL(query):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(query)
    output = c.fetchall()
    conn.commit()
    conn.close()
    return output

def email(toEmail,subject,body):
    password = "pgks lufx otqe obru"
    email_sender = "anirudhaaanekal@gmail.com"
    email_password = password
    email_receiver = toEmail

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return "Email sent successfully"
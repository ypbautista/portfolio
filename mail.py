from flask_mail import Mail, Message
import threading

mail = Mail()

def send_email(app, recipient, subject, body):
    msg = Message(
        subject=subject,
        recipients=[recipient],
        body=body
    )

    def send_async():
        with app.app_context():
            try:
                mail.send(msg)
            except Exception as e:
                print("Email failed:", e)

    threading.Thread(target=send_async).start()
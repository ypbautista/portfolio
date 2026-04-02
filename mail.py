from flask_mail import Mail, Message

mail = Mail()

def send_email(app, recipient, subject, body):
    with app.app_context():
        msg = Message(
            subject=subject,
            recipients=[recipient],
            body=body
        )
        mail.send(msg)
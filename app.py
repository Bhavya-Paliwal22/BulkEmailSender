from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_email():
    try:
        sender_email = request.form['sender_email']
        app_password = request.form['app_password']

        recipients = request.form['recipients'].split(',')

        subject = request.form['subject']
        message = request.form['message']

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)

        success_count = 0

        for email in recipients:
            email = email.strip()
            server.sendmail(sender_email, email, msg.as_string())
            success_count += 1

        server.quit()

        return f"""
        <h2>✅ Emails Sent Successfully!</h2>
        <p>Total Emails Sent: {success_count}</p>
        <a href="/">Go Back</a>
        """

    except Exception as e:
        return f"""
        <h2>❌ Error</h2>
        <p>{e}</p>
        <a href="/">Go Back</a>
        """

if __name__ == '__main__':
    app.run(debug=True)


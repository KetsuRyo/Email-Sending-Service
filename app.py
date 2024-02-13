from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/emails', methods=['POST'])
def send_email():
    data = request.json
    sender_email = "your_email@example.com"  # This will be the email used to send messages.
    receiver_email = data['to']
    password = "your_password"  # Consider using environment variables or encrypted secrets for this.

    subject = data['subject']
    body = data['body']

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Use your SMTP server here.
            server.starttls()
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

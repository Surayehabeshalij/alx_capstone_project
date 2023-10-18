from flask import Flask, render_template, request

app = Flask(__name__)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Perform form validation
        if not name:
            return render_template('contact.html', error='Please enter your name.')
        if not email:
            return render_template('contact.html', error='Please enter your email.')
        if not message:
            return render_template('contact.html', error='Please enter your message.')

        # Send email
        sender_email = 'your_sender_email@gmail.com'
        sender_password = 'your_sender_email_password'
        recipient_email = 'surafelshemsu@gmail.com'

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'New Contact Form Submission'

        # Add the message body
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Create a secure connection to the SMTP server
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, msg.as_string())

            # Redirect to thank you page
            return render_template('thank_you.html')
        except Exception as e:
            return render_template('contact.html', error='Error occurred while sending the email.')

    # For GET requests or when form validation fails
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

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

        # Perform any desired actions (e.g., send email, save to a database)

        # Redirect to thank you page
        return render_template('thank_you.html')

    # For GET requests or when form validation fails
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
fernet = Fernet(key)

# Homepage - serve the HTML form for encryption
@app.route('/')
def index():
    return render_template('index.html')

# Encrypt endpoint
@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    encrypted_message = fernet.encrypt(message.encode())
    return render_template('result.html', result=encrypted_message.decode(), action='Encrypt')

# Decrypt endpoint
@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['encrypted_message']
    decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
    return render_template('result.html', result=decrypted_message, action='Decrypt')

# Result page with back button
@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html', result='', action='Back')

if __name__ == '__main__':
    app.run(debug=True)

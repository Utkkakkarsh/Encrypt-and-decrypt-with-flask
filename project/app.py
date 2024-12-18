from flask import Flask, render_template, request
from cryptography.fernet import Fernet

# Initialize Flask app
app = Flask(__name__)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route("/", methods=["GET", "POST"])
def index():
    encrypted_message = ""
    decrypted_message = ""
    
    if request.method == "POST":
        action = request.form["action"]
        message = request.form["message"]
        
        if action == "encrypt":
            encrypted_message = cipher_suite.encrypt(message.encode()).decode()
        elif action == "decrypt":
            try:
                decrypted_message = cipher_suite.decrypt(message.encode()).decode()
            except Exception as e:
                decrypted_message = "Error decrypting message"

    return render_template("index.html", encrypted_message=encrypted_message, 
                           decrypted_message=decrypted_message)

if __name__ == "__main__":
    app.run(debug=True)

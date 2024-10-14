import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to generate a random password based on user criteria
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters  # Adds both uppercase and lowercase letters
    if use_numbers:
        characters += string.digits  # Adds numbers
    if use_symbols:
        characters += string.punctuation  # Adds symbols
    
    if not characters:
        return None  # If no character set is selected, return None

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    error = None

    if request.method == 'POST':
        try:
            # Get form data
            length = int(request.form['length'])
            use_letters = 'letters' in request.form
            use_numbers = 'numbers' in request.form
            use_symbols = 'symbols' in request.form
            
            if length <= 0:
                error = "Password length must be a positive number."
            else:
                password = generate_password(length, use_letters, use_numbers, use_symbols)
                if not password:
                    error = "Please select at least one character set (letters, numbers, symbols)."
        
        except ValueError:
            error = "Invalid input. Please enter a valid number for length."

    return render_template('index.html', password=password, error=error)

# Run the application on port 5001
if __name__ == '__main__':
    app.run(port=5001)

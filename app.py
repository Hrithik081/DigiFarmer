# from flask import Flask, render_template, request, redirect, url_for, flash, session

# app = Flask(__name__)
# app.secret_key = 'supersecretkey'  # Used for session management

# # Dummy user data
# users = {
#     'admin': 'password123',
#     'user1': 'mypassword'
# }

# @app.route('/')
# def home():
#     if 'username' in session:
#         return redirect(url_for('dashboard'))
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Check if username exists and password matches
#         if username in users and users[username] == password:
#             session['username'] = username
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials. Please try again.')
#             return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))
#     return render_template('dashboard.html', username=session['username'])

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     flash('You have been logged out.')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)






# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# import os

# app = Flask(__name__)
# app.secret_key = 'supersecretkey'

# # Configuration for file uploads
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure the uploads directory exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # Check allowed file extensions
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def home():
#     if 'username' in session:
#         return redirect(url_for('dashboard'))
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Dummy user authentication (replace with DB lookup in production)
#         if username == 'admin' and password == 'password123':
#             session['username'] = username
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials. Please try again.')
#             return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))
    
#     # List all uploaded files
#     uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('dashboard.html', username=session['username'], uploaded_files=uploaded_files)

# @app.route('/upload/<file_type>', methods=['POST'])
# def upload_file(file_type):
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))

#     # Check if the post request has the file part
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(url_for('dashboard'))
    
#     file = request.files['file']
    
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(url_for('dashboard'))
    
#     if file and allowed_file(file.filename):
#         # Save the file with a prefixed name to distinguish file types
#         filename = f"{file_type}_{session['username']}_{file.filename}"
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         flash(f'{file_type.capitalize()} card uploaded successfully.')
#         return redirect(url_for('dashboard'))

# @app.route('/uploads/<filename>')
# def view_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/delete/<filename>', methods=['POST'])
# def delete_file(filename):
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.exists(file_path):
#         os.remove(file_path)
#         flash('File deleted successfully.')
#     else:
#         flash('File not found.')
#     return redirect(url_for('dashboard'))

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     flash('You have been logged out.')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# import os

# app = Flask(__name__)
# app.secret_key = 'supersecretkey'

# # Configuration for file uploads
# UPLOAD_FOLDER = 'uploads'
# ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure the uploads directory exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# # Dummy user data for login (for production, replace with a database)
# users = {
#     'admin': 'password123',
#     'user1': 'mypassword'
# }

# # Helper function to check allowed file types
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def home():
#     if 'username' in session:
#         return redirect(url_for('main_dashboard'))
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Dummy user authentication (replace with DB lookup in production)
#         if username in users and users[username] == password:
#             session['username'] = username
#             return redirect(url_for('main_dashboard'))
#         else:
#             flash('Invalid credentials. Please try again.')
#             return redirect(url_for('login'))

#     return render_template('login.html')

# @app.route('/dashboard')
# def main_dashboard():
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))
    
#     return render_template('main_dashboard.html', username=session['username'])

# @app.route('/documents')
# def documents_dashboard():
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))

#     # List all uploaded files
#     uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('documents.html', username=session['username'], uploaded_files=uploaded_files)

# @app.route('/upload/<file_type>', methods=['POST'])
# def upload_file(file_type):
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))

#     # Check if the post request has the file part
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(url_for('documents_dashboard'))
    
#     file = request.files['file']
    
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(url_for('documents_dashboard'))
    
#     if file and allowed_file(file.filename):
#         # Save the file with a prefixed name to distinguish file types
#         filename = f"{file_type}_{session['username']}_{file.filename}"
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         flash(f'{file_type.capitalize()} card uploaded successfully.')
#         return redirect(url_for('documents_dashboard'))

# @app.route('/uploads/<filename>')
# def view_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/delete/<filename>', methods=['POST'])
# def delete_file(filename):
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.exists(file_path):
#         os.remove(file_path)
#         flash('File deleted successfully.')
#     else:
#         flash('File not found.')
#     return redirect(url_for('documents_dashboard'))

# @app.route('/digicard')
# def digicard_dashboard():
#     if 'username' not in session:
#         flash('You need to login first!')
#         return redirect(url_for('login'))

#     # Placeholder DigiCard page
#     return render_template('digicard.html', username=session['username'])

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     flash('You have been logged out.')
#     return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import os
import qrcode
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Dummy user data for login (for production, replace with a database)
users = {
    'admin': 'password123',
    'user1': 'mypassword'
}

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('main_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Dummy user authentication (replace with DB lookup in production)
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('main_dashboard'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def main_dashboard():
    if 'username' not in session:
        flash('You need to login first!')
        return redirect(url_for('login'))
    
    return render_template('main_dashboard.html', username=session['username'])

@app.route('/documents')
def documents_dashboard():
    if 'username' not in session:
        flash('You need to login first!')
        return redirect(url_for('login'))

    # List all uploaded files
    uploaded_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('documents.html', username=session['username'], uploaded_files=uploaded_files)

@app.route('/upload/<file_type>', methods=['POST'])
def upload_file(file_type):
    if 'username' not in session:
        flash('You need to login first!')
        return redirect(url_for('login'))

    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('documents_dashboard'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('documents_dashboard'))
    
    if file and allowed_file(file.filename):
        # Save the file with a prefixed name to distinguish file types
        filename = f"{file_type}_{session['username']}_{file.filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash(f'{file_type.capitalize()} card uploaded successfully.')
        return redirect(url_for('documents_dashboard'))

@app.route('/uploads/<filename>')
def view_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash('File deleted successfully.')
    else:
        flash('File not found.')
    return redirect(url_for('documents_dashboard'))

@app.route('/digicard', methods=['GET', 'POST'])
def digicard_dashboard():
    if 'username' not in session:
        flash('You need to login first!')
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Process user information and generate QR code
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']

        # Generate QR code containing user details
        qr_data = f"Name: {name}\nPhone: {phone}\nAddress: {address}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill='black', back_color='white')

        # Save QR code as image in memory (to display on the page)
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        qr_img_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Handle profile picture upload
        profile_picture = None
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = f"profile_{session['username']}_{file.filename}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                profile_picture = filename

        return render_template('digicard.html', 
                               username=session['username'], 
                               name=name, 
                               phone=phone, 
                               address=address, 
                               profile_picture=profile_picture, 
                               qr_img_data=qr_img_data)

    return render_template('digicard_form.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)




# # # Username: admin
# # # Password: password123
# # # Username: user1
# # # Password: mypassword
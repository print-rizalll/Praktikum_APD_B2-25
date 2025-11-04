from data_data import users_db, user_session

def validasi_login(username, password):
    try:
        valid = username in users_db and users_db[username]["password"] == password
        data = users_db[username] if valid else None
        return valid, data
    except:
        return False, None

def register_user(username, password, confirm_password):
    try:
        if not username or not password:
            return False, "Username dan password tidak boleh kosong!"
        
        if password != confirm_password:
            return False, "Password dan konfirmasi tidak cocok!"
        
        if username in users_db:
            return False, "Username sudah terdaftar!"
        
        if len(password) < 5:
            return False, "Password minimal 5 karakter!"
        
        users_db[username] = {"password": password, "role": "pengguna"}
        return True, "Registrasi berhasil!"
    except Exception as e:
        return False, f"Error: {e}"

def login_user(username, role):
    user_session["username"] = username
    user_session["role"] = role

def logout_user():
    user_session["username"] = None
    user_session["role"] = None
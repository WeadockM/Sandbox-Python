import sqlite3
import bcrypt

class AuthAgent():
  def __init__(self):
    self.dbConnection = sqlite3.connect('auth.db')
    self.dbCursor = self.dbConnection.cursor()
    self.pepper = b'P$n@'

  def get_connection(self):
    return self.dbConnection
  
  def get_cursor(self):
    return self.dbCursor
  
  def create_table(self):
    self.get_cursor().execute('''
      CREATE TABLE IF NOT EXISTS auth (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      external_id TEXT UNIQUE,
      password_hash TEXT NOT NULL,
      salt TEXT)
    ''')

  def create_test_auth(self):
    salt = bcrypt.gensalt()
    self.get_cursor().execute('INSERT OR REPLACE INTO auth (id, external_id, password_hash, salt) VALUES (?,?,?,?)',
      (1, 1, bcrypt.hashpw((self.pepper + b'admin'), salt), salt))
    self.get_connection().commit()

  def create_auth(self, externalId, password):
    salt = bcrypt.gensalt()
    passwordHash = bcrypt.hashpw((self.pepper + password.encode()), salt)
    self.get_cursor().execute('INSERT OR IGNORE INTO auth (external_id, password_hash, salt) VALUES (?,?,?)',
      (externalId, passwordHash, salt))
    self.get_connection().commit()

  def get_auth_list(self):
    res = self.get_cursor().execute('SELECT id, external_id, password_hash, salt FROM auth')
    return res.fetchall()

  def get_auth(self, externalId):
    res = self.get_cursor().execute('SELECT id, external_id, password_hash, salt FROM auth WHERE external_id = ?', (externalId,))
    return res.fetchall()
  
  def clear_auth_list(self):
    self.get_cursor().execute('DELETE FROM auth')
    self.get_connection().commit()

  def get_auth_by_credentials(self, externalId, password):
    salt = self.get_cursor().execute('SELECT salt FROM auth WHERE external_id = ?', (externalId,)).fetchone()[0]
    passwordHash = bcrypt.hashpw((self.pepper + password.encode()), salt)
    res = self.get_cursor().execute('SELECT * FROM auth WHERE external_id = ? AND password_hash = ?', (externalId, passwordHash)).fetchone()
    if res is None:
      return {'Success': False, 'External Id': ''}
    else:
      return {'Success': True, 'External Id': res[0]}
    
  def update_password(self, externalId, newPassword):
    salt = bcrypt.gensalt()
    passwordHash = bcrypt.hashpw((self.pepper + newPassword.encode()), salt)
    self.get_cursor().execute("UPDATE auth SET password_hash = ?, salt = ? WHERE external_id = ?", (passwordHash, salt, externalId))
    self.get_connection().commit()

authAgent = AuthAgent()

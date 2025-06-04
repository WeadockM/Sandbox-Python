<div align="center">

# 🔐 AuthAgent

**A lightweight authentication module using SQLite and bcrypt for secure password hashing**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)

</div>

---

## 🚀 Features

* ✅ Create and manage a simple `auth` table
* 🔒 Securely store passwords with bcrypt, salt, and a static pepper
* ➕ Add and retrieve user credentials
* 🔐 Authenticate users with provided credentials
* ♻️ Update existing passwords
* 🧹 Clear the database for testing or reset purposes

---

## 📦 Requirements

* Python 3.6+
* `bcrypt` library

Install requirements:

```bash
pip install bcrypt
```

---

## 💻 Usage

```python
from auth_agent import AuthAgent

# Instantiate and set up
auth = AuthAgent()
auth.create_table()

# Create a test admin user
auth.create_test_auth()

# Add a new user
auth.create_auth('user1', 'securepassword123')

# List all users
print(auth.get_auth_list())

# Authenticate user
result = auth.get_auth_by_credentials('user1', 'securepassword123')
print(result)  # {'Success': True, 'External Id': 1}

# Update a user's password
auth.update_password('user1', 'newpassword456')

# Clear all users (use cautiously)
auth.clear_auth_list()
```

---

## 🧱 Class: `AuthAgent`

### 🔧 Constructor

```python
auth = AuthAgent()
```

* Initializes the SQLite connection and sets a static pepper.

### 🛠️ Methods

#### `create_table()`

Creates the `auth` table if it doesn't exist.

#### `create_test_auth()`

Inserts a test user with `external_id = 1` and password `admin`.

#### `create_auth(externalId: str, password: str)`

Adds a new user to the database with hashed and salted password.

#### `get_auth_list() -> list`

Returns all records from the `auth` table.

#### `get_auth(externalId: str) -> list`

Returns a record for the specified `external_id`.

#### `clear_auth_list()`

Deletes all entries from the `auth` table.

#### `get_auth_by_credentials(externalId: str, password: str) -> dict`

Verifies user credentials. Returns:

```python
{'Success': True, 'External Id': <id>}
# or
{'Success': False, 'External Id': ''}
```

#### `update_password(externalId: str, newPassword: str)`

Updates the password (hash + salt) for the specified `external_id`.

---

## 🛡️ Security Notes

* A hardcoded **pepper** (`P$n@`) is used in password hashing for added security.
  ⚠️ **For production, move this to a secure config or environment variable.**
* Passwords are hashed with **bcrypt** and uniquely salted per user.

---

## 📄 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).

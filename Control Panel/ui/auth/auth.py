from PyQt5.QtWidgets import (
  QWidget,
  QVBoxLayout,
  QHBoxLayout,
  QLineEdit,
  QPushButton,
  QLabel,
  QMessageBox,
  QDesktopWidget,
)

from database.db import get_user_by_credentials

from ui.main_window import MainWindow

from utils.styles import AUTH_STYLE

class AuthApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 400, 300)

        # Create UI elements
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")

        # Layouts
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        self.form_layout.addWidget(self.username_label)
        self.form_layout.addWidget(self.username_input)
        self.form_layout.addWidget(self.password_label)
        self.form_layout.addWidget(self.password_input)

        self.button_layout.addWidget(self.login_button)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)

        self.setLayout(self.layout)

        # Connect login button to the authentication function
        self.login_button.clicked.connect(self.authenticate_user)

        # Connect Enter key to trigger login
        self.username_input.returnPressed.connect(self.authenticate_user)
        self.password_input.returnPressed.connect(self.authenticate_user)

        # Apply styling
        self.setStyleSheet(AUTH_STYLE)

    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def authenticate_user(self):
        """Authenticate the user by checking username and password"""
        username = self.username_input.text()
        password = self.password_input.text()

        # Query the database for the user credentials
        user = get_user_by_credentials(username, password)

        if user:
            QMessageBox.information(self, "Success", "Login successful!")
            self.username_input.clear()
            self.password_input.clear()

            # Hide the login window and open the main window
            self.hide()
            self.main_window = MainWindow()  # Create the main window object
            self.main_window.show()  # Show the main window
            self.main_window.center_on_screen()

        else:
            QMessageBox.warning(self, "Error", "Invalid username or password!")

    def apply_styles(self):
        """Apply modern styles to the authentication page"""
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f4f9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            QLabel {
                font-size: 18px;
                font-weight: 600;
                color: #333;
                margin-bottom: 10px;
            }

            QLineEdit {
                background-color: #fff;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                margin-bottom: 20px;
            }

            QLineEdit:focus {
                border: 2px solid #6C6AFF;
                background-color: #f1f1f1;
            }

            QPushButton {
                background-color: #6C6AFF;
                color: #fff;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                font-size: 16px;
                font-weight: bold;
                margin-top: 20px;
            }

            QPushButton:hover {
                background-color: #4b4eff;
            }

            QPushButton:pressed {
                background-color: #4040e0;
            }

            QVBoxLayout {
                spacing: 20px;
                padding: 20px;
            }

            QHBoxLayout {
                alignment: center;
                margin-top: 20px;
            }

            QFormLayout {
                spacing: 15px;
                margin-top: 20px;
            }

            QLineEdit, QPushButton {
                min-width: 250px;
            }

            /* Centering the layout horizontally */
            QWidget {
                margin-left: auto;
                margin-right: auto;
            }

            /* Make sure everything fits within a nice space */
            QVBoxLayout {
                margin: 0;
                padding: 0;
            }

            QFormLayout {
                margin: 0;
                padding: 0;
            }
        """)
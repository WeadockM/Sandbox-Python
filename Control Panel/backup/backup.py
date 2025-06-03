import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QApplication,
  QWidget,
  QVBoxLayout,
  QHBoxLayout,
  QLineEdit,
  QPushButton,
  QLabel,
  QMessageBox,
  QMainWindow,
  QListWidget,
  QTableWidget,
  QTableWidgetItem,
  QSplitter,
  QSpacerItem,
  QSizePolicy,
  QInputDialog,
  QFormLayout,
  QDialog,
  QStackedWidget,
  QDesktopWidget,
  QHeaderView
)

from database.db import (
    create_table,
    list_all_users,
    get_user_by_credentials,
    update_password,
    update_user,
    insert_user,
    get_connection
)

from ui.auth.auth import AuthApp

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
        self.apply_styles()

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Control Panel')
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget and set the layout
        central_widget = QWidget(self)
        central_layout = QHBoxLayout()

        # Create the QSplitter for the navigation bar and the main content area
        self.splitter = QSplitter(Qt.Horizontal)

        # Left side - Navigation menu
        self.nav_menu = QListWidget(self)
        self.nav_menu.addItem('Home')
        self.nav_menu.addItem('Settings')
        self.nav_menu.addItem('Users')
        self.nav_menu.addItem('About')

        # Connect selection change event
        self.nav_menu.currentItemChanged.connect(self.change_content)

        # Right side - Main content area (using QStackedWidget)
        self.stacked_widget = QStackedWidget(self)
        self.home_page = QLabel('Welcome to the Home page!')
        self.about_page = QLabel('About us: This is a simple PyQt5 GUI.')
        self.settings_page = QLabel('Settings: Customize your preferences here.')

        # Style labels on pages for nicer header appearance
        for label in (self.home_page, self.about_page, self.settings_page):
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 24px; font-weight: 600; color: #222; padding: 20px;")

        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.about_page)
        self.stacked_widget.addWidget(self.settings_page)

        # Add navigation menu and main content to the splitter
        self.splitter.addWidget(self.nav_menu)
        self.splitter.addWidget(self.stacked_widget)

        # Set the splitter proportions
        self.splitter.setSizes([200, 600])  # Set fixed width for the navigation menu

        # Set up the layout
        central_layout.addWidget(self.splitter)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        # Apply styling to the navigation bar and other UI parts
        self.apply_styles()

    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def change_content(self):
        current_item = self.nav_menu.currentItem()
        if current_item:
            selected_text = current_item.text()
            if selected_text == 'Home':
                self.stacked_widget.setCurrentWidget(self.home_page)
            elif selected_text == 'About':
                self.stacked_widget.setCurrentWidget(self.about_page)
            elif selected_text == 'Settings':
                self.stacked_widget.setCurrentWidget(self.settings_page)
            elif selected_text == 'Users':
                self.show_users()

    def apply_styles(self):
        # Navigation bar styling
        self.nav_menu.setStyleSheet("""
            QListWidget {
                background-color: #2c2f33;
                color: #fff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 18px;
                border: none;
                border-radius: 10px;
                padding: 0;
                margin: 0;
            }

            QListWidget::item {
                padding: 12px;
                margin-bottom: 4px;
                border-radius: 8px;
                background-color: #40444b;
            }

            QListWidget::item:hover {
                background-color: #5865f2;
            }

            QListWidget::item:selected {
                background-color: #4752c4;
                color: #fff;
                font-weight: bold;
            }

            QListWidget::item:!selected {
                background-color: #40444b;
                color: #fff;
            }
        """)

        # Main window background and content styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f6fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 16px;
                color: #333;
            }

            QStackedWidget {
                background-color: #ffffff;
                border-radius: 12px;
                padding: 30px;
                margin: 20px;
                /* shadow effect */
                border: 1px solid #ddd;
            }

            QLabel {
                color: #222;
            }

            QPushButton {
                background-color: #5865f2;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 600;
                min-width: 120px;
            }

            QPushButton:hover {
                background-color: #4752c4;
            }

            QPushButton:pressed {
                background-color: #3b41a6;
            }

            /* Style QTableWidget in users page */
            QTableWidget {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 8px;
                gridline-color: #ddd;
                font-size: 15px;
            }

            QHeaderView::section {
                background-color: #5865f2;
                color: white;
                font-weight: bold;
                border: none;
                padding: 5px;
            }
        """)

    def show_users(self):
        users = list_all_users()

        if users:
            # Create a table widget for the users list
            self.user_table = QTableWidget(self)
            self.user_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.user_table.setRowCount(len(users))
            self.user_table.setColumnCount(3)  # Now three columns: ID, Username, and Email
            self.user_table.setHorizontalHeaderLabels(["ID", "Username", "Email"])
            self.user_table.horizontalHeader().setStretchLastSection(True)
            self.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


            # Populate the table with the user data
            for row, user in enumerate(users):
                self.user_table.setItem(row, 0, QTableWidgetItem(str(user[0])))  # ID
                self.user_table.setItem(row, 1, QTableWidgetItem(user[1]))  # Username
                self.user_table.setItem(row, 2, QTableWidgetItem(user[2]))  # Email

            # Make the table rows selectable
            self.user_table.setSelectionBehavior(QTableWidget.SelectRows)

            # Create the header label for the user page
            header_label = QLabel("User List", self)
            header_label.setAlignment(Qt.AlignCenter)
            header_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-bottom: 20px;")

            # Add the Reset Password and Add User buttons
            self.reset_password_button = QPushButton("Reset Password", self)
            self.add_user_button = QPushButton("Add User", self)
            self.edit_user_button = QPushButton("Edit User", self)
            self.edit_user_button.clicked.connect(lambda: self.edit_user(self.user_table))


            # Connect the buttons to their respective functions
            self.reset_password_button.clicked.connect(self.reset_password)
            self.add_user_button.clicked.connect(self.add_user)

            # Create a layout to center the header, table, and buttons
            user_layout = QVBoxLayout()
            user_layout.addWidget(header_label)
            user_layout.addWidget(self.user_table)
            
            # Create horizontal layout for action buttons
            button_layout = QHBoxLayout()
            button_layout.addWidget(self.reset_password_button)
            button_layout.addWidget(self.edit_user_button)
            button_layout.addWidget(self.add_user_button)

            # Optional: add spacing between buttons
            button_layout.setSpacing(20)

            # Add button layout to main user layout
            user_layout.addLayout(button_layout)
            user_layout.addSpacing(15)

            # Add some spacing to center the table vertically
            spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
            user_layout.addItem(spacer)

            # Create a widget to contain the header, table, and buttons
            user_widget = QWidget(self)
            user_widget.setLayout(user_layout)

            # Set the users widget as the current page in the stacked widget
            if hasattr(self, 'user_widget'):
              self.stacked_widget.removeWidget(self.user_widget)

            self.user_widget = user_widget
            self.stacked_widget.addWidget(self.user_widget)
            self.stacked_widget.setCurrentWidget(self.user_widget)

        else:
            self.stacked_widget.setCurrentWidget(self.home_page)  # Fallback to home page if no users found
            QMessageBox.warning(self, "No Users", "No users found.")

    def reset_password(self):
        """Reset the password for the selected user"""
        # Get the selected row
        selected_row = self.user_table.currentRow()
        if selected_row != -1:
            user_id = self.user_table.item(selected_row, 0).text()
            new_password, ok = QInputDialog.getText(self, "Reset Password", f"Enter new password for user ID {user_id}:", QLineEdit.Password)
            if ok and new_password:
                update_password(user_id, new_password)
                QMessageBox.information(self, "Success", "Password reset successfully!")
                self.show_users()  # Refresh the user list after the reset
            else:
                QMessageBox.warning(self, "Error", "Password reset failed or not provided.")
        else:
            QMessageBox.warning(self, "Error", "No user selected.")

    def add_user(self):
        """Show the Add User dialog and create a new user"""
        dialog = AddUserDialog(get_connection())
        dialog.exec_()

    def edit_user(self, table):
      selected_row = table.currentRow()
      if selected_row != -1:
          user_id = table.item(selected_row, 0).text()
          current_username = table.item(selected_row, 1).text()
          current_email = table.item(selected_row, 2).text()

          dialog = QDialog(self)
          dialog.setWindowTitle("Edit User")
          dialog.setFixedSize(300, 200)

          layout = QFormLayout(dialog)

          username_input = QLineEdit(current_username)
          email_input = QLineEdit(current_email)

          layout.addRow("Username:", username_input)
          layout.addRow("Email:", email_input)

          save_button = QPushButton("Save")
          cancel_button = QPushButton("Cancel")
          save_button.clicked.connect(lambda: self.save_edited_user(user_id, username_input.text(), email_input.text(), dialog))

          button_layout = QHBoxLayout()
          button_layout.addWidget(save_button)
          button_layout.addWidget(cancel_button)
          layout.addRow(button_layout)

          cancel_button.clicked.connect(dialog.reject)
          dialog.exec_()
      else:
          QMessageBox.warning(self, "Error", "No user selected.")

    def save_edited_user(self, user_id, new_username, new_email, dialog):
      if new_username and new_email:
          update_user(user_id, new_username, new_email)
          QMessageBox.information(self, "Success", "User updated successfully!")
          dialog.accept()
          self.show_users()  # Refresh the table
      else:
          QMessageBox.warning(self, "Error", "All fields are required.")

class AddUserDialog(QDialog):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Add User")
        self.setGeometry(150, 150, 400, 200)

        # Create the form layout
        self.form_layout = QFormLayout()

        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.email_input = QLineEdit(self)

        self.form_layout.addRow("Username:", self.username_input)
        self.form_layout.addRow("Password:", self.password_input)
        self.form_layout.addRow("Email:", self.email_input)

        # Create the buttons
        self.add_button = QPushButton("Add User", self)
        self.cancel_button = QPushButton("Cancel", self)

        self.form_layout.addRow(self.add_button, self.cancel_button)

        # Set the dialog layout
        self.setLayout(self.form_layout)

        # Connect buttons
        self.add_button.clicked.connect(self.add_user)
        self.cancel_button.clicked.connect(self.reject)

    def add_user(self):
        """Add a new user to the database"""
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()

        if username and password and email:
            insert_user(username, password, email)
            QMessageBox.information(self, "Success", "User added successfully!")
            self.accept()  # Close the dialog
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields.")


def main():
    create_table()
    app = QApplication(sys.argv)
    window = AuthApp()  # Show the login page initially
    window.show()
    window.center_on_screen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

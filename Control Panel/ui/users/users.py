from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
  QWidget,
  QVBoxLayout,
  QHBoxLayout,
  QPushButton,
  QLabel,
  QMessageBox,
  QHeaderView,
  QSizePolicy,
  QTableWidget,
  QTableWidgetItem,
  QSpacerItem,
  QInputDialog,
  QLineEdit,
  QDialog,
  QFormLayout
)

from database.db import list_all_users, update_password, update_user, insert_user, get_connection

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

class UsersPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
    
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
              mainWindow.removeWidget(self.user_widget)

            self.user_widget = user_widget
            mainWindow.addWidget(self.user_widget)
            mainWindow.setCurrentWidget(self.user_widget)

        else:
            mainWindow.setCurrentWidget(self.home_page)  # Fallback to home page if no users found
            QMessageBox.warning(self, "No Users", "No users found.")

    def show_users(self, mainWindow):
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
            mainWindow.removeWidget(self.user_widget)

          self.user_widget = user_widget
          mainWindow.addWidget(self.user_widget)
          mainWindow.setCurrentWidget(self.user_widget)

      else:
          mainWindow.setCurrentWidget(self.home_page)  # Fallback to home page if no users found
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
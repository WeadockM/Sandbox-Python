import sys
from PyQt5.QtWidgets import QApplication
from database.db import create_table
from ui.auth.auth import AuthApp

def main():
    create_table()
    app = QApplication(sys.argv)
    window = AuthApp()  # Show the login page initially
    window.show()
    window.center_on_screen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

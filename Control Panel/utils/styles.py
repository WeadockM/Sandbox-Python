# style.py

MAIN_STYLE = """
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
        """

AUTH_STYLE = """
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
        """

NAV_STYLE = """
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
        """
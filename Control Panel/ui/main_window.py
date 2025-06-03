from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QWidget,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QListWidget,
  QSplitter,
  QStackedWidget,
  QDesktopWidget,
)


from ui.users.users import UsersPage

from utils.styles import NAV_STYLE, MAIN_STYLE

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

        # Navigation bar styling
        self.nav_menu.setStyleSheet(NAV_STYLE)
        # Main window background and content styling
        self.setStyleSheet(MAIN_STYLE)

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
                UsersPage(self.stacked_widget)

    def apply_styles(self):
        # Navigation bar styling
        self.nav_menu.setStyleSheet(NAV_STYLE)

        # Main window background and content styling
        self.setStyleSheet(MAIN_STYLE)
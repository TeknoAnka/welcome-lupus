import os
import sys
import subprocess
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QSpacerItem, 
                             QSizePolicy)
from PyQt6.QtCore import Qt, QSize, QUrl, QPoint
from PyQt6.QtGui import QFont, QColor, QPalette, QDesktopServices, QIcon

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to LupuS")
        self.setFixedSize(800, 500)
        self.setWindowIcon(QIcon("icons/lupus.png"))
        
        # Frameless Window
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Center the window on screen
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Main Widget and Layout
        self.main_widget = QWidget()
        self.main_widget.setObjectName("MainContainer")
        self.setCentralWidget(self.main_widget)
        
        self.layout = QVBoxLayout(self.main_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Style Sheets (QSS)
        self.setStyleSheet("""
            QWidget#MainContainer {
                background-color: #121212;
                border-radius: 15px;
                border: 1px solid #00bcff;
            }
            QLabel#Title {
                color: #00bcff;
                font-size: 48px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            QLabel#Subtitle {
                color: #B0B0B0;
                font-size: 18px;
                margin-bottom: 30px;
            }
            QPushButton {
                background-color: #1E1E1E;
                color: #E0E0E0;
                border: 1px solid #333333;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 16px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #2C2C2C;
                border: 1px solid #00bcff;
            }
            QPushButton#CloseBtn {
                background-color: transparent;
                border: none;
                border-radius: 0;
                min-width: 40px;
                max-width: 40px;
                padding: 5px;
                margin-top: 9px;
            }
            QFrame#Separator {
                background-color: #333333;
                max-height: 1px;
            }
        """)

        # UI Elements
        self.setup_ui()

        # For window dragging
        self.oldPos = self.pos()

    def setup_ui(self):

        # Separator
        separator = QFrame()
        separator.setObjectName("Separator")

        # Title Bar (for Close Button)
        title_bar = QHBoxLayout()
        title_bar.setContentsMargins(10, 10, 10, 0)
        title_bar.addStretch()
        
        self.close_btn = QPushButton()
        self.close_btn.setIcon(QIcon("icons/close.png"))
        self.close_btn.setObjectName("CloseBtn")
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.clicked.connect(self.close)
        title_bar.addWidget(self.close_btn)

        # Content Container
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(50, 0, 50, 50)
        content_layout.setSpacing(20)

        folder = os.path.dirname(os.path.abspath(__file__))
        icon = os.path.join(folder, "icons/lupus.png")

        # Header Section
        self.title_label = QLabel()
        self.title_label.setText(
            f"<table border='0' cellpadding='0' cellspacing='0' align='center'>"
            f"  <tr>"
            f"    <td valign='middle'>"
            f"      <img src='{icon}' width='100' height='100' />"
            f"    </td>"
            f"    <td valign='middle' style='padding-left: 12px;'>"
            f"      LupuS"
            f"    </td>"
            f"  </tr>"
            f"</table>"
        )
        self.title_label.setObjectName("Title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.subtitle_label = QLabel("The Power of Freedom, The Spirit of Speed.")
        self.subtitle_label.setObjectName("Subtitle")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setWordWrap(True)
        
        self.layout.addLayout(title_bar)

        content_layout.addWidget(separator)

        content_layout.addWidget(separator)

        content_layout.addWidget(self.title_label)

        content_layout.addWidget(separator)
        content_layout.addWidget(self.subtitle_label)
        
        content_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Button Section
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)
        btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.install = QPushButton("Install")
        self.install.setCursor(Qt.CursorShape.PointingHandCursor)
        self.install.clicked.connect(self.run_yali)

        btn_layout.addWidget(self.install)

        content_layout.addLayout(btn_layout)
        
        content_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.layout.addLayout(content_layout)

    # Window Dragging Logic
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

    def run_yali(self):
        try:
            subprocess.Popen(["yali"])
        except Exception as e:
            print(f"Error starting 'yali': {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec())

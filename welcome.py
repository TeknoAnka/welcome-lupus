import sys
import os
import subprocess
import shutil
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame, QSpacerItem, 
                             QSizePolicy, QCheckBox)
from PyQt6.QtCore import Qt, QSize, QUrl, QPoint
from PyQt6.QtGui import QFont, QColor, QPalette, QDesktopServices, QIcon, QPixmap

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to LupuS")
        self.setFixedSize(1000, 600)
        self.setWindowIcon(QIcon("icons/lupus.png"))

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
            QFrame#Separator {
                background-color: #333333;
                max-height: 1px;
            }
            QPushButton#Website, QPushButton#Github, QPushButton#YouTube, QPushButton#X {
                border: none;
                margin: 0;
            }
            QLabel#Title {
                color: #00bcff;
                font-size: 40px;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            QLabel#Subtitle {
                color: #B0B0B0;
                font-size: 18px;
                margin-bottom: 10px;
            }
            QWidget#MainContainer {
                background-color: #121212;
                border-radius: 15px;
                border: 1px solid #00bcff;
            }
            QPushButton#CloseBtn {
                background-color: transparent;
                margin-top: 9px;
                border: none;
                min-width: 40px;
                max-width: 40px;
                padding: 5px;
            }
            QPushButton#CenterBtn {
                background-color: #1E1E1E;
                color: #E0E0E0;
                border: 1px solid #333333;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 16px;
                min-width: 150px;
            }
            QPushButton#CenterBtn:hover {
                background-color: #2C2C2C;
                border: 1px solid #00bcff;
            }
            QCheckBox {
                color: #B0B0B0;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 4px;
                border: 1px solid #333333;
                background-color: #1E1E1E;
            }
            QCheckBox::indicator:hover {
                border: 1px solid #00bcff;
            }
            QCheckBox::indicator:checked {
                background-color: #00bcff;
                border: 1px solid #00bcff;
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

        windowbar = QHBoxLayout()
        windowbar.setContentsMargins(10, 10, 10, 0)
        windowbar.addStretch()

        folder = os.path.dirname(os.path.abspath(__file__))
        icon = os.path.join(folder, "icons/lupus.png")
        
        self.close_btn = QPushButton()
        self.close_btn.setIcon(QIcon("icons/close.png"))
        self.close_btn.setObjectName("CloseBtn")
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.clicked.connect(self.close)

        windowbar.addWidget(self.close_btn)

        self.layout.addLayout(windowbar)

        title_bar = QLabel()
        title_bar.setText(
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
        title_bar.setContentsMargins(10, 10, 10, 10)
        title_bar.setObjectName("Title")

        self.subtitle_label = QLabel("The Power of Freedom, The Spirit of Speed.")
        self.subtitle_label.setObjectName("Subtitle")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setWordWrap(True)

        self.Kaptan = QPushButton("Kaptan")
        self.Kaptan.setObjectName("CenterBtn")
        self.Kaptan.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Kaptan.clicked.connect(self.open_kaptan)

        self.Updater = QPushButton("PiSi Updater")
        self.Updater.setObjectName("CenterBtn")
        self.Updater.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Updater.clicked.connect(self.open_updater)

        self.Gaming = QPushButton("Install GameTools")
        self.Gaming.setObjectName("CenterBtn")
        self.Gaming.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Gaming.clicked.connect(self.open_gmi)

        self.Graphics = QPushButton("Install Graphics")
        self.Graphics.setObjectName("CenterBtn")
        self.Graphics.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Graphics.clicked.connect(self.open_gci)

        self.DNS = QPushButton("DNS Changer")
        self.DNS.setObjectName("CenterBtn")
        self.DNS.setCursor(Qt.CursorShape.PointingHandCursor)
        self.DNS.clicked.connect(self.open_dnsc)

        self.Printer = QPushButton("Add Printer")
        self.Printer.setObjectName("CenterBtn")
        self.Printer.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Printer.clicked.connect(self.add_printer)

        self.Winboat = QPushButton("Install Winboat")
        self.Winboat.setObjectName("CenterBtn")
        self.Winboat.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Winboat.clicked.connect(self.install_winboat)

        self.Waydroid = QPushButton("Install Waydroid")
        self.Waydroid.setObjectName("CenterBtn")
        self.Waydroid.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Waydroid.clicked.connect(self.install_waydroid)

        center_btn_layout = QHBoxLayout()
        center_btn_layout.setSpacing(20)
        center_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        second_center_btn_layout = QHBoxLayout()
        second_center_btn_layout.setSpacing(20)
        second_center_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        third_center_btn_layout = QHBoxLayout()
        third_center_btn_layout.setSpacing(20)
        third_center_btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(title_bar)
        self.layout.addWidget(separator)
        self.layout.addWidget(self.subtitle_label)

        center_btn_layout.addWidget(self.Kaptan)
        center_btn_layout.addWidget(self.Updater)
        center_btn_layout.addWidget(self.Graphics)

        second_center_btn_layout.addWidget(self.Gaming)
        second_center_btn_layout.addWidget(self.Waydroid)
        second_center_btn_layout.addWidget(self.Winboat)

        third_center_btn_layout.addWidget(self.DNS)
        third_center_btn_layout.addWidget(self.Printer)

        # Content Container
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(50, 0, 50, 50)
        content_layout.setSpacing(20)
        content_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        content_layout.addWidget(separator)
        content_layout.addWidget(separator)

        content_layout.addLayout(center_btn_layout)
        content_layout.addLayout(second_center_btn_layout)
        content_layout.addLayout(third_center_btn_layout)

        content_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Button Section
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)
        btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Website = QPushButton()
        self.Website.setIcon(QIcon("icons/teknoanka.png"))
        self.Website.setObjectName("Website")
        self.Website.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Website.clicked.connect(self.open_website)
        
        self.Github = QPushButton()
        self.Github.setIcon(QIcon("icons/github.png"))
        self.Github.setObjectName("Github")
        self.Github.setCursor(Qt.CursorShape.PointingHandCursor)
        self.Github.clicked.connect(self.open_github)
        
        self.X = QPushButton()
        self.X.setIcon(QIcon("icons/x.png"))
        self.X.setObjectName("X")
        self.X.setCursor(Qt.CursorShape.PointingHandCursor)
        self.X.clicked.connect(self.open_x)

        self.YouTube = QPushButton()
        self.YouTube.setIcon(QIcon("icons/youtube.png"))
        self.YouTube.setObjectName("YouTube")
        self.YouTube.setCursor(Qt.CursorShape.PointingHandCursor)
        self.YouTube.clicked.connect(self.open_youtube)

        btn_layout.addWidget(self.Website)
        btn_layout.addWidget(self.Github)
        btn_layout.addWidget(self.YouTube)
        btn_layout.addWidget(self.X)

        # Bottom Row: Autostart Checkbox on Left, Social Icons Centered
        bottom_row_layout = QHBoxLayout()
        bottom_row_layout.setContentsMargins(0, 0, 0, 0)

        self.autostart_cb = QCheckBox("Run on startup")
        self.autostart_cb.setCursor(Qt.CursorShape.PointingHandCursor)

        # Check current autostart status
        autostart_path = os.path.expanduser("~/.config/autostart/lupus-welcome.desktop")
        if os.path.exists(autostart_path):
            self.autostart_cb.setChecked(True)

        self.autostart_cb.toggled.connect(self.toggle_autostart)

        left_spacer_widget = QWidget()
        left_spacer_widget.setMinimumWidth(160)
        left_layout = QHBoxLayout(left_spacer_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.addWidget(self.autostart_cb)

        right_spacer_widget = QWidget()
        right_spacer_widget.setMinimumWidth(160)

        bottom_row_layout.addWidget(left_spacer_widget)
        bottom_row_layout.addStretch()
        bottom_row_layout.addLayout(btn_layout)
        bottom_row_layout.addStretch()
        bottom_row_layout.addWidget(right_spacer_widget)

        content_layout.addLayout(bottom_row_layout)

        self.layout.addLayout(content_layout)

    def toggle_autostart(self, checked):
        autostart_dir = os.path.expanduser("~/.config/autostart")
        autostart_file = os.path.join(autostart_dir, "lupus-welcome.desktop")
        desktop_file = os.path.expanduser("~/.local/share/applications/lupus-welcome.desktop")

        if checked:
            try:
                os.makedirs(autostart_dir, exist_ok=True)
                if os.path.exists(desktop_file):
                    shutil.copy(desktop_file, autostart_file)
                else:
                    bin_path = os.path.expanduser("~/.local/bin/lupus-welcome")
                    icon_path = os.path.expanduser("~/.local/share/lupus-welcome/icons/lupus.png")
                    if not os.path.exists(icon_path):
                        folder = os.path.dirname(os.path.abspath(__file__))
                        icon_path = os.path.join(folder, "icons/lupus.png")
                    with open(autostart_file, "w", encoding="utf-8") as f:
                        f.write(
                            "[Desktop Entry]\n"
                            "Version=1.0\n"
                            "Type=Application\n"
                            "Name=LupuS Welcome\n"
                            "Comment=LupuS Hoş Geldiniz Uygulaması\n"
                            f"Exec={bin_path}\n"
                            f"Icon={icon_path}\n"
                            "Terminal=false\n"
                            "Categories=Utility;System;\n"
                            "StartupNotify=true\n"
                        )
            except Exception as e:
                print(f"Autostart ekleme hatası: {e}")
        else:
            if os.path.exists(autostart_file):
                try:
                    os.remove(autostart_file)
                except Exception as e:
                    print(f"Autostart kaldırma hatası: {e}")

    # Window Dragging Logic
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()

    def open_website(self):
        QDesktopServices.openUrl(QUrl("https://www.teknoanka.com"))

    def open_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/TeknoAnka"))
    
    def open_x(self):
        QDesktopServices.openUrl(QUrl("https://x.com/TeknoAnka"))

    def open_youtube(self):
        QDesktopServices.openUrl(QUrl("https://www.youtube.com/@TeknoAnkaOfficial"))

    def open_kaptan(self):
        subprocess.Popen(["kaptan"])

    def open_gmi(self):
        subprocess.Popen(["game-tools-installer"])

    def open_dnsc(self):
        subprocess.Popen(["dns-changer"])

    def install_waydroid(self):
        subprocess.check_call(["alacritty --command sudo pisi it waydroid"], shell=True)

    def install_winboat(self):
        subprocess.check_call(["alacritty --command sudo pisi it winboat"], shell=True)

    def open_updater(self):
        subprocess.Popen(["pisi-update"])

    def open_gci(self):
        subprocess.Popen(["graphics-card-installer"])

    def add_printer(self):
        subprocess.Popen(["system-config-printer"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec())

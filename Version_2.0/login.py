from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QFrame, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, pyqtSignal, QPropertyAnimation, QPoint, QTimer
from PyQt5.QtGui import QFont, QColor

class LoginWindow(QWidget):
    login_successful = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Gym Management System - Login")
        self.setGeometry(100, 100, 500, 650)
        self.setFixedSize(500, 650)
        self.setObjectName("MainWindow")
        
        self.setStyleSheet("""
            QWidget#MainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364);
            }
        """)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        self.login_card = QFrame()
        self.login_card.setStyleSheet("""
            QFrame {
                background: rgba(20, 25, 30, 0.7);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
        """)
        self.login_card.setFixedSize(420, 520)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 20)
        self.login_card.setGraphicsEffect(shadow)
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(20)
        
        logo = QLabel("🏋")
        logo.setFont(QFont("Segoe UI", 40))
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("background: transparent; border: none; color: #00d2ff;")
        card_layout.addWidget(logo)
        
        title = QLabel("GYM Management System")
        title.setFont(QFont("Segoe UI Black", 15))
        title.setStyleSheet("color: white; background: transparent; border: none; letter-spacing: 2px;")
        title.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title)
        
        subtitle = QLabel("Welcome Back!")
        subtitle.setFont(QFont("Segoe UI", 11, QFont.Bold))
        subtitle.setStyleSheet("color: #00d2ff; background: transparent; border: none; letter-spacing: 4px;")
        subtitle.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(subtitle)
        
        card_layout.addSpacing(15)
        
        username_container = QFrame()
        username_container.setStyleSheet("""
            QFrame {
                background: rgba(0, 0, 0, 0.4);
                border-radius: 12px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }
            QFrame:hover {
                border: 1px solid rgba(0, 210, 255, 0.5);
            }
        """)
        username_layout = QHBoxLayout()
        username_layout.setContentsMargins(15, 8, 15, 8)
        
        username_icon = QLabel("👤")
        username_icon.setFont(QFont("Segoe UI", 16))
        username_icon.setStyleSheet("background: transparent; border: none; color: #a0a5a8;")
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                color: white;
                font-family: 'Segoe UI';
                font-size: 15px;
                padding: 5px;
            }
            QLineEdit::placeholder {
                color: #6c757d;
            }
        """)
        
        username_layout.addWidget(username_icon)
        username_layout.addWidget(self.username_input)
        username_container.setLayout(username_layout)
        card_layout.addWidget(username_container)
        
        password_container = QFrame()
        password_container.setStyleSheet("""
            QFrame {
                background: rgba(0, 0, 0, 0.4);
                border-radius: 12px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }
            QFrame:hover {
                border: 1px solid rgba(0, 210, 255, 0.5);
            }
        """)
        password_layout = QHBoxLayout()
        password_layout.setContentsMargins(15, 8, 15, 8)
        
        password_icon = QLabel("🔒")
        password_icon.setFont(QFont("Segoe UI", 16))
        password_icon.setStyleSheet("background: transparent; border: none; color: #a0a5a8;")
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                color: white;
                font-family: 'Segoe UI';
                font-size: 15px;
                padding: 5px;
            }
            QLineEdit::placeholder {
                color: #6c757d;
            }
        """)
        
        password_layout.addWidget(password_icon)
        password_layout.addWidget(self.password_input)
        password_container.setLayout(password_layout)
        card_layout.addWidget(password_container)
        
        card_layout.addSpacing(15)
        
        self.login_btn = QPushButton("SECURE LOGIN")
        self.login_btn.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0052D4, stop:0.5 #4364F7, stop:1 #6FB1FC);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 16px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6FB1FC, stop:0.5 #4364F7, stop:1 #0052D4);
            }
            QPushButton:pressed {
                background: #003a99;
            }
        """)
        self.login_btn.clicked.connect(self.check_login)
        card_layout.addWidget(self.login_btn)
        
        info_label = QLabel("Username: admin / Password: admin")
        info_label.setFont(QFont("Segoe UI", 9))
        info_label.setStyleSheet("color: #6c757d; background: transparent; border: none;")
        info_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(info_label)
        
        self.login_card.setLayout(card_layout)
        layout.addWidget(self.login_card)
        self.setLayout(layout)
        
        self.password_input.returnPressed.connect(self.check_login)
    
    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if username == "admin" and password == "admin":
            self.login_btn.setText("✓ ACCESS GRANTED")
            self.login_btn.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #11998e, stop:1 #38ef7d);
                    color: white;
                    border: none;
                    border-radius: 12px;
                    padding: 16px;
                    font-weight: bold;
                    letter-spacing: 1px;
                }
            """)
            QTimer.singleShot(500, self.login_successful.emit)
            QTimer.singleShot(500, self.close)
        else:
            self.shake_window()
            self.login_btn.setText("✗ ACCESS DENIED")
            self.login_btn.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #cb2d3e, stop:1 #ef473a);
                    color: white;
                    border: none;
                    border-radius: 12px;
                    padding: 16px;
                    font-weight: bold;
                    letter-spacing: 1px;
                }
            """)
            QTimer.singleShot(2000, self.reset_login_button)
            self.password_input.clear()
            self.password_input.setFocus()
    
    def shake_window(self):
        original_pos = self.pos()
        self.shake_anim = QPropertyAnimation(self, b"pos")
        self.shake_anim.setDuration(400)
        self.shake_anim.setLoopCount(1)
        
        self.shake_anim.setKeyValueAt(0, original_pos)
        self.shake_anim.setKeyValueAt(0.1, original_pos + QPoint(-10, 0))
        self.shake_anim.setKeyValueAt(0.2, original_pos + QPoint(10, 0))
        self.shake_anim.setKeyValueAt(0.3, original_pos + QPoint(-10, 0))
        self.shake_anim.setKeyValueAt(0.4, original_pos + QPoint(10, 0))
        self.shake_anim.setKeyValueAt(0.5, original_pos + QPoint(-10, 0))
        self.shake_anim.setKeyValueAt(0.6, original_pos + QPoint(10, 0))
        self.shake_anim.setKeyValueAt(0.7, original_pos + QPoint(-5, 0))
        self.shake_anim.setKeyValueAt(0.8, original_pos + QPoint(5, 0))
        self.shake_anim.setKeyValueAt(0.9, original_pos + QPoint(-2, 0))
        self.shake_anim.setKeyValueAt(1, original_pos)
        
        self.shake_anim.start()
    
    def reset_login_button(self):
        self.login_btn.setText("SECURE LOGIN")
        self.login_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0052D4, stop:0.5 #4364F7, stop:1 #6FB1FC);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 16px;
                letter-spacing: 1px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6FB1FC, stop:0.5 #4364F7, stop:1 #0052D4);
            }
            QPushButton:pressed {
                background: #003a99;
            }
        """)

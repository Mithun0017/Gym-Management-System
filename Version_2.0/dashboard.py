import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QFrame, QGraphicsDropShadowEffect, QScrollArea)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class DashboardCard(QPushButton):
    def __init__(self, title, subtitle, icon_text, neon_color, parent=None):
        super().__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedHeight(150)
        self.neon_color = neon_color
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(8)
        
        self.icon_label = QLabel(icon_text)
        self.icon_label.setFont(QFont("Segoe UI Emoji", 32)) 
        self.icon_label.setStyleSheet("background: transparent; border: none;")
        self.icon_label.setAlignment(Qt.AlignLeft)
        
        self.title_label = QLabel(title)
        self.title_label.setFont(QFont("Segoe UI", 14, QFont.Bold))
        self.title_label.setStyleSheet("color: white; background: transparent; border: none;")
        self.title_label.setAlignment(Qt.AlignLeft)
        
        self.subtitle_label = QLabel(subtitle)
        self.subtitle_label.setFont(QFont("Segoe UI", 10))
        self.subtitle_label.setStyleSheet("color: #a0a5a8; background: transparent; border: none;")
        self.subtitle_label.setAlignment(Qt.AlignLeft)
        self.subtitle_label.setWordWrap(True)

        layout.addWidget(self.icon_label)
        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)
        layout.addStretch()

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: rgba(0, 0, 0, 0.4);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }}
            QPushButton:hover {{
                background-color: rgba(20, 30, 40, 0.8);
                border: 1px solid {self.neon_color};
            }}
            QPushButton:pressed {{
                background-color: rgba(0, 0, 0, 0.8);
                border: 1px solid {self.neon_color};
            }}
        """)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(8)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.setGraphicsEffect(shadow)

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Gym Management System - Dashboard")
        self.setMinimumSize(900, 600)
        self.resize(1100, 750)
        self.setObjectName("DashboardMain")
        
        self.setStyleSheet("""
            QWidget#DashboardMain {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364);
            }
        """)
        
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = QFrame()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: rgba(10, 15, 20, 0.7);
                border-right: 1px solid rgba(255, 255, 255, 0.08);
            }
        """)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(20, 40, 20, 20)

        brand = QLabel("GYM")
        brand.setFont(QFont("Segoe UI", 22, QFont.Bold))
        brand.setStyleSheet("color: white; background: transparent; border: none; letter-spacing: 2px;")
        brand.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(brand)
        
        sidebar_layout.addSpacing(40)
        
        welcome = QLabel("Welcome Admin!")
        welcome.setFont(QFont("Segoe UI", 11))
        welcome.setStyleSheet("color: #00d2ff; background: transparent; border: none; letter-spacing: 1px;")
        welcome.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(welcome)
        
        sidebar_layout.addStretch()
        
        footer = QLabel("GYM Management System")
        footer.setFont(QFont("Segoe UI", 9, QFont.Bold))
        footer.setStyleSheet("color: #6c757d; background: transparent; border: none; letter-spacing: 1px;")
        footer.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(footer)
        
        main_layout.addWidget(sidebar)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: rgba(255, 255, 255, 0.05);
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(0, 210, 255, 0.5);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        content_area = QWidget()
        content_area.setObjectName("ScrollContent")
        content_area.setStyleSheet("QWidget#ScrollContent { background: transparent; }")
        
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(40, 40, 40, 40)
        
        header_text = QLabel("Management Center")
        header_text.setFont(QFont("Segoe UI Black", 26))
        header_text.setStyleSheet("color: white; background: transparent; letter-spacing: 2px;")
        content_layout.addWidget(header_text)
        
        tagline = QLabel("Real-Time Database Analytics")
        tagline.setFont(QFont("Segoe UI", 11))
        tagline.setStyleSheet("color: #a0a5a8; background: transparent;")
        content_layout.addWidget(tagline)
        
        content_layout.addSpacing(30)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(25)
        
        for i in range(3):
            grid_layout.setColumnStretch(i, 1)

        buttons_data = [
            ("Members", "Manage gym members", "👥", "#00d2ff", self.open_members),
            ("Trainers", "Manage training staff", "🏋️", "#38ef7d", self.open_trainers),
            ("Body Metrics", "Track client progress", "⚖️", "#f64f59", self.open_metrics),
            ("Workout Plans", "Create custom routines", "📋", "#c471ed", self.open_plans),
            ("Payments", "Record transactions", "💳", "#fbd786", self.open_payments),
            ("Memberships", "Manage plan tiers", "🏷️", "#11998e", self.open_memberships),
            ("Equipment", "Track gym inventory", "🏋️‍♂️", "#f7797d", self.open_equipment),
            ("Analytics", "View business insights", "📊", "#00c6ff", self.open_analytics),
            ("Exit System", "Securely close app", "🚪", "#eb3349", self.close)
        ]

        row, col = 0, 0
        for text, sub, icon, neon_color, func in buttons_data:
            card = DashboardCard(text, sub, icon, neon_color)
            card.clicked.connect(func)
            grid_layout.addWidget(card, row, col)
            
            col += 1
            if col > 2: 
                col = 0
                row += 1

        content_layout.addLayout(grid_layout)
        content_layout.addStretch()
        
        scroll_area.setWidget(content_area)
        main_layout.addWidget(scroll_area)

    def open_members(self):
        from members import MembersWindow
        self.members_window = MembersWindow()
        self.members_window.show()
    
    def open_trainers(self):
        from trainers import TrainersWindow
        self.trainers_window = TrainersWindow()
        self.trainers_window.show()
    
    def open_metrics(self):
        from metrics import MetricsWindow
        self.metrics_window = MetricsWindow()
        self.metrics_window.show()
    
    def open_plans(self):
        from plans import WorkoutPlansWindow
        self.plans_window = WorkoutPlansWindow()
        self.plans_window.show()
    
    def open_payments(self):
        from payments import PaymentsWindow
        self.payments_window = PaymentsWindow()
        self.payments_window.show()
    
    def open_memberships(self):
        from memberships import MembershipsWindow
        self.memberships_window = MembershipsWindow()
        self.memberships_window.show()
    
    def open_equipment(self):
        from equipment import EquipmentWindow
        self.equipment_window = EquipmentWindow()
        self.equipment_window.show()
        
    def open_analytics(self):
        from analytics import AnalyticsWindow
        self.analytics_window = AnalyticsWindow()
        self.analytics_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())

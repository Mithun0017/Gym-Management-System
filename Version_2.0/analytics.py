from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QFrame, QPushButton, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor
from database import Database
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime, timedelta

class AnalyticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_all_data)
        self.timer.start(5000) 
        
        self.refresh_all_data()
    
    def init_ui(self):
        self.setWindowTitle("Real-Time Analytics Dashboard")
        self.setGeometry(50, 50, 1600, 900)
        self.setObjectName("AnalyticsMain")
        
        self.setStyleSheet("""
            QWidget#AnalyticsMain {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f2027, stop:0.5 #203a43, stop:1 #2c5364);
                color: #ecf0f1;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(25)
        
        header = self.create_header()
        main_layout.addWidget(header)
        
        kpi_layout = self.create_kpi_cards()
        main_layout.addLayout(kpi_layout)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setStyleSheet("""
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
        """)
        
        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("background: transparent;")
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(0, 10, 0, 0)
        
        charts_grid = QGridLayout()
        charts_grid.setSpacing(25)
        
        for i in range(2):
            charts_grid.setColumnStretch(i, 1)
        
        self.revenue_chart = self.create_chart_widget("MONTHLY REVENUE TREND", 0)
        self.membership_chart = self.create_chart_widget("MEMBERSHIP DISTRIBUTION", 1)
        charts_grid.addWidget(self.revenue_chart, 0, 0)
        charts_grid.addWidget(self.membership_chart, 0, 1)
        
        self.growth_chart = self.create_chart_widget("MEMBER GROWTH OVER TIME", 2)
        self.gender_chart = self.create_chart_widget("GENDER DISTRIBUTION", 3)
        charts_grid.addWidget(self.growth_chart, 1, 0)
        charts_grid.addWidget(self.gender_chart, 1, 1)
        
        self.trainer_chart = self.create_chart_widget("TRAINER WORKLOAD", 4)
        self.equipment_chart = self.create_chart_widget("EQUIPMENT CONDITION STATUS", 5)
        charts_grid.addWidget(self.trainer_chart, 2, 0)
        charts_grid.addWidget(self.equipment_chart, 2, 1)
        
        self.payment_chart = self.create_chart_widget("PAYMENT METHODS USAGE", 6)
        self.bmi_chart = self.create_chart_widget("MEMBER BMI DISTRIBUTION", 7)
        charts_grid.addWidget(self.payment_chart, 3, 0)
        charts_grid.addWidget(self.bmi_chart, 3, 1)
        
        scroll_layout.addLayout(charts_grid)
        scroll.setWidget(scroll_widget)
        
        main_layout.addWidget(scroll)
        
        footer = self.create_footer()
        main_layout.addWidget(footer)
    
    def create_header(self):
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background: rgba(20, 25, 30, 0.7);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
        """)
        header_frame.setFixedHeight(100)
        
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(30, 0, 30, 0)
        
        title = QLabel("REAL-TIME ANALYTICS")
        title.setFont(QFont("Segoe UI Black", 24))
        title.setStyleSheet("color: white; background: transparent; border: none; letter-spacing: 2px;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        live_label = QLabel("● LIVE")
        live_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        live_label.setStyleSheet("""
            color: #ff4757;
            background: transparent;
            border: none;
        """)
        header_layout.addWidget(live_label)
        
        header_layout.addSpacing(15)
        
        refresh_btn = QPushButton("Refresh Data")
        refresh_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        refresh_btn.setCursor(Qt.PointingHandCursor)
        refresh_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0052D4, stop:0.5 #4364F7, stop:1 #6FB1FC);
                color: white;
                border: none;
                padding: 10px 24px;
                border-radius: 16px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6FB1FC, stop:0.5 #4364F7, stop:1 #0052D4);
            }
        """)
        refresh_btn.clicked.connect(self.refresh_all_data)
        header_layout.addWidget(refresh_btn)
        
        return header_frame
    
    def create_kpi_cards(self):
        kpi_layout = QHBoxLayout()
        kpi_layout.setSpacing(20)
        
        self.kpi_cards = []
        kpi_data = [
            ("TOTAL MEMBERS", "0", "#00d2ff"),
            ("MONTHLY REVENUE", "₹0", "#38ef7d"),
            ("ACTIVE TRAINERS", "0", "#f64f59"),
            ("EQUIPMENT", "0", "#fbd786"),
            ("GROWTH RATE", "0%", "#c471ed")
        ]
        
        for title, value, color in kpi_data:
            card = self.create_kpi_card(title, value, color)
            self.kpi_cards.append(card)
            kpi_layout.addWidget(card['frame'])
        
        return kpi_layout
    
    def create_kpi_card(self, title, value, color):
        card_frame = QFrame()
        card_frame.setStyleSheet(f"""
            QFrame {{
                background: rgba(0, 0, 0, 0.4);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-bottom: 3px solid {color};
            }}
            QFrame:hover {{
                background: rgba(20, 30, 40, 0.8);
            }}
        """)
        card_frame.setMinimumHeight(130)
        
        layout = QVBoxLayout(card_frame)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)
        
        value_label = QLabel(value)
        value_label.setFont(QFont("Segoe UI", 32, QFont.Bold))
        value_label.setStyleSheet("background: transparent; border: none; color: white;")
        value_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(value_label)
        
        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 10, QFont.Bold))
        title_label.setStyleSheet("background: transparent; border: none; color: #a0a5a8; letter-spacing: 1px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        return {'frame': card_frame, 'value_label': value_label, 'title': title}
    
    def create_chart_widget(self, title, chart_id):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background: rgba(0, 0, 0, 0.4);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.05);
            }
        """)
        frame.setMinimumHeight(400)
        
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 11, QFont.Bold))
        title_label.setStyleSheet("color: #00d2ff; background: transparent; border: none; letter-spacing: 1px;")
        layout.addWidget(title_label)
        
        layout.addSpacing(10)
        
        figure = Figure(figsize=(8, 4), facecolor='none')
        canvas = FigureCanvas(figure)
        canvas.setStyleSheet("background: transparent;")
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(canvas)
        
        frame.figure = figure
        frame.canvas = canvas
        frame.chart_id = chart_id
        
        return frame
    
    def create_footer(self):
        footer = QLabel("Last updated: Loading...")
        footer.setFont(QFont("Segoe UI", 9))
        footer.setStyleSheet("color: #6c757d; background: transparent;")
        footer.setAlignment(Qt.AlignCenter)
        self.footer_label = footer
        return footer
    
    def refresh_all_data(self):
        self.update_kpi_cards()
        self.update_revenue_chart()
        self.update_membership_chart()
        self.update_growth_chart()
        self.update_gender_chart()
        self.update_trainer_chart()
        self.update_equipment_chart()
        self.update_payment_chart()
        self.update_bmi_chart()
        
        self.footer_label.setText(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} • Auto-refreshing every 5 seconds")
    
    def update_kpi_cards(self):
        try:
            members = self.db.get_all_members()
            trainers = self.db.get_all_trainers()
            equipment = self.db.get_all_equipment()
            
            conn = self.db.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("SELECT SUM(amount) FROM payments WHERE date >= date('now', '-30 days')")
            monthly_revenue = cursor.fetchone()[0] or 0
            
            cursor.execute("SELECT COUNT(*) FROM members WHERE join_date >= date('now', '-30 days')")
            recent_members = cursor.fetchone()[0] or 0
            
            cursor.execute("SELECT COUNT(*) FROM members WHERE join_date >= date('now', '-60 days') AND join_date < date('now', '-30 days')")
            previous_members = cursor.fetchone()[0] or 1
            conn.close()
            
            growth_rate = ((recent_members - previous_members) / previous_members * 100) if previous_members > 0 else 0
            
            self.kpi_cards[0]['value_label'].setText(str(len(members) if members else 0))
            self.kpi_cards[1]['value_label'].setText(f"₹{monthly_revenue:,.0f}")
            self.kpi_cards[2]['value_label'].setText(str(len(trainers) if trainers else 0))
            self.kpi_cards[3]['value_label'].setText(str(len(equipment) if equipment else 0))
            self.kpi_cards[4]['value_label'].setText(f"{growth_rate:+.1f}%")
        except Exception:
            pass 
    
    def update_revenue_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            months, revenues = [], []
            for i in range(11, -1, -1):
                month_start = (datetime.now() - timedelta(days=30*i)).strftime('%Y-%m')
                cursor.execute("SELECT SUM(amount) FROM payments WHERE strftime('%Y-%m', date) = ?", (month_start,))
                revenue = cursor.fetchone()[0] or 0
                months.append(month_start)
                revenues.append(revenue)
            conn.close()
            
            fig = self.revenue_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            ax.fill_between(range(len(months)), revenues, alpha=0.3, color='#00d2ff')
            ax.plot(months, revenues, marker='o', linewidth=2, markersize=6, color='#00d2ff', markerfacecolor='#ffffff')
            
            ax.tick_params(colors='#a0a5a8', labelsize=8)
            ax.grid(True, alpha=0.1, color='white')
            ax.spines['bottom'].set_color('#444')
            ax.spines['left'].set_color('#444')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
            
            fig.tight_layout()
            self.revenue_chart.canvas.draw()
        except Exception:
            pass

    def update_membership_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT m.type, COUNT(mem.member_id) 
                FROM memberships m LEFT JOIN members mem ON m.membership_id = mem.membership_id
                GROUP BY m.type
            """)
            data = cursor.fetchall()
            conn.close()
            
            if not data or all(count == 0 for _, count in data): data = [("No Data", 1)]
            labels = [row[0] for row in data]
            sizes = [row[1] for row in data]
            
            fig = self.membership_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            colors = ['#00d2ff', '#38ef7d', '#f64f59', '#c471ed', '#fbd786', '#11998e']
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'color': '#a0a5a8', 'fontsize': 9})
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                
            fig.tight_layout()
            self.membership_chart.canvas.draw()
        except Exception:
            pass

    def update_growth_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            months, counts = [], []
            for i in range(11, -1, -1):
                month_start = (datetime.now() - timedelta(days=30*i)).strftime('%Y-%m')
                cursor.execute("SELECT COUNT(*) FROM members WHERE strftime('%Y-%m', join_date) <= ?", (month_start,))
                count = cursor.fetchone()[0] or 0
                months.append(month_start)
                counts.append(count)
            conn.close()
            
            fig = self.growth_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            ax.bar(months, counts, color='#c471ed', alpha=0.7)
            z = np.polyfit(range(len(counts)), counts, 1)
            p = np.poly1d(z)
            ax.plot(months, p(range(len(counts))), color='#ffffff', linestyle='--', linewidth=2, alpha=0.8)
            
            ax.tick_params(colors='#a0a5a8', labelsize=8)
            ax.grid(True, alpha=0.1, color='white')
            ax.spines['bottom'].set_color('#444')
            ax.spines['left'].set_color('#444')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
            
            fig.tight_layout()
            self.growth_chart.canvas.draw()
        except Exception:
            pass

    def update_gender_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT gender, COUNT(*) FROM members GROUP BY gender")
            data = cursor.fetchall()
            conn.close()
            
            if not data: data = [("No Data", 1)]
            labels = [row[0] for row in data]
            sizes = [row[1] for row in data]
            
            fig = self.gender_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            colors = ['#00d2ff', '#f64f59', '#fbd786']
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'color': '#a0a5a8', 'fontsize': 9}, pctdistance=0.85)
            
            centre_circle = plt.Circle((0, 0), 0.70, fc='#14191e') 
            ax.add_artist(centre_circle)
            
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                
            fig.tight_layout()
            self.gender_chart.canvas.draw()
        except Exception:
            pass

    def update_trainer_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT t.name, COUNT(m.member_id) 
                FROM trainers t LEFT JOIN members m ON t.trainer_id = m.trainer_id
                GROUP BY t.trainer_id ORDER BY COUNT(m.member_id) DESC LIMIT 10
            """)
            data = cursor.fetchall()
            conn.close()
            
            if not data: data = [("No Trainers", 0)]
            names = [row[0][:15] for row in data] 
            counts = [row[1] for row in data]
            
            fig = self.trainer_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            ax.barh(names, counts, color='#38ef7d', alpha=0.7)
            
            ax.tick_params(colors='#a0a5a8', labelsize=8)
            ax.grid(True, alpha=0.1, color='white', axis='x')
            ax.spines['bottom'].set_color('#444')
            ax.spines['left'].set_color('#444')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            fig.tight_layout()
            self.trainer_chart.canvas.draw()
        except Exception:
            pass

    def update_equipment_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT condition, COUNT(*) FROM equipment GROUP BY condition")
            data = cursor.fetchall()
            conn.close()
            
            if not data: data = [("No Data", 1)]
            labels = [row[0] for row in data]
            sizes = [row[1] for row in data]
            
            fig = self.equipment_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            color_map = {'Excellent': '#38ef7d', 'Good': '#00d2ff', 'Fair': '#fbd786', 'Needs Repair': '#f64f59', 'Out of Service': '#eb3349'}
            colors = [color_map.get(label, '#95a5a6') for label in labels]
            
            ax.bar(labels, sizes, color=colors, alpha=0.8)
            
            ax.tick_params(colors='#a0a5a8', labelsize=8)
            ax.grid(True, alpha=0.1, color='white', axis='y')
            ax.spines['bottom'].set_color('#444')
            ax.spines['left'].set_color('#444')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
            
            fig.tight_layout()
            self.equipment_chart.canvas.draw()
        except Exception:
            pass

    def update_payment_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT payment_mode, COUNT(*) FROM payments GROUP BY payment_mode")
            data = cursor.fetchall()
            conn.close()
            
            if not data: data = [("No Data", 1)]
            labels = [row[0] for row in data]
            sizes = [row[1] for row in data]
            
            fig = self.payment_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            colors = ['#11998e', '#fbd786', '#00d2ff', '#c471ed']
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'color': '#a0a5a8', 'fontsize': 9})
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
                
            fig.tight_layout()
            self.payment_chart.canvas.draw()
        except Exception:
            pass

    def update_bmi_chart(self):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT bmi FROM body_metrics 
                WHERE bmi IS NOT NULL AND record_id IN (SELECT MAX(record_id) FROM body_metrics GROUP BY member_id)
            """)
            data = cursor.fetchall()
            conn.close()
            
            bmis = [row[0] for row in data] if data else [22.5]
            
            fig = self.bmi_chart.figure
            fig.clear()
            ax = fig.add_subplot(111)
            ax.set_facecolor('none')
            fig.patch.set_facecolor('none')
            
            n, bins, patches = ax.hist(bmis, bins=20, color='#00d2ff', alpha=0.7)
            
            for i, patch in enumerate(patches):
                if bins[i] < 18.5: patch.set_facecolor('#00d2ff') 
                elif bins[i] < 25: patch.set_facecolor('#38ef7d') 
                elif bins[i] < 30: patch.set_facecolor('#fbd786') 
                else: patch.set_facecolor('#f64f59') 
            
            ax.tick_params(colors='#a0a5a8', labelsize=8)
            ax.grid(True, alpha=0.1, color='white', axis='y')
            ax.spines['bottom'].set_color('#444')
            ax.spines['left'].set_color('#444')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            ax.axvline(18.5, color='white', linestyle='--', alpha=0.3, linewidth=1)
            ax.axvline(25, color='white', linestyle='--', alpha=0.3, linewidth=1)
            ax.axvline(30, color='white', linestyle='--', alpha=0.3, linewidth=1)
            
            fig.tight_layout()
            self.bmi_chart.canvas.draw()
        except Exception:
            pass
    
    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

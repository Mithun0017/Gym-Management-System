from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QComboBox, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import Database
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MetricsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_members()
    
    def init_ui(self):
        self.setWindowTitle("Body Metrics Tracking")
        self.setGeometry(100, 100, 1200, 700)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Body Metrics Tracking")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.member_combo = QComboBox()
        self.member_combo.currentIndexChanged.connect(self.load_metrics)
        
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Weight in kg")
        
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Height in cm")
        
        self.bmi_display = QLineEdit()
        self.bmi_display.setPlaceholderText("Auto-calculated")
        self.bmi_display.setReadOnly(True)
        
        form_layout.addWidget(QLabel("Select Member:"), 0, 0)
        form_layout.addWidget(self.member_combo, 0, 1)
        
        form_layout.addWidget(QLabel("Weight (kg):"), 0, 2)
        form_layout.addWidget(self.weight_input, 0, 3)
        
        form_layout.addWidget(QLabel("Height (cm):"), 1, 0)
        form_layout.addWidget(self.height_input, 1, 1)
        
        form_layout.addWidget(QLabel("BMI:"), 1, 2)
        form_layout.addWidget(self.bmi_display, 1, 3)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Add Metric")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_metric)
        buttons_layout.addWidget(add_btn)
        
        calculate_btn = QPushButton("Calculate BMI")
        calculate_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        calculate_btn.clicked.connect(self.calculate_bmi)
        buttons_layout.addWidget(calculate_btn)
        
        show_chart_btn = QPushButton("Show Progress Chart")
        show_chart_btn.setStyleSheet("background-color: #9b59b6; color: white; padding: 8px; font-weight: bold;")
        show_chart_btn.clicked.connect(self.show_chart)
        buttons_layout.addWidget(show_chart_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Record ID", "Date", "Weight (kg)", "Height (cm)", "BMI"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        main_layout.addWidget(self.table)
        
        info_label = QLabel(
            "BMI Categories: Underweight (<18.5) | Normal (18.5-24.9) | "
            "Overweight (25-29.9) | Obese (≥30)"
        )
        info_label.setStyleSheet("color: #7f8c8d; font-size: 10px; padding: 5px;")
        info_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(info_label)
        
        self.setLayout(main_layout)
    
    def load_members(self):
        self.member_combo.clear()
        self.member_combo.addItem("-- Select Member --", None)
        members = self.db.get_all_members()
        for member in members:
            self.member_combo.addItem(f"{member[1]} (ID: {member[0]})", member[0])
    
    def load_metrics(self):
        member_id = self.member_combo.currentData()
        if member_id:
            metrics = self.db.get_member_metrics(member_id)
            self.table.setRowCount(len(metrics))
            
            for row, metric in enumerate(metrics):
                for col, value in enumerate(metric):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(row, col, item)
        else:
            self.table.setRowCount(0)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            
            if height <= 0 or weight <= 0:
                QMessageBox.warning(self, "Error", "Weight and height must be positive!")
                return
            
            height_m = height / 100 
            bmi = weight / (height_m ** 2)
            self.bmi_display.setText(f"{bmi:.2f}")
            
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
            
            QMessageBox.information(self, "BMI Calculated", 
                                  f"BMI: {bmi:.2f}\nCategory: {category}")
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid weight and height!")
    
    def add_metric(self):
        try:
            member_id = self.member_combo.currentData()
            if not member_id:
                QMessageBox.warning(self, "Error", "Please select a member!")
                return
            
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            
            if height <= 0 or weight <= 0:
                QMessageBox.warning(self, "Error", "Weight and height must be positive!")
                return
            
            self.db.add_body_metric(member_id, weight, height)
            QMessageBox.information(self, "Success", "Body metric added successfully!")
            self.load_metrics()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid weight and height!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add metric: {str(e)}")
    
    def show_chart(self):
        member_id = self.member_combo.currentData()
        if not member_id:
            QMessageBox.warning(self, "Error", "Please select a member!")
            return
        
        metrics = self.db.get_member_metrics(member_id)
        if not metrics:
            QMessageBox.information(self, "No Data", "No metrics found for this member!")
            return
        
        metrics = list(reversed(metrics))
        
        dates = [m[1] for m in metrics]
        weights = [m[2] for m in metrics]
        bmis = [m[4] for m in metrics]
        
        chart_window = QWidget()
        chart_window.setWindowTitle(f"Progress Chart - {self.member_combo.currentText()}")
        chart_window.setGeometry(200, 200, 900, 600)
        
        layout = QVBoxLayout()
        
        fig = Figure(figsize=(10, 6))
        
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.plot(dates, weights, marker='o', linewidth=2, markersize=8, color='#3498db')
        ax1.set_xlabel('Date', fontsize=12)
        ax1.set_ylabel('Weight (kg)', fontsize=12)
        ax1.set_title('Weight Progress', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
        
        ax2 = fig.add_subplot(2, 1, 2)
        ax2.plot(dates, bmis, marker='s', linewidth=2, markersize=8, color='#e74c3c')
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylabel('BMI', fontsize=12)
        ax2.set_title('BMI Progress', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        ax2.tick_params(axis='x', rotation=45)
        
        ax2.axhspan(0, 18.5, alpha=0.2, color='blue', label='Underweight')
        ax2.axhspan(18.5, 25, alpha=0.2, color='green', label='Normal')
        ax2.axhspan(25, 30, alpha=0.2, color='orange', label='Overweight')
        ax2.axhspan(30, 50, alpha=0.2, color='red', label='Obese')
        ax2.legend(loc='upper right')
        
        fig.tight_layout()
        
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
        chart_window.setLayout(layout)
        chart_window.show()
        
        self.chart_window = chart_window
    
    def clear_form(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.bmi_display.clear()

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QComboBox, QMessageBox, QHeaderView, QSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import Database

class WorkoutPlansWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_members()
        self.load_trainers()
        self.load_plans()
    
    def init_ui(self):
        self.setWindowTitle("Workout Plans Management")
        self.setGeometry(100, 100, 1000, 600)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Workout Plans Management")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.member_combo = QComboBox()
        
        self.trainer_combo = QComboBox()
        
        self.goal_input = QLineEdit()
        self.goal_input.setPlaceholderText("E.g., Weight Loss, Muscle Gain, Endurance")
        
        self.level_combo = QComboBox()
        self.level_combo.addItems(["Beginner", "Intermediate", "Advanced", "Elite"])
        
        self.duration_spin = QSpinBox()
        self.duration_spin.setMinimum(1)
        self.duration_spin.setMaximum(52)
        self.duration_spin.setValue(12)
        self.duration_spin.setSuffix(" weeks")
        
        form_layout.addWidget(QLabel("Select Member:"), 0, 0)
        form_layout.addWidget(self.member_combo, 0, 1)
        
        form_layout.addWidget(QLabel("Assign Trainer:"), 0, 2)
        form_layout.addWidget(self.trainer_combo, 0, 3)
        
        form_layout.addWidget(QLabel("Goal:"), 1, 0)
        form_layout.addWidget(self.goal_input, 1, 1)
        
        form_layout.addWidget(QLabel("Level:"), 1, 2)
        form_layout.addWidget(self.level_combo, 1, 3)
        
        form_layout.addWidget(QLabel("Duration:"), 2, 0)
        form_layout.addWidget(self.duration_spin, 2, 1)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Create Plan")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_plan)
        buttons_layout.addWidget(add_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        refresh_btn = QPushButton("Refresh")
        refresh_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        refresh_btn.clicked.connect(self.load_plans)
        buttons_layout.addWidget(refresh_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Plan ID", "Member", "Trainer", "Goal", "Level", "Duration (weeks)"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        main_layout.addWidget(self.table)
        
        info_label = QLabel(
            "💡 Tip: Workout plans help trainers customize training programs for members based on their goals and fitness level."
        )
        info_label.setStyleSheet("color: #7f8c8d; font-size: 10px; padding: 5px;")
        info_label.setWordWrap(True)
        main_layout.addWidget(info_label)
        
        self.setLayout(main_layout)
    
    def load_members(self):
        self.member_combo.clear()
        self.member_combo.addItem("-- Select Member --", None)
        members = self.db.get_all_members()
        for member in members:
            self.member_combo.addItem(f"{member[1]} (ID: {member[0]})", member[0])
    
    def load_trainers(self):
        self.trainer_combo.clear()
        self.trainer_combo.addItem("-- Select Trainer --", None)
        trainers = self.db.get_all_trainers()
        for trainer in trainers:
            self.trainer_combo.addItem(
                f"{trainer[1]} - {trainer[2]}", 
                trainer[0]
            )
    
    def load_plans(self):
        plans = self.db.get_all_workout_plans()
        self.table.setRowCount(len(plans))
        
        for row, plan in enumerate(plans):
            for col, value in enumerate(plan):
                item = QTableWidgetItem(str(value) if value else "N/A")
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
    
    def add_plan(self):
        try:
            member_id = self.member_combo.currentData()
            trainer_id = self.trainer_combo.currentData()
            goal = self.goal_input.text().strip()
            level = self.level_combo.currentText()
            duration = self.duration_spin.value()
            
            if not member_id:
                QMessageBox.warning(self, "Error", "Please select a member!")
                return
            
            if not trainer_id:
                QMessageBox.warning(self, "Error", "Please select a trainer!")
                return
            
            if not goal:
                QMessageBox.warning(self, "Error", "Please enter a goal!")
                return
            
            self.db.add_workout_plan(member_id, trainer_id, goal, level, duration)
            QMessageBox.information(self, "Success", "Workout plan created successfully!")
            self.load_plans()
            self.clear_form()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create plan: {str(e)}")
    
    def clear_form(self):
        self.member_combo.setCurrentIndex(0)
        self.trainer_combo.setCurrentIndex(0)
        self.goal_input.clear()
        self.level_combo.setCurrentIndex(0)
        self.duration_spin.setValue(12)

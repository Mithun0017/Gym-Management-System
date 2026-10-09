from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import Database

class TrainersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_trainers()
    
    def init_ui(self):
        self.setWindowTitle("Trainers Management")
        self.setGeometry(100, 100, 1000, 600)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Trainers Management")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.trainer_id_input = QLineEdit()
        self.trainer_id_input.setPlaceholderText("Auto")
        self.trainer_id_input.setReadOnly(True)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter trainer name")
        
        self.specialization_input = QLineEdit()
        self.specialization_input.setPlaceholderText("E.g., Weight Training, Yoga, Cardio")
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter phone number")
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter email")
        
        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText("Enter salary amount")
        
        form_layout.addWidget(QLabel("Trainer ID:"), 0, 0)
        form_layout.addWidget(self.trainer_id_input, 0, 1)
        
        form_layout.addWidget(QLabel("Name:"), 0, 2)
        form_layout.addWidget(self.name_input, 0, 3)
        
        form_layout.addWidget(QLabel("Specialization:"), 1, 0)
        form_layout.addWidget(self.specialization_input, 1, 1)
        
        form_layout.addWidget(QLabel("Phone:"), 1, 2)
        form_layout.addWidget(self.phone_input, 1, 3)
        
        form_layout.addWidget(QLabel("Email:"), 2, 0)
        form_layout.addWidget(self.email_input, 2, 1)
        
        form_layout.addWidget(QLabel("Salary (₹):"), 2, 2)
        form_layout.addWidget(self.salary_input, 2, 3)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Add Trainer")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_trainer)
        buttons_layout.addWidget(add_btn)
        
        update_btn = QPushButton("Update Trainer")
        update_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        update_btn.clicked.connect(self.update_trainer)
        buttons_layout.addWidget(update_btn)
        
        delete_btn = QPushButton("Delete Trainer")
        delete_btn.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-weight: bold;")
        delete_btn.clicked.connect(self.delete_trainer)
        buttons_layout.addWidget(delete_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Specialization", "Phone", "Email", "Salary (₹)"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.table_clicked)
        main_layout.addWidget(self.table)
        
        self.setLayout(main_layout)
    
    def load_trainers(self):
        trainers = self.db.get_all_trainers()
        self.table.setRowCount(len(trainers))
        
        for row, trainer in enumerate(trainers):
            for col, value in enumerate(trainer):
                item = QTableWidgetItem(str(value) if value else "N/A")
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
    
    def add_trainer(self):
        try:
            name = self.name_input.text().strip()
            specialization = self.specialization_input.text().strip()
            phone = self.phone_input.text().strip()
            email = self.email_input.text().strip()
            salary = float(self.salary_input.text())
            
            if not name:
                QMessageBox.warning(self, "Error", "Please enter trainer name!")
                return
            
            self.db.add_trainer(name, specialization, phone, email, salary)
            QMessageBox.information(self, "Success", "Trainer added successfully!")
            self.load_trainers()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid salary amount!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add trainer: {str(e)}")
    
    def update_trainer(self):
        try:
            trainer_id = self.trainer_id_input.text()
            if not trainer_id:
                QMessageBox.warning(self, "Error", "Please select a trainer to update!")
                return
            
            name = self.name_input.text().strip()
            specialization = self.specialization_input.text().strip()
            phone = self.phone_input.text().strip()
            email = self.email_input.text().strip()
            salary = float(self.salary_input.text())
            
            self.db.update_trainer(trainer_id, name, specialization, phone, email, salary)
            QMessageBox.information(self, "Success", "Trainer updated successfully!")
            self.load_trainers()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid salary amount!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update trainer: {str(e)}")
    
    def delete_trainer(self):
        trainer_id = self.trainer_id_input.text()
        if not trainer_id:
            QMessageBox.warning(self, "Error", "Please select a trainer to delete!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     "Are you sure you want to delete this trainer?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                self.db.delete_trainer(trainer_id)
                QMessageBox.information(self, "Success", "Trainer deleted successfully!")
                self.load_trainers()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete trainer: {str(e)}")
    
    def table_clicked(self, row):
        self.trainer_id_input.setText(self.table.item(row, 0).text())
        self.name_input.setText(self.table.item(row, 1).text())
        self.specialization_input.setText(self.table.item(row, 2).text())
        self.phone_input.setText(self.table.item(row, 3).text())
        self.email_input.setText(self.table.item(row, 4).text())
        self.salary_input.setText(self.table.item(row, 5).text())
    
    def clear_form(self):
        self.trainer_id_input.clear()
        self.name_input.clear()
        self.specialization_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.salary_input.clear()

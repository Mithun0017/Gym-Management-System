from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QComboBox, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import Database

class MembersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_members()
        self.load_memberships()
        self.load_trainers()
    
    def init_ui(self):
        self.setWindowTitle("Members Management")
        self.setGeometry(100, 100, 1200, 700)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Members Management")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.member_id_input = QLineEdit()
        self.member_id_input.setPlaceholderText("Auto")
        self.member_id_input.setReadOnly(True)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter full name")
        
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter age")
        
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female", "Other"])
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter phone number")
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter email")
        
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter address")
        
        self.membership_combo = QComboBox()
        
        self.trainer_combo = QComboBox()
        
        form_layout.addWidget(QLabel("Member ID:"), 0, 0)
        form_layout.addWidget(self.member_id_input, 0, 1)
        
        form_layout.addWidget(QLabel("Name:"), 0, 2)
        form_layout.addWidget(self.name_input, 0, 3)
        
        form_layout.addWidget(QLabel("Age:"), 1, 0)
        form_layout.addWidget(self.age_input, 1, 1)
        
        form_layout.addWidget(QLabel("Gender:"), 1, 2)
        form_layout.addWidget(self.gender_combo, 1, 3)
        
        form_layout.addWidget(QLabel("Phone:"), 2, 0)
        form_layout.addWidget(self.phone_input, 2, 1)
        
        form_layout.addWidget(QLabel("Email:"), 2, 2)
        form_layout.addWidget(self.email_input, 2, 3)
        
        form_layout.addWidget(QLabel("Address:"), 3, 0)
        form_layout.addWidget(self.address_input, 3, 1, 1, 3)
        
        form_layout.addWidget(QLabel("Membership:"), 4, 0)
        form_layout.addWidget(self.membership_combo, 4, 1)
        
        form_layout.addWidget(QLabel("Trainer:"), 4, 2)
        form_layout.addWidget(self.trainer_combo, 4, 3)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Add Member")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_member)
        buttons_layout.addWidget(add_btn)
        
        update_btn = QPushButton("Update Member")
        update_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        update_btn.clicked.connect(self.update_member)
        buttons_layout.addWidget(update_btn)
        
        delete_btn = QPushButton("Delete Member")
        delete_btn.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-weight: bold;")
        delete_btn.clicked.connect(self.delete_member)
        buttons_layout.addWidget(delete_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Age", "Gender", "Phone", "Email", 
            "Address", "Join Date", "Membership", "Trainer"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.table_clicked)
        main_layout.addWidget(self.table)
        
        self.setLayout(main_layout)
    
    def load_memberships(self):
        self.membership_combo.clear()
        self.membership_combo.addItem("-- Select Membership --", None)
        memberships = self.db.get_all_memberships()
        for membership in memberships:
            self.membership_combo.addItem(
                f"{membership[1]} (₹{membership[2]})", 
                membership[0]
            )
    
    def load_trainers(self):
        self.trainer_combo.clear()
        self.trainer_combo.addItem("-- Select Trainer --", None)
        trainers = self.db.get_all_trainers()
        for trainer in trainers:
            self.trainer_combo.addItem(trainer[1], trainer[0])
    
    def load_members(self):
        members = self.db.get_all_members()
        self.table.setRowCount(len(members))
        
        for row, member in enumerate(members):
            for col, value in enumerate(member):
                item = QTableWidgetItem(str(value) if value else "N/A")
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
    
    def add_member(self):
        try:
            name = self.name_input.text().strip()
            age = int(self.age_input.text())
            gender = self.gender_combo.currentText()
            phone = self.phone_input.text().strip()
            email = self.email_input.text().strip()
            address = self.address_input.text().strip()
            membership_id = self.membership_combo.currentData()
            trainer_id = self.trainer_combo.currentData()
            
            if not name:
                QMessageBox.warning(self, "Error", "Please enter member name!")
                return
            
            self.db.add_member(name, age, gender, phone, email, address, membership_id, trainer_id)
            QMessageBox.information(self, "Success", "Member added successfully!")
            self.load_members()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid age!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add member: {str(e)}")
    
    def update_member(self):
        try:
            member_id = self.member_id_input.text()
            if not member_id:
                QMessageBox.warning(self, "Error", "Please select a member to update!")
                return
            
            name = self.name_input.text().strip()
            age = int(self.age_input.text())
            gender = self.gender_combo.currentText()
            phone = self.phone_input.text().strip()
            email = self.email_input.text().strip()
            address = self.address_input.text().strip()
            membership_id = self.membership_combo.currentData()
            trainer_id = self.trainer_combo.currentData()
            
            self.db.update_member(member_id, name, age, gender, phone, email, address, 
                                membership_id, trainer_id)
            QMessageBox.information(self, "Success", "Member updated successfully!")
            self.load_members()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid age!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update member: {str(e)}")
    
    def delete_member(self):
        member_id = self.member_id_input.text()
        if not member_id:
            QMessageBox.warning(self, "Error", "Please select a member to delete!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     "Are you sure you want to delete this member?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                self.db.delete_member(member_id)
                QMessageBox.information(self, "Success", "Member deleted successfully!")
                self.load_members()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete member: {str(e)}")
    
    def table_clicked(self, row):
        self.member_id_input.setText(self.table.item(row, 0).text())
        self.name_input.setText(self.table.item(row, 1).text())
        self.age_input.setText(self.table.item(row, 2).text())
        
        gender = self.table.item(row, 3).text()
        index = self.gender_combo.findText(gender)
        if index >= 0:
            self.gender_combo.setCurrentIndex(index)
        
        self.phone_input.setText(self.table.item(row, 4).text())
        self.email_input.setText(self.table.item(row, 5).text())
        self.address_input.setText(self.table.item(row, 6).text())
        
    
    def clear_form(self):
        self.member_id_input.clear()
        self.name_input.clear()
        self.age_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.phone_input.clear()
        self.email_input.clear()
        self.address_input.clear()
        self.membership_combo.setCurrentIndex(0)
        self.trainer_combo.setCurrentIndex(0)

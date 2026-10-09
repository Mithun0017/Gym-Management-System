from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QComboBox, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import Database
from datetime import datetime, timedelta

class PaymentsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_members()
        self.load_all_payments()
    
    def init_ui(self):
        self.setWindowTitle("Payments Management")
        self.setGeometry(100, 100, 1000, 600)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Payments Management")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.member_combo = QComboBox()
        self.member_combo.currentIndexChanged.connect(self.load_member_payments)
        
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter payment amount")
        
        self.payment_mode_combo = QComboBox()
        self.payment_mode_combo.addItems([
            "Cash", "Credit Card", "Debit Card", "UPI", "Net Banking", "Cheque"
        ])
        
        self.status_label = QLabel("Status: Not Selected")
        self.status_label.setStyleSheet("padding: 5px; font-weight: bold;")
        
        form_layout.addWidget(QLabel("Select Member:"), 0, 0)
        form_layout.addWidget(self.member_combo, 0, 1)
        
        form_layout.addWidget(QLabel("Amount (₹):"), 0, 2)
        form_layout.addWidget(self.amount_input, 0, 3)
        
        form_layout.addWidget(QLabel("Payment Mode:"), 1, 0)
        form_layout.addWidget(self.payment_mode_combo, 1, 1)
        
        form_layout.addWidget(QLabel("Membership Status:"), 1, 2)
        form_layout.addWidget(self.status_label, 1, 3)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Record Payment")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_payment)
        buttons_layout.addWidget(add_btn)
        
        check_status_btn = QPushButton("Check Membership Status")
        check_status_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        check_status_btn.clicked.connect(self.check_membership_status)
        buttons_layout.addWidget(check_status_btn)
        
        view_all_btn = QPushButton("View All Payments")
        view_all_btn.setStyleSheet("background-color: #9b59b6; color: white; padding: 8px; font-weight: bold;")
        view_all_btn.clicked.connect(self.load_all_payments)
        buttons_layout.addWidget(view_all_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "Payment ID", "Member", "Date", "Amount (₹)", "Payment Mode"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        main_layout.addWidget(self.table)
        
        self.setLayout(main_layout)
    
    def load_members(self):
        self.member_combo.clear()
        self.member_combo.addItem("-- Select Member --", None)
        members = self.db.get_all_members()
        for member in members:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT m.member_id, m.join_date, mb.duration
                FROM members m
                LEFT JOIN memberships mb ON m.membership_id = mb.membership_id
                WHERE m.member_id = ?
            ''', (member[0],))
            member_data = cursor.fetchone()
            conn.close()
            
            self.member_combo.addItem(
                f"{member[1]} (ID: {member[0]})", 
                member_data
            )
    
    def load_member_payments(self):
        member_data = self.member_combo.currentData()
        if member_data:
            member_id = member_data[0]
            payments = self.db.get_member_payments(member_id)
            self.table.setRowCount(len(payments))
            
            for row, payment in enumerate(payments):
                member_name = self.member_combo.currentText().split(' (')[0]
                row_data = [
                    payment[0],  
                    member_name,  
                    payment[1],  
                    payment[2],  
                    payment[3]   
                ]
                
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(row, col, item)
        else:
            self.table.setRowCount(0)
    
    def load_all_payments(self):
        payments = self.db.get_all_payments()
        self.table.setRowCount(len(payments))
        
        for row, payment in enumerate(payments):
            for col, value in enumerate(payment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
    
    def add_payment(self):
        try:
            member_data = self.member_combo.currentData()
            if not member_data:
                QMessageBox.warning(self, "Error", "Please select a member!")
                return
            
            member_id = member_data[0]
            amount = float(self.amount_input.text())
            payment_mode = self.payment_mode_combo.currentText()
            
            if amount <= 0:
                QMessageBox.warning(self, "Error", "Amount must be positive!")
                return
            
            self.db.add_payment(member_id, amount, payment_mode)
            QMessageBox.information(self, "Success", "Payment recorded successfully!")
            self.load_member_payments()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid amount!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to record payment: {str(e)}")
    
    def check_membership_status(self):
        member_data = self.member_combo.currentData()
        if not member_data:
            QMessageBox.warning(self, "Error", "Please select a member!")
            return
        
        member_id, join_date, duration = member_data
        
        if not join_date or not duration:
            self.status_label.setText("Status: No Membership")
            self.status_label.setStyleSheet("color: #95a5a6; padding: 5px; font-weight: bold;")
            return
        
        join_dt = datetime.strptime(join_date, '%Y-%m-%d')
        expiry_dt = join_dt + timedelta(days=duration)
        today = datetime.now()
        
        days_left = (expiry_dt - today).days
        
        if days_left > 0:
            self.status_label.setText(f"Status: Active ({days_left} days left)")
            self.status_label.setStyleSheet("color: #27ae60; padding: 5px; font-weight: bold;")
        elif days_left >= -7: 
            self.status_label.setText(f"Status: Expiring Soon ({abs(days_left)} days ago)")
            self.status_label.setStyleSheet("color: #f39c12; padding: 5px; font-weight: bold;")
        else:
            self.status_label.setText(f"Status: Expired ({abs(days_left)} days ago)")
            self.status_label.setStyleSheet("color: #e74c3c; padding: 5px; font-weight: bold;")
    
    def clear_form(self):
        self.amount_input.clear()
        self.payment_mode_combo.setCurrentIndex(0)
        self.status_label.setText("Status: Not Selected")
        self.status_label.setStyleSheet("padding: 5px; font-weight: bold;")

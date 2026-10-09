from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QSpinBox, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from database import Database

class MembershipsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_memberships()
    
    def init_ui(self):
        self.setWindowTitle("Membership Plans Management")
        self.setGeometry(100, 100, 800, 500)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Membership Plans Management")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.membership_id_input = QLineEdit()
        self.membership_id_input.setPlaceholderText("Auto")
        self.membership_id_input.setReadOnly(True)
        
        self.type_input = QLineEdit()
        self.type_input.setPlaceholderText("E.g., Monthly, Quarterly, Yearly")
        
        self.fee_input = QLineEdit()
        self.fee_input.setPlaceholderText("Enter membership fee")
        
        self.duration_spin = QSpinBox()
        self.duration_spin.setMinimum(1)
        self.duration_spin.setMaximum(365)
        self.duration_spin.setValue(30)
        self.duration_spin.setSuffix(" days")
        
        form_layout.addWidget(QLabel("Membership ID:"), 0, 0)
        form_layout.addWidget(self.membership_id_input, 0, 1)
        
        form_layout.addWidget(QLabel("Type:"), 0, 2)
        form_layout.addWidget(self.type_input, 0, 3)
        
        form_layout.addWidget(QLabel("Fee (₹):"), 1, 0)
        form_layout.addWidget(self.fee_input, 1, 1)
        
        form_layout.addWidget(QLabel("Duration:"), 1, 2)
        form_layout.addWidget(self.duration_spin, 1, 3)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Add Plan")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_membership)
        buttons_layout.addWidget(add_btn)
        
        update_btn = QPushButton("Update Plan")
        update_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        update_btn.clicked.connect(self.update_membership)
        buttons_layout.addWidget(update_btn)
        
        delete_btn = QPushButton("Delete Plan")
        delete_btn.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-weight: bold;")
        delete_btn.clicked.connect(self.delete_membership)
        buttons_layout.addWidget(delete_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "ID", "Type", "Fee (₹)", "Duration (days)"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.table_clicked)
        main_layout.addWidget(self.table)
        
        info_label = QLabel(
            "💡 Common Plans: Monthly (30 days), Quarterly (90 days), "
            "Half-Yearly (180 days), Yearly (365 days)"
        )
        info_label.setStyleSheet("color: #7f8c8d; font-size: 10px; padding: 5px;")
        info_label.setWordWrap(True)
        main_layout.addWidget(info_label)
        
        self.setLayout(main_layout)
    
    def load_memberships(self):
        memberships = self.db.get_all_memberships()
        self.table.setRowCount(len(memberships))
        
        for row, membership in enumerate(memberships):
            for col, value in enumerate(membership):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
    
    def add_membership(self):
        try:
            type_name = self.type_input.text().strip()
            fee = float(self.fee_input.text())
            duration = self.duration_spin.value()
            
            if not type_name:
                QMessageBox.warning(self, "Error", "Please enter membership type!")
                return
            
            if fee <= 0:
                QMessageBox.warning(self, "Error", "Fee must be positive!")
                return
            
            self.db.add_membership(type_name, fee, duration)
            QMessageBox.information(self, "Success", "Membership plan added successfully!")
            self.load_memberships()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid fee amount!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add membership: {str(e)}")
    
    def update_membership(self):
        try:
            membership_id = self.membership_id_input.text()
            if not membership_id:
                QMessageBox.warning(self, "Error", "Please select a membership to update!")
                return
            
            type_name = self.type_input.text().strip()
            fee = float(self.fee_input.text())
            duration = self.duration_spin.value()
            
            if not type_name:
                QMessageBox.warning(self, "Error", "Please enter membership type!")
                return
            
            self.db.update_membership(membership_id, type_name, fee, duration)
            QMessageBox.information(self, "Success", "Membership plan updated successfully!")
            self.load_memberships()
            self.clear_form()
        
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid fee amount!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update membership: {str(e)}")
    
    def delete_membership(self):
        membership_id = self.membership_id_input.text()
        if not membership_id:
            QMessageBox.warning(self, "Error", "Please select a membership to delete!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     "Are you sure you want to delete this membership plan?\n"
                                     "This may affect existing members!",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                self.db.delete_membership(membership_id)
                QMessageBox.information(self, "Success", "Membership plan deleted successfully!")
                self.load_memberships()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete membership: {str(e)}")
    
    def table_clicked(self, row):
        self.membership_id_input.setText(self.table.item(row, 0).text())
        self.type_input.setText(self.table.item(row, 1).text())
        self.fee_input.setText(self.table.item(row, 2).text())
        self.duration_spin.setValue(int(self.table.item(row, 3).text()))
    
    def clear_form(self):
        self.membership_id_input.clear()
        self.type_input.clear()
        self.fee_input.clear()
        self.duration_spin.setValue(30)

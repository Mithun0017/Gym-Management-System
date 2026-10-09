from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QComboBox, QMessageBox, QHeaderView, QDateEdit)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from database import Database

class EquipmentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.init_ui()
        self.load_equipment()
    
    def init_ui(self):
        self.setWindowTitle("Equipment Management")
        self.setGeometry(100, 100, 1000, 600)
        
        main_layout = QVBoxLayout()
        
        header = QLabel("Equipment Management")
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        form_layout = QGridLayout()
        
        self.equipment_id_input = QLineEdit()
        self.equipment_id_input.setPlaceholderText("Auto")
        self.equipment_id_input.setReadOnly(True)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("E.g., Treadmill, Dumbbell Set")
        
        self.type_combo = QComboBox()
        self.type_combo.addItems([
            "Cardio", "Strength", "Free Weights", "Machines", 
            "Accessories", "Functional", "Other"
        ])
        
        self.purchase_date_input = QDateEdit()
        self.purchase_date_input.setDate(QDate.currentDate())
        self.purchase_date_input.setCalendarPopup(True)
        self.purchase_date_input.setDisplayFormat("yyyy-MM-dd")
        
        self.condition_combo = QComboBox()
        self.condition_combo.addItems([
            "Excellent", "Good", "Fair", "Needs Repair", "Out of Service"
        ])
        
        form_layout.addWidget(QLabel("Equipment ID:"), 0, 0)
        form_layout.addWidget(self.equipment_id_input, 0, 1)
        
        form_layout.addWidget(QLabel("Name:"), 0, 2)
        form_layout.addWidget(self.name_input, 0, 3)
        
        form_layout.addWidget(QLabel("Type:"), 1, 0)
        form_layout.addWidget(self.type_combo, 1, 1)
        
        form_layout.addWidget(QLabel("Purchase Date:"), 1, 2)
        form_layout.addWidget(self.purchase_date_input, 1, 3)
        
        form_layout.addWidget(QLabel("Condition:"), 2, 0)
        form_layout.addWidget(self.condition_combo, 2, 1)
        
        main_layout.addLayout(form_layout)
        
        buttons_layout = QHBoxLayout()
        
        add_btn = QPushButton("Add Equipment")
        add_btn.setStyleSheet("background-color: #27ae60; color: white; padding: 8px; font-weight: bold;")
        add_btn.clicked.connect(self.add_equipment)
        buttons_layout.addWidget(add_btn)
        
        update_btn = QPushButton("Update Equipment")
        update_btn.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-weight: bold;")
        update_btn.clicked.connect(self.update_equipment)
        buttons_layout.addWidget(update_btn)
        
        delete_btn = QPushButton("Delete Equipment")
        delete_btn.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-weight: bold;")
        delete_btn.clicked.connect(self.delete_equipment)
        buttons_layout.addWidget(delete_btn)
        
        clear_btn = QPushButton("Clear Form")
        clear_btn.setStyleSheet("background-color: #95a5a6; color: white; padding: 8px; font-weight: bold;")
        clear_btn.clicked.connect(self.clear_form)
        buttons_layout.addWidget(clear_btn)
        
        main_layout.addLayout(buttons_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Type", "Purchase Date", "Condition"
        ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.table_clicked)
        main_layout.addWidget(self.table)
        
        self.summary_label = QLabel()
        self.summary_label.setStyleSheet("color: #2c3e50; padding: 5px; font-weight: bold;")
        self.summary_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.summary_label)
        
        self.setLayout(main_layout)
    
    def load_equipment(self):
        equipment_list = self.db.get_all_equipment()
        self.table.setRowCount(len(equipment_list))
        
        condition_counts = {}
        
        for row, equipment in enumerate(equipment_list):
            for col, value in enumerate(equipment):
                item = QTableWidgetItem(str(value) if value else "N/A")
                item.setTextAlignment(Qt.AlignCenter)
                
                if col == 4:  
                    condition = str(value)
                    condition_counts[condition] = condition_counts.get(condition, 0) + 1
                    
                    if condition == "Excellent":
                        item.setBackground(Qt.green)
                    elif condition == "Good":
                        item.setBackground(Qt.lightGray)
                    elif condition == "Fair":
                        item.setBackground(Qt.yellow)
                    elif condition == "Needs Repair":
                        item.setBackground(Qt.darkYellow)
                    elif condition == "Out of Service":
                        item.setBackground(Qt.red)
                
                self.table.setItem(row, col, item)
        
        total = len(equipment_list)
        self.summary_label.setText(
            f"Total Equipment: {total} | "
            f"Excellent: {condition_counts.get('Excellent', 0)} | "
            f"Good: {condition_counts.get('Good', 0)} | "
            f"Fair: {condition_counts.get('Fair', 0)} | "
            f"Needs Repair: {condition_counts.get('Needs Repair', 0)} | "
            f"Out of Service: {condition_counts.get('Out of Service', 0)}"
        )
    
    def add_equipment(self):
        try:
            name = self.name_input.text().strip()
            eq_type = self.type_combo.currentText()
            purchase_date = self.purchase_date_input.date().toString("yyyy-MM-dd")
            condition = self.condition_combo.currentText()
            
            if not name:
                QMessageBox.warning(self, "Error", "Please enter equipment name!")
                return
            
            self.db.add_equipment(name, eq_type, purchase_date, condition)
            QMessageBox.information(self, "Success", "Equipment added successfully!")
            self.load_equipment()
            self.clear_form()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add equipment: {str(e)}")
    
    def update_equipment(self):
        try:
            equipment_id = self.equipment_id_input.text()
            if not equipment_id:
                QMessageBox.warning(self, "Error", "Please select equipment to update!")
                return
            
            name = self.name_input.text().strip()
            eq_type = self.type_combo.currentText()
            purchase_date = self.purchase_date_input.date().toString("yyyy-MM-dd")
            condition = self.condition_combo.currentText()
            
            if not name:
                QMessageBox.warning(self, "Error", "Please enter equipment name!")
                return
            
            self.db.update_equipment(equipment_id, name, eq_type, purchase_date, condition)
            QMessageBox.information(self, "Success", "Equipment updated successfully!")
            self.load_equipment()
            self.clear_form()
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update equipment: {str(e)}")
    
    def delete_equipment(self):
        equipment_id = self.equipment_id_input.text()
        if not equipment_id:
            QMessageBox.warning(self, "Error", "Please select equipment to delete!")
            return
        
        reply = QMessageBox.question(self, "Confirm Delete", 
                                     "Are you sure you want to delete this equipment?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                self.db.delete_equipment(equipment_id)
                QMessageBox.information(self, "Success", "Equipment deleted successfully!")
                self.load_equipment()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete equipment: {str(e)}")
    
    def table_clicked(self, row):
        self.equipment_id_input.setText(self.table.item(row, 0).text())
        self.name_input.setText(self.table.item(row, 1).text())
        
        eq_type = self.table.item(row, 2).text()
        index = self.type_combo.findText(eq_type)
        if index >= 0:
            self.type_combo.setCurrentIndex(index)
        
        purchase_date_str = self.table.item(row, 3).text()
        if purchase_date_str != "N/A":
            date = QDate.fromString(purchase_date_str, "yyyy-MM-dd")
            self.purchase_date_input.setDate(date)
        
        condition = self.table.item(row, 4).text()
        index = self.condition_combo.findText(condition)
        if index >= 0:
            self.condition_combo.setCurrentIndex(index)
    
    def clear_form(self):
        self.equipment_id_input.clear()
        self.name_input.clear()
        self.type_combo.setCurrentIndex(0)
        self.purchase_date_input.setDate(QDate.currentDate())
        self.condition_combo.setCurrentIndex(0)

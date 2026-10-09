import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='gym.db'):
        self.db_name = db_name
        self.create_tables()
        self.insert_default_data()
    
    def get_connection(self):
        return sqlite3.connect(self.db_name)
    
    def create_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memberships (
                membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                fee REAL NOT NULL,
                duration INTEGER NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trainers (
                trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                specialization TEXT,
                phone TEXT,
                email TEXT,
                salary REAL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                join_date TEXT,
                membership_id INTEGER,
                trainer_id INTEGER,
                FOREIGN KEY (membership_id) REFERENCES memberships(membership_id),
                FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS body_metrics (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER,
                date TEXT,
                weight REAL,
                height REAL,
                bmi REAL,
                FOREIGN KEY (member_id) REFERENCES members(member_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workout_plans (
                plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER,
                trainer_id INTEGER,
                goal TEXT,
                level TEXT,
                duration INTEGER,
                FOREIGN KEY (member_id) REFERENCES members(member_id),
                FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER,
                date TEXT,
                amount REAL,
                payment_mode TEXT,
                FOREIGN KEY (member_id) REFERENCES members(member_id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipment (
                equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT,
                purchase_date TEXT,
                condition TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_default_data(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM memberships")
        if cursor.fetchone()[0] == 0:
            default_plans = [
                ('Monthly', 1500, 30),
                ('Quarterly', 4000, 90),
                ('Half-Yearly', 7500, 180),
                ('Yearly', 14000, 365)
            ]
            cursor.executemany(
                "INSERT INTO memberships (type, fee, duration) VALUES (?, ?, ?)",
                default_plans
            )
            conn.commit()
        
        conn.close()
    
    
    def add_member(self, name, age, gender, phone, email, address, membership_id, trainer_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        join_date = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
            INSERT INTO members (name, age, gender, phone, email, address, join_date, membership_id, trainer_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, gender, phone, email, address, join_date, membership_id, trainer_id))
        
        conn.commit()
        conn.close()
    
    def get_all_members(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT m.member_id, m.name, m.age, m.gender, m.phone, m.email, 
                   m.address, m.join_date, 
                   mb.type as membership, t.name as trainer
            FROM members m
            LEFT JOIN memberships mb ON m.membership_id = mb.membership_id
            LEFT JOIN trainers t ON m.trainer_id = t.trainer_id
        ''')
        
        members = cursor.fetchall()
        conn.close()
        return members
    
    def update_member(self, member_id, name, age, gender, phone, email, address, membership_id, trainer_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE members 
            SET name=?, age=?, gender=?, phone=?, email=?, address=?, membership_id=?, trainer_id=?
            WHERE member_id=?
        ''', (name, age, gender, phone, email, address, membership_id, trainer_id, member_id))
        
        conn.commit()
        conn.close()
    
    def delete_member(self, member_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM members WHERE member_id=?", (member_id,))
        conn.commit()
        conn.close()
    
    def add_trainer(self, name, specialization, phone, email, salary):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO trainers (name, specialization, phone, email, salary)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, specialization, phone, email, salary))
        
        conn.commit()
        conn.close()
    
    def get_all_trainers(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trainers")
        trainers = cursor.fetchall()
        conn.close()
        return trainers
    
    def update_trainer(self, trainer_id, name, specialization, phone, email, salary):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE trainers 
            SET name=?, specialization=?, phone=?, email=?, salary=?
            WHERE trainer_id=?
        ''', (name, specialization, phone, email, salary, trainer_id))
        
        conn.commit()
        conn.close()
    
    def delete_trainer(self, trainer_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM trainers WHERE trainer_id=?", (trainer_id,))
        conn.commit()
        conn.close()
    
    
    def add_body_metric(self, member_id, weight, height):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        date = datetime.now().strftime('%Y-%m-%d')
        height_m = height / 100  
        bmi = weight / (height_m ** 2)
        
        cursor.execute('''
            INSERT INTO body_metrics (member_id, date, weight, height, bmi)
            VALUES (?, ?, ?, ?, ?)
        ''', (member_id, date, weight, height, round(bmi, 2)))
        
        conn.commit()
        conn.close()
    
    def get_member_metrics(self, member_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT record_id, date, weight, height, bmi
            FROM body_metrics
            WHERE member_id=?
            ORDER BY date DESC
        ''', (member_id,))
        
        metrics = cursor.fetchall()
        conn.close()
        return metrics
    
    
    def add_workout_plan(self, member_id, trainer_id, goal, level, duration):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO workout_plans (member_id, trainer_id, goal, level, duration)
            VALUES (?, ?, ?, ?, ?)
        ''', (member_id, trainer_id, goal, level, duration))
        
        conn.commit()
        conn.close()
    
    def get_all_workout_plans(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT wp.plan_id, m.name as member, t.name as trainer, 
                   wp.goal, wp.level, wp.duration
            FROM workout_plans wp
            JOIN members m ON wp.member_id = m.member_id
            JOIN trainers t ON wp.trainer_id = t.trainer_id
        ''')
        
        plans = cursor.fetchall()
        conn.close()
        return plans
    
    
    def add_payment(self, member_id, amount, payment_mode):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        date = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
            INSERT INTO payments (member_id, date, amount, payment_mode)
            VALUES (?, ?, ?, ?)
        ''', (member_id, date, amount, payment_mode))
        
        conn.commit()
        conn.close()
    
    def get_member_payments(self, member_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT payment_id, date, amount, payment_mode
            FROM payments
            WHERE member_id=?
            ORDER BY date DESC
        ''', (member_id,))
        
        payments = cursor.fetchall()
        conn.close()
        return payments
    
    def get_all_payments(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT p.payment_id, m.name as member, p.date, p.amount, p.payment_mode
            FROM payments p
            JOIN members m ON p.member_id = m.member_id
            ORDER BY p.date DESC
        ''')
        
        payments = cursor.fetchall()
        conn.close()
        return payments
    
    
    def add_membership(self, type, fee, duration):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO memberships (type, fee, duration)
            VALUES (?, ?, ?)
        ''', (type, fee, duration))
        
        conn.commit()
        conn.close()
    
    def get_all_memberships(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM memberships")
        memberships = cursor.fetchall()
        conn.close()
        return memberships
    
    def update_membership(self, membership_id, type, fee, duration):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE memberships 
            SET type=?, fee=?, duration=?
            WHERE membership_id=?
        ''', (type, fee, duration, membership_id))
        
        conn.commit()
        conn.close()
    
    def delete_membership(self, membership_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM memberships WHERE membership_id=?", (membership_id,))
        conn.commit()
        conn.close()
    
    
    def add_equipment(self, name, type, purchase_date, condition):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO equipment (name, type, purchase_date, condition)
            VALUES (?, ?, ?, ?)
        ''', (name, type, purchase_date, condition))
        
        conn.commit()
        conn.close()
    
    def get_all_equipment(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipment")
        equipment = cursor.fetchall()
        conn.close()
        return equipment
    
    def update_equipment(self, equipment_id, name, type, purchase_date, condition):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE equipment 
            SET name=?, type=?, purchase_date=?, condition=?
            WHERE equipment_id=?
        ''', (name, type, purchase_date, condition, equipment_id))
        
        conn.commit()
        conn.close()
    
    def delete_equipment(self, equipment_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment WHERE equipment_id=?", (equipment_id,))
        conn.commit()
        conn.close()

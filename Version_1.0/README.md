# 🏋️ Gym Management System

A simple **Gym Management System** built with **Python and MySQL** to manage gym member records efficiently through a menu-driven command-line interface.

The system provides basic member management operations such as **adding, viewing, updating, and deleting gym members**, while storing member information in a MySQL database.

---

## ✨ Features

- 👤 Add new gym members
- 📋 View all registered gym members
- ✏️ Update existing member information
- 🗑️ Delete gym members
- ⚖️ Store bodyweight and BMI information
- 🎫 Support multiple membership types
- 💾 Persistent data storage using MySQL
- 🔄 Automatic database table creation
- 🖥️ Simple menu-driven CLI interface

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| 🐍 **Python** | Application logic |
| 🐬 **MySQL** | Database management |
| 🔌 **mysql-connector-python** | Python–MySQL connectivity |
| 💻 **CLI** | User interface |

---

## 📂 Project Structure

```text
Gym-Management-System/
│
├── Gym Management.py
└── README.md
```

---

## 🗄️ Database Structure

The application uses a MySQL database named:

```text
gym_management_db
```

A `gym_members` table is created automatically when the application starts.

### `gym_members`

| Column | Type | Description |
|---|---|---|
| `ID` | INT | Unique member ID |
| `Name` | VARCHAR(255) | Member name |
| `Age` | INT | Member age |
| `Gender` | VARCHAR(10) | Member gender |
| `Bodyweight` | FLOAT | Member bodyweight |
| `BMI` | FLOAT | Body Mass Index |
| `Membership_type` | VARCHAR(20) | Membership plan |

The table uses an auto-incrementing primary key for member IDs.

---

## 🎯 Membership Types

The application currently accepts membership types such as:

```text
Yearly
Monthly
Daily pass
```

---

## 📋 Main Menu

When the application starts, users are presented with:

```text
================================== Main Menu: ==================================
→ 1. Management
→ 2. Membership
→ 3. Exit
```

### Management

The Management menu provides:

```text
1. View Gym Members
2. Delete Gym Member
3. Back
4. Update
```

### Membership

The Membership option allows a new gym member to be registered.

---

## ⚙️ Core Operations

### ➕ Add Member

Users can enter:

- Name
- Age
- Gender
- Bodyweight
- BMI
- Membership type

The information is inserted into the `gym_members` table.

### 👀 View Members

The application retrieves all records from the database and displays each member's:

```text
ID
Name
Age
Gender
Bodyweight
BMI
Membership Type
```



### ✏️ Update Member

An existing member can be updated using their ID. The application allows modification of all stored member information.

### 🗑️ Delete Member

Members can be removed from the database by providing their member ID.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Gym-Management-System.git
```

```bash
cd Gym-Management-System
```

### 2. Install Python

Make sure Python 3.x is installed.

Check your installation:

```bash
python --version
```

### 3. Install MySQL Connector

Install the required Python package:

```bash
pip install mysql-connector-python
```

### 4. Configure MySQL

Make sure your MySQL server is running.

Create the database:

```sql
CREATE DATABASE gym_management_db;
```

The application will automatically create the required `gym_members` table when it starts.

### 5. Configure Database Credentials

Update the database connection settings in the Python file:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="gym_management_db"
)
```

> ⚠️ **Security:** Never commit your actual MySQL password to GitHub. Use environment variables or a configuration file excluded through `.gitignore`.

### 6. Run the Application

```bash
python "Gym Management.py"
```

---

## 🔄 Application Flow

```text
                ┌───────────────────┐
                │   Start Program   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Connect to MySQL  │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Create Table if   │
                │    Not Existing   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │    Main Menu      │
                └───────┬───┬───────┘
                        │   │
             ┌──────────┘   └──────────┐
             ▼                         ▼
      ┌──────────────┐          ┌──────────────┐
      │ Management   │          │  Membership  │
      └──────┬───────┘          └──────┬───────┘
             │                         │
       ┌─────┼─────┐                   ▼
       ▼     ▼     ▼             Add Member
      View Delete Update
       │     │     │
       └─────┴─────┘
             │
             ▼
          Main Menu
```

---

## 🧠 What I Learned

This project helped strengthen practical knowledge of:

- Python functions
- Conditional statements
- Loops and menu-driven programs
- MySQL database connectivity
- SQL `CREATE`, `SELECT`, `INSERT`, `UPDATE`, and `DELETE`
- CRUD operations
- Database table design
- Python database connectors
- Handling user input
- Building a basic database-backed application

---

## 🔮 Future Improvements

Possible improvements for future versions:

- 🔐 User authentication and admin login
- 🖥️ Graphical User Interface
- 📊 Dashboard and analytics
- 💳 Payment and subscription tracking
- 📅 Attendance management
- 🏃 Workout-plan management
- 👨‍🏫 Trainer management
- 📈 Progress tracking
- 🔎 Member search and filtering
- 📄 Report generation
- 📱 Responsive/web-based version
- 🔒 Environment-based database credentials
- ✅ Input validation and error handling

---

## 📸 Screenshots

Add screenshots of the application here:

```text
screenshots/
├── main-menu.png
├── management-menu.png
├── add-member.png
├── members-list.png
└── update-member.png
```

Example:

```markdown
![Main Menu](screenshots/main-menu.png)
```

---

## 📌 Project Status

**Version:** 1.0  
**Status:** 🟢 Functional / Academic Project

The current version implements the core gym-member CRUD workflow using Python and MySQL.

---

## 👨‍💻 Author

**Mithun**

B.Tech Computer Science & Engineering  
SRM Institute of Science and Technology

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📄 License

This project is intended for **educational and academic purposes**.
# 🏋️ Gym Management System

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![MySQL](https://img.shields.io/badge/MySQL-5.7+-orange.svg)](https://www.mysql.com/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://riverbankcomputing.com/software/pyqt/)
[![SQLite3](https://img.shields.io/badge/SQLite3-Latest-lightblue.svg)](https://www.sqlite.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3+-red.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active%20Development-brightgreen.svg)]()
[![Versions](https://img.shields.io/badge/versions-2-blue.svg)]()

> **Two complete gym management solutions: CLI+MySQL for learning, GUI+SQLite for production**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Comparison](#quick-comparison)
- [Version 1.0 (CLI)](#version-10-cli--mysql)
- [Version 2.0 Advanced (GUI)](#version-20-advanced-gui--sqlite)
- [Installation](#installation)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This repository contains **two complete implementations** of a gym management system, showcasing progression from a simple CLI application to a professional desktop application.

### Why Two Versions?

- **Version 1**: Perfect for learning CRUD operations, database connectivity, and CLI design
- **Version 2**: Production-ready with modern UI, analytics, and advanced features
- **Together**: Show progression and growth in software development

---

## 🆚 Quick Comparison

| Feature | V1 (CLI) | V2 (GUI) |
|---------|----------|----------|
| **Interface** | Command-line | Modern GUI |
| **Database** | MySQL | SQLite |
| **Setup Time** | 5 minutes | 2 minutes |
| **Learning Curve** | Beginner | Intermediate |
| **Features** | Basic (1 module) | Advanced (10 modules) |
| **Analytics** | ❌ None | ✅ 6 Real-time Charts |
| **Offline Support** | ❌ Requires MySQL | ✅ Works Offline |
| **UI Design** | Traditional | Modern (Glass Morphism) |
| **Code Size** | ~100 lines | ~4,000 lines |
| **Best For** | Learning | Production |
| **Database Setup** | Manual SQL | Auto-generated |

---

## 🔄 Version 1.0 (CLI + MySQL)

### Quick Start

```bash
# Navigate to V1
cd v1-cli-mysql

# Install dependencies
pip install -r requirements.txt

# Setup MySQL database
mysql -u root -p < database_setup.sql

# Run application
python Gym_Management.py
```

### ✨ Features

- ✅ Add new gym members
- ✅ View all members
- ✅ Update member information
- ✅ Delete members
- ✅ Membership type tracking
- ✅ BMI management

### 📊 Database

- **Type**: MySQL
- **Tables**: 1 (gym_members)
- **Columns**: 7
- **Setup**: Manual SQL script

### 📖 Documentation

- [V1 README](v1-cli-mysql/README.md)
- [V1 Setup Guide](v1-cli-mysql/SETUP_GUIDE.md)
- [Database Schema](v1-cli-mysql/database_setup.sql)

### 🎓 What You'll Learn

- MySQL connectivity
- Python database operations
- CLI menu systems
- CRUD operations
- User input handling
- Error handling

### 💡 Example Code

```python
# Connect to database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="gym_management_db"
    )

# Add a member
def add_gym_member(connection):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    # Insert to database
    cursor.execute(
        "INSERT INTO gym_members (name, age) VALUES (%s, %s)",
        (name, age)
    )
    connection.commit()
```

---

## 🎨 Version 2.0 Advanced (GUI + SQLite)

### Quick Start

```bash
# Navigate to V2
cd v2-gui-sqlite

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

**Note**: Database auto-creates on first run!

### ✨ Features (10 Modules)

1. **👥 Members Management** - Complete member lifecycle
2. **🏋️ Trainers Management** - Trainer profiles & specializations
3. **⚖️ Body Metrics** - Weight/height tracking with auto-calculated BMI
4. **📋 Workout Plans** - Customized fitness programs
5. **💳 Payments** - Transaction recording & membership expiry
6. **🏷️ Memberships** - Plan tiers and pricing
7. **🏋️‍♂️ Equipment** - Inventory management with condition tracking
8. **📊 Analytics Dashboard** - 6 real-time charts with auto-refresh
9. **⚙️ Settings** - Configuration options
10. **🚪 Exit** - Safe shutdown

### 📊 Analytics Dashboard

**4 KPI Cards:**
- Total Members (with growth %)
- Active Trainers (with status)
- Total Revenue (with trend)
- Equipment Status

**6 Interactive Charts:**
1. 📈 Monthly Revenue Trend
2. 🥧 Membership Distribution
3. 📊 Member Growth
4. 🔥 Peak Hours Analysis
5. ⭐ Trainer Performance
6. ⚙️ Equipment Status

### 🎨 UI/UX Features

- **Glass Morphism Design** - Modern frosted glass effect
- **Gradient Backgrounds** - Purple-pink color scheme
- **Smooth Animations** - Login transitions, button effects
- **Dark Theme** - Optimized for analytics charts
- **Professional Styling** - Enterprise-grade appearance

### 💾 Database

- **Type**: SQLite3
- **Tables**: 7 normalized tables
- **Columns**: 38 total
- **Setup**: Automatic on first run

### 📖 Documentation

- [V2 README](v2-gui-sqlite/README.md)
- [V2 Setup Guide](v2-gui-sqlite/SETUP_GUIDE.md)
- [Architecture](v2-gui-sqlite/docs/architecture.md)
- [Database Schema](v2-gui-sqlite/docs/database_schema.md)

### 🎓 What You'll Learn

- PyQt5 GUI development
- Modern UI/UX design
- SQLite database management
- Data visualization (Matplotlib)
- Real-time updates
- MVC architecture
- Animation & styling

---

## 💻 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### For Version 1 (CLI)

```bash
cd v1-cli-mysql

# Install Python package
pip install -r requirements.txt

# Install MySQL (if not already installed)
# Windows: Download from mysql.com
# macOS: brew install mysql
# Linux: sudo apt-get install mysql-server

# Setup database
mysql -u root -p < database_setup.sql

# Run
python Gym_Management.py
```

**Default MySQL Credentials:**
```
Username: root
Password: (your MySQL password)
```

### For Version 2 (GUI)

```bash
cd v2-gui-sqlite

# Install dependencies
pip install -r requirements.txt

# Run (database auto-creates)
python main.py
```

**Default Login:**
```
Username: admin
Password: admin123
```

### 🪟 Windows Users

```bash
# V1
cd v1-cli-mysql
python Gym_Management.py

# V2
cd v2-gui-sqlite
python main.py
```

### 🐧 Linux/Mac Users

```bash
# V1
cd v1-cli-mysql
python3 Gym_Management.py

# V2
cd v2-gui-sqlite
python3 main.py
```

---

## 📚 Documentation

### Quick Links

#### Version 1 Documentation
- [V1 README](v1-cli-mysql/README.md) - Detailed V1 documentation
- [V1 Setup Guide](v1-cli-mysql/SETUP_GUIDE.md) - Step-by-step installation
- [Database Setup](v1-cli-mysql/database_setup.sql) - MySQL schema

#### Version 2 Documentation
- [V2 README](v2-gui-sqlite/README.md) - Detailed V2 documentation
- [V2 Setup Guide](v2-gui-sqlite/SETUP_GUIDE.md) - Installation guide
- [Architecture](v2-gui-sqlite/docs/architecture.md) - System design
- [Database Schema](v2-gui-sqlite/docs/database_schema.md) - Tables & relationships

#### Comparison & Migration
- [Architecture Comparison](docs/ARCHITECTURE_COMPARISON.md) - V1 vs V2 detailed
- [Migration Guide](docs/MIGRATION_GUIDE.md) - Upgrading from V1 to V2
- [Development Roadmap](docs/DEVELOPMENT_ROADMAP.md) - Future plans
- [Changelog](docs/CHANGELOG.md) - Version history

#### Contributing
- [Contributing Guidelines](docs/CONTRIBUTING.md) - How to contribute
- [Code Standards](docs/CONTRIBUTING.md#code-standards) - Coding conventions

---

## 🚀 Workflow Examples

### Version 1 (CLI) Workflow

```
1. Start application
   python Gym_Management.py

2. Choose option from menu
   Main Menu:
   → 1. Management
   → 2. Membership
   → 3. Exit

3. Perform actions
   - View all members
   - Add new member
   - Update member info
   - Delete member

4. Exit
   Press Ctrl+C or select Exit
```

### Version 2 (GUI) Workflow

```
1. Login
   admin / admin123

2. Dashboard
   Click any module card

3. Perform CRUD operations
   - Fill form → Click action button
   - Click table row → Edit → Update

4. View Analytics
   Click "Analytics" card
   - See 4 KPI cards
   - View 6 charts (auto-refresh)
   - Use time period filter

5. Exit
   Click Exit button or close window
```

---

## 📊 Project Statistics

### Version 1
```
Python Files:        1
Lines of Code:       ~100
Database Tables:     1
Features:            6
Complexity:          Low
Setup Time:          5 minutes
Learning Focus:      CRUD + MySQL
```

### Version 2
```
Python Files:        14
Lines of Code:       ~4,000
Documentation Pages: 50+
Database Tables:     7
Features:            10 modules
Modules:             Analytics, UI, DB
Complexity:          High
Setup Time:          2 minutes
Learning Focus:      Full-stack development
```

---

## 🔧 Technology Stack

### Version 1
- **Language**: Python 3.7+
- **Database**: MySQL 5.7+
- **Interface**: Command-line

### Version 2
- **Language**: Python 3.7+
- **Framework**: PyQt5 5.15+
- **Database**: SQLite3
- **Visualization**: Matplotlib 3.3+
- **Architecture**: MVC Pattern

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Quick Contribution Guide

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** with clear message
6. **Push** and create PR

### Areas for Contribution

#### Version 1 (CLI)
- [ ] Export to CSV
- [ ] Backup functionality
- [ ] Input validation
- [ ] Error handling

#### Version 2 (GUI)
- [ ] Email notifications
- [ ] SMS integration
- [ ] Export to PDF
- [ ] Dark mode
- [ ] Multi-language support
- [ ] User authentication

#### Both Versions
- [ ] Unit tests
- [ ] Integration tests
- [ ] Documentation
- [ ] Bug fixes
- [ ] Performance improvements

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 🗺️ Development Roadmap

### Current Status
- ✅ Version 1.0 - Complete & Stable
- ✅ Version 2.0 - Complete & Production-Ready

### Next Milestones

#### Version 2.1 (Q1 2025)
- [ ] Email notifications
- [ ] Export to Excel/PDF
- [ ] Attendance tracking
- [ ] Dark mode toggle

#### Version 3.0 (Q3 2025)
- [ ] Cloud synchronization
- [ ] Mobile app
- [ ] Web portal
- [ ] Multi-user authentication

See [DEVELOPMENT_ROADMAP.md](docs/DEVELOPMENT_ROADMAP.md) for details.

---

## 🐛 Troubleshooting

### Version 1 Issues

**MySQL Connection Error**
```
Solution: Check MySQL is running and credentials are correct
Windows: Start MySQL service
macOS: brew services start mysql
Linux: sudo service mysql start
```

**Import Error**
```bash
pip install --upgrade mysql-connector-python
```

### Version 2 Issues

**PyQt5 Import Error**
```bash
pip install --upgrade PyQt5
```

**Matplotlib Not Showing**
```bash
pip install matplotlib --upgrade
```

**Database Issues**
```bash
# Delete gym.db and restart application
# Database will auto-regenerate with clean schema
```

See detailed troubleshooting in version-specific READMEs.

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### What You Can Do
- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute copies
- ✅ Use privately

### Requirements
- ⚠️ Include license notice
- ⚠️ No liability or warranty

---

## 👤 Author

**Mithun**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@gmail.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Portfolio: [yoursite.com](https://yoursite.com) (optional)

---

## ⭐ Show Support

If this project helped you:
- **Star** ⭐ this repository
- **Fork** 🍴 to contribute
- **Share** 📢 with others
- **Report** 🐛 issues
- **Suggest** 💡 features

---

## 🙏 Acknowledgments

### Technologies
- Python community
- PyQt5 framework
- SQLite team
- Matplotlib developers

### References
- [Python Documentation](https://docs.python.org/)
- [PyQt5 Documentation](https://doc.qt.io/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

---

## 📞 Support & Questions

### Getting Help

1. **Check Documentation**
   - Read version-specific README
   - Review setup guides
   - Check troubleshooting section

2. **Search Issues**
   - [Open Issues](../../issues)
   - [Closed Issues](../../issues?q=is%3Aissue+is%3Aclosed)

3. **Create Issue**
   - Describe your problem
   - Include error message
   - Specify Python/OS version

4. **Start Discussion**
   - Ask questions
   - Share ideas
   - Discuss features

---

## 📈 Repository Stats

```
Languages:          Python
Total Files:        50+
Total Lines:        4,100+
Documentation:      50+ pages
Database Tables:    8 (across both versions)
Supported Platforms: Windows, macOS, Linux
```

---

## 🎓 Learning Value

This repository demonstrates:

### Software Development Skills
✅ Full-stack application development
✅ Database design & optimization
✅ GUI development with modern frameworks
✅ Data visualization techniques
✅ Version control & collaboration

### Programming Concepts
✅ CRUD operations
✅ Object-oriented programming
✅ MVC architecture
✅ Design patterns
✅ Data normalization

### Tools & Technologies
✅ Python (CLI & GUI)
✅ MySQL & SQLite
✅ PyQt5 framework
✅ Matplotlib charting
✅ Git version control

---

## 🎯 Perfect For

- 🎓 **Students** - Learning full-stack development
- 💼 **Beginners** - Starting with Python/databases
- 📚 **Educators** - Teaching CRUD operations
- 💻 **Developers** - Portfolio showcase
- 🏋️ **Gym Owners** - Managing operations

---

<div align="center">

### 🚀 Ready to Get Started?

**[Click Here for Quick Start Guide](#installation)**

---

### ⭐ Don't Forget to Star! ⭐

Made with ❤️ for the Python community

[Fork](../../fork) | [Star](../../) | [Watch](../../subscription)

**Happy Coding!** 💻✨

---

Last Updated: December 2024  
Status: ✅ Active Development  
Version: 1.0 (CLI) + 2.0 Advanced (GUI)

</div>

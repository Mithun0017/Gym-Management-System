# 🏋️ Gym Management System

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![MySQL](https://img.shields.io/badge/MySQL-5.7+-orange.svg)](https://www.mysql.com/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://riverbankcomputing.com/software/pyqt/)
[![SQLite3](https://img.shields.io/badge/SQLite3-Latest-lightblue.svg)](https://www.sqlite.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3+-red.svg)](https://matplotlib.org/)
[![Status](https://img.shields.io/badge/status-Active%20Development-brightgreen.svg)]()
[![Versions](https://img.shields.io/badge/versions-2-blue.svg)]()

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

### 📖 Documentation

- [V2 README](v2-gui-sqlite/README.md)
- [V2 Setup Guide](v2-gui-sqlite/SETUP_GUIDE.md)
- [Architecture](v2-gui-sqlite/docs/architecture.md)
- [Database Schema](v2-gui-sqlite/docs/database_schema.md)

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
Username: yourusername
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

---

## 👤 Author

**Mithun**
- GitHub: [@Mithun0017](https://github.com/Mithun0017)
- Email: mithun200617@gmail.com
- LinkedIn: [Mithun0017](https://linkedin.com/in/Mithun0017)
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

<div align="center">

### 🚀 Ready to Get Started?

**[Click Here for Quick Start Guide](#installation)**

---

### ⭐ Don't Forget to Star! ⭐

Made with ❤️ for the Python community

**Happy Coding!** 💻✨

---

</div>

import sys
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
from dashboard import Dashboard

class GymManagementSystem:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("Gym Management System")
        
        self.app.setStyle('Fusion')
        
        self.login_window = LoginWindow()
        self.login_window.login_successful.connect(self.show_dashboard)
        self.login_window.show()
    
    def show_dashboard(self):
        self.dashboard = Dashboard()
        self.dashboard.show()
    
    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    gym_app = GymManagementSystem()
    gym_app.run()

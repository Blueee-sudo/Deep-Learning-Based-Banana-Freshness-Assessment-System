import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.set_window_style()
        self.set_connections()

    def init_ui(self):
        # 窗口基本设置
        self.setWindowTitle("系统登录")
        self.setWindowIcon(QIcon("D:/banana/基于深度学习的香蕉新鲜度等级识别系统/系统图标.jpg"))
        self.resize(800, 600)
        self.setFixedSize(800, 600)  # 固定窗口大小

        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 40, 50, 40)
        main_layout.setSpacing(30)

        # 标题
        title_label = QLabel("香蕉新鲜度等级识别系统")
        title_label.setFont(QFont("微软雅黑", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50;")
        main_layout.addWidget(title_label)

        # 用户名输入
        user_layout = QHBoxLayout()
        user_label = QLabel("用户名:")
        user_label.setFixedWidth(130)
        user_label.setFont(QFont("微软雅黑", 15))
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("请输入用户名")
        self.user_input.setStyleSheet(self.get_input_style())
        # 输入框
        self.user_input.setMinimumHeight(42)
        self.user_input.setMinimumWidth(280)
        user_layout.addWidget(user_label)
        user_layout.addWidget(self.user_input)
        main_layout.addLayout(user_layout)

        # 密码输入
        pwd_layout = QHBoxLayout()
        pwd_label = QLabel("密   码:")
        pwd_label.setFixedWidth(130)
        pwd_label.setFont(QFont("微软雅黑", 15))
        self.pwd_input = QLineEdit()
        self.pwd_input.setPlaceholderText("请输入密码")
        self.pwd_input.setEchoMode(QLineEdit.Password)
        self.pwd_input.setStyleSheet(self.get_input_style())
        # 同步输入框尺寸
        self.pwd_input.setMinimumHeight(42)
        self.pwd_input.setMinimumWidth(280)
        pwd_layout.addWidget(pwd_label)
        pwd_layout.addWidget(self.pwd_input)
        main_layout.addLayout(pwd_layout)

        # 登录按钮
        self.login_btn = QPushButton("登录")
        self.login_btn.setFixedHeight(50)
        self.login_btn.setStyleSheet(self.get_button_style())
        main_layout.addWidget(self.login_btn)

    def set_window_style(self):
        # 窗口整体样式
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
            }
        """)

    def set_connections(self):
        self.login_btn.clicked.connect(self.check_login)

    def get_input_style(self):
        return """
            QLineEdit {
                border: 1px solid #e0e0e0;
                border-radius: 8px;  
                padding: 0 15px;  
                font-size: 15px;  
                color: #34495e;
            }
            QLineEdit:focus {
                border-color: #3498db;
                outline: none;
            }
        """

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #3498db;
                border: none;
                color: white;
                font-size: 17px;  
                font-weight: 500;
                border-radius: 8px;  
            }
            QPushButton:hover {
                background-color: #2980b9;
                border: 1px solid #2573a7;
            }
            QPushButton:pressed {
                background-color: #20638f;
            }
        """

    def check_login(self):
        # 验证逻辑保持不变
        username = self.user_input.text()
        password = self.pwd_input.text()

        if username == "ll" and password == "2213040106":
            self.accept()
        else:
            QMessageBox.warning(self, "登录失败", "用户名或密码错误", QMessageBox.Ok)

    def accept(self):
        self.close()
        # 延迟导入主窗口避免循环依赖
        from main import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
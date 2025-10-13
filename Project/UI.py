import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QFileDialog, QSlider, QTableWidget,
                             QTableWidgetItem, QGroupBox, QComboBox, QSpinBox, QDoubleSpinBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QImage, QIcon


class UIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("香蕉新鲜度等级识别系统")
        self.setWindowIcon(QIcon("D:/基于深度学习的香蕉新鲜度等级识别系统/Project/系统图标.jpg"))
        self.resize(1400, 900)  # 调整初始窗口尺寸

        # 主窗口中心部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 主布局（调整为左侧60%，右侧40%）
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # 增加整体边距
        self.main_layout.setSpacing(25)  # 增加组件间距

        # 左侧面板 (图像显示)
        self.left_panel = QVBoxLayout()
        self.main_layout.addLayout(self.left_panel, 60)  # 左侧占比60%

        # 原始图像显示（优化分组框样式）
        self.original_image_group = QGroupBox("原始图像")
        self.original_image_layout = QVBoxLayout()
        self.original_image_label = QLabel()
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.original_image_label.setMinimumSize(800, 450)  # 调整最小显示尺寸
        self.original_image_layout.setContentsMargins(15, 25, 15, 15)  # 增加内边距
        self.original_image_layout.addWidget(self.original_image_label)
        self.original_image_group.setLayout(self.original_image_layout)
        self.left_panel.addWidget(self.original_image_group)

        # 检测结果图像显示
        self.result_image_group = QGroupBox("检测结果")
        self.result_image_layout = QVBoxLayout()
        self.result_image_label = QLabel()
        self.result_image_label.setAlignment(Qt.AlignCenter)
        self.result_image_label.setMinimumSize(800, 450)
        self.result_image_layout.setContentsMargins(15, 25, 15, 15)
        self.result_image_layout.addWidget(self.result_image_label)
        self.result_image_group.setLayout(self.result_image_layout)
        self.left_panel.addWidget(self.result_image_group)

        # 右侧面板 (控制面板)
        self.right_panel = QVBoxLayout()
        self.main_layout.addLayout(self.right_panel, 40)  # 右侧占比40%
        self.right_panel.setSpacing(20)  # 增加垂直间距

        # 模型选择（优化分组框内边距）
        self.model_group = QGroupBox("模型设置")
        self.model_layout = QVBoxLayout()
        self.model_layout.setContentsMargins(15, 25, 15, 15)
        self.model_combo = QComboBox()
        self.model_combo.addItems(["best"])
        self.model_combo.setStyleSheet("QComboBox { padding: 6px; font-size: 13px; }")  # 调整下拉框样式
        self.model_layout.addWidget(QLabel("选择模型:"))
        self.model_layout.addWidget(self.model_combo)
        self.model_group.setLayout(self.model_layout)
        self.right_panel.addWidget(self.model_group)

        # 检测参数（优化标签间距）
        self.params_group = QGroupBox("检测参数")
        self.params_layout = QVBoxLayout()
        self.params_layout.setContentsMargins(15, 25, 15, 15)
        self.params_layout.setSpacing(12)  # 增加参数行间距

        # 置信度阈值
        self.confidence_label = QLabel("置信度阈值: 0.25")
        self.confidence_label.setStyleSheet("font-size: 13px;")
        self.confidence_slider = QSlider(Qt.Horizontal)
        self.confidence_slider.setRange(0, 100)
        self.confidence_slider.setValue(25)
        self.confidence_spinbox = QDoubleSpinBox()
        self.confidence_spinbox.setRange(0.0, 1.0)
        self.confidence_spinbox.setSingleStep(0.05)
        self.confidence_spinbox.setValue(0.25)
        self.confidence_spinbox.setStyleSheet("QDoubleSpinBox { padding: 4px; font-size: 12px; }")

        # IoU阈值
        self.iou_label = QLabel("IoU阈值: 0.45")
        self.iou_label.setStyleSheet("font-size: 13px;")
        self.iou_slider = QSlider(Qt.Horizontal)
        self.iou_slider.setRange(0, 100)
        self.iou_slider.setValue(45)
        self.iou_spinbox = QDoubleSpinBox()
        self.iou_spinbox.setRange(0.0, 1.0)
        self.iou_spinbox.setSingleStep(0.05)
        self.iou_spinbox.setValue(0.45)
        self.iou_spinbox.setStyleSheet("QDoubleSpinBox { padding: 4px; font-size: 12px; }")

        self.params_layout.addWidget(self.confidence_label)
        self.params_layout.addWidget(self.confidence_slider)
        self.params_layout.addWidget(self.confidence_spinbox)
        self.params_layout.addWidget(self.iou_label)
        self.params_layout.addWidget(self.iou_slider)
        self.params_layout.addWidget(self.iou_spinbox)
        self.params_group.setLayout(self.params_layout)
        self.right_panel.addWidget(self.params_group)

        # 功能按钮（调整按钮尺寸和间距）
        self.buttons_group = QGroupBox("功能操作")
        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setContentsMargins(15, 25, 15, 15)
        self.buttons_layout.setSpacing(12)  # 增加按钮间距

        self.image_btn = QPushButton("图片检测")
        self.video_btn = QPushButton("视频检测")
        self.camera_btn = QPushButton("摄像头检测")
        self.stop_btn = QPushButton("停止检测")
        self.save_btn = QPushButton("保存结果")

        # 统一按钮样式（增加高度和字体大小）
        btn_style = """
            QPushButton {
                background-color: #3498db;
                border: none;
                color: white;
                padding: 10px;
                font-size: 14px;
                font-weight: 500;
                border-radius: 6px;
                height: 40px;
            }
            QPushButton:hover {
                background-color: #2980b9;
                border: 1px solid #2573a7;
            }
            QPushButton:pressed {
                background-color: #20638f;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
            }
        """
        self.image_btn.setStyleSheet(btn_style)
        self.video_btn.setStyleSheet(btn_style)
        self.camera_btn.setStyleSheet(btn_style)
        self.stop_btn.setStyleSheet(btn_style)
        self.save_btn.setStyleSheet(btn_style)

        self.buttons_layout.addWidget(self.image_btn)
        self.buttons_layout.addWidget(self.video_btn)
        self.buttons_layout.addWidget(self.camera_btn)
        self.buttons_layout.addWidget(self.stop_btn)
        self.buttons_layout.addWidget(self.save_btn)
        self.buttons_group.setLayout(self.buttons_layout)
        self.right_panel.addWidget(self.buttons_group)

        # 检测结果表格（优化列宽和表头样式）
        self.results_group = QGroupBox("检测结果")
        self.results_layout = QVBoxLayout()
        self.results_layout.setContentsMargins(15, 25, 15, 15)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(4)
        self.results_table.setHorizontalHeaderLabels(["类别", "置信度", "位置(x)", "位置(y)"])
        self.results_table.setColumnWidth(0, 120)  # 调整列宽
        self.results_table.setColumnWidth(1, 100)
        self.results_table.setColumnWidth(2, 100)
        self.results_table.setColumnWidth(3, 100)
        self.results_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                font-size: 13px;
            }
            QHeaderView::section {
                background-color: #f5f5f5;
                padding: 8px;
                border: none;
                font-weight: bold;
                font-size: 13px;
            }
            QTableWidgetItem {
                padding: 6px;
            }
        """)

        self.results_layout.addWidget(self.results_table)
        self.results_group.setLayout(self.results_layout)
        self.right_panel.addWidget(self.results_group)

        # 状态栏（增加背景色和内边距）
        self.status_bar = self.statusBar()
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #f8f9fa;
                border-top: 1px solid #e9ecef;
                padding-left: 10px;
                font-size: 13px;
            }
        """)
        self.status_bar.showMessage("就绪")

        # 整体样式表（优化分组框、标签等基础样式）
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QGroupBox {
                border: 1px solid #e9ecef;
                border-radius: 8px;
                margin-top: 15px;
                padding-top: 20px;
                font-size: 14px;
                font-weight: 600;
                color: #2c3e50;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 8px;
                background-color: #f8f9fa;
            }
            QLabel {
                font-size: 13px;
                color: #34495e;
            }
            QSlider::groove:horizontal {
                height: 6px;
                background: #e0e0e0;
                margin: 0 4px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #3498db;
                border: 2px solid white;
                width: 18px;
                height: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }
        """)

        # 连接信号和槽（保持原有逻辑不变）
        self.confidence_slider.valueChanged.connect(self.update_confidence)
        self.confidence_spinbox.valueChanged.connect(self.update_confidence_slider)
        self.iou_slider.valueChanged.connect(self.update_iou)
        self.iou_spinbox.valueChanged.connect(self.update_iou_slider)

    def update_confidence(self, value):
        confidence = value / 100.0
        self.confidence_spinbox.setValue(confidence)
        self.confidence_label.setText(f"置信度阈值: {confidence:.2f}")

    def update_confidence_slider(self, value):
        self.confidence_slider.setValue(int(value * 100))

    def update_iou(self, value):
        iou = value / 100.0
        self.iou_spinbox.setValue(iou)
        self.iou_label.setText(f"IoU阈值: {iou:.2f}")

    def update_iou_slider(self, value):
        self.iou_slider.setValue(int(value * 100))

    def display_image(self, label, image):
        if image is not None:
            h, w, ch = image.shape
            bytes_per_line = ch * w
            q_img = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            # 优化图像缩放方式（保持宽高比，使用平滑缩放）
            label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def clear_results(self):
        self.results_table.setRowCount(0)

    def add_detection_result(self, class_name, confidence, x, y):
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        # 优化表格内容显示（居中对齐）
        self.results_table.setItem(row, 0, QTableWidgetItem(class_name))
        self.results_table.setItem(row, 1, QTableWidgetItem(f"{confidence:.2f}"))
        self.results_table.item(row, 1).setTextAlignment(Qt.AlignCenter)
        self.results_table.setItem(row, 2, QTableWidgetItem(f"{x:.1f}"))
        self.results_table.item(row, 2).setTextAlignment(Qt.AlignCenter)
        self.results_table.setItem(row, 3, QTableWidgetItem(f"{y:.1f}"))
        self.results_table.item(row, 3).setTextAlignment(Qt.AlignCenter)

    def update_status(self, message):
        self.status_bar.showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UIWindow()
    window.show()
    sys.exit(app.exec_())
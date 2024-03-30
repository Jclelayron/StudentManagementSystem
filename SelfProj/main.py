from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton,\
    QComboBox
import sys

class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        #Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()
        self.distance_combo_box = QComboBox()
        self.distance_combo_box.addItems(["Imperial (miles)", "Metric (km)"])
        
        time_label = QLabel("Time(hours):")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.output_label = QLabel(" ")

        #Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.distance_combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit,  1 ,1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)
        
    def calculate_speed(self):
        computed_val = round(float(self.distance_line_edit.text())/float(self.time_line_edit.text()), 2)
        if self.distance_combo_box.currentIndex() == 0:
            speed = f"Average Speed: {computed_val} mph"
        elif self.distance_combo_box.currentIndex() == 1:
            speed = f"Average Speed: {computed_val} kmph"
        self.output_label.setText(speed)
        
app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculator()
average_speed_calculator.show()
sys.exit(app.exec())
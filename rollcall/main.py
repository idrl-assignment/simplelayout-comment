import sys
from pathlib import Path
import itertools
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

from Ui_rollcall_dialog import Ui_Dialog


here = Path(__file__).resolve().parent


def get_lt(path):
    with open(path, "r", encoding="utf-8") as file:
        lt = file.readlines()
    return lt


class rollWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, interval=20):
        super().__init__(parent)
        self.setupUi(self)
        self.interval = interval

        self.running = False
        self.checkboxes = []
        self.students_lt = get_lt(here / "students_lt.txt")
        self.init_checkbox(self.students_lt)
        self.timer = QTimer(self)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.timer.timeout.connect(self.update)

    def init_lt_cycle(self):
        lt = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        self.lt_cycle = itertools.cycle(lt)

    def init_checkbox(self, lt: list):
        for student in lt:
            checkbox = QCheckBox(text=student)
            checkbox.setChecked(True)
            self.checkboxes.append(checkbox)
            self.verticalLayout.addWidget(checkbox)

    def start(self):
        self.init_lt_cycle()
        self.timer.start(self.interval)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)

    def stop(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def update(self):
        student = next(self.lt_cycle)
        self.label_result.setText(student)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = rollWindow(interval=10)
    main_window.show()
    sys.exit(app.exec_())

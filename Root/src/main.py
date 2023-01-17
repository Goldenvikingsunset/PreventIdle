import time
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QDialog, QComboBox, QListWidget
from PyQt5.QtCore import Qt, QTimer

class TypingTest(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Typing Test")

        # create a combo box to select the test string
        self.text_combo_box = QComboBox()
        self.text_combo_box.addItems(["Text 1", "Text 2", "Text 3", "Custom Text"])
        self.text_combo_box.activated.connect(self.select_text)

        # create a label to display the test string
        self.text_label = QLabel()
        self.text_label.setAlignment(Qt.AlignCenter)

        # create a line edit to accept user input
        self.user_input = QLineEdit()

        # create a start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_test)

        # create a stop button
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_test)
        self.stop_button.setEnabled(False)

        # create a layout to hold the text label, user input, and buttons
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_combo_box)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.user_input)

        # create a layout to hold the start and stop buttons
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.start_button)
        self.buttons_layout.addWidget(self.stop_button)
        self.layout.addLayout(self.buttons_layout)

        self.setLayout(self.layout)

        # create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # create a leaderboard
        self.leaderboard = QListWidget()
        self.leaderboard.setFixedSize(200, 300)
        self.layout.addWidget(self.leaderboard)
        
        self.texts = ["The quick brown fox jumps over the lazy dog. " * 5,"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"]
        self.select_text(0)

    def select_text(self, index):
        if index == 3:
            self.text = input("Enter the text you want to use for the test:")
        else:
            self.text = self.texts[index]
        self.text_label.setText(self.text)

    def start_test(self):
        self.start_time = time.time()
        self.user_input.setReadOnly(False)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.timer.start(1000)
        self.elapsed_time = 0
        
    def update_timer(self):
        self.elapsed_time += 1
        if self.elapsed_time == 60:
            self.stop_test()
        
    def stop_test(self):
        self.timer.stop()
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        user_input_text = self.user_input.text()
        speed = len(user_input_text) / total_time
        accuracy = (len(self.text) - abs(len(self.text) - len(user_input_text))) / len(self.text) * 100
        wpm = speed * 60 / 5
        score = wpm * accuracy / 100

        print("Time taken: {:.2f} seconds".format(total_time))
        print("Speed: {:.2f} characters per second".format(speed))
        print("Accuracy: {:.2f}%".format(accuracy))
        print("Words per minute: {:.2f}".format(wpm))
        print("Score: {:.2f}".format(score))
        
        #add the score and username to the leaderboard
        name = input("Enter your name: ")
        self.leaderboard.addItem(f"{name} - {score:.2f}")

        self.user_input.setReadOnly(True)
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

if __name__ == '__main__':
    app = QApplication([])
    typing_test = TypingTest()
    typing_test.show()
    app.exec_()

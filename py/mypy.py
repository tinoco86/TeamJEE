#Final: Team Project    #Professor Avner Biblarz     #CST 205     #Homework 4
#BY: Evert Rodriguez, Jessica Jimenez, and Eric Tinoco

#Objective 1:
#Objective 2:
import sys
from PIL import Image
from main_project import SRec
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QComboBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # To hold each image 
        # p1 = QPixmap("")
        # p2 = QPixmap("")
        # p3 = QPixmap("")
        # p4 = QPixmap("")
        # p5 = QPixmap("")
        # p6 = QPixmap("")
        # p7 = QPixmap("")
        # p8 = QPixmap("")
        # p9 = QPixmap("")


        #picture = QPixmap(" ")
        #self.resetLabel = None
        #self.resetLabel = QLabel()

        #self.picture_label = QLabel("Image Name: ", self)
        #self.my_line_edit = QLineEdit(self)
        
        #self.drop_box = QComboBox()
        #self.drop_box.addItems(style_list)
        #self.style_label = QLabel("Manipulate the Style: ", self)

        self.search_button = QPushButton("I'm Listening", self)
        #self.response_label = QLabel(self)

        #h_layout1 = QHBoxLayout()
        #h_layout1.addWidget(self.picture_label)
        #h_layout1.addWidget(self.my_line_edit)

        #h_layout2 = QHBoxLayout()
        #h_layout2.addWidget(self.style_label)
        #h_layout2.addWidget(self.drop_box)

        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(self.search_button)
        #h_layout3.addWidget(self.response_label)

        #h_layout4 = QHBoxLayout()
        #h_layout4.addWidget(self.resetLabel)
        #self.resetLabel.setPixmap(picture)

        global v_layout
        v_layout = QVBoxLayout()

        #v_layout.addLayout(h_layout1)
        #v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        #v_layout.addLayout(h_layout4)
        
        # Sets all of the layouts
        self.setLayout(v_layout)
        
        # Uppon clicking on the search button, It goes to the function "on_click"
        self.search_button.clicked.connect(self.on_click)

        # Set title of the page
        self.setWindowTitle("I'm Listening")
        # Set size of the page
        self.setGeometry(550, 250, 300, 300)
        # Shows everything on the page
        self.show()

    # on_click goes to here
    @pyqtSlot()
    def on_click(self):
        someText = SRec() # Runs main_project.py and returns the text from voice recognition to "someText"
        tags = someText.split() # To refine search, words will be split into tags. 

        for word in tags:
            print(word)
        #print("Here are some images of: " + someText)

    # Anything needing updating goes here. After each search phrase, the images will update here
    #@pyqtSlot()
    #def update_img(self, picture):

app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
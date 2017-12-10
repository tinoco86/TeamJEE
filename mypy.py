#Final: Team JEE SEARCH IMAGE Project    
#Professor Avner Biblarz  
#CST 205     
#BY: Evert Rodriguez, Jessica Jimenez, and Eric Tinoco
# The Program will run through a GUI. When The GUI appears the user will be asked “What Image would you like to search for?” with audio. 
#The user will speak to the GUI to search for the image. The GUI will get the users speech input and transform it into a text. 
#The text will be used to search for the image using flicker. 
import pyttsx3
import sys
import requests
import urllib.request
from PIL import Image
from main_project import SRec
from get_pictures import flickr_search
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QComboBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
#-------------text to speech start---------------
# Gets the user audio input and trasforms it into txt. 
#engine = pyttsx3.init()
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-450)
#voices = engine.getProperty('voices')
#for voice in voices:
#   engine.setProperty('voice', voice.id)
#-------------text to speech end---------------
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # To hold each image
        p1 = QPixmap(" ")
        p2 = QPixmap(" ")
        p3 = QPixmap(" ")

        #self.resetLabel = None
        self.resetLabel1 = QLabel()
        self.resetLabel2 = QLabel()
        self.resetLabel3 = QLabel()

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
        
        #Displays images 1,2 and 3 in GUI
        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(self.resetLabel1)
        h_layout4.addWidget(self.resetLabel2)
        h_layout4.addWidget(self.resetLabel3)
        self.resetLabel1.setPixmap(p1)
        self.resetLabel2.setPixmap(p2)
        self.resetLabel3.setPixmap(p3)

        global v_layout
        v_layout = QVBoxLayout()

        #v_layout.addLayout(h_layout1)
        #v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)

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
        #engine.say('What would you like to search for?')
        #engine.runAndWait()
        someText = SRec() # Runs main_project.py and returns the text from voice recognition to "someText"
        link1 = flickr_search(someText)
        link2 = flickr_search(someText)
        link3 = flickr_search(someText)
        print(someText)
        pic1 = ""
        pic2 = ""
        pic3 = ""
        for i in range(1, 4):
            #print(i)
            if i == 1:
                with urllib.request.urlopen(link1) as url:
                    with open('temp.jpg','wb') as f:
                        f.write(url.read())
                pic1 = QPixmap('temp.jpg')
            elif i == 2:
                with urllib.request.urlopen(link2) as url:
                    with open('temp.jpg','wb') as f:
                        f.write(url.read())
                pic2 = QPixmap('temp.jpg')
            elif i == 3:
                with urllib.request.urlopen(link3) as url:
                    with open('temp.jpg','wb') as f:
                        f.write(url.read())
                pic3 = QPixmap('temp.jpg')
        self.update_img(pic1, pic2, pic3)
        #img = Image.open('temp.jpg')
        #img.show()
        #self.update_img(img)

        #print(url)
        #for word in tags:
        #    print(word)
        #print("Here are some images of: " + someText)


    #Anything needing updating goes here. After each search phrase, the images will update here
    @pyqtSlot()
    def update_img(self, picture1, picture2, picture3):
        self.resetLabel1.setPixmap(picture1)
        self.resetLabel2.setPixmap(picture2)
        self.resetLabel3.setPixmap(picture3)

app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())

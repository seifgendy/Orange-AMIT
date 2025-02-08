from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtGui import QDesktopServices  # Import QDesktopServices for desktop opening
import requests


class Ui_MainWindow(object):
    a = 0  # Horizontal offset for positioning
    b = 0  # Vertical offset for positioning
    x = 1280  # Window width
    y = 720   # Window height
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.x, self.y)  # Set initial window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("""
        *{ color:#000000; }
        #MainSide{ background-color:#000000; }
        #LeftSide{ background-color:#808080; }
        #RightSide{ background-color:#000000; }
        """)
        self.centralwidget.setObjectName("centralwidget")

        self.MainSide = QtWidgets.QWidget(self.centralwidget)
        self.MainSide.setGeometry(QtCore.QRect(self.a, self.b, self.x, self.y))  # Full window size
        self.MainSide.setObjectName("MainSide")

        self.RightSide = QtWidgets.QWidget(self.MainSide)
        self.RightSide.setGeometry(QtCore.QRect(self.a + 960, self.b + 60, self.x / 4, self.y / 1.2))  # Adjust size relative to main window
        self.RightSide.setObjectName("RightSide")

        # 🔒 Lock Button
        self.Lock = QtWidgets.QPushButton(self.RightSide)
        self.Lock.setGeometry(QtCore.QRect(self.a + 20, self.b + 20, self.x / 4.5, self.y / 12))  # Adjust button size
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Lock.setFont(font)

        self.lock_icon_locked = QtGui.QIcon("lock.png")  # Locked state icon
        self.lock_icon_unlocked = QtGui.QIcon("lock-open-alt.png")  # Unlocked state icon
        self.lock_state = False  # Default: Unlocked state

        self.Lock.setIcon(self.lock_icon_unlocked)
        self.Lock.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Lock.setObjectName("Lock")
        self.Lock.clicked.connect(self.toggle_lock)  # Connect button to function

        self.Bluetooth = QtWidgets.QPushButton(self.RightSide)
        self.Bluetooth.setGeometry(QtCore.QRect(self.a + 20, self.b + 120, self.x / 4.5, self.y / 12))  # Adjust button size
        font.setBold(True)
        self.Bluetooth.setFont(font)
        self.Bluetooth.setIcon(QtGui.QIcon("bluetooth-alt.png"))
        self.Bluetooth.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Bluetooth.setObjectName("Bluetooth")


        self.Navigation = QtWidgets.QPushButton(self.RightSide)
        self.Navigation.setGeometry(QtCore.QRect(self.a + 20, self.b + 220, self.x / 4.5, self.y / 12))  # Adjust button size
        self.Navigation.setFont(font)
        self.Navigation.setIcon(QtGui.QIcon("map-marker.png"))
        self.Navigation.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Navigation.setObjectName("Navigation")
        self.Navigation.clicked.connect(self.show_map)

        self.SignDetection = QtWidgets.QPushButton(self.RightSide)
        self.SignDetection.setGeometry(QtCore.QRect(self.a + 20, self.b + 320, self.x / 4.5, self.y / 12))  # Adjust button size
        self.SignDetection.setFont(font)
        self.SignDetection.setIcon(QtGui.QIcon("road-sign.png"))
        self.SignDetection.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.SignDetection.setObjectName("SignDetection")

        self.Radio = QtWidgets.QPushButton(self.RightSide)
        self.Radio.setGeometry(QtCore.QRect(self.a + 20, self.b + 420, self.x / 4.5, int(self.y / 12)))  # Adjust button size
        self.Radio.setFont(font)
        self.Radio.setIcon(QtGui.QIcon("radio.png"))
        self.Radio.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Radio.setObjectName("Radio")
        self.Radio.clicked.connect(self.open_radio)  # Connect to the open radio function


        self.LeftSide = QtWidgets.QWidget(self.MainSide)
        self.LeftSide.setGeometry(QtCore.QRect(self.a, self.b + 10, self.x / 1.33, self.y))  # Adjust size relative to main window
        self.LeftSide.setObjectName("LeftSide")

        self.label = QtWidgets.QLabel(self.LeftSide)
        self.label.setGeometry(QtCore.QRect(self.a + 30, self.b, self.x / 1.42, self.b / 1.0589))  # Adjust label size
        self.label.setText("")
        self.label.setObjectName("label")


        # WebEngineView to display map or radio or temp
        self.map_viewer = QWebEngineView(self.LeftSide)
        self.map_viewer.setGeometry(QtCore.QRect(30, 0, 900, 680))  # Adjust map viewer size
        self.map_viewer.setObjectName("map_viewer")

        # ⏰ Time Label (Position top right corner)
        self.Time = QtWidgets.QLabel(self.MainSide)
        self.Time.setGeometry(QtCore.QRect( int(self.a + 970), int(self.b +10 ), 100, 40))  # Adjust time label position
        self.Time.setStyleSheet("font-size: 16px; color: gray;")
        self.Time.setFont(font)
        self.Time.setObjectName("Time")

        # 🌡 Temperature Label (Below Time)
        self.temp = QtWidgets.QLabel(self.MainSide)
        self.temp.setGeometry(QtCore.QRect( int(self.a + 1150),int(self.b +10 ), 150, 40))  # Position below time
        self.temp.setStyleSheet("font-size: 16px; color: gray;")
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")


        # Lock Message Label (Popup on Left Side)
        self.lock_message = QtWidgets.QLabel(self.LeftSide)
        self.lock_message.setGeometry(QtCore.QRect(int(self.a + 300), int(self.b + 300), 400, 100))
        self.lock_message.setStyleSheet("font-size: 30px; color: white; background-color: gray; padding: 10px; border-radius: 10px;")
        self.lock_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lock_message.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ⏳ Timer to update time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()  # Initial update

        # Timer for Temperature
        self.temp_timer = QTimer()
        self.temp_timer.timeout.connect(self.update_temperature)
        self.temp_timer.start(60000)
        self.update_temperature()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bluetooth.setText(_translate("MainWindow", "     Bluetooth"))
        self.Lock.setText(_translate("MainWindow", "     Lock"))
        self.Navigation.setText(_translate("MainWindow", "     Navigation"))
        self.SignDetection.setText(_translate("MainWindow", "   Sign Detection"))
        self.Radio.setText(_translate("MainWindow", "     Radio"))
        self.Time.setText(_translate("MainWindow", "00:00"))
        self.temp.setText(_translate("MainWindow", "Temp"))

    def update_time(self):
        """ Update the time label with the current time """
        current_time = QDateTime.currentDateTime().toString("hh:mm")
        self.Time.setText(current_time)

    def toggle_lock(self):
        """ Toggle the lock icon between locked and unlocked and show a message """
        if self.lock_state:
            self.Lock.setIcon(self.lock_icon_unlocked)  # Unlock icon
            self.Lock.setText("     Unlock")
            message = "🔓 Unlocked"
        else:
            self.Lock.setIcon(self.lock_icon_locked)  # Lock icon
            self.Lock.setText("     Lock")
            message = "🔒 Locked"
    
        self.lock_state = not self.lock_state  # Toggle state
    
        # Show message in the Left Side
        self.lock_message.setText(message)
        self.lock_message.setVisible(True)
    
        # Hide message after 2 seconds
        QtCore.QTimer.singleShot(2000, lambda: self.lock_message.setVisible(False))

    def show_map(self):
        """ Show the map when Navigation button is clicked """
        # Use a map URL to load in the QWebEngineView (Google Maps example)
        map_url = "https://www.google.com/maps"
        self.map_viewer.setUrl(QtCore.QUrl(map_url))  # Load the URL into the map viewer

    def open_radio(self):
        """ Open the radio URL inside the QWebEngineView """
        radio_url = "https://radio.garden/visit/cairo/vtWTDbUW"
        self.map_viewer.setUrl(QUrl(radio_url))  # Load the radio URL in the web viewer

    def update_temperature(self):
        """ Fetch temperature from OpenWeatherMap API """
        API_KEY = "764ace33f1778d77731a5f44453469f2"  
        CITY = "Cairo"
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(URL)
            data = response.json()

            if response.status_code == 200:
                temp_value = data["main"]["temp"]
                self.temp.setText(f"🌡 {temp_value}°C")  
            else:
                self.temp.setText("❌ Error")
        except Exception as e:
            print("Error fetching temperature:", e)
            self.temp.setText("❌ Error")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import math
import os
from PyQt5 import QtWidgets, uic
import PyQt5
import threading
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication
import time

app = QtWidgets.QApplication([])
timr = uic.loadUi("timrv2.ui")


def min_up():
    if 9 <= int(timr.min_lbl.text()) < 59:
        mins = timr.min_lbl.text()
        mins = int(mins) + 1
        mins = str(mins)
        timr.min_lbl.setText(mins)
    elif 9 > int(timr.min_lbl.text()) >= 0:
        mins = timr.min_lbl.text()
        mins = int(mins) + 1
        mins = "0" + str(mins)
        timr.min_lbl.setText(mins)
    elif int(timr.min_lbl.text()) == 59:
        timr.min_lbl.setText("00")
        hr = timr.hr_lbl.text()
        hr = int(hr) + 1
        hr = str(hr)
        timr.hr_lbl.setText(hr)


def min_down():
    if int(timr.min_lbl.text()) > 10:
        mins = timr.min_lbl.text()
        mins = int(mins) - 1
        mins = str(mins)
        timr.min_lbl.setText(mins)
    elif 10 >= int(timr.min_lbl.text()) > 1:
        mins = timr.min_lbl.text()
        mins = int(mins) - 1
        mins = "0" + str(mins)
        timr.min_lbl.setText(mins)
    elif int(timr.min_lbl.text()) == 1:
            timr.min_lbl.setText("00")
    elif int(timr.min_lbl.text()) == 0:
        if int(timr.hr_lbl.text()) != 0:
            hr_down()
            timr.min_lbl.setText("59")


def hr_up():
    hr = int(timr.hr_lbl.text())
    hr = hr + 1
    timr.hr_lbl.setText(str(hr))


def hr_down():
    hr = int(timr.hr_lbl.text())
    if hr > 0:
        hr = hr - 1
        timr.hr_lbl.setText(str(hr))


def hr_set24():
    timr.hr_lbl.setText("24")


def hr_set10():
    timr.hr_lbl.setText("10")


def min_set30():
    timr.min_lbl.setText("30")


def min_set15():
    timr.min_lbl.setText("15")


def sec_down():
    if int(timr.sec_lbl.text()) > 10:
        mins = timr.sec_lbl.text()
        mins = int(mins) - 1
        mins = str(mins)
        timr.sec_lbl.setText(mins)
    elif 10 >= int(timr.sec_lbl.text()) > 1:
        mins = timr.sec_lbl.text()
        mins = int(mins) - 1
        mins = "0" + str(mins)
        timr.sec_lbl.setText(mins)
    elif int(timr.sec_lbl.text()) == 1:
            timr.sec_lbl.setText("00")
    elif int(timr.sec_lbl.text()) == 0 and int(timr.min_lbl.text()) > 0 or int(timr.hr_lbl.text()) != 0:
        min_down()
        timr.sec_lbl.setText("59")
    else:
        timr.sec_lbl.setText("00")


def sec_up():
    if 9 <= int(timr.sec_lbl.text()) < 59:
        mins = timr.sec_lbl.text()
        mins = int(mins) + 1
        mins = str(mins)
        timr.sec_lbl.setText(mins)
    elif 59 > int(timr.sec_lbl.text()) >= 0:
        mins = timr.sec_lbl.text()
        mins = int(mins) + 1
        mins = "0" + str(mins)
        timr.sec_lbl.setText(mins)
    if int(timr.sec_lbl.text()) == 59:
        timr.sec_lbl.setText("00")
        min_up()


def sec_up30():
    if int(timr.sec_lbl.text()) == 0:
        timr.sec_lbl.setText("30")
    elif int(timr.sec_lbl.text()) == 30:
        min_up()
        timr.sec_lbl.setText("00")


def sec_down30():
    if int(timr.sec_lbl.text()) == 0:
        timr.sec_lbl.setText("30")
        min_down()
    elif int(timr.sec_lbl.text()) == 30:
        timr.sec_lbl.setText("00")
    elif int(timr.sec_lbl.text()) == 0 and int(timr.min_lbl.text()) == 0:
        timr.sec_lbl.setText("00")
        timr.min_lbl.setText("00")


def teemr():
    total_time = (int(timr.hr_lbl.text()) * 3600) + (int(timr.min_lbl.text()) * 60) + (int(timr.sec_lbl.text()))
    if total_time != 0:
        threading.Timer(1, teemr).start()
        sec_down()
    elif total_time == 0:
        if timr.radio_restart.isChecked():
            os.system("shutdown -t 0 -r -f")
        elif timr.radio_sleep.isChecked():
            os.system("shutdown.exe /h")
        elif timr.radio_sd.isChecked():
            os.system("shutdown -s -t 0")


timr.start_btn.clicked.connect(teemr)
timr.sec_up.clicked.connect(sec_up)
timr.sec_down.clicked.connect(sec_down)
timr.sec_down30.clicked.connect(sec_down30)
timr.sec_up30.clicked.connect(sec_up30)
timr.hr_set24.clicked.connect(hr_set24)
timr.hr_set10.clicked.connect(hr_set10)
timr.min_set15.clicked.connect(min_set15)
timr.min_set30.clicked.connect(min_set30)
timr.hr_up.clicked.connect(hr_up)
timr.hr_down.clicked.connect(hr_down)
timr.min_up.clicked.connect(min_up)
timr.min_down.clicked.connect(min_down)


timr.show()
app.exec()

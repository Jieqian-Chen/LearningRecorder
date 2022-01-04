#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File Name: {FileName}.py
#
# Created by: Jieqian Chen
#
# File Description: This file is for {File Purpose} based on PyQt5.
#
# Created Date: 2022.xx.xx

__version__ = "0.0.1"

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

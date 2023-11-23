# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 687)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_menu_bar = QWidget(self.centralwidget)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setMinimumSize(QSize(0, 64))
        self.top_menu_bar.setMaximumSize(QSize(16777215, 64))
        self.horizontalLayout = QHBoxLayout(self.top_menu_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_import_view = QPushButton(self.top_menu_bar)
        self.btn_import_view.setObjectName(u"btn_import_view")

        self.horizontalLayout.addWidget(self.btn_import_view)

        self.btn_export_view = QPushButton(self.top_menu_bar)
        self.btn_export_view.setObjectName(u"btn_export_view")

        self.horizontalLayout.addWidget(self.btn_export_view)


        self.verticalLayout.addWidget(self.top_menu_bar)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_menu_bar = QWidget(self.widget_2)
        self.left_menu_bar.setObjectName(u"left_menu_bar")
        self.left_menu_bar.setMinimumSize(QSize(240, 0))
        self.left_menu_bar.setMaximumSize(QSize(240, 16777215))
        self.label = QLabel(self.left_menu_bar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-70, 210, 749, 277))

        self.horizontalLayout_2.addWidget(self.left_menu_bar)

        self.display_widget = QWidget(self.widget_2)
        self.display_widget.setObjectName(u"display_widget")
        self.display_widget.setMinimumSize(QSize(600, 540))

        self.horizontalLayout_2.addWidget(self.display_widget)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_import_view.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_export_view.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EXAMPLE", None))
    # retranslateUi


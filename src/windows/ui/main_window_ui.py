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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 687)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_menu_bar = QWidget(self.centralwidget)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setMinimumSize(QSize(0, 64))
        self.top_menu_bar.setMaximumSize(QSize(16777215, 64))
        self.horizontalLayout = QHBoxLayout(self.top_menu_bar)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_import_view = QPushButton(self.top_menu_bar)
        self.btn_import_view.setObjectName(u"btn_import_view")
        self.btn_import_view.setMinimumSize(QSize(80, 0))
        self.btn_import_view.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btn_import_view)

        self.btn_dicom_view = QPushButton(self.top_menu_bar)
        self.btn_dicom_view.setObjectName(u"btn_dicom_view")

        self.horizontalLayout.addWidget(self.btn_dicom_view)

        self.btn_export_view = QPushButton(self.top_menu_bar)
        self.btn_export_view.setObjectName(u"btn_export_view")
        self.btn_export_view.setMinimumSize(QSize(80, 0))
        self.btn_export_view.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btn_export_view)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.top_menu_bar, 0, 0, 1, 1)

        self.bodywidget = QWidget(self.centralwidget)
        self.bodywidget.setObjectName(u"bodywidget")
        self.horizontalLayout_2 = QHBoxLayout(self.bodywidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bar = QWidget(self.bodywidget)
        self.left_menu_bar.setObjectName(u"left_menu_bar")
        self.left_menu_bar.setMinimumSize(QSize(240, 0))
        self.left_menu_bar.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.viewswidget = QStackedWidget(self.left_menu_bar)
        self.viewswidget.setObjectName(u"viewswidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(32)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.btn_import_mesh = QPushButton(self.page_1)
        self.btn_import_mesh.setObjectName(u"btn_import_mesh")

        self.verticalLayout.addWidget(self.btn_import_mesh)

        self.viewswidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.viewswidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)

        self.viewswidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.viewswidget, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 491, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.left_menu_bar)

        self.displayviewwidget = QWidget(self.bodywidget)
        self.displayviewwidget.setObjectName(u"displayviewwidget")
        self.displayviewwidget.setMinimumSize(QSize(600, 540))
        self.gridLayout = QGridLayout(self.displayviewwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.displayviewwidget)


        self.gridLayout_2.addWidget(self.bodywidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.viewswidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_import_view.setText(QCoreApplication.translate("MainWindow", u"import mesh", None))
        self.btn_dicom_view.setText(QCoreApplication.translate("MainWindow", u"import dicom", None))
        self.btn_export_view.setText(QCoreApplication.translate("MainWindow", u"export mesh", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"mesh", None))
        self.btn_import_mesh.setText(QCoreApplication.translate("MainWindow", u"import mesh", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"dicom", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"export", None))
    # retranslateUi


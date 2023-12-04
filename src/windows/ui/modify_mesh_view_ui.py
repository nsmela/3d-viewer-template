# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_mesh_view.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Mesh_View(object):
    def setupUi(self, Mesh_View):
        if not Mesh_View.objectName():
            Mesh_View.setObjectName(u"Mesh_View")
        Mesh_View.resize(240, 400)
        self.verticalLayout = QVBoxLayout(Mesh_View)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(Mesh_View)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(32)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.btn_add_sphere = QPushButton(Mesh_View)
        self.btn_add_sphere.setObjectName(u"btn_add_sphere")

        self.verticalLayout.addWidget(self.btn_add_sphere)

        self.btn_remove_sphere = QPushButton(Mesh_View)
        self.btn_remove_sphere.setObjectName(u"btn_remove_sphere")

        self.verticalLayout.addWidget(self.btn_remove_sphere)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Mesh_View)

        QMetaObject.connectSlotsByName(Mesh_View)
    # setupUi

    def retranslateUi(self, Mesh_View):
        Mesh_View.setWindowTitle(QCoreApplication.translate("Mesh_View", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("Mesh_View", u"modify", None))
        self.btn_add_sphere.setText(QCoreApplication.translate("Mesh_View", u"add sphere", None))
        self.btn_remove_sphere.setText(QCoreApplication.translate("Mesh_View", u"remove sphere", None))
    # retranslateUi


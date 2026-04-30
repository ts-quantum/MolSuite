# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 323)
        self.Apply = QPushButton(Settings)
        self.Apply.setObjectName(u"Apply")
        self.Apply.setGeometry(QRect(260, 200, 113, 32))
        self.Cancel = QPushButton(Settings)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setGeometry(QRect(260, 240, 113, 32))
        self.layoutWidget = QWidget(Settings)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 235, 301))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.bridging = QCheckBox(self.layoutWidget)
        self.bridging.setObjectName(u"bridging")
        self.bridging.setChecked(True)

        self.verticalLayout.addWidget(self.bridging)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.edit_rmsd = QLineEdit(self.layoutWidget)
        self.edit_rmsd.setObjectName(u"edit_rmsd")

        self.verticalLayout.addWidget(self.edit_rmsd)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.bridging_pts = QLineEdit(self.layoutWidget)
        self.bridging_pts.setObjectName(u"bridging_pts")

        self.verticalLayout.addWidget(self.bridging_pts)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.splicing = QCheckBox(self.layoutWidget)
        self.splicing.setObjectName(u"splicing")
        self.splicing.setChecked(True)

        self.verticalLayout.addWidget(self.splicing)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.splicing_pts = QLineEdit(self.layoutWidget)
        self.splicing_pts.setObjectName(u"splicing_pts")

        self.verticalLayout.addWidget(self.splicing_pts)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.Apply.setText(QCoreApplication.translate("Settings", u"Apply", None))
        self.Cancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"General Settings", None))
        self.bridging.setText(QCoreApplication.translate("Settings", u"Activate Bridging", None))
        self.label_5.setText(QCoreApplication.translate("Settings", u"RMSD Quality Threshold (and Bridging Trigger)", None))
        self.edit_rmsd.setText(QCoreApplication.translate("Settings", u"0.02", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"No. of Bridging Points", None))
        self.bridging_pts.setText(QCoreApplication.translate("Settings", u"10", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Settings for Alignment Masked  (Fragment Logic)", None))
        self.splicing.setText(QCoreApplication.translate("Settings", u"Activate Splicing ", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"No. of Splicing Points in each direction", None))
        self.splicing_pts.setText(QCoreApplication.translate("Settings", u"30", None))
    # retranslateUi


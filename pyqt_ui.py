# Form implementation generated from reading ui file 'pyqt_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 650))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(0, -10, 1111, 631))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.card_front_textbox = QtWidgets.QTextBrowser(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_front_textbox.sizePolicy().hasHeightForWidth())
        self.card_front_textbox.setSizePolicy(sizePolicy)
        self.card_front_textbox.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.card_front_textbox.setFont(font)
        self.card_front_textbox.setObjectName("card_front_textbox")
        self.verticalLayout_8.addWidget(self.card_front_textbox)
        self.card_back_textbox = QtWidgets.QTextBrowser(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_back_textbox.sizePolicy().hasHeightForWidth())
        self.card_back_textbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.card_back_textbox.setFont(font)
        self.card_back_textbox.setObjectName("card_back_textbox")
        self.verticalLayout_8.addWidget(self.card_back_textbox)
        self.gridLayout_2.addWidget(self.frame_3, 1, 1, 1, 1)
        self.card_progress_label = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.card_progress_label.setFont(font)
        self.card_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.card_progress_label.setObjectName("card_progress_label")
        self.gridLayout_2.addWidget(self.card_progress_label, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(parent=self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_card_btn = QtWidgets.QPushButton(parent=self.frame)
        self.prev_card_btn.setObjectName("prev_card_btn")
        self.horizontalLayout.addWidget(self.prev_card_btn)
        self.next_card_btn = QtWidgets.QPushButton(parent=self.frame)
        self.next_card_btn.setObjectName("next_card_btn")
        self.horizontalLayout.addWidget(self.next_card_btn)
        self.show_details_btn = QtWidgets.QPushButton(parent=self.frame)
        self.show_details_btn.setObjectName("show_details_btn")
        self.horizontalLayout.addWidget(self.show_details_btn)
        self.mark_review_btn = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.mark_review_btn.setFont(font)
        self.mark_review_btn.setObjectName("mark_review_btn")
        self.horizontalLayout.addWidget(self.mark_review_btn)
        self.gridLayout_2.addWidget(self.frame, 4, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.review_label = QtWidgets.QLabel(parent=self.frame_4)
        self.review_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.review_label.setFont(font)
        self.review_label.setStyleSheet("")
        self.review_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.review_label.setObjectName("review_label")
        self.verticalLayout.addWidget(self.review_label)
        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame1 = QtWidgets.QFrame(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chapter_label = QtWidgets.QLabel(parent=self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.chapter_label.setFont(font)
        self.chapter_label.setObjectName("chapter_label")
        self.horizontalLayout_4.addWidget(self.chapter_label)
        self.chapter_combobox = QtWidgets.QComboBox(parent=self.frame_8)
        self.chapter_combobox.setMinimumSize(QtCore.QSize(65, 0))
        self.chapter_combobox.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.chapter_combobox.setFont(font)
        self.chapter_combobox.setObjectName("chapter_combobox")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.chapter_combobox.addItem("")
        self.horizontalLayout_4.addWidget(self.chapter_combobox)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.objective_label = QtWidgets.QLabel(parent=self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.objective_label.setFont(font)
        self.objective_label.setObjectName("objective_label")
        self.horizontalLayout_5.addWidget(self.objective_label)
        self.objective_combobox = QtWidgets.QComboBox(parent=self.frame_9)
        self.objective_combobox.setMinimumSize(QtCore.QSize(65, 0))
        self.objective_combobox.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.objective_combobox.setFont(font)
        self.objective_combobox.setObjectName("objective_combobox")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.objective_combobox.addItem("")
        self.horizontalLayout_5.addWidget(self.objective_combobox)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.section_label = QtWidgets.QLabel(parent=self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.section_label.setFont(font)
        self.section_label.setObjectName("section_label")
        self.horizontalLayout_6.addWidget(self.section_label)
        self.section_combobox = QtWidgets.QComboBox(parent=self.frame_10)
        self.section_combobox.setMinimumSize(QtCore.QSize(65, 0))
        self.section_combobox.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.section_combobox.setFont(font)
        self.section_combobox.setObjectName("section_combobox")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.section_combobox.addItem("")
        self.horizontalLayout_6.addWidget(self.section_combobox)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.refresh_btn = QtWidgets.QPushButton(parent=self.frame_12)
        font = QtGui.QFont()
        font.setBold(False)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setObjectName("refresh_btn")
        self.verticalLayout_5.addWidget(self.refresh_btn)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.reset_filters_btn = QtWidgets.QPushButton(parent=self.frame_14)
        self.reset_filters_btn.setObjectName("reset_filters_btn")
        self.verticalLayout_7.addWidget(self.reset_filters_btn)
        self.verticalLayout_3.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(parent=self.frame1)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.show_review_cards_btn = QtWidgets.QPushButton(parent=self.frame_13)
        self.show_review_cards_btn.setObjectName("show_review_cards_btn")
        self.verticalLayout_6.addWidget(self.show_review_cards_btn)
        self.verticalLayout_3.addWidget(self.frame_13)
        self.gridLayout_2.addWidget(self.frame1, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_3.addWidget(self.frame_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOrder_Cards = QtWidgets.QMenu(parent=self.menuEdit)
        self.menuOrder_Cards.setObjectName("menuOrder_Cards")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuPreferences = QtWidgets.QMenu(parent=self.menuSettings)
        self.menuPreferences.setObjectName("menuPreferences")
        self.menuWindow = QtWidgets.QMenu(parent=self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Cards = QtGui.QAction(parent=MainWindow)
        self.actionOpen_Cards.setObjectName("actionOpen_Cards")
        self.actionSave_Cards = QtGui.QAction(parent=MainWindow)
        self.actionSave_Cards.setObjectName("actionSave_Cards")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.prefHide_Marked_For_Review = QtGui.QAction(parent=MainWindow)
        self.prefHide_Marked_For_Review.setCheckable(True)
        self.prefHide_Marked_For_Review.setChecked(True)
        self.prefHide_Marked_For_Review.setEnabled(True)
        self.prefHide_Marked_For_Review.setObjectName("prefHide_Marked_For_Review")
        self.actionAscending = QtGui.QAction(parent=MainWindow)
        self.actionAscending.setObjectName("actionAscending")
        self.actionDescending = QtGui.QAction(parent=MainWindow)
        self.actionDescending.setObjectName("actionDescending")
        self.actionShuffle_Cards = QtGui.QAction(parent=MainWindow)
        self.actionShuffle_Cards.setObjectName("actionShuffle_Cards")
        self.menuFile.addAction(self.actionOpen_Cards)
        self.menuFile.addAction(self.actionSave_Cards)
        self.menuOrder_Cards.addAction(self.actionAscending)
        self.menuOrder_Cards.addAction(self.actionDescending)
        self.menuEdit.addAction(self.menuOrder_Cards.menuAction())
        self.menuEdit.addAction(self.actionShuffle_Cards)
        self.menuPreferences.addAction(self.prefHide_Marked_For_Review)
        self.menuSettings.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.card_front_textbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.card_back_textbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.card_progress_label.setText(_translate("MainWindow", "Card 0/0"))
        self.prev_card_btn.setText(_translate("MainWindow", "Previous Card"))
        self.next_card_btn.setText(_translate("MainWindow", "Next Card"))
        self.show_details_btn.setText(_translate("MainWindow", "Show Details"))
        self.mark_review_btn.setText(_translate("MainWindow", "Mark For Review"))
        self.review_label.setText(_translate("MainWindow", "MARKED FOR REVIEW"))
        self.label.setText(_translate("MainWindow", "FILTERS"))
        self.chapter_label.setText(_translate("MainWindow", "Chapter"))
        self.chapter_combobox.setItemText(0, _translate("MainWindow", "Any"))
        self.chapter_combobox.setItemText(1, _translate("MainWindow", "0"))
        self.chapter_combobox.setItemText(2, _translate("MainWindow", "1"))
        self.chapter_combobox.setItemText(3, _translate("MainWindow", "2"))
        self.chapter_combobox.setItemText(4, _translate("MainWindow", "3"))
        self.chapter_combobox.setItemText(5, _translate("MainWindow", "4"))
        self.chapter_combobox.setItemText(6, _translate("MainWindow", "5"))
        self.chapter_combobox.setItemText(7, _translate("MainWindow", "6"))
        self.chapter_combobox.setItemText(8, _translate("MainWindow", "7"))
        self.chapter_combobox.setItemText(9, _translate("MainWindow", "8"))
        self.chapter_combobox.setItemText(10, _translate("MainWindow", "9"))
        self.chapter_combobox.setItemText(11, _translate("MainWindow", "10"))
        self.objective_label.setText(_translate("MainWindow", "Objective"))
        self.objective_combobox.setItemText(0, _translate("MainWindow", "Any"))
        self.objective_combobox.setItemText(1, _translate("MainWindow", "0"))
        self.objective_combobox.setItemText(2, _translate("MainWindow", "1"))
        self.objective_combobox.setItemText(3, _translate("MainWindow", "2"))
        self.objective_combobox.setItemText(4, _translate("MainWindow", "3"))
        self.objective_combobox.setItemText(5, _translate("MainWindow", "4"))
        self.objective_combobox.setItemText(6, _translate("MainWindow", "5"))
        self.objective_combobox.setItemText(7, _translate("MainWindow", "6"))
        self.objective_combobox.setItemText(8, _translate("MainWindow", "7"))
        self.objective_combobox.setItemText(9, _translate("MainWindow", "8"))
        self.objective_combobox.setItemText(10, _translate("MainWindow", "9"))
        self.objective_combobox.setItemText(11, _translate("MainWindow", "10"))
        self.section_label.setText(_translate("MainWindow", "Section"))
        self.section_combobox.setItemText(0, _translate("MainWindow", "Any"))
        self.section_combobox.setItemText(1, _translate("MainWindow", "0"))
        self.section_combobox.setItemText(2, _translate("MainWindow", "1"))
        self.section_combobox.setItemText(3, _translate("MainWindow", "2"))
        self.section_combobox.setItemText(4, _translate("MainWindow", "3"))
        self.section_combobox.setItemText(5, _translate("MainWindow", "4"))
        self.section_combobox.setItemText(6, _translate("MainWindow", "5"))
        self.section_combobox.setItemText(7, _translate("MainWindow", "6"))
        self.section_combobox.setItemText(8, _translate("MainWindow", "7"))
        self.section_combobox.setItemText(9, _translate("MainWindow", "8"))
        self.section_combobox.setItemText(10, _translate("MainWindow", "9"))
        self.section_combobox.setItemText(11, _translate("MainWindow", "10"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.reset_filters_btn.setText(_translate("MainWindow", "Reset All Filters"))
        self.show_review_cards_btn.setText(_translate("MainWindow", "Show Only Cards Under Review"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuOrder_Cards.setTitle(_translate("MainWindow", "Order Cards"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Cards.setText(_translate("MainWindow", "Open"))
        self.actionSave_Cards.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.prefHide_Marked_For_Review.setText(_translate("MainWindow", "Hide Marked For Review"))
        self.actionAscending.setText(_translate("MainWindow", "Ascending"))
        self.actionDescending.setText(_translate("MainWindow", "Descending"))
        self.actionShuffle_Cards.setText(_translate("MainWindow", "Shuffle Cards"))

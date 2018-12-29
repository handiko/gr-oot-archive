/********************************************************************************
** Form generated from reading UI file 'showpngpicture.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SHOWPNGPICTURE_H
#define UI_SHOWPNGPICTURE_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QRadioButton>
#include <QtGui/QScrollArea>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ShowPngPicture
{
public:
    QGridLayout *gridLayout;
    QScrollArea *displayArea;
    QLabel *displayWidget;
    QHBoxLayout *horizontalLayout;
    QRadioButton *reverse;
    QSpacerItem *horizontalSpacer;
    QPushButton *saveButton;

    void setupUi(QWidget *ShowPngPicture)
    {
        if (ShowPngPicture->objectName().isEmpty())
            ShowPngPicture->setObjectName(QString::fromUtf8("ShowPngPicture"));
        ShowPngPicture->resize(447, 383);
        gridLayout = new QGridLayout(ShowPngPicture);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        displayArea = new QScrollArea(ShowPngPicture);
        displayArea->setObjectName(QString::fromUtf8("displayArea"));
        displayArea->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        displayArea->setWidgetResizable(true);
        displayWidget = new QLabel();
        displayWidget->setObjectName(QString::fromUtf8("displayWidget"));
        displayWidget->setGeometry(QRect(0, 0, 425, 328));
        displayArea->setWidget(displayWidget);

        gridLayout->addWidget(displayArea, 0, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        reverse = new QRadioButton(ShowPngPicture);
        reverse->setObjectName(QString::fromUtf8("reverse"));

        horizontalLayout->addWidget(reverse);

        horizontalSpacer = new QSpacerItem(68, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        saveButton = new QPushButton(ShowPngPicture);
        saveButton->setObjectName(QString::fromUtf8("saveButton"));

        horizontalLayout->addWidget(saveButton);


        gridLayout->addLayout(horizontalLayout, 1, 0, 1, 1);


        retranslateUi(ShowPngPicture);

        QMetaObject::connectSlotsByName(ShowPngPicture);
    } // setupUi

    void retranslateUi(QWidget *ShowPngPicture)
    {
        ShowPngPicture->setWindowTitle(QApplication::translate("ShowPngPicture", "Image Display", 0, QApplication::UnicodeUTF8));
        reverse->setText(QApplication::translate("ShowPngPicture", "Display invers", 0, QApplication::UnicodeUTF8));
        saveButton->setText(QApplication::translate("ShowPngPicture", "Save Image to File", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class ShowPngPicture: public Ui_ShowPngPicture {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SHOWPNGPICTURE_H

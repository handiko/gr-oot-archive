/********************************************************************************
** Form generated from reading UI file 'show_text_window.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SHOW_TEXT_WINDOW_H
#define UI_SHOW_TEXT_WINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QScrollArea>
#include <QtGui/QSpacerItem>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_show_text_window
{
public:
    QGridLayout *gridLayout;
    QScrollArea *displayArea;
    QLabel *textDisplay;
    QHBoxLayout *horizontalLayout;
    QPushButton *clear;
    QSpacerItem *horizontalSpacer;
    QPushButton *save;

    void setupUi(QWidget *show_text_window)
    {
        if (show_text_window->objectName().isEmpty())
            show_text_window->setObjectName(QString::fromUtf8("show_text_window"));
        show_text_window->resize(400, 300);
        gridLayout = new QGridLayout(show_text_window);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        displayArea = new QScrollArea(show_text_window);
        displayArea->setObjectName(QString::fromUtf8("displayArea"));
        displayArea->setWidgetResizable(true);
        textDisplay = new QLabel();
        textDisplay->setObjectName(QString::fromUtf8("textDisplay"));
        textDisplay->setGeometry(QRect(0, 0, 378, 245));
        textDisplay->setFrameShape(QFrame::Panel);
        textDisplay->setFrameShadow(QFrame::Raised);
        textDisplay->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);
        displayArea->setWidget(textDisplay);

        gridLayout->addWidget(displayArea, 0, 0, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        clear = new QPushButton(show_text_window);
        clear->setObjectName(QString::fromUtf8("clear"));

        horizontalLayout->addWidget(clear);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        save = new QPushButton(show_text_window);
        save->setObjectName(QString::fromUtf8("save"));

        horizontalLayout->addWidget(save);


        gridLayout->addLayout(horizontalLayout, 1, 0, 1, 1);


        retranslateUi(show_text_window);

        QMetaObject::connectSlotsByName(show_text_window);
    } // setupUi

    void retranslateUi(QWidget *show_text_window)
    {
        show_text_window->setWindowTitle(QApplication::translate("show_text_window", "TextDisplay", 0, QApplication::UnicodeUTF8));
        clear->setText(QApplication::translate("show_text_window", "Clear", 0, QApplication::UnicodeUTF8));
        save->setText(QApplication::translate("show_text_window", "Save text to file", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class show_text_window: public Ui_show_text_window {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SHOW_TEXT_WINDOW_H

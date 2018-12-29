/****************************************************************************
** Meta object code from reading C++ file 'show_text_window.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../lib/show_text_window.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'show_text_window.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_show_text_window[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       2,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      18,   17,   17,   17, 0x08,
      30,   17,   17,   17, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_show_text_window[] = {
    "show_text_window\0\0text2File()\0clearText()\0"
};

void show_text_window::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        show_text_window *_t = static_cast<show_text_window *>(_o);
        switch (_id) {
        case 0: _t->text2File(); break;
        case 1: _t->clearText(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData show_text_window::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject show_text_window::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_show_text_window,
      qt_meta_data_show_text_window, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &show_text_window::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *show_text_window::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *show_text_window::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_show_text_window))
        return static_cast<void*>(const_cast< show_text_window*>(this));
    return QWidget::qt_metacast(_clname);
}

int show_text_window::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

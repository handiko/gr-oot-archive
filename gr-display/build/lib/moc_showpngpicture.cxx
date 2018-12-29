/****************************************************************************
** Meta object code from reading C++ file 'showpngpicture.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../lib/showpngpicture.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'showpngpicture.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_ShowPngPicture[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      18,   16,   15,   15, 0x0a,
      53,   15,   15,   15, 0x0a,
      76,   70,   15,   15, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_ShowPngPicture[] = {
    "ShowPngPicture\0\0,\0setPixel(const unsigned char*,int)\0"
    "saveImage2File()\0order\0storeReverse(bool)\0"
};

void ShowPngPicture::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        ShowPngPicture *_t = static_cast<ShowPngPicture *>(_o);
        switch (_id) {
        case 0: _t->setPixel((*reinterpret_cast< const unsigned char*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 1: _t->saveImage2File(); break;
        case 2: _t->storeReverse((*reinterpret_cast< bool(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData ShowPngPicture::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject ShowPngPicture::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_ShowPngPicture,
      qt_meta_data_ShowPngPicture, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &ShowPngPicture::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *ShowPngPicture::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *ShowPngPicture::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_ShowPngPicture))
        return static_cast<void*>(const_cast< ShowPngPicture*>(this));
    return QWidget::qt_metacast(_clname);
}

int ShowPngPicture::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

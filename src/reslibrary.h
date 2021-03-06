#ifndef RESLIBRARY_H
#define RESLIBRARY_H

#include <QWidget>
#include <QList>
#include <QListWidgetItem>
#include <Python.h>

namespace Ui {
class ResLibrary;
}
class MyListWidget;
class DetailView;

//******************
// ResLibrary
//*****************
class ResLibrary : public QWidget
{
    Q_OBJECT
public:
    explicit ResLibrary(QWidget *parent = 0);
    void addItem(const QString &name, const QByteArray &pic_url, const QByteArray &flag);
    void clearItem(void);
    PyObject *openDetailPage(PyObject *dict);

private:
    Ui::ResLibrary *ui;
    int current_plugin;
    int current_page;
    QString current_tag;
    QString current_country;
    QString current_key;
    MyListWidget *listWidget;
    DetailView *detailView;

private slots:
    void reSearch(void);
    void keySearch(void);
    void onItemDoubleClicked(QListWidgetItem *item);
    void onPageChanged(int newPage);
    void onPrevPage(void);
    void onNextPage(void);
};

extern ResLibrary *res_library;

#endif // RESLIBRARY_H

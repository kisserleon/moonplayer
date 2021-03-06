#ifndef SETTINGSDIALOG_H
#define SETTINGSDIALOG_H

#include <QDialog>

namespace Ui {
class SettingsDialog;
}
class QButtonGroup;

class SettingsDialog : public QDialog
{
    Q_OBJECT
    
public:
    explicit SettingsDialog(QWidget *parent = 0);
    ~SettingsDialog();
    void switchToPluginsTab(void);
    
private:
    Ui::SettingsDialog *ui;
    QButtonGroup *group;

private slots:
    void loadSettings(void);
    void saveSettings(void);
    void onDirButton(void);
    void onFontButton(void);
    void openPluginsFolder(void);
};

extern SettingsDialog *settingsDialog;

void initSettings(void);

#endif // SETTINGS_H

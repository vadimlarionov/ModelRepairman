Модель ремонтника
=================

### Учебный проект по курсу "Аналитические модели АСОИУ"

## Пишем на PyQt5
#### Requirements
* Python 3.5.2
* Qt Creator 5.7
#### Порядок установки
1. Устанавливаем Python, если его нет;
2. Скачиваем [Qt Creator](https://www.qt.io/download-open-source/). Именно Creator, т.к. все библиотеки Qt нам не нужны;
2. ```pip install pyqt5 ```
3. [PyCharm](https://www.jetbrains.com/pycharm/) в качестве IDE.


#### Приступаем к разработке
Цель: пишем логику на Python, интерфейс на Qt.
##### В Qt Creator
*Файл* -> *Создать файл или проект* -> *Файлы и классы: Qt* -> *Форма Qt Designer* -> *Dialog without Buttons* -> название yourwindow.ui в папке с проектом -> *Далее* -> *Завершить*.
В открывшемся окне справа переименовать форму (объект) в YourWindow. Тогда генерируемый *ui_yourwindow.py* файл будет содержать класс *Ui_YourWindow*.

##### В PyCharm
*File* -> *Settings* -> В поиске пишем "File watcher" -> *import*. В открывшемся окне выбираем [watcherTasks.xml](./conf/watcherTasks.xml). Затем открываем добавившийся "Qt Ui to Python". В графе *program* указываем путь к pyic5 (`which pyuic5`).

Теперь File Watcher отслеживает все изменения *.ui файлов в папке с проектом и генерирует на их основе .py файлы.


При разработке свой класс должен наследоваться от `QDialog` и `Ui_YourWindow` классов. Пример в [main.py](./main.py) файле.

## Собираем .exe в Windows
Порядок установки компонент такой же, как и выше.
В качестве сборщика используем [PyInstaller](http://www.pyinstaller.org/)
1. Поставить *PyInstaller* `pip install pyinstaller`
2. Удалить *PyInstaller* `pip uninstall pyinstaller`
3. Поставить *PyInstaller* с GitHub
```sh
git clone https://github.com/pyinstaller/pyinstaller
cd pyinstaller
python setup.py install
```
4. Собираем
```sh
pyinstaller --paths "C:\Program Files\Python35-32\Lib\site-packages\PyQt5\Qt\bin" --onefile --noconsole FILE.py
```

Можно попробовать собрать через PyInstaller из репозиториев pip, но на момент написания этого туториала PyInstaller из pip не поддерживал PyQt 5.7.

## Сборка в Windows XP
1. Ставим *Virtual Box*;
2. Накатываем *Windows XP*;
3. Скачиваем *Google Chrome*, т.к. IE не сможет скачать Python;
4. Python 3.4.3. Новее не запустится;
5. [PyQt 5.5.1](https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/). Новее, опять же, не запустится;
6. Собираем так: `pyinstaller --onefile --noconsole FILE.py`

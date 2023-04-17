# Обрезка ссылок с помощью Битли
Наша программа помогает сократить ссылку и посчитать количество кликов по сокращенной ссылке.

### Как установить
Python3 должен быть уже установлен. Затем використовуйте pip(или pip3, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
## Как запустить
Чтобы программа сократила ссылку надо написать команду в таком формате:

```
python main.py --url https://www.google.com/
```

Чтобы программа посчитала количество кликов по сокращенной ссылке надо написать команду в таком формате:

```
python main.py --url https://bit.ly/3FbdZxl
```
## Переменные окружения
Часть настроек программы находится в переменных окружения.
Переменные окружения - это переменные, значения которых присваиваются программе Python извне.
Для их определения, создайте файл .env рядом с main.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Пример содержания файла .env: 

```
BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7
```
### Цель проекта
Код написания исследования на онлайн-курсе для веб-разработчиков dvmn.org .

Проект для тестирования проекта *flask-app-example* (https://gitlab.monq.ru/p.alekseev/flask-app-example/)

Тестируется *UI* и *API*.

Для запуска 

```
py.test -v TestCases
```

Если py.test (pytest) не запускается, то можно попробовать запустить через виртуальное окружение *Python* (см. https://python-scripts.com/question/28726)
```
Попробуйте установить pytest на virtualenv:

pip install virtualenv
python -m venv env
cd env/scripts
activate.bat

pip install pytest
pip install requests
pip install jsonpath
pip install selenium
```

Полонский Денис, denuha@mail.ru
# PyServer-Ping

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Montserrat&weight=500&size=25&duration=2800&pause=800&color=DC143C&vCenter=true&width=500&height=30&lines=S+U+T+I+V+I+S+M+Project.;.)

[![Telegram](https://img.shields.io/badge/SawGoD-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/SawGoD)

---

### О проекте:
Это аналог команды telnet в Windows. Для проверки доступности списка серверов. 

`main.py` содержит код, который реализует логику проверки подключения к серверам и сохраняет результаты в файл `results_дата_время.txt`.
Для этого используется библиотека `socket`.

При каждом подключении к серверу, в консоль выводится соответствующий текст с указанием сервера.

---

## Работа с кодом: 

1. Скачайте PyServer-Ping удобным способом. Например [архивом](https://github.com/SawGoD/PyServer-Ping/archive/refs/heads/main.zip), его слудет распаковать в любое место.

2. Устновите необходимый порт `port = XXXX`

3. Укажите необходимый сервер `server = sub{}.hosting.domain.ru`

    - `{}` - _Необходимо писать там, где указывается числовой индекс._
    
        _К примеру:_ `sub1.hosting.domain.ru` = `sub{}.hosting.domain.ru`

4. Укажите диапазон серверов `serverRange = range(from, to+1)`

    - `from` - _Начало диапазона._
    - `to` - _Конец диапазона._ 

5. Запустите код: `main.py`.

6. Результаты будут сохранены в файле `results_дата_время.txt`.

### Вид результатов в файле results*.txt:
<details>
    <summary>Раскрыть</summary>

```txt
Connection to sub1.hosting.domain.ru:XXXX - FAILED: timed out
Connection to sub2.hosting.domain.ru:XXXX - SUCCESSFUL
Connection to sub3.hosting.domain.ru:XXXX - FAILED: [WinError 10061] Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение
```
</details>


# Проект парсинга PEP на Scrapy
Парсер, поможет быть в курсе важных изменений стандартов [PEP](https://peps.python.org/):
- составит актуальный перечень стандартов [PEP](https://peps.python.org/) с текущим статусом.
- выведет количество стандартов [PEP](https://peps.python.org/) в каждом статусе
## Используемые технологии
В данном проекте были применены следующие технологии:
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)
- [CSV](https://ru.wikipedia.org/wiki/CSV)
## Как запустить проект
- Клонировать репозиторий
```
git clone https://github.com/esk-git/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
### Запуск программы
Для запуска программы нужно указать в терминале
```
scrapy crawl pep
```
Программа создаст 2 csv файла в папке `./results`:
- **pep_{ДатаВремя}.csv** - содержит перечень всех стандартов PEP с актуальным статусом (таблица содержит колонки "number", "name", "status")
- **status_summary_{ДатаВремя}.csv** - содержит перечень статусов и количество стандартов в каждом статусе (в таблице две колонки "Статус" и "Количество")

#### Автор
Каликов Евгений

![Jokes Card](https://readme-jokes.vercel.app/api)
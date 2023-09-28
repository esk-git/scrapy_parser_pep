# Проект парсинга PEP на Scrapy
Парсер, поможет быть в курсе важных изменений стандартов [PEP](https://peps.python.org/):
- соберёт ссылки на статьи о нововведениях и достанет из них справочную информацию
- актуальный перечень стандартов [PEP](https://peps.python.org/) с текущим статусом.
- оличество стандартов [PEP](https://peps.python.org/) в каждом статусе
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
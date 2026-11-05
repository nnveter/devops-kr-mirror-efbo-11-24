# Контрольная работа №1 — Git

Сальников Илья Андреевич, ЭФБО-11-24, №23 по списку.

Исходный шаблон: https://gitverse.ru/dgimatdinov/devops-kr-template

Проект импортирован из GitVerse в GitHub с сохранением истории. Ветка `master`
названа `main`. Выполнены четыре учебных коммита, interactive rebase
(`pick`, `fixup`, `fixup`, `drop`) и разрешение конфликтов с
`upstream/feature/instructor-change`. Сохранены валидаторы email, телефона и СНИЛС.

## Проверка

```sh
python -m pip install pytest
python -m pytest -v
```

## Исправления шаблона

- В `test/test_validator.py` отсутствовали импорты функций.
- Для СНИЛС `001001999` контрольная сумма равна 65, а не 32:
  `1×7 + 1×4 + 9×3 + 9×2 + 9×1 = 65`. Исправлены тестовые данные,
  ошибочный пример сохранён как отрицательный тест.
- Телефон проверяется через `fullmatch` и ASCII-цифры; завершающий перевод
  строки и Unicode-цифры не принимаются.

Основной репозиторий: https://github.com/nnveter/devops-kr1-efbo-11-24

Зеркало: https://github.com/nnveter/devops-kr-mirror-efbo-11-24

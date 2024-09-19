# Fastapi_calculator на poetry
простенький фласк калькулятор для лёгких подсчётов по типу: 2+2

## Начало работы

Следуйте этим инструкциям, чтобы запустить проект.

### Установка

1. Откройте терминал.
2. Установите проект

```bash
git clone https://github.com/prerreslin/fastapi_calculator.git
```

3.Перейдите в проект
```bash
cd fastapi_calculator
```

4.Создайте виртуальное окружение:
```bash
python -m venv .venv
```


5. Активируйте виртуальное окружение:
```bash
source .venv/bin/activate  # Для macOS/Linux
.\.venv\Scripts\activate   # Для Windows
```


6. Установите Poetry, если он еще не установлен:
```bash
pip install poetry
```


7. Установите зависимости из pyproject.toml:
```bash
poetry install
```


8. После установки зависимостей выполните команду:
```bash
poetry run run_app
```

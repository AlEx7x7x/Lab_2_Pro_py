# Lab 02 — Структури даних та функціональна декомпозиція (Варіант 3)

Аналіз товарів магазину: фільтрація, пошук, групування, сортування, агрегація.

## Встановлення і запуск

    pip install -e .
    python -m data_processor.main
    python -m data_processor.benchmark
    python -m pytest

## Структура

    src/data_processor/
        data.py        - дані (list, tuple, dict)
        processors.py  - set/dict comprehension, defaultdict, Counter
        analytics.py   - lambda, closure, *args, **kwargs, decorator
        decorators.py  - measure_time, repeat
        benchmark.py   - порівняння пошуку в list і dict
    tests/             - тести

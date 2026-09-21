from collections.abc import Callable
from .decorators import measure_time

@measure_time
def calculate_average(students: list[dict]) -> float:
    """Обчислення середнього балу. Використано generator expression[cite: 1]."""
    if not students:
        return 0.0
    return sum(student["grade"] for student in students) / len(students)

def find_best_student(students: list[dict]) -> dict | None:
    """Пошук найкращого студента за допомогою lambda[cite: 1]."""
    if not students:
        return None
    return max(students, key=lambda student: student["grade"])

def sort_by_grade(students: list[dict], reverse: bool = True) -> list[dict]:
    """Сортування студентів за балом за допомогою lambda[cite: 1]."""
    return sorted(students, key=lambda student: student["grade"], reverse=reverse)

def calculate_average_values(*values: float) -> float:
    """Демонстрація використання змінної кількості позиційних аргументів (*args)[cite: 1]."""
    if not values:
        return 0.0
    return sum(values) / len(values)

def create_record(**fields) -> dict:
    """Демонстрація використання довільних іменованих аргументів (**kwargs)[cite: 1]."""
    return dict(fields)

def create_grade_filter(minimum_grade: float) -> Callable[[dict], bool]:
    """Створення фільтра. Демонстрація замикання (closure)[cite: 1].
    Внутрішня функція пам'ятає змінну minimum_grade навіть після завершення роботи зовнішньої[cite: 1].
    """
    def predicate(student: dict) -> bool:
        return student["grade"] >= minimum_grade
    return predicate

def filter_items(items: list[dict], predicate: Callable[[dict], bool]) -> list[dict]:
    """Універсальна функція фільтрації (завдання підвищеної складності). Використано list comprehension[cite: 1]."""
    return [item for item in items if predicate(item)]
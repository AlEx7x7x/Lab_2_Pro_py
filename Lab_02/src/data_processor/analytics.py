from collections.abc import Callable

from data_processor.decorators import measure_time


@measure_time
def calculate_total_value(products: list[dict]) -> float:
    """Загальна вартість залишків. Використано generator expression."""
    return sum(p["price"] * p["quantity"] for p in products)


def find_most_expensive(products: list[dict]) -> dict | None:
    """Найдорожчий товар за допомогою lambda."""
    if not products:
        return None
    return max(products, key=lambda p: p["price"])


def sort_by_price(products: list[dict], reverse: bool = True) -> list[dict]:
    """Рейтинг за ціною за допомогою lambda."""
    return sorted(products, key=lambda p: p["price"], reverse=reverse)


def average_price_demo(*prices: float) -> float:
    """Демонстрація *args: середня ціна переданих значень."""
    if not prices:
        return 0.0
    return sum(prices) / len(prices)


def create_product_record(**fields) -> dict:
    """Демонстрація **kwargs: створення запису про товар."""
    return dict(fields)


def create_quantity_filter(threshold: int) -> Callable[[dict], bool]:
    """Closure: predicate запам'ятовує threshold після завершення зовнішньої функції."""
    def predicate(product: dict) -> bool:
        return product["quantity"] < threshold
    return predicate


def filter_items(items: list[dict], predicate: Callable[[dict], bool]) -> list[dict]:
    """Універсальна функція фільтрації (list comprehension)."""
    return [item for item in items if predicate(item)]
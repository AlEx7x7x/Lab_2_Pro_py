from collections import Counter, defaultdict

def get_unique_categories(products: list[dict]) -> set[str]:
    """Унікальні категорії через set comprehension."""
    return {p["category"] for p in products}

def create_product_index(products: list[dict]) -> dict[int, dict]:
    """dict-index за кодом товару."""
    return {p["code"]: p for p in products}

def group_by_category(products: list[dict]) -> dict[str, list[dict]]:
    """Групування за категоріями через defaultdict."""
    result = defaultdict(list)
    for p in products:
        result[p["category"]].append(p)
    return dict(result)

def count_items_by_category(products: list[dict]) -> Counter:
    """Підрахунок товарів по категоріям."""
    return Counter(p["category"] for p in products)

def filter_by_category(products: list[dict], category: str) -> list[dict]:
    """Товари заданої категорії (list comprehension)."""
    return [p for p in products if p["category"] == category]

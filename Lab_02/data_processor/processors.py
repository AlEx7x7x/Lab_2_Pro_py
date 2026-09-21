from collections import Counter, defaultdict

def get_unique_categories(products: list[dict]) -> set[str]:
    """Унікальні категорії через set comprehension[cite: 1]."""
    return {p["category"] for p in products}

def create_product_index(products: list[dict]) -> dict[int, dict]:
    """dict-index за кодом товару[cite: 1]."""
    return {p["code"]: p for p in products}

def group_by_category(products: list[dict]) -> dict[str, list[dict]]:
    """Групування за категоріями через defaultdict[cite: 1]."""
    result = defaultdict(list)
    for p in products:
        result[p["category"]].append(p)
    return dict(result)

def count_items_by_category(products: list[dict]) -> Counter:
    """Підрахунок товарів по категоріям."""
    return Counter(p["category"] for p in products)
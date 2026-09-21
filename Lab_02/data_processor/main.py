from .data import products
from .processors import get_unique_categories, create_product_index, group_by_category, count_items_by_category
from .analytics import calculate_total_value, find_most_expensive, sort_by_price, create_quantity_filter, filter_items, average_price_demo, create_product_record

def print_items(title: str, items: list[dict]) -> None:
    print(f"\n{title}\n" + "-" * 60)
    for p in items:
        print(f"{p['code']:4} {p['name']:18} {p['category']:18} {p['price']:8.2f} {p['quantity']:4} шт.")

def main() -> None:
    print_items("Всі товари", products)
    
    print("\nУнікальні категорії:", get_unique_categories(products))
    print(f"Загальна вартість залишків: {calculate_total_value(products):.2f}")
    
    best = find_most_expensive(products)
    print(f"Найдорожчий товар: {best['name']} ({best['price']} грн)")
    
    print_items("Рейтинг товарів за ціною (спадання)", sort_by_price(products))
    
    grouped = group_by_category(products)
    print("\nГрупування за категоріями:")
    for cat, items in grouped.items():
        print(f"{cat}: {len(items)} найменувань")
        
    index = create_product_index(products)
    print("\nПошук за кодом 103 (O(1)):", index.get(103))
    
    is_low_stock = create_quantity_filter(5)
    print_items("Товари, кількість яких < 5 (Критичний залишок)", filter_items(products, is_low_stock))
    
    print(f"\nСередня ціна вибраних (через *args): {average_price_demo(25000, 800, 1500):.2f}")
    new_prod = create_product_record(code=106, name="Клавіатура", category="Електроніка", price=1200.0, quantity=15)
    print("Новий запис (через **kwargs):", new_prod)

if __name__ == "__main__":
    main()
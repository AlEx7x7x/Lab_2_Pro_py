from data_processor.analytics import (
    average_price_demo,
    calculate_total_value,
    create_product_record,
    create_quantity_filter,
    filter_items,
    find_most_expensive,
    sort_by_price,
)
from data_processor.data import CATEGORIES, products
from data_processor.processors import (
    count_items_by_category,
    create_product_index,
    filter_by_category,
    get_unique_categories,
    group_by_category,
)


def print_items(title: str, items: list[dict]) -> None:
    print(f"\n{title}\n" + "-" * 60)
    for p in items:
        print(f"{p['code']:4} {p['name']:18} {p['category']:18} {p['price']:8.2f} {p['quantity']:4} шт.")


def main() -> None:
    print_items("Всі товари", products)

    print("\nДопустимі категорії (tuple):", CATEGORIES)
    print("Унікальні категорії:", get_unique_categories(products))
    print_items(f"Категорія '{CATEGORIES[0]}'", filter_by_category(products, CATEGORIES[0]))

    print(f"\nЗагальна вартість залишків: {calculate_total_value(products):.2f}")

    best = find_most_expensive(products)
    if best:
        print(f"Найдорожчий товар: {best['name']} ({best['price']} грн)")

    print_items("Рейтинг товарів за ціною (спадання)", sort_by_price(products))

    print("\nГрупування за категоріями:")
    for cat, items in group_by_category(products).items():
        print(f"{cat}: {len(items)} найменувань")

    print("\nКількість товарів по категоріях (Counter):")
    for cat, count in count_items_by_category(products).items():
        print(cat, count)

    index = create_product_index(products)
    print("\nПошук за кодом 103 (O(1)):", index.get(103))

    is_low_stock = create_quantity_filter(5)
    print_items("Товари, кількість яких < 5", filter_items(products, is_low_stock))

    print(f"\nСередня ціна (через *args): {average_price_demo(25000, 800, 1500):.2f}")
    new_prod = create_product_record(
        code=106, name="Клавіатура", category="Електроніка", price=1200.0, quantity=15
    )
    print("Новий запис (через **kwargs):", new_prod)


if __name__ == "__main__":
    main()

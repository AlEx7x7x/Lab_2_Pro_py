from data_processor.analytics import (
    calculate_total_value,
    create_quantity_filter,
    filter_items,
    find_most_expensive,
    sort_by_price,
)
from data_processor.data import products
from data_processor.processors import (
    count_items_by_category,
    create_product_index,
    filter_by_category,
    get_unique_categories,
    group_by_category,
)


def test_unique_categories():
    assert get_unique_categories(products) == {"Електроніка", "Побутова техніка", "Аксесуари"}


def test_index_and_filter_by_category():
    assert create_product_index(products)[103]["name"] == "Мікрохвильова піч"
    assert len(filter_by_category(products, "Електроніка")) == 2


def test_group_and_counter():
    assert len(group_by_category(products)["Побутова техніка"]) == 2
    assert count_items_by_category(products)["Аксесуари"] == 1


def test_total_value_and_most_expensive():
    assert calculate_total_value(products) == 369500.0
    assert find_most_expensive(products)["code"] == 101


def test_sort_by_price_descending():
    prices = [p["price"] for p in sort_by_price(products)]
    assert prices == sorted(prices, reverse=True)


def test_closure_quantity_filter():
    low = filter_items(products, create_quantity_filter(5))
    assert {p["code"] for p in low} == {104, 105}

from time import perf_counter

from data_processor.processors import create_product_index


def find_linear(products: list[dict], code: int) -> dict | None:
    for p in products:
        if p["code"] == code:
            return p
    return None


def run(sizes=(1_000, 10_000, 100_000), repeats=200) -> None:
    print(f"{'Records':>8} | {'list search, s':>15} | {'dict search, s':>15} | {'build index, s':>15}")
    for n in sizes:
        data = [{"code": i, "category": "X"} for i in range(n)]
        target = n - 1  # найгірший випадок для list

        t = perf_counter()
        for _ in range(repeats):
            find_linear(data, target)
        t_list = (perf_counter() - t) / repeats

        t = perf_counter()
        index = create_product_index(data)
        t_build = perf_counter() - t

        t = perf_counter()
        for _ in range(repeats):
            index.get(target)
        t_dict = (perf_counter() - t) / repeats

        print(f"{n:>8} | {t_list:>15.8f} | {t_dict:>15.8f} | {t_build:>15.8f}")


if __name__ == "__main__":
    run()
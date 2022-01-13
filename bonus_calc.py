def calc_bonus_modifier(perf_review_result: float) -> float:
    if not 1 <= perf_review_result <= 5:
        raise ValueError(
            f'Результат Performance Review должен быть от 1 до 5 включительно. Значение: {perf_review_result}')
    perf_review_result_to_modifier = {
        2: 1,
        2.5: 1.25,
        3: 1.5,
        3.5: 2,
        4: 2.5,
    }
    for reference, modifier in perf_review_result_to_modifier.items():
        if perf_review_result < reference:
            return modifier
    return 3


def calc_relative_bonus_size_modifier(engineer_lvl: int) -> float:
    if not 7 <= engineer_lvl <= 17:
        raise ValueError(f'Уровень инженера должен быть от 7 до 17 включительно. Значение: {engineer_lvl}')
    levels_to_size = {
        10: 0.05,
        13: 0.1,
        15: 0.15,
    }
    for key, value in levels_to_size.items():
        if engineer_lvl < key:
            return value
    return 0.2


def calc_bonus_total(salary: int, perf_review_result: float, engineer_level: int) -> int:
    if not 70_000 <= salary <= 750_000:
        raise ValueError(f'Зарплата должна быть от 70к до 750к включительно. Значение: {salary}')
    # квартальная же зп, правильно?
    salary *= 3
    return int(salary * calc_relative_bonus_size_modifier(engineer_level) * calc_bonus_modifier(perf_review_result))


# def main():
#     salary = int(input('Введите ЗП(70_000..750_000): '))
#     perf_review_result = float(input('Введите результат квартального Performance Review(1..5): '))
#     engineer_level = int(input('Введите уровень инженера(7..17): '))
#     bonus = calc_bonus_total(salary, perf_review_result, engineer_level)
#     print(f'Размер премии составляет {bonus}')


if __name__ == '__main__':
    # main()
    salary = int(input('Введите ЗП(70_000..750_000): '))
    perf_review_result = float(input('Введите результат квартального Performance Review(1..5): '))
    engineer_level = int(input('Введите уровень инженера(7..17): '))
    bonus = calc_bonus_total(salary, perf_review_result, engineer_level)
    print(f'Размер премии составляет {bonus}')

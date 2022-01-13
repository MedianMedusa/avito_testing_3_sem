import bonus_calc as calc
import pytest
from allpairspy import AllPairs

salaries_list = list(range(20_000, 850_000, 50_000)) + ['string', None]
perf_review_results_list = list(i / 2 for i in range(2, 10)) + ['string', None]
engineer_levels_list = list(range(6, 19)) + ['string', None]

all_pairs = [pair for pair in AllPairs(
    [salaries_list, perf_review_results_list, engineer_levels_list]
)]


@pytest.mark.parametrize(
    'perf_review_result, expected',
    [
        (1, 1),
        (2, 1.25),
        (2.5, 1.5),
        (3, 2),
        (3.5, 2.5),
        (4, 3),
        (5, 3)
    ]
)
def test_calc_bonus_modifier_positive(perf_review_result, expected):
    assert calc.calc_bonus_modifier(perf_review_result) == expected


@pytest.mark.parametrize(
    'perf_review_result, expected_error',
    [
        (0, ValueError),
        (None, TypeError),
        ('some string', TypeError),
        (5.1, ValueError)
    ]
)
def test_calc_bonus_modifier_negative(perf_review_result, expected_error):
    with pytest.raises(expected_error):
        calc.calc_bonus_modifier(perf_review_result)


@pytest.mark.parametrize(
    'lvl, expected',
    [
        (7, 0.05),
        (9, 0.05),
        (10, 0.1),
        (13, 0.15),
        (15, 0.2),
        (17, 0.2),
    ]
)
def test_calc_relative_bonus_size_modifier_positive(lvl, expected):
    assert calc.calc_relative_bonus_size_modifier(lvl) == expected


@pytest.mark.parametrize(
    'lvl, expected_error',
    [
        (0, ValueError),
        (6.5, ValueError),
        (None, TypeError),
        ('some string', TypeError),
        (17.1, ValueError),
        (18, ValueError)
    ]
)
def test_calc_relative_bonus_size_modifier_negative(lvl, expected_error):
    with pytest.raises(expected_error):
        calc.calc_relative_bonus_size_modifier(lvl)


@pytest.mark.parametrize(
    'salary, rev_result, lvl, expected',
    [
        (70_000, 1, 7, 70000 * 3 * 0.05),
        (70_000, 2, 7, 70_000 * 3 * 0.05 * 1.25),
        (70_000, 2, 17, 70_000 * 3 * 0.2 * 1.25),
        (750_000, 5, 17, 750_000 * 3 * 0.2 * 3)
    ]
)
def test_bonus_calculation_positive(salary, rev_result, lvl, expected):
    assert calc.calc_bonus_total(salary, rev_result, lvl) == expected


@pytest.mark.parametrize(
    'salary, rev_result, lvl, expected_err',
    [
        (65_000, 1, 7, ValueError),
        (750_001, 2, 7, ValueError),
        ('70_000', 2, 17, TypeError),
        (None, 5, 17, TypeError)
    ]
)
def test_bonus_calculation_negative(salary, rev_result, lvl, expected_err):
    with pytest.raises(expected_err):
        calc.calc_bonus_total(salary, rev_result, lvl)


@pytest.mark.parametrize(
    'salary, rev_result, lvl',
    all_pairs
)
def test_bonus_calculation_random(salary, rev_result, lvl):
    possible_errors = (ValueError, TypeError)
    # with pytest.raises(possible_errors):
    try:
        result = calc.calc_bonus_total(salary, rev_result, lvl)
        assert result not in possible_errors
    except possible_errors:
        assert True

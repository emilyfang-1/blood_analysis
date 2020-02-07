import pytest


def test_HDL_analysis_normal():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(80)
    expected = "Normal"
    assert answer == expected


@pytest.mark.parametrize("i, o", [
    (100, 'Normal'),
    (50, 'Borderline low'),
    (20, 'Low'),
    (55.5, 'Borderline low'),
    ])
def test_HDL_analysis_parametrize(i, o):
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(i)
    expected = o
    assert answer == expected


def test_HDL_analysis_bl():
    from chol_analysis import HDL_analysis
    answer = HDL_analysis(40)
    expected = "Borderline low"
    assert answer == expected


def test_LDL_analysis():
    from chol_analysis import LDL_analysis
    answer = LDL_analysis(165)
    expected = "High"
    assert answer == expected


def test_fever_check():
    from chol_analysis import fever_check
    new_data = [96.0, 100.5, 105.1, 97]
    answer = fever_check(new_data)
    expected = True
    assert answer == expected

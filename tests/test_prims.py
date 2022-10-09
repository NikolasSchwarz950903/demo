import pytest
from src.prim import prim_numbers


@pytest.mark.parametrize(
    ("n", "expected_count"),
    [
        (100, 25),
        (1_000, 168),
        (10_000, 1229),
        (31, 11),
    ]
)
def test_prims(n: int, expected_count: int):
    # Super test!
    assert len(list(prim_numbers(n))) == expected_count


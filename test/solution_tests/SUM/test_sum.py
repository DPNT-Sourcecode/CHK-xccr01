
from solutions.SUM import sum_solution

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_dif_sum(self):
        assert sum_solution.compute(5, 2) == 7




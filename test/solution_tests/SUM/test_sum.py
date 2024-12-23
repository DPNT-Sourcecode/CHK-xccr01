
from solutions.SUM import sum_solution
import sys

sys.path.insert('~/iwoca/accelerate_runner/test/solutions/SUM')


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3



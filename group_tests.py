import group
import unittest


class TestCases(unittest.TestCase):

    def test_group_of_3_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        fr = group.groups_of_3(nums)
        om = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert fr == om

    def test_group_of_3_2(self):
        nums = [1, 32, 93, 12, 0, -12, 32, -45]
        fr = group.groups_of_3(nums)
        om = [[1, 32, 93], [12, 0, -12], [32, -45]]
        assert fr == om

    def test_group_of_3_3(self):
        nums = []
        fr = group.groups_of_3(nums)
        om = []
        assert fr == om
if __name__ == '__main__':
    unittest.main()
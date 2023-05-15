# Task 1
# Design Recipe
# 1) it will take a list of integers and put three numbers into a list then put that list into a list and repeat
# 2) groups_of_3(lst: list[int])->list[list[int]]:
# 3) template of function
#   - iterate over the given list
#   - go over the list in steps of 3 and add each number into a list
#   - slices the list from the current index to index 3
# 4) test case:         def test_group_of_3_2(self):
#                           nums = [1, 32, 93, 12, 0, -12, 32, -45]
#                           fr = group.groups_of_3(nums)
#                           om = [[1, 32, 93], [12, 0, -12], [32, -45]]
#                           assert fr == om
# 5)

def groups_of_3(lst: list[int]) -> list[list[int]]:
    return [lst[i:i+3] for i in range(0, len(lst), 3)]

class Solution:
    def lemonadeChange(self, nums: list[int]) -> bool:
        five = ten = 0

        for bill in nums:
            if bill == 5:
                five +=1

            elif bill == 10:
                if five:
                    five-=1
                    ten += 1
                else:
                    return False

            else:

                if five and ten:
                    five -=1
                    ten  -=1
                elif five > 2:
                    five-=3
                else:
                    return False
        return True

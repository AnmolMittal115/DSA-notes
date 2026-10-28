class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort( key=lambda x: x[1], reverse = True)
        total = 0

        for boxes, units in boxTypes:

            taking = min( boxes, truckSize )

            total += taking * units
            truckSize -= taking

            if truckSize == 0:
                break
        return total

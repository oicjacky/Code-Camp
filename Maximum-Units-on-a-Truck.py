''' 
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
 
Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

 
Constraints:
1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
'''
from typing import List

class Solution:

    #NOTE: sort by the `numberOfUnitsPerBoxi` then put it into truck
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda ele: ele[1], reverse=True)
        truck_boxes, truck_elements = 0, 0
        for ele in boxTypes:
            while ele[0] > 0 and truck_boxes < truckSize:
                truck_boxes += 1
                ele[0] -= 1
                truck_elements += ele[1]
                print(ele[0], truck_boxes, truck_elements)
        return truck_elements
    
    #NOTE: change the while loop (one unit at a time)
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda ele: ele[1], reverse=True)
        truck_elements = 0
        for ele in boxTypes:
            if truckSize - ele[0] <= 0:
                truck_elements += truckSize *ele[1]
                break
            truckSize -= ele[0]
            truck_elements += ele[0] *ele[1]
            print(ele[0], truckSize, truck_elements)
        return truck_elements


if __name__ == "__main__":
    print(Solution().maximumUnits([[1,3],[2,2],[3,1]], 4)) #8
    print(Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)) #91
    
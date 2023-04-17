from typing import List

# The bus goes along both directions i.e. clockwise and counterclockwise.

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        pos1 = min(start, destination)
        pos2 = max(start, destination)
        return min(sum(distance[pos1:pos2]), sum(distance)-sum(distance[pos1:pos2]))
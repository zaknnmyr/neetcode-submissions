class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-n for n in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
            num1 = heapq.heappop(self.maxHeap) * -1
            num2 = heapq.heappop(self.maxHeap) * -1
            if num1 > num2:
                heapq.heappush(self.maxHeap, (num1 - num2) * -1)
            elif num1 < num2:
                heapq.heappush(self.maxHeap, (num2 - num1) * -1)
        
        if len(self.maxHeap) == 0:
            return 0
        else:
            return (self.maxHeap[0] * -1)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            if x < y:
                new_stone = x - y
                heapq.heappush(stones, new_stone)
        
        if stones:
            return abs(heapq.heappop(stones))
        else:
            return 0
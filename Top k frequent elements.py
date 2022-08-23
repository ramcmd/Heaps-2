class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
                
        m = []
        result = []

        for key,val in hashmap.items():
            heapq.heappush(m , [-val, key])

            if len(m) > len(hashmap) - k:
                result.append(heapq.heappop(m)[1])

        return result
                
            
            
                
                
                
            
        
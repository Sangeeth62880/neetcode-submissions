class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        while maxheap or q:
            time += 1
            if maxheap:
                ct = heapq.heappop(maxheap) + 1
                if ct!=0:
                    q.append([ct,time+n])
            if q and q[0][1] == time:
                    res = q.popleft()[0]
                    heapq.heappush(maxheap,res)
        return time



        
            

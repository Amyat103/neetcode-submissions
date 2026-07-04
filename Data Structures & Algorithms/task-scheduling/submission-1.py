class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        tasks = ["X","X","Y","Y"],n=2 > X|Y||X|Y
        constaint- other than task need n break betwee
        can tasks be empty? no at least 1 ok
        1) first thing came up is
        1st, map tasks into dict, so {task: # of times}
        might need another task for buffer
        buffer = {x:n, y:n}
        ill have a main loop where
        while mapped: (the dict)
        choose 1 taks, say x
        add to buffer x : n
        next cycle choose 1 task not in buffer
        y : n
        at same time -=1 to buffer, if done, remove from buffer
        also check mapped, if -=1 <=0, remove from mapped
        go until eveyrthing done
        return a tracked ans
        for this sol : O(m * n) maybe? 
        2) is there a better way
        greedy? maybe choose most occ, to buffer faster, 
        most occ to least
        maybe i can heapq for this, like
        count all put into tuple
        (#, task), pop out highest, and -= 1 push abck in
        that way highest count get buffer and can do most optimal
        O(heapq) n log n * m
        3) anything else
        ill do heap since a bit faster
        failed attempt:
                # count and push heap
        count = {}
        for t in tasks:
            if t not in count:
                count[t] = 0
            count[t] += 1
        #make heap
        new_tasks = []
        for t,c in count:
            (-c, t).heappush(new_task)
        
        #need buffer count? need a buffer #waht about instead of dict, i do [0]*26, and count?
        buffer = defaultdict(int)
        ans = 0

        while new_tasks: #while heap we keep going and inc
            num, task = heapq.heappop(new_tasks)
            #push abck in after inc
            if num + 1 < 0:
                (num+1, task).heapq.heappush(new_tasks)
            buffer[num] = n - 1


        saw ans
        pattenr is close to waht i had but missing key queue
        so same use heap, but can ignore letter since no need to return order
        just time. so heap contain count
        we do min heap, eveyr time we run a heappop, put into queue
        (#num left, time when it can be popped out)
        have a time var, main tracker, and counter += 1
        heap gets their stuff back when queue buffer time is reached
        """
        count = {}
        for t in tasks:
            if t not in count:
                count[t] = 0
            count[t] += 1
        heap = []
        for c in count.values():
            heapq.heappush(heap, -c)
        #now heap have min heap neg count
        queue = deque([])
        time =0

        while heap or queue:
            time += 1
            #1) pop highest 2) -=1, if still need, queue.append(curr, buff)
            #3) time += 1, keep inc, if queue[0][1] == time, reached, popleft
            #and append to heap again for next cycle
            if heap:
                curr = heapq.heappop(heap)
                curr += 1
                if curr < 0:
                    queue.append((curr, time + n))
            #check queue remove
            if queue and queue[0][1] == time:
                node, time = queue.popleft()
                heapq.heappush(heap, node)
            

        return time















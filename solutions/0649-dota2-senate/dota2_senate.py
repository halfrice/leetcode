# https://leetcode.com/problems/dota2-senate/

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()  # Radiant Queue
        dq = deque()  # Dire Queue

        # Build both Radiant and Dire Queues with their respective indexes
        for i, s in enumerate(senate):
            if s == 'R':
                rq.append(i)
            else:
                dq.append(i)

        # Compare opposing senators position in the senate by index
        while rq and dq:
            # If the Radiant Senator votes before the Dire Senator
            if rq[0] < dq[0]:
                # Radiant Senator votes and is placed at the back of the queue
                rq.append(rq[0] + len(senate))
            # If the Dire Senator votes before the Radiant Senator
            else:
                # Dire Senator votes and is placed at the back of the queue
                dq.append(dq[0] + len(senate))

            # Deque both opposing senators
            rq.popleft()
            dq.popleft()

        return 'Radiant' if rq else 'Dire'

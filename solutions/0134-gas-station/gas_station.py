# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            # Get the total amount of gas in the tank after cost at this index
            total += gas[i] - cost[i]

            # If the total is less than zero then the result can't be at this index
            if total < 0:
                # Reset total and preset result to be the next index
                total = 0
                res = i + 1

        return res

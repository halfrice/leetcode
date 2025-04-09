# https://leetcode.com/problems/keys-and-rooms/


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # Depth-first search solution
        def dfs(room):
            if room in visited:
                return

            visited.add(room)

            for key in rooms[room]:
                dfs(key)

        visited = set()

        dfs(0)

        return len(visited) == len(rooms)

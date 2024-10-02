from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        fringe = deque([0])
        visited = set()
        while len(fringe):
            for idx in range(len(fringe)):
                room_idx = fringe.popleft()
                if room_idx not in visited:
                    fringe.extend(rooms[room_idx])
                visited.add(room_idx)
        return len(visited) == len(rooms)

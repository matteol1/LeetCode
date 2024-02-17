class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        visited.add(0)
        my_stack = [0]
        while len(my_stack):
            new_index = my_stack.pop(-1)
            for entry in rooms[new_index]:
                if entry not in visited:
                    my_stack.append(entry)
                visited.add(entry)
            if len(visited) == len(rooms):
                return True
        return False
import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by start time
        meetings.sort()
        
        # free_rooms: stores indices of available rooms
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # busy_rooms: stores (end_time, room_number)
        busy_rooms = []
        
        # count: stores number of meetings held in each room
        count = [0] * n
        
        for start, end in meetings:
            # 1. Free up rooms whose meetings have finished by 'start' time
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            # 2. Assign a room
            if free_rooms:
                room = heapq.heappop(free_rooms)
                # Meeting starts on time
                heapq.heappush(busy_rooms, (end, room))
                count[room] += 1
            else:
                # 3. No rooms free, delay the meeting
                earliest_finish, room = heapq.heappop(busy_rooms)
                duration = end - start
                new_end = earliest_finish + duration
                heapq.heappush(busy_rooms, (new_end, room))
                count[room] += 1
        
        # 4. Find the room with max meetings
        max_meetings = -1
        result_room = 0
        for i in range(n):
            if count[i] > max_meetings:
                max_meetings = count[i]
                result_room = i
                
        return result_room
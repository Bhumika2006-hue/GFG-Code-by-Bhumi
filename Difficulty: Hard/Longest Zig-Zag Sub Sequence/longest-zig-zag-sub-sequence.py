class Solution:
    def ZigZagMaxLength(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        # 'up' tracks the max length ending with an upward move
        # 'down' tracks the max length ending with a downward move
        up = 1
        down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # We found a rising edge; it can follow a falling edge
                up = down + 1
            elif nums[i] < nums[i-1]:
                # We found a falling edge; it can follow a rising edge
                down = up + 1
                
        # The answer is the maximum of the two states
        return max(up, down)
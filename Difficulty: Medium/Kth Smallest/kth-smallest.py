import heapq

class Solution:
    def kthSmallest(self, arr, k):
        # We use a Max-Heap to keep track of the k smallest elements.
        # Python's heapq is a Min-Heap, so we store negative values to simulate a Max-Heap.
        max_heap = []
        
        for num in arr:
            # Push negative of num onto the heap
            heapq.heappush(max_heap, -num)
            
            # If heap size exceeds k, remove the largest element
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # The top of the max_heap is the kth smallest element (negated)
        return -max_heap[0]
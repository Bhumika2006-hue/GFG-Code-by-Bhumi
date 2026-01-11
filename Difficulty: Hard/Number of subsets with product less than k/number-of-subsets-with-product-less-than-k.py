import bisect

class Solution:
    def numOfSubsets(self, arr, k):
        n = len(arr)
        
        # Helper function to generate all possible subset products
        def get_subset_products(sub_arr):
            products = [1]
            for x in sub_arr:
                new_products = []
                for p in products:
                    if p * x <= k:
                        new_products.append(p * x)
                products.extend(new_products)
            return products

        # Split array into two halves
        mid = n // 2
        left_products = get_subset_products(arr[:mid])
        right_products = get_subset_products(arr[mid:])
        
        # Sort the right products for binary search
        right_products.sort()
        
        ans = 0
        # For every product in the left half, find matching products in the right half
        for p_left in left_products:
            # We need p_left * p_right <= k  =>  p_right <= k // p_left
            target = k // p_left
            # Count elements in right_products <= target
            count = bisect.bisect_right(right_products, target)
            ans += count
            
        # Subtract 1 because the empty subset (product 1 from both halves) is counted,
        # but the problem asks for non-empty subsets.
        return ans - 1
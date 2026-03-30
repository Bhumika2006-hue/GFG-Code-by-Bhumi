
class Solution {
  public:
      int minCost(vector<vector<int>>& houses) {
         int n = houses.size();
        if (n == 0) return 0;

        // Priority queue to select the edge with the smallest weight
        priority_queue<pair<int, int>,
                       vector<pair<int, int>>,
                       greater<pair<int, int>>> minHeap;

        // Vector to track visited nodes
        vector<bool> inMST(n, false);

        // Start with the first house
        minHeap.push({0, 0});
        int totalCost = 0;
        int edgesUsed = 0;

        while (!minHeap.empty() && edgesUsed < n) {
            pair<int, int> topElement = minHeap.top();
            minHeap.pop();
            int cost = topElement.first;
            int u = topElement.second;

            if (inMST[u]) continue;

            // Include this node in MST
            inMST[u] = true;
            totalCost += cost;
            edgesUsed++;

            // Update the priority queue with the adjacent nodes
            for (int v = 0; v < n; ++v) {
                if (!inMST[v]) {
                    int distance = abs(houses[u][0] - houses[v][0]) +
                                   abs(houses[u][1] - houses[v][1]);
                    minHeap.push({distance, v});
                }
            }
        }

        return totalCost;
    }
    
};



class Solution {
  public:
    vector<int> articulationPoints(int V, vector<vector<int>>& edges) {
        vector<vector<int>> adj = constructAdj(V, edges);
        
        // Initialize helper vectors
        vector<int> disc(V, 0), low(V, 0), visited(V, 0), isAP(V, 0);
        int time = 0;

        // Find articulation points in all components
        for (int u = 0; u < V; u++) {
            if (!visited[u]) {
                findPoints(adj, u, visited, disc, low, time, -1, isAP);
            }
        }
        // Collect all articulation points
        vector<int> result;
        for (int u = 0; u < V; u++) {
            if (isAP[u]) {
                result.push_back(u);
            }
        }

        return result.empty() ? vector<int>{-1} : result;
    }

  private:
    vector<vector<int>> constructAdj(int V, vector<vector<int>> &edges) {
        vector<vector<int>> adj(V);
        for (auto &edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        return adj;
    }

    void findPoints(vector<vector<int>> &adj, int u, vector<int> &visited,
                    vector<int> &disc, vector<int> &low, 
                    int &time, int parent, vector<int> &isAP) {
        visited[u] = 1;
        disc[u] = low[u] = ++time;
        int children = 0;

        for (int v : adj[u]) {
            if (!visited[v]) {
                children++;
                findPoints(adj, v, visited, disc, low, time, u, isAP);

                low[u] = min(low[u], low[v]);

                if (parent != -1 && low[v] >= disc[u]) {
                    isAP[u] = 1;
                }
            } else if (v != parent) {
                low[u] = min(low[u], disc[v]);
            }
        }

        if (parent == -1 && children > 1) {
            isAP[u] = 1;
        }
    }
};


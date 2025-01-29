class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.union_find(edges)
    
    def union_find(self, edges: List[List[int]]) -> List[int]:
        """
        Creates a flat hierarchy of nodes - Path compression
        Neetcode: https://www.youtube.com/watch?v=1lNK80tOTfc
        Time Complexity: O((N+N)*alpha(N)) ~ O(V+E)
        Space Complexity: O(N)
        """
        N = len(edges)
        # Start with 'Every node is a parent to itself'
        parents = [i for i in range(N+1)]
        # Size of each connected component
        rank = [1] * (N+1)

        def find(node: int) -> int:
            # Time Complexity: O(alpha(N)) ~ O(1)
            # Recursively goes up the node to find the parent
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(node_1: int, node_2: int) -> bool:
            parent_1, parent_2 = find(node_1), find(node_2)
            if parent_1 == parent_2:
                # Cannot be unified since they have the same parent
                return False
            # Check which parent has the higher rank
            if rank[parent_1] > rank[parent_2]:
                parents[parent_2] = parent_1
                rank[parent_1] += parent_2
            else:
                parents[parent_1] = parent_2
                rank[parent_2] += parent_1
            return True
        
        for node_1, node_2 in edges:
            if not union(node_1, node_2):
                return (node_1, node_2)

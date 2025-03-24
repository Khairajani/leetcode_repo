class Solution:
    
    def create_adjacency_list(self, elements):
        adjacency_list_original = {}
        adjacency_list_reverse = {}

        for s, d in elements:
            # Add edge from source to destination
            if s in adjacency_list_original:
                existing_neigh = adjacency_list_original[s]
                existing_neigh.append(d)
                adjacency_list_original[s] = existing_neigh
            else:
                adjacency_list_original[s] = [d]

            # For forward/backend adjacency OR original/reverse adacancy
            if d in adjacency_list_reverse:
                existing_neigh = adjacency_list_reverse[d]
                existing_neigh.append(s)
                adjacency_list_reverse[d] = existing_neigh
            else:
                adjacency_list_reverse[d] = [s]
        
        self.adjacency_list_original = adjacency_list_original
        self.adjacency_list_reverse = adjacency_list_reverse

    def solve(self, node):
        for neigh in self.adjacency_list_original.get(node, []):
            if not self.visited_nodes.get(neigh, False):
                self.result+=1
                self.visited_nodes[neigh] = True
                self.solve(neigh)

        for neigh in self.adjacency_list_reverse.get(node, []):
            if not self.visited_nodes.get(neigh, False):
                self.visited_nodes[neigh] = True
                self.solve(neigh)

        return

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.create_adjacency_list(connections)
        self.result = 0

        source_node = 0
        self.visited_nodes = {source_node:True}
        self.solve(source_node)
        return self.result
        
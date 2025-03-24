class Solution:
    def create_adjacency_list(self, elements, bidirectional=False):
        adjacency_list = {}
        for s, d in elements:
            # Add edge from source to destination
            if s in adjacency_list:
                existing_neigh = adjacency_list[s]
                existing_neigh.append(d)
                adjacency_list[s] = existing_neigh
            else:
                adjacency_list[s] = [d]
            
            # For bidirectional graph, add edge from destination to source
            if bidirectional:
                if d in adjacency_list:
                    existing_neigh = adjacency_list[d]
                    existing_neigh.append(s)
                    adjacency_list[d] = existing_neigh
                else:
                    adjacency_list[d] = [s]
        return adjacency_list

    def graph_bfs(self, source):
        result = []
        visited_nodes = {}
        if not self.adjacency_list:
            return result,visited_nodes
        
        level_queue = [source]
        visited_nodes[source] = True

        while level_queue:
            non_visited_new_level_nodes = []
            element_in_current_level = len(level_queue)
            
            for i in range(element_in_current_level):
                curr_element = level_queue.pop(0)
                non_visited_new_level_nodes.append(curr_element)
                for neigh in self.adjacency_list.get(curr_element, []):
                    if not visited_nodes.get(neigh, False):
                        level_queue.append(neigh)
                        visited_nodes[neigh] = True  # Mark as visited when adding to queue
            result.extend(non_visited_new_level_nodes)

        return result, visited_nodes

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool: 
        self.adjacency_list = self.create_adjacency_list(edges, True)
        result, visited_nodes = self.graph_bfs(source)
        print(result)
        if source==destination or visited_nodes.get(destination) is not None:
            return True
        return False
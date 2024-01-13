from heapq import heappop, heappush
from search_node import Node



class SearchTreePQD:
    
    def __init__(self):
        self._open = []
        self._closed = dict()
        self._enc_open_dublicates = 0
                                      
    def __len__(self):
        return len(self._open) + len(self._closed)
                
    def open_is_empty(self) -> bool:
        return not self._open
    
    def add_to_open(self, item: Node):
        heappush(self._open, item)

    def get_best_node_from_open(self) -> Node:
        best_node = heappop(self._open)
        while self.was_expanded(best_node):
            if not self._open:
                return None
            best_node = heappop(self._open)
            self._enc_open_dublicates +=1
        return best_node

    def add_to_closed(self, item: Node):
        self._closed[item] = item

    def was_expanded(self, item: Node) -> bool:
        return item in self._closed

    @property
    def opened(self):
        return self._open
    
    @property
    def expanded(self):
        return self._closed.values()

    @property
    def number_of_open_dublicates(self):
        return self._enc_open_dublicates
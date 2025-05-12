import random

class ConstantDS:
    """O(1) insert, remove, and get-random data stucture."""

    def __init__(self) -> None:
        self.values: List[int] = []
        self.idx_map: Dict[int, int] = {}

    def insert(self, val) -> None:
        if val in self.idx_map:
            return
        
        self.values.append(val)
        self.idx_map[val] = len(self.values) - 1
        
    def remove(self, val) -> None:
        if val not in self.idx_map:
            return
        
        idx = self.idx_map[val]
        last_idx = len(self.values) - 1
        
        if idx != last_idx:
            self.values[idx] = self.values[-1]
            self.idx_map[self.values[last_idx]] = idx
        
        self.values.pop()
        del self.idx_map[val]

    def get_random(self) -> int:
        return random.choice(self.values)

    def show(self) -> None:
        print(self.values)
        print(self.idx_map)
            
def main():
    rs = ConstantDS()
    
    for x in (5, 3, 10, 20):
        rs.insert(x)
    
    rs.show()

    print(f'Random pick from list: {rs.get_random()}')
    
    rs.remove(5)
    rs.show()

if __name__ == "__main__":
    main()


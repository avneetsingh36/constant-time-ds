## constant-ds

`constant-ds.py` implements `ConstantDS`, a randomized set with **O(1)** `insert`, `remove` and `get_random`.

## Usage

    from constant_ds import ConstantDS
    rs = ConstantDS()
    for x in (5, 3, 10, 20):
        rs.insert(x)
    rs.show()                    # [5, 3, 10, 20]
    print(rs.get_random())       # e.g. 3
    rs.remove(5)
    rs.show()                    # [20, 3, 10]

## API
- `insert(val)` → None  
- `remove(val)` → None  
- `get_random()` → int  
- `show()` → None

Data structure that can perform insert, remove, and get_random in constant time.

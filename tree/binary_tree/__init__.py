from .avl_tree import AVLtree
from .binary_search_tree import BinarySearchTree
from .fenwick_tree import FenwickTree
from .lazy_segment_tree import SegmentTree as ST1
from .non_recursive_segment_tree import SegmentTree as ST2
from .red_black_tree import RedBlackTree
from .segment_tree import SegmentTree as ST3



__all__ = ['AVLTree',
           'BinarySearchTree',
           'FenwickTree',
           'RedBlackTree',
           'LazySegmentTree',
           'NRSegmentTree',
           'SegmentTree'
]

class AVLTree(AVLtree): pass
class LazySegmentTree(ST1): pass
class NRSegmentTree(ST2): pass
class SegmentTree(ST3): pass

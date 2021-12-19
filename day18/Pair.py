from math import floor, ceil

class Pair:
    def __init__(self, arr, parent=None):
        self.parent = parent
        self.left = arr[0] if isinstance(arr[0], int) else Pair(arr[0], self)
        self.right = arr[1] if isinstance(arr[1], int) else Pair(arr[1], self)

    def depth(self):
        ldepth = 1 if isinstance(self.left, int) else 1 + self.left.depth()
        rdepth = 1 if isinstance(self.right, int) else 1 + self.right.depth()
        return max(ldepth, rdepth)

    def is_leaf(self):
        return isinstance(self.left, int) and isinstance(self.right, int)

    # Mark -- "My explode "closest" left function was to go back up
    # the tree until I could go left once, then I go right until a
    # terminal node, it seems to have worked
    def reg_left(self):
        p = self
        while p and (p.is_left_child() or p.is_root()):
            p = p.parent
        if p is None:
            return None, None
        else:
            if isinstance(p.parent.left, int):
                return p.parent, 'left'
            else:
                p = p.parent.left
                while p:
                    if isinstance(p.right, int):
                        return p, 'right'
                    else:
                        p = p.right
                return None, None
        
    def reg_right(self):
        p = self
        while p and (p.is_right_child() or p.is_root()):
            p = p.parent
        if p is None:
            return None, None
        else:
            if isinstance(p.parent.right, int):
                return p.parent, 'right'
            else:
                p = p.parent.right
                while p:
                    if isinstance(p.left, int):
                        return p, 'left'
                    else:
                        p = p.left
                return None, None

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return self.parent is None

    def explodable(self):
        stack = [(self, 0)]
        while len(stack):
            pair, d = stack.pop()
            if isinstance(pair, Pair):
                if pair.is_leaf() and d >= 4:
                    return pair
                else:
                    stack.append((pair.right, d+1))
                    stack.append((pair.left, d+1))
        return None

    def explode(self):
        p,lr = self.reg_left()
        if p:
            if lr == 'left':
                p.left += self.left
            else:
                p.right += self.left
        p,lr = self.reg_right()
        if p:
            if lr == 'left':
                p.left += self.right
            else:
                p.right += self.right

        if self.is_left_child():
            self.parent.left = 0
        else:
            self.parent.right = 0

    def splittable(self):
        stack = [(self, None)]
        while len(stack):
            pair, parent = stack.pop()
            if isinstance(pair, int) and pair >= 10:
                return parent
            elif isinstance(pair, Pair):
                stack.append((pair.right, pair))
                stack.append((pair.left, pair))
        return None

    def split(self):
        if isinstance(self.left, int) and self.left >= 10:
            val = self.left
            self.left = Pair([floor(val/2), ceil(val/2)], self)
        else:
            val = self.right
            self.right = Pair([floor(val/2), ceil(val/2)], self)

    def magnitude(self):
        if isinstance(self.left, int):
            lmag = 3 * self.left
        else:
            lmag = 3 * self.left.magnitude()

        if isinstance(self.right, int):
            rmag = 2 * self.right
        else:
            rmag = 2 * self.right.magnitude()

        return lmag + rmag            

    def __str__(self):
        return f'[{self.left},{self.right}]'

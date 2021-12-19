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

    def reg_left(self):
        p = self.parent
        while p and p.is_left_child():
            p = p.parent
        if p.parent is None:
            if isinstance(p.left, int):
                return p
            else:
                return None
        p = p.parent
        while p and isinstance(p.left, Pair):
            p = p.left
        if p:
            return p
        else:
            return None
        # if p.is_right_child():
        #     p = p.parent
        # while p and p.is_left_child():
        #     p = p.parent
        # if p and p.is_right_child():
        #     if isinstance(p.left, int):
        #         return p
        #     else:
        #         stack = [(p.parent.left, p.parent)]
        #         while len(stack):
        #             p, parent= stack.pop()
        #             if isinstance(p, int):
        #                 return parent
        #             else:
        #                 stack.append((p.left, p))
        #                 stack.append((p.right, p))
        # return None
        
    def reg_right(self):
        p = self.parent
        while p and p.is_right_child():
            p = p.parent
        if p.parent is None:
            if isinstance(p.right, int):
                return p
            else:
                return None
        p = p.parent
        while p and isinstance(p.right, Pair):
            p = p.right
        if p:
            return p
        else:
            return None
        # if p.is_left_child():
        #     p = p.parent
        # while p and p.is_right_child():
        #     p = p.parent
        # if p and p.is_left_child():
        #     if isinstance(p.right, int):
        #         return p
        #     else:
        #         stack = [(p.parent.right, p.parent)]
        #         while len(stack):
        #             p, parent= stack.pop()
        #             if isinstance(p, int):
        #                 return parent
        #             else:
        #                 stack.append((p.left, p))
        #                 stack.append((p.right, p))
        # return None

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

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
        if p := self.reg_left():
            p.left += self.left
            # if isinstance(p.right, int):
            #     p.right += self.left
            # else:
            #     p.left += self.left
        if p := self.reg_right():
            p.right += self.right
            # if isinstance(p.left, int):
            #     p.left += self.right
            # else:
            #     p.right += self.right

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

    def __str__(self):
        return f'[{self.left},{self.right}]'
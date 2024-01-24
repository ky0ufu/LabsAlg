import math

class PersistentTree:
    def __init__(self, arr):
        def is_2_power(num):
            return num & (num - 1) == 0

        def inner_get_sum(cur_node, l_ind, r_ind):
            if cur_node["l_ind"] - cur_node["r_ind"] > 0:
                return 0
            elif cur_node["l_ind"] == l_ind and cur_node["r_ind"] == r_ind:
                return cur_node["val"]
            else:
                if not cur_node["is_leaf"]:
                    l_sum = inner_get_sum(cur_node["l"], max(cur_node["l"]["l_ind"], l_ind), min(cur_node["l"]["r_ind"], r_ind))
                    r_sum = inner_get_sum(cur_node["r"], max(cur_node["r"]["l_ind"], l_ind), min(cur_node["r"]["r_ind"], r_ind))
                    return l_sum + r_sum
                else:
                    return 0

        def inner_set_elem(cur_node, leaf_pos, val):
            if cur_node["is_leaf"]:
                new_node = {"l": None, "r": None, "l_ind": leaf_pos, "r_ind": leaf_pos, "is_leaf": True, "val": val}
                return new_node
            else:
                l_node = inner_set_elem(cur_node["l"], leaf_pos, val) if leaf_pos <= cur_node["l"]["r_ind"] else cur_node["l"]
                r_node = inner_set_elem(cur_node["r"], leaf_pos, val) if leaf_pos > cur_node["l"]["r_ind"] else cur_node["r"]
                new_val = l_node["val"] + r_node["val"]
                new_node = {"l": l_node, "r": r_node, "l_ind": cur_node["l_ind"], "r_ind": cur_node["r_ind"], "is_leaf": False, "val": new_val}
                return new_node

        nodes_count = int(math.pow(2, math.ceil(math.log2(len(arr)))) if not is_2_power(len(arr)) else len(arr))
        primary_nodes_count = nodes_count
        nodes_count = nodes_count * 2 - 1
        height = int(math.log2(nodes_count + 1))

        layer1 = []
        layer2 = []

        cur_layer = layer1
        prev_layer = layer2

        for i in range(nodes_count):
            val = arr[i] if i < len(arr) else 0
            cur_layer.append({"l": None, "r": None, "l_ind": i, "r_ind": i, "is_leaf": True, "val": val})

        cur_layer, prev_layer = prev_layer, cur_layer

        while len(prev_layer) != 1:
            for i in range(len(prev_layer) // 2):
                l = prev_layer[2 * i]
                r = prev_layer[2 * i + 1]
                new_val = l["val"] + r["val"]
                new_node = {"l": l, "r": r, "l_ind": l["l_ind"], "r_ind": r["r_ind"], "is_leaf": False, "val": new_val}
                cur_layer.append(new_node)
            cur_layer, prev_layer = prev_layer, cur_layer
            cur_layer.clear()

        self._roots = [prev_layer[0]]

    def set_elem(self, version, pos, val):
        self._roots.append(self._inner_set_elem(self._roots[version], pos, val))

    def get_elem(self, version, pos):
        return self.get_sum(version, pos, pos)

    def get_sum(self, version, l, r):
        return self._inner_get_sum(self._roots[version], l, r)

    def _inner_get_sum(self, cur_node, l_ind, r_ind):
        if cur_node["l_ind"] - cur_node["r_ind"] > 0:
            return 0
        elif cur_node["l_ind"] == l_ind and cur_node["r_ind"] == r_ind:
            return cur_node["val"]
        else:
            if not cur_node["is_leaf"]:
                l_sum = self._inner_get_sum(cur_node["l"], max(cur_node["l"]["l_ind"], l_ind), min(cur_node["l"]["r_ind"], r_ind))
                r_sum = self._inner_get_sum(cur_node["r"], max(cur_node["r"]["l_ind"], l_ind), min(cur_node["r"]["r_ind"], r_ind))
                return l_sum + r_sum
            else:
                return 0

    def _inner_set_elem(self, cur_node, leaf_pos, val):
        if cur_node["is_leaf"]:
            new_node = {"l": None, "r": None, "l_ind": leaf_pos, "r_ind": leaf_pos, "is_leaf": True, "val": val}
            return new_node
        else:
            l_node = self._inner_set_elem(cur_node["l"], leaf_pos, val) if leaf_pos <= cur_node["l"]["r_ind"] else cur_node["l"]
            r_node = self._inner_set_elem(cur_node["r"], leaf_pos, val) if leaf_pos > cur_node["l"]["r_ind"] else cur_node["r"]
            new_val = l_node["val"] + r_node["val"]
            new_node = {"l": l_node, "r": r_node, "l_ind": cur_node["l_ind"], "r_ind": cur_node["r_ind"], "is_leaf": False, "val": new_val}
            return new_node

def tests():
    tree1 = PersistentTree([1, 2, 3])

    if tree1.get_elem(0, 0) != 1:
        return False
    if tree1.get_elem(0, 1) != 2:
        return False
    if tree1.get_elem(0, 2) != 3:
        return False

    if tree1.get_sum(0, 0, 2) != 6:
        return False
    if tree1.get_sum(0, 0, 1) != 3:
        return False
    if tree1.get_sum(0, 0, 0) != 1:
        return False
    if tree1.get_sum(0, 1, 2) != 5:
        return False

    tree2 = PersistentTree([1, 2, 3, 4, 5])

    if tree2.get_sum(0, 2, 4) != 12:
        return False

    tree2.set_elem(0, 0, 6)

    if tree2.get_elem(0, 0) != 1:
        return False
    if tree2.get_elem(1, 0) != 6:
        return False

    if tree2.get_sum(0, 0, 2) != 6:
        return False
    if tree2.get_sum(1, 0, 2) != 11:
        return False

    return True

if __name__ == "__main__":
    print("true" if tests() else "false")


    def perform_operation(op, operand1, operand2=0):
        if op == '+':
            return operand1 + operand2
        elif op == '-':
            return operand1 - operand2
        elif op == '*':
            return operand1 * operand2
        elif op == '/':
            if operand2 == 0:
                raise ValueError("Division by zero")
            return operand1 / operand2
        elif op == '^':
            return operand1 ** operand2
        elif op == '%':
            return operand1 % operand2
        elif op == 'l':
            if operand1 <= 0:
                raise ValueError("non-positive number in log")
            return math.log(operand1)
        elif op == 'c':
            return math.cos(operand1)
        elif op == 's':
            return math.sin(operand1)
        elif op == 't':
            return math.tan(operand1)
        elif op == 'g':
            return 1 / math.tan(operand1)
        elif op == '_':
            return operand1 * -1
        elif op == '!':
            return factorial(operand1)
        else:
            raise ValueError("Invalid operator")

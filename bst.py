class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array_to_bst(array_nums):
    if not array_nums:
        return None

    mid = (len(array_nums)) / 2
    root = TreeNode(array_nums[int(mid)])
    root.left = array_to_bst(array_nums[:int(mid)])
    root.right = array_to_bst(array_nums[int(mid) + 1:])
    return root


def preOrder(node):
    if not node:
        return 0
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


def solution(node):
    if node is None:
        return False
    return 1 + max(solution(node.left), solution(node.right))


if __name__ == '__main__':
    result = array_to_bst(A)
    print(solution(result))


def func(x):
    return x + 1


def test_func():
    assert func(4) == 5

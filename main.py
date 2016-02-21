import random
import traceback
import inspect
import __builtin__

def random_function(root = None):
    path = []
    ascend_probability = 0.9
    if root is None:
        root = eval(random.choice(dir(__builtin__)))
        while True:
            response = random_function(root)
            if response is not None:
                return response
    if type(root) == type(random_function):
        if random.random() < 0.8:
            return root
    while True:
        thingy = getattr(root, random.choice(dir(root)))
        func = random_function(thingy)
        if func is None:
            if random.random() > 0.9:
                return None
            else:
                continue
        else:
            if random.random() < 0.9:
                return func
            else:
                return None

def pick_random_function(num_args):
    while True:
        func = random_function()
        if len(inspect.getargspec(func)[0]) == num_args:
            return func

class function_tree_leaf:
    def __init__(self, root = None):
        self.root = root
        node = root
        level = 0
        while node is not None:
            node = node.root
            level += 1
        self.level = level
    def evaluate_once(self):
        min_args = 0
        if self.level == 0:min_args = 2
        if self.level == 1:min_args = 1
        max_args = max([10-self.level,0])
        num_args = random.randint(min_args, max_args)
        func = pick_random_function(num_args)
        args = []
        for arg in range(num_args):
            retvalue = None
            while retvalue is None:
                retvalue = function_tree_leaf(self).evaluate()
            args.append(retvalue)
        return func(*args)
    def evaluate(self):
        while True:
            try:
                return self.evaluate_once()
            except:
                traceback.print_exc()

if __name__ == '__main__':
    print function_tree_leaf().evaluate()

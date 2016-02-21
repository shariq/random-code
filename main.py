import random
import traceback
import inspect
import __builtin__

def random_function(root = None):
    path = []
    ascend_probability = 0.9
    while root is None:
        try:
            root = eval(random.choice(dir(__builtin__)))
        except:
            continue
        while True:
            response = random_function(root)
            if response is not None:
                return response
    if type(root) == type(random_function):
        if random.random() < 0.95:
            return root
    if random.random() < 0.8:
        return None
    while True:
        try:
            thingy = getattr(root, random.choice(dir(root)))
        except:
            if random.random() > 0.9:
                return None
            else:
                continue
        func = random_function(thingy)
        if func is None:
            if random.random() > 0.5:
                return None
            else:
                continue
        else:
            return func

def pick_random_function(min_args, max_args):
    while True:
        func = random_function()
        if min_args <= len(inspect.getargspec(func)[0]) <= max_args:
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
        func = pick_random_function(min_args, max_args)
        args = []
        for arg in range(num_args):
            retvalue = None
            while retvalue is None:
                retvalue = function_tree_leaf(self).evaluate()
            args.append(retvalue)
        print 'calling', func.__name__, 'with args', ' '.join(map(str,args))
        return func(*args)
    def evaluate(self):
        while True:
            try:
                return self.evaluate_once()
            except:
                pass
                traceback.print_exc()
                raw_input()

if __name__ == '__main__':
    print function_tree_leaf().evaluate()

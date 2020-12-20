# tuple, set, list, dict
from collections import namedtuple, deque, OrderedDict, defaultdict, Counter

# 1
Point = namedtuple("Point11", ["x", "y", "z"])
p = Point(1, 2, 3)
# p.x
# print(p[2])

# 2
my_deque = deque()
my_deque.append(11)
my_deque.append(33)
my_deque.appendleft(22)
# print("deque: ", my_deque)
# print("len deque: ", len(my_deque))
# print("deque pop: ", my_deque.pop())
# print("deque popleft: ", my_deque.popleft())
# print("deque: ", my_deque)


# 3
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
# print("ordered_dict: ", ordered_dict)
# print("ordered_dict a: ", ordered_dict["a"])
# print("ordered_dict keys: ",ordered_dict.keys())
# print("ordered_dict values: ",ordered_dict.values())
# print("ordered_dict items: ",ordered_dict.items())


# 4
def foo():
    return "Hi"

def_dict = defaultdict(foo)
def_dict['a'] = 1
def_dict['b'] = 2
# print("def_dict a: ", def_dict["a"])
# print("def_dict t: ", def_dict["t"])


# 5
counter = Counter({"a": 1, "b":2, "c":3})
print("counter: ", counter['b'])
# наиболее часто встречаемые символы в перечисляемом массиве
print("most_common: ", Counter("assdaaa").most_common(2))

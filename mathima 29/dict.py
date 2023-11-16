namespace = {}

namespace["x"] = 10
namespace["y"] = 20


def add(a, b):
    return a + b


namespace['add'] = add

result = namespace['add'](namespace["x"], namespace['y'])
print(result)

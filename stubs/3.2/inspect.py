# Stubs for inspect

from typing import Undefined, Any, Tuple, List, Function

_object = object

def getmembers(obj: object, predicate: Function[[Any], bool]) -> List[Tuple[str, object]]:
    return []

def isclass(obj: object) -> bool:
    return False

# namedtuple('Attribute', 'name kind defining_class object')
class Attribute(tuple):
    name = Undefined(str)
    kind = Undefined(str)
    defining_class = Undefined(type)
    object = Undefined(_object)

def classify_class_attrs(cls: type) -> List[Attribute]:
    return []

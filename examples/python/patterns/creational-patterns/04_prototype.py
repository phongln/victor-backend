from __future__ import annotations
from copy import deepcopy
from typing import Any
from datetime import datetime


class Prototype():
    def __init__(self):
        self._primitive = None
        self._component = None
        self._circular_ref = None

    @property
    def primitive(self):
        return self._primitive

    @primitive.setter
    def primitive(self, primitive):
        self._primitive = primitive

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, component):
        self._component = component

    @property
    def circular_ref(self):
        return self._circular_ref

    @circular_ref.setter
    def circular_ref(self, value):
        self._circular_ref = value

    def clone(self):
        self.component = deepcopy(self.component)
        self.circular_ref = deepcopy(self.circular_ref)
        self.circular_ref.prototype = self

        return deepcopy(self)


class ComponentWithBackReference():
    def __init__(self, prototype):
        self._prototype = prototype

    @property
    def prototype(self):
        return self._prototype

    @prototype.setter
    def prototype(self, prototype):
        self._prototype = prototype


if __name__ == '__main__':
    p1 = Prototype()
    p1.primitive = 235
    p1.component = datetime.now()
    p1.circular_ref = ComponentWithBackReference(p1)
    p2 = p1.clone()

    if p1.primitive is p2.primitive:
        print("Primitive field values have been carried over to a clone. Yay!")
    else:
        print("Primitive field values have not been copied. Booo!")

    if p1.component is p2.component:
        print("Simple component has not been cloned. Booo!")
    else:
        print("Simple component has been cloned. Yay!")

    if p1.circular_ref is p2.circular_ref:
        print("Component with back reference has not been cloned. Booo!")
    else:
        print("Component with back reference has been cloned. Yay!")

    if p1.circular_ref.prototype is p2.circular_ref.prototype:
        print("Component with back reference is linked to original object. Booo!", end="")
    else:
        print("Component with back reference is linked to the clone. Yay!", end="")

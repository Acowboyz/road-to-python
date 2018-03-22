def upper_attr(future_class_name, future_class_parents, future_class_attr):
    
    # covert the attribute name to capital except the name which starts with "__" 
    newAttr = {}
    
    for name, value in future_class_attr.items():
        if not name.startwith("__"):
                newAttr[name.upper()] = value

    return type(future_class_name, future_class_parents, newAttr)

class Foo(object):
    __metaclass__ = upper_attr
    bar = "bip"

print(hasattr(Foo, "bar"))
print(hasattr(Foo, "BAR"))

t = Foo()
print(t.BAR)
print(t.bar)

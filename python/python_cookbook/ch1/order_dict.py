from collections import OrderedDict

def iter(dic):
    for key in dic:
        print(key)

print("key inserted order: foo->bar->spam->grok")

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print("-"*50)
print("order dictionary:")
iter(d)

d = {}
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print("-"*50)
print("normal dictionary:")
iter(d)

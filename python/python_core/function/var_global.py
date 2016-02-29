global_str = 'foo'
def foo():
    local_str = 'bar'
    return global_str + local_str

print foo()

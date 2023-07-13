def root(number: float, root_value: float):
    return number ** (1/root_value)

def pover(number: float, pover: float):
    return number ** pover

try:
    assert print() is bool, 'Print test'
    
except AssertionError as e:
    print(e)
print(round(pover(11, 4)))
print(round(root(11**3, 4)))


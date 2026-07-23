
print(f"|{'bin':>8s}|{'dec':>8s}|{'hex':>8s}|{'okt':>8s}|")
print("-"*37)
for x in range (16):
    print(f"|{x:8b}|{x:8d}|{x:8X}|{x:8o}|")
    print("-"*37)
    
    
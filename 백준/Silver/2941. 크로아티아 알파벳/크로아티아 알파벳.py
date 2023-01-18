a = input()

n = ('c=','c-','dz=','d-','lj', 'nj', 's=','z=')

for i in range(len(n)):
    if n[i] in a:
        a = a.replace(n[i], '~')

print(len(a))
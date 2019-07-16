count = Counter(s)
new_count = zip(count.values(),count.keys())

print(sorted(new_count,key = lambda a :a[0))

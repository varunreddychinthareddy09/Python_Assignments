D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#union

dict_union = {}
for key in sorted(D1.keys()|D2.keys()):
    dict_union[key] = D1.get(key) or D2.get(key)
print(dict_union)

#intersection

dict_intersection = {}
for key in sorted(D1.keys() & D2.keys()):
    dict_intersection[key] = D1[key]
print(dict_intersection)

#dict1-dict2

dict_difference = {}
for key in sorted(D1.keys()-D2.keys()):
    dict_difference[key] = D1[key]
print(dict_difference)

#merging values of same keys 

dict_merged = {}
for key in sorted(D1.keys()|D2.keys()):
    dict_merged[key] = D1.get(key,0)+D2.get(key,0)
print(dict_merged)
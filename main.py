import json

def selection_sort(data, key):
    n = len(data)
    for i in range(n-1):
        m = data[i][key]
        p = i
        for j in range(i+1, n):
            if m > data[j][key]:
                m = data[j][key]
                p = j
        if p != i:
            t = data[i][key]
            data[i][key] = data[p][key]
            data[p][key] = t


data = json.load(open("valid_data.txt", encoding="windows-1251"))
selection_sort(data, 'height')

json.dump(data, open("result_sort.json", "w", encoding="windows-1251"), ensure_ascii=False, indent=5)
result = json.load(open("result_sort.json", encoding="windows-1251"))
print(result)

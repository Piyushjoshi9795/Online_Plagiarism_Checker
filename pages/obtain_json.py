# import json
#
# data = dict()
#
# with open("hash_value.txt", 'r') as f:
#     data = json.loads(f.read())
#     f.close()
#
# print(len(data))
#
# for k, v in data.items():
#     print(v)

orders = {
    'cappuccino': 54,
    'latte': 56,
    'espresso': 72,
    'americano': 48,
    'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)[:2]

for i in sort_orders:
    print(i[0], i[1])

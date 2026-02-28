#29. Get the top three items in a shop

d = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

top3 = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

for item, price in top3:
    print(item, price)
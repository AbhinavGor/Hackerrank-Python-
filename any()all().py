totalinputs,Numbers = int(raw_input()),raw_input().split()
print all([int(i)>0 for i in Numbers]) and any([j == j[::-1] for j in Numbers])
# Enter your code here. Read input from STDIN. Print output to STDOUT
vals = input()
val = vals.split()

poly = str(input())

polyf = poly.replace('x',str(vals[0]))

print(polyf)
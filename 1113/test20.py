x2 = lambda x : x * 2

num = [1,3,5,7,9]
lst = list( map(x2,num) )
print(lst)

x3 = lambda x : (x%2)==0
nums = [1,2,3,11,12,13,21,22,23]
lst = list( filter( x3,nums ) )
print(lst)
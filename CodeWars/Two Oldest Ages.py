'''
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].
The order of the numbers passed in could be any order. The array will always include at least 2 items.
For example:

twoOldestAges( [1, 2, 10, 8] ) // should return [8, 10]
'''


def two_oldest_ages(ages):
  a=int(max(ages))
  ages.remove(a)
  b=int(max(ages))
  ages.remove(b)
  c=[b,a]
  print(c)
  return(c)
  
#Testes
case1 = [1, 5, 87, 45, 8, 8] 
case2 = [6, 5, 83, 5, 3, 18] 
case3 = [10, 1]  

two_oldest_ages(case1) #deve retornar [45, 87]
two_oldest_ages(case2) #deve retornar [18, 83]
two_oldest_ages(case3) #deve retornar [1, 10]

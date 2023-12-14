def minimum(list1):
  ret = None
  for i in list1:
    if ret == None:
      ret = i
    elif i < ret:
      ret = i
  return ret

def maximum(list1):
  ret = None
  for i in list1:
    if ret == None:
      ret = i
    elif i > ret:
      ret = i
  return ret

def traceroo(func):
  def log(*args):
    print(func(*args))
    print("stores args in a list, returns a tuple packed with the fuctions running on the list before created")
  return log

def func1(n1,n2,n3):
  n_list = [n1,n2,n3]
  return (minimum(n_list),maximum(n_list),sum(n_list))

@traceroo
def func2(*args:int)->tuple:
  list1 = args
  return (minimum(list1),maximum(list1),sum(list1))

def list_primes(maxN):
  dictionary1 = {}
  rangen=[x for x in range(2,maxN+1,1)]
  for i in rangen:
    dictionary1[i] = None
  def find_minimum(d):
    list1=[]
    for i,j in d.items():
      if j == None: list1.append(i)
    return min(list1)

  while None in dictionary1.values():
    p = find_minimum(dictionary1)
    dictionary1[p] = True
    n = 2
    while p * n <= max(dictionary1.keys()):
      dictionary1[p*n] = False
      n+=1
  
  return_list = []
  for i,j in dictionary1.items():
      if j: return_list.append(i)
  return return_list
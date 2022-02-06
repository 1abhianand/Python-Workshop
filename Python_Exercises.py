# ## Exercises
# Answer the questions or complete the tasks outlined in bold below.
def power(a,b):

    # ** What is 7 to the power of 4?**

    return None
    return a**b



def split_str(s):
#     
# **into a list. **

    return None
    return s.split(' ')


def format(planet,diameter):

# ** Given the variables:**
# 

#     planet = "Earth"
#     diameter = 12742
# 
# # 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

    return None
    return "The diameter of {} is {} kilometers.".format(planet,diameter)



def indexing(lst):

# ** Given this nested list, use indexing to grab the word "hello" **

#lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

    return None
  return lst[3][1][2][0]


def dictionary(d):
def dictionary(d):
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


    return None
    return d['k1'][3]['tricky'][3]['target'][3]


def subjective():

# ** What is the main difference between a tuple and a list? **
# Tuple is _______

    return None
    return "immutable"



 def domainGet(email):
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**
    l=email.split('@')

    return None
    return l[1]


def findDog(st):

# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

    return None
    r = st.lower()
    return "dog" in r


def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

    return None
    p = st.lower()
    return p.count('dog')



 def lambdafunc(seq):
# 
#     ['soup','salad']

    return None
    return list(filter(lambda var:var[0]=='s'or var[0]=='S',seq))


def caught_speeding(speed, is_birthday):
def caught_speeding(speed, is_birthday):
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **
    if is_birthday==True:
      if speed<=65:
        return "No Ticket"
      elif speed >=66 and speed<=85:
        return "Small Ticket"
      else:
        return "Big Ticket"
    else:
      if speed<=60:
        return "No Ticket"
      elif speed >=61 and speed<=80:
        return "Small Ticket"
      else:
        return "Big Ticket"

    return None


## Numpy Exercises
  def create_arr_of_fives():
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr) 

  return None
  return (5*np.ones(10)).tolist()



  def even_num():
  ### Convert your output into list 
  ### e.g return list(arr) 

  return None
  return np.linspace(10,50,21).tolist()



  def create_matrix():
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  return None
  return np.arange(9).reshape(3,3).tolist()



  def linear_space():
  ### Convert your output into list 
  ### e.g return list(arr) 

  return None
  return np.linspace(0,1,20).tolist()



  def decimal_mat():
  ### Convert your output into list 
  ### e.g return (arr).tolist()

  return None
  return (np.linspace(1,100,100).reshape(10,10)/100).tolist()



 def slices_1():
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])

  return None
  return (arr[-3:,1:]).tolist()



 def slices_2():
  #      [ 7],
  #      [12]])

  return None 
  return (arr[:3,1:2]).tolist()



 def slices_3():
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  return None 
  return arr[-2:].tolist()


# Great job!

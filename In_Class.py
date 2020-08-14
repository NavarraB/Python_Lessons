#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('being a good person')


# In[4]:


print('Hello world')


# In[5]:


print('We can use single quotes')  # we can use all of them 4 type ' ' or " " or ''' ''' or """ """ for strings
print("or double quotes")          # print() is a function.
print('''or triple quotes''')      # we use string type data for texts
print("""or triple-double quotes""")


# In[6]:


print('no pain')
print()  # this is the empty-line. we use for empty line print().
print('no gain')


# In[8]:


print('3.14')  # this is string data type str
print(3)       # this is integer data type (signed integer) int
print(3.14)    # this is floating data type (floating point) float  we use . for decimal not ,


# In[9]:


print('PEP8 Rules')  # This is Python Enhancement Proposal. Rules for standardization. 
                     # Limit all lines to a maximum of 79 characters.
                     # No whistespace inside () [] {}
                     # No whitespace before ( 
                     # No whitespace before , ; :
                     # Avoid to whitespace anywhere. it is usually invisible.
                     # Always surround a single space on either side of = + - > is and or .......


# In[10]:


print('docstring')  # we use docstrings for see the functions comments/rules/options
                    # we call docstring with print(functionname.__doc__) with two _ (underline)


# In[11]:


def new_func() : # we use def for create a function
                 # we add docstring with """ """ (triple-double quotes)
        """ It's a docstrings of new_func."""
print(new_func.__doc__)  # we call docstring of new_func()


# In[12]:


print(print.__doc__)  # we call docstring of print() func.


# In[17]:


variable_name_str = 'naming variable'  # we can create variable. we have to use lowercase and use underline only.
blue_line = 'blue'                     # we can't use spaces in variable names.
holocaust = 'song'                     # try to limit with 3 words.
print(variable_name_str)
print(blue_line)
print(holocaust)


# In[18]:


print('string for text 345')  # str
print(23)                     # int
print(-3.14)                  # float
print(2+5j)                   # complex
print(True)                   # bool


# In[19]:


a = 'class'
print(a)
print(type(a))
b = 12
print(b)
print(type(b))
c = 54.85
print(c)
print(type(c))
d = 12.6j
print(d)
print(type(d))
e = False
print(e)
print(type(e))


# In[20]:


a, b, c, d, e = 'pulp fiction', 34, -1.2, 1+78j, True
print(a, b, c, d, e) 
print(type(a), type(b), type(c), type(d), type(e))


# In[21]:


first_number = 14
second_number = 6
third_number = 34
first_number = third_number
third_number = second_number
second_number = 156
print(first_number, second_number, third_number, sep='+')
print('total=', first_number+second_number+third_number)
print('total' + 'number')
print('total', 'number')
print('total number of these numbers \na.12 \nb.16 \n=28')


# In[22]:


a = 28
print(a)
print(type(a))
b = str(a)
print(b)
print(type(b))


# In[23]:


a = 3
b = float(a)
print(b)


# In[24]:


a = 3
a = float(a)
print(a)
print(type(a))
a = int(a)
print(a)
print(type(a))
a = str(a)
print(a)
print(type(a))


# In[29]:


a = 3.14
print(a)
a = int(a)
print(a)


# In[30]:


a = 3
a = bool(a)
print(a)
b = 0
b = bool(b)
print(b)


# In[31]:


a = 3
a = complex(a)
print(a)


# In[32]:


print(2 + 1)  # int+int=int
print(7 - 8)


# In[33]:


print(2 + 1.0)  # int+float=float
print(2 - 0.15)  # int-float=float


# In[34]:


print(46 / 23)  #division gives float
print(46 / 20)


# In[35]:


print(8 * 9)
print(8 * 2.1)


# In[36]:


print(81 // 10)  # 8.1 but // gives only integer part of division     floor division


# In[37]:


print(9 % 2)  # it gives remainder of division. It means 9 is odd.    modulus
print(8 % 2)  # it means 8 is even.


# In[38]:


print(3 ** 2)  # means 3*3
print(4 ** 3)  # means 4*4*4


# In[39]:


print(49 ** 0.5)  # it gives float


# In[40]:


print((7 + 9) / 2 ** 2 - 1)  # priority---- (parentheses)-(power(**))-(unary minus)-(*,/)-(+,-)


# In[41]:


print('blue', end='')  # default value is end='\n' so it goes new line every time. 
print('purple', end=' ')
print('yellow', end='\n')
print('black')


# In[42]:


x = 5
x /= 5
print(x)
x *= 3
print(x)
x = int(x)
print(x)
x = 5
print(x)
x -= 2
print(x)
x += 2
print('we make x again as a:', x)


# In[43]:


print('If we use t with back-slash it will give tab space \tlike this')


# In[44]:


print('b with back-slash ignores the before one likeP\b this')


# In[46]:


print ('I\'am studying python')  # \ before ' ignores the error -- \ is invisible before the '


# In[47]:


print('\\')  # first \ invisible


# In[50]:


a = (1 + 3) ** (2 ** (1 * 2 / 2) / 2)  # if there is a division (/) result has to be float
print(a)


# In[49]:


a = 3
b = 4
c = (3 ** 2 + 4 ** 2) ** 0.5
print(c)


# In[1]:


logic = True or not False and False and True or not False or True or not True  # 1.not 2.and 3.or
        # True or True and False and True or True or True or False
        # True or False or True or True or False
print(logic)


# In[10]:


print(2 and 3)  # and look for False, or look for True
print(3 and 2)  # always take right side when both of them true ---- take left both of them false   for and statements
print(3 or 2)   # always take left side when both of them true ----take right both of them false    for or statements
print(0 and 2)  # zero of any numeric type (0, 0.0, 0.0j) is false
print(2 and 0)
print([] and 2)  # empty sequences and collections ''()[]{}(0) are false
print(None and 5)  # None is false
print(2 and 'navarra')  # others are true
print(() or 5)


# In[7]:


city = 'abcdefg'
print(city[:])       # print(city) from 0                              # string[:]        full copy
print(city[1:])      # print(city) from 1                              # string[start:]   start from
print(city[:1])      # just first word                                 
print(city[:2])      # print first and second words                    # string[:stop]    stop this point 
print(city[::1])     # 1 step from 0                              
print(city[::2])     # 2 step from 0                                   # string[::step]   write step step, start from given
print(city[1::2])    # 2 step from 1
print(city[::-3])    # negative index -7/-1 write g,d,a(-1,-4-7)
print(city[-3:])     # negative index start from -3 , a=-7 , g=-1
print(city[:-4])     # negative index write until -4 


# In[11]:


fruit = 'orange'  # 0 is o, r is 1, 2 is a ......
print(fruit)
print(fruit[1])
print(fruit[2:5])
print(fruit[-3])
print(fruit[3:])
print(fruit[:2])
print(fruit[2::3])
print(len(fruit))  # it gives lenght ot the word


# In[15]:


print('apple' + 'banana')
print(3 * 'apple')
print('apple ' + 'banana')
print(3 * 'apple ')
fruit = 'apple'
fruit += 'banana'
print(fruit)
fruit *= 3
print(fruit)
print(* 'apple')  # * seperate string characters with a space


# In[20]:


# we use % for formatting strings
# %s, %d, %f
phrase = 'I have %d %s and %.1f brothers' % (4, 'children', 5)
print(phrase)


# In[22]:


fruit = input('which fruit do you want? ')
amount = input('how many kgs do you want? ')
pocket = input('how many pockets sugar? ')
print('%(amount).2f kg of %(fruit)s and %(pocket)d pocket' % {'amount':float(amount), 'fruit':fruit, 'pocket':int(pocket)})


# In[24]:


sentence = 'actually i never eat pork'
print('%.12s' % sentence)  # 12 characters of sentence


# In[42]:


fruit = 'Orange'                 # str.format()
amount = 3
print('We bought {} kg {} from grocery.'.format(amount, fruit.upper()))


# In[29]:


print('{} is the biggest {} in the {}'.format('Turkey', 'country', 'Europe'))
print('{0} is the biggest {2} in the {1}'.format('Turkey', 'World', 'country'))
print('{country} is the biggest {word} in the {continental}'.format(country = 'Turkey', continental = 'Asia', word = 'country'))


# In[30]:


text = '{:.2f} {:.1f} {:.2f}'.format(3.1463, 5.367, 7.324324)
print(text)


# In[31]:


text = '{:.2s} {:.1s} {:.3s}'.format('3.1463', '5.367', 'abcdef')
print(text)


# In[32]:


text1 = '{:>10}'.format('test')   # test 4 character. There are 6 indentations. total 10.
print(text1)


# In[33]:


text1 = "!{:^10}!".format('test')    # test 4 character. There are 3 indentations left side and 3 indentations right side. 
print(text1)


# In[37]:


print('<==={:x>30}===>'.format(''))
print('<==={:^30}===>'.format('Python'))
print('<==={:x<30}===>'.format(''))


# In[40]:


name = input('What is your name? ')
job = input('What do you do? ')
age = input('How old are you? ')
print(f'My name is {name}. I am {job}. I am {age} years old.')


# In[41]:


name = 'MARIAM'
print(f'My name is {name.capitalize()}.')


# In[48]:


email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9))      # startswith is starting point exact point of index
print(email.endswith("-", 1, 32))   # endswith is ending point it needs starting point with exact+1 point of index
print(email.startswith('c', 10))    
print(email.endswith('c', 5, 11))
print(email.endswith('s'))


# In[51]:


print('ahmet'.startswith(('a', 'h'), 2))
print('ahmet'.startswith(('a', 'h', 'm'), 2))
print('ahmet'.startswith(('a', 'h'), 1))


# In[55]:


sentence = 'it will be GOOD!'
print(sentence.upper())               # all words are uppercase
print(sentence.lower())               # all words are lowercase
print(sentence.capitalize())          # first character of first word is uppercase others are lowercase
print(sentence.swapcase())            # vice versa upper to lower, lower to upper
print(sentence.title())               # first characters of all words are uppercase others are lowercase
print(sentence.replace('l', 'r'))     # replace the all l to r
print(sentence.replace('l', 'r', 1))  # replace just first l to r
print(sentence)                       


# In[56]:


text = 'the better the family, the better the society'
print(text.title().swapcase())


# In[57]:


text = 'S0d0me and G0m0re'
text = text.replace('0', 'o')
print(text)


# In[58]:


palabra = '    go outside and walk    '
print(palabra)
print(palabra.strip())
print(palabra.strip().lstrip('g'))
print(palabra.rstrip().rstrip('kal'))


# In[73]:


text = 'tyou can learn almost everything in pre-classz'
print(text.strip('zt').upper())
print(text.strip('youzt' [3:]))
print(text.strip('zt' [-1]))


# In[71]:


text = 'In God wee Trust'
a = text.index('wee')
print(text.replace('ee', 'e'))
print(a)


# In[74]:


year = int(input('Give me a year: '))
leap = bool((not year % 4) and (year % 100)) or (not year % 400)
print(((leap) * '{} is a leap year'.format(year)) or (not leap) * '{} is not a leap year'.format(year))


# In[1]:


# There are 4 collection data types in the Python.
# List, Tuple, Set, Dictionary

# List : is a collection which is ordered and changeable. In python lists are written with square brackets [].
country = ['Turkey', 'Spain', 'Mexico', 'Argentina', 'Venezuela']
print(country)


# In[2]:


string_1 = 'I quit smoking'
new_list_1 = list(string_1)        # we use list() to create list type and it gives multi element list. iterable.
print(new_list_1)
new_list_2 = [string_1]            # we use [] to create list type and it gives single element list
print(new_list_2)


# In[3]:


text_1 = "2020's hard"
print(list(text_1))
print([text_1])
text_2 = 2, 3, 4, 5
print(list(text_2))
print([text_2])
xyz = []
print(xyz)
abc = list()
print(abc)


# In[4]:


emp_list = []
emp_list.append(1)
emp_list.append(2)
emp_list.append(3)
emp_list.append(4)
print(emp_list)


# In[6]:


numbers = [1, 3, 5, 7]
numbers.insert(4, 9)
print(numbers)


# In[7]:


numbers2 = ['1', '4', '7', '9']
numbers2.remove('7')
print(numbers2)


# In[8]:


list_1 = ['Ankara', 'İstanbul', 'Bolu', 'İstanbul', 'Bolu', 'Muğla']
list_1.remove('Bolu')
print(list_1)
list_1.remove('Bolu')
print(list_1)


# In[9]:


colors = ['red', 'blue', 'green', 'white1', 'black', 'white0']
colors.sort()
print(colors)
colors.reverse()
print(colors)


# In[10]:


mixed_list = [1, 'A', 3.14]
print(mixed_list)


# In[11]:


empty_list = []
print(empty_list)
empty_list.append(12)       # we attend value in list with .append()
empty_list.append('abc')
print(empty_list)


# In[12]:


list_1 = ['Ankara', 'İstanbul', 'Bolu']
print(list_1)
list_1.append('İzmir')    # it is added end of list
print(list_1)


# In[13]:


print(list_1)
list_1.insert(2, 'Muğla')  # it is added to 2.sequence (0,1,2,3,4...)
print(list_1)


# In[14]:


print(list_1)
list_1.sort()   # it lists the items in alphabetical order
print(list_1)


# In[15]:


print(list_1)
list_1.remove('Muğla')   # it removes Muğla from the list
print(list_1)


# In[16]:


print(list_1)
list_1[3] = 'Kocaeli'   # we assign Kocaeli to 3.
print(list_1)


# In[18]:


list_1 = ['Ankara', 'Bolu', 'Muğla', 'Kocaeli', 'İstanbul', 'İzmir']
print(list_1)
del list_1[0:4]  # we delete 0-1-2-3
print(list_1)


# In[20]:


letters = ['a', 'b', 'c']
print(letters)
#copy
letters_same = letters.copy()
print(letters_same)
# add
letters.append('d')
print(letters)
letters.insert(0, 'e')
print(letters)
# remove
letters.pop()
print(letters)
letters.pop(0)
print(letters)
letters.remove('b')
print(letters)
del letters[0]
print(letters)
letters.clear()
print(letters)


# In[21]:


palabras = ['a', 'h', 'c', 'f', 'b']
print(palabras.index('h'))
print(palabras.count('d'))


# In[22]:


colors = ['red', 'blue', 'green', 'white', 'black', 'white']
print(colors)
print(colors[2])
print(colors.index('black'))
print(colors.index('white', 4))
print(colors.count('white'))


# In[23]:


odd_numbers = list(range(1,10,2))
print(odd_numbers)
numbers = list(range(10))
print(numbers[1::2])


# In[24]:


city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
city_list = []
print(city_list)
city_list.append(city)
print(city_list)
print(city_list[0])
print(city_list[0][2])
print(city_list[0][2][3])
city_list.append('Europe')
print(city_list)


# In[25]:


numbers = list(range(11))
print(numbers)
print(numbers[0:11:2])
print(numbers[:])
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)


# In[26]:


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[3:])
print(animals[:5])
print(animals[::2])


# In[27]:


print([[12, 34, 56]][0])
print([[12, 34, 56]][-1])


# In[28]:


odd_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_no[7:3:-1])
print(odd_no[2:6:-1])
print(1 in odd_no)
print(11 in odd_no)
print(1 not in odd_no)
numbers = odd_no.copy()
print(numbers)


# In[29]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[30]:


colors = ['red', 'blue', 'green', 'white', 'black', 'white']
colors.extend('yellow')
print(colors)


# In[33]:


# tuples are faster than list.
# we use tuples for unchanged data. Tuples are immutable. indexable.
# normal parantheses () are used for tuples. Round brackets and comma.
# tuples are fast, they work rapidly. it is faster than list.


# In[32]:


empty_tuple = ()
print(type(empty_tuple))
tuple_1 = ('a')
print(type(tuple_1))
tuple_2 = ('a',)         # we have to use comma for tuple type.
print(type(tuple_2))


# In[34]:


planets = 'mercury', 'jupiter', 'saturn'
aer = 1, 2, 3, 4
print(aer)
print(type(aer))
print(planets)
print(type(planets))
empty_tuple_1 = tuple('alps')   # iterable
print(empty_tuple_1)
print(type(empty_tuple_1))
abc = ('alps')                  # it is str.
abc = (abc,)
print(abc)
print(type(abc))
zaq = (1,)
print(zaq)
print(zaq[0])
print(type(zaq))


# In[35]:


tuple_lesson = tuple(range(1, 11))
print(tuple_lesson)
print(type(tuple_lesson))
number = (range(1, 11))
print(number)
print(type(number))


# In[36]:


mix_value_tuple = (0, 'bird', 3.14, True)
print(mix_value_tuple)
print(len(mix_value_tuple))
print(mix_value_tuple[1:3])
print(mix_value_tuple[1])                  # allows indexing like lists.
mix_value_tuple[1] = 'fish'                # we cant assign new value


# In[38]:


mix_tuple = ('11', 11, [2, 'two', ('six', 6)], (5, 'fair'))
print(mix_tuple[-1], type(mix_tuple[-1]))
print(mix_tuple[-1][-1])
print(mix_tuple[3][1])
print(mix_tuple[2][2][0])
print(mix_tuple[2])


# In[39]:


x = ('apple', 'banana', 'cherry')
print(x)
y = list(x)             #we changed type tuple to list to change values.
y[1] = 'kiwi'
y.append('melon')
x = tuple(y)
print(x)


# In[1]:


tuple2 = ('a', 'b', 'c')
del tuple2                   # we cant remove item from tuple, but we can delete tuple completely.
print(tuple2)


# In[2]:


tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


# In[3]:


tuple4 = (1, 4, 7, 3, 8, 5, 7, 9, 0, 21, 56, 67, 1, 7, 9)
print(tuple4.count(2))
print(tuple4.count(7))
print(tuple4.index(7))
print(tuple4.index(7, 3))


# In[4]:


thistuple = tuple(('apple', 'banana', 'cherry'))   # one parenthese gives error
print(thistuple, type(thistuple))
thistuple2 = tuple('red')
print(thistuple2, type(thistuple2))
thistuple3 = 1, 2, 3
print(thistuple3, type(thistuple3))
thistuple4 = tuple('a', 'b,' 'c')         # one parenthese gives error we have to use double.
print(thistuple4, type(thistuple4)) 


# In[5]:


tuple10 = 123,
print(tuple10, type(tuple10))


# In[8]:


tup = (1, 3, 5, 7, 9)
for x in tup:
    print(x)
print()
print(1 in tup)
print(2 not in tup)
print(len(tup))


# In[9]:


# Dictionary is a collection which is unordered, changeable and indexed. Nu duplicate members.
# Store item pairs. key and value. Dictionaries are enclosed by curly braces {}. seperated by comma , . 
# key : value.


# In[13]:


first_dict = {'team1' : 'Liverpool', 'team2' : 'Chelsea', 3 : 'Arsenal'}
print(first_dict)
print(type(first_dict))
second_dict = dict(team='Liverpool', num1=12, bool1=True, list1=[1, 'a'], tuple1=(12, 'ab'))
print(second_dict)
print(type(second_dict))
empty_dict = {}
print(empty_dict)
print(type(empty_dict))
empty_dict2 = dict()
print(empty_dict2)
print(type(empty_dict2))


# In[14]:


my_dict = {'key1' : 'value1',
           'key2' : 'value2',
           'key3' : 'value3'}
print(my_dict)
print(my_dict['key2'])              # unordered and indexed
my_dict['key4'] = 'value0'          # changeable
print(my_dict)
my_dict['key4'] = 'value4'          # changeable
print(my_dict)
print(my_dict['key1'])              # indexable
print(my_dict.get('key1'))
my_2dict = my_dict.copy()
print(my_2dict)


# In[26]:


print(my_dict.items())
print()
print(my_dict.keys())
print()
print(my_dict.values())


# In[17]:


fam = {1 : 'Torres', (1, 2) : 'Drogba', 'name3' : 'Anelka'}
print(fam)
fam['name4'] = 'Lampard'
print(fam)
fam.update({5 : 'Gerrard'})
print(fam)
fam.update({7 : 'Ballack', '6' : 'Diego'})
print(fam)
fam.update({7 : 'Ballack', '6' : 'Cole'})
print(fam)
fam.update({6 : 'Eto'})
print(fam)
del fam[6]
print(fam)
del (fam['6'], fam[7])
print(fam)


# In[24]:


fam1 = dict(team1 = 'Chelsea', team2 = 'Liverpool', team3 = 'Arsenal')
print(fam1)
print(fam1.keys())
print(list(fam1.keys()))
print(list(fam1.keys())[0:2])
print(list(fam1.values()))
print(list(fam1.items()))
print('team1' in fam1)
print(12 not in fam1)
print('Arsenal' in fam1.values())


# In[27]:


second_dict = dict(team1='Liverpool', num1=12, bool1=True, list1=[1, 'a'], tuple1=(12, 'ab'))
print(second_dict)
second_dict.update({'num1' : 3.14})        # update new value / change the value
print(second_dict)
del second_dict['tuple1']                  # remove
print(second_dict)
second_dict.pop('list1')
print(second_dict)
second_dict.popitem()                      # it removes last item
print(second_dict)
second_dict['tuple2'] = ('qw', 34)         # add
print(second_dict)
print('num1' in second_dict)
print('num1' not in second_dict)
print(len(second_dict))
second_dict.clear()
print(second_dict)
del second_dict
print(second_dict)


# In[28]:


nested_dict = {
            'students' : 
               {'1. Class' : 
                {'1A' : {'Amount' : 23, 'Gender' : [[12, 'Female'], [11, 'Male']]},
                '1B': {'Amount' : 24, 'Gender' : [[11, 'Female'], [13, 'Male']]}
                },
               '2. Class' : 
                {'2A' : {'Amount' : 12, 'Gender' : [[7, 'Female'], [5, 'Male']]},
                '2B' : {'Amount' : 13, 'Gender' : [[6, 'Female'], [7, 'Male']]}
                }
                },
              'teachers' : 
               {'1. Class' :
               {'Amount' : 3, 'Gender' : [[2, 'Female'], [1, 'Male']]},
               '2. Class' :
               {'Amount' : 2, 'Gender' : [[1, 'Female'], [1, 'Male']]}
               }                  
              }
print(nested_dict)
print()
print(nested_dict['students']['2. Class'])
print()
print(list(nested_dict['students']['2. Class']))           # default ==> .keys
print()
print(list(nested_dict['students']['2. Class'].items()))


# In[29]:


friends = {'friend1' : {'first' : 'Sue', 'last' : 'Bold'},
           'friend2' : {'first' : 'Steve', 'last' : 'Smith'}
          }
print(friends)
print()
mix = {'friends' : {'friend1' : {'first' : 'Sue', 'last' : 'Bold'},
                    'friend2' : {'first' : 'Steve', 'last' : 'Smith'}
                   },
       'fam' : {'team1' : {'first' : 'Chel', 'last' : 'Sea'},
                'team2' : {'first' : 'Liver', 'last' : 'Pool'}
               }
      }
print(mix)
print(list(list(mix['friends'].values())[0].values()))
print(list(list(mix['fam'].values())[1].values())[0], list(list(mix['fam'].values())[1].values())[1].lower(), sep='')


# In[30]:


my_dict = {'key1' : 'value1',
           'key2' : 'value2',
           'key3' : 'value3'}
for x in my_dict:
    print(x)
print()
for y in my_dict.values():
    print(y)
print()
for z in my_dict.items():
    print(z)


# In[31]:


# Set is a collection type. unordered and unindexed. No duplicate members. Without insertion order but sorted order.
# Written with curly brackets.
# Sets are unordered so you can not be sure in which order the items will appear.
first_set = {'Turkey', 'Spain', 'France', False, 34, 3.14}
print(first_set)
print()
second_set = {34, 21, 23, 4, 67, 78765, 20, 12, 543,}
print(second_set)
print(second_set)
print()
empty_set = set()
print(empty_set)
print()
third_set = set('collection')
print(third_set)
print()
list12 = [34, 'istanbul', False, 3.14, False]
fourth_set = set(list12)
print(fourth_set)
print(type(fourth_set))
print(list12)
print(type(list12))


# In[40]:


letter = 'a b c d'.split()
print(set(letter))
letters2 = 'abcd'
print(set(letters2))
a = {'abcd'}
print(a)


# In[35]:


a = set('philadelphia')
b = set('dolphin')
print(a)
print(b)


# In[38]:


date_t = set('04/07/2020')
date_t1 = {'04/07/2020'}
print(date_t)
print(date_t1)


# In[41]:


given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]
out_list = set(given_list)
print(out_list)


# In[46]:


a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)
print()
print(a - b)
print(a.difference(b))
print()
print(a | b)
print(a.union(b))
print(len(a.union(b)))
print()
print(a & b)
print(a.intersection(b))
print()
print(a ^ b)           # a | b - a & b
print(a.symmetric_difference(b))


# In[42]:


usa = set('washington')
print(usa)
newzea = set('wellington')
print(newzea)
print(usa & newzea)
print(usa | newzea)
print(usa - newzea)
print(newzea - usa)


# In[47]:


# remove, discard, pop  # remove can give an error if value has not created. but discard doesnt give an error.
a.remove('c')
print(a)
a.discard('q')
print(a)
a.pop()                 # we cant know which one will be removed because it is unordered.
print(a)
# add, update           # we cant change items but we can add items.
b.add('yz')
print(b)
b.add(2)
print(b)
b.update('qw')
print(b)
print()
print('c' in a)
print('y' in b)
print('c' not in a)
b.clear()
print(b)
del a
print(a)


# In[48]:


thisset = {'apple', 'banana', 'cherry', 'melon'}
for x in thisset:
    print(x)          # output is unordered.
print()
print('kiwi' in thisset)


# In[50]:


sales = {
    'cost_value' : 31.87,
    'sell_value' : 45.00,
    'inventory' : 1000
}
the_profit = (sales['sell_value'] - sales['cost_value']) * sales['inventory']
print(the_profit)
the_profit = float('{:.1f}'.format(the_profit))
print(type(the_profit))
print(the_profit)
print('The total profit is $', int(the_profit), sep = '')


# In[53]:


right_hand = set()
right_hand.update('yhnujmıköolçpşğiü')
left_hand = set()
left_hand.update('qazwsxedcrfvtgb')
word = input('Give me a word: ')
given_word = set(word)
print(bool((left_hand & given_word) and (right_hand & given_word)))


# In[54]:


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
numbers.sort()
print(numbers)
numbers2 = set(numbers)
numbers2 = list(numbers2)
numbers2.sort()
print(numbers2)
a = len(numbers2)
print(a)
zz = list(range(a))
print(zz)
list_1 = [numbers.count(numbers2[zz[0]]), numbers.count(numbers2[zz[1]]), numbers.count(numbers2[zz[2]]),           numbers.count(numbers2[zz[3]]), numbers.count(numbers2[zz[4]]), numbers.count(numbers2[zz[5]])]
print(list_1)
list_2 = list_1.copy()
list_2.sort(reverse = True)
print(list_2)
repeat = list_2[0]
print(repeat)
print(list_1.index(repeat))
b = list_1.index(repeat)
print(numbers2[b])
freq_num = numbers2[b]
print('The most frequent number is {} and it was {} times repeated.'.format(freq_num, repeat))


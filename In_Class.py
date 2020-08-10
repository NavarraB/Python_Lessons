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


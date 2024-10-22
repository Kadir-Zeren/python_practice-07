city_list = [['New York', 'London', 'Istanbul', 'Seoul' , 'Sydney' ]]
print(city_list[0]) # access to first and only element

city_list = [ 'New York' , 'London' , 'Istanbul', 'Seoul' , 'Sydney' ]
print(city_list[0][2])

city_list = [['New York', 'London', 'Istanbul', 'Seoul', 'Sydney' ]]
print(city_list[0][2][3])

even_numbers = [2, 4, 6, 8, 10, 12, 14]
print(even_numbers[2:5])

a = range(1,11)
type(a)
print(a)
range(1, 11)
list(a)
list(range(2,15,2))

odd_numbers = list(range(11))
print(odd_numbers)
print(odd_numbers[1:11:2])

animals = ['elephant' , 'bear' , 'fox' , 'wolf' , 'rabbit' , 'deer' , 'giraffe']
print(animals[: ]) # all elements of the list

animals = ['elephant' , 'bear' , 'fox' , 'wolf' , 'rabbit', 'deer' , 'giraffe']
print(animals[3:])

animals = ['elephant', 'bear' , 'fox' , 'wolf' , 'rabbit' , 'deer' , 'giraffe' ]
print(animals[:5])

mix_list = [1, [1, "one", 2, "two", 3, "three"], 4]
print(mix_list[1][1:6:2])

city = ['New York', 'London', 'Istanbul' , 'Seoul' , 'Sydney' ]
print(city[-4])

reef = ['swordfish' , 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus' ]
print(reef[ ::- 2])

tuple_1 = ('h', 'a', 'p', 'p' , 'y' )
word = 'happy'  
tuple_2 = tuple(word)
print(tuple_1)
print(tuple_2)

my_tuple = ("Solar")
print(my_tuple, type(my_tuple), sep="\n")

solar = "Earth", "Venus", "Uranus"
print(solar, type(solar), sep="\n")

my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)
my_list = list(my_tuple)
print(type(my_list), my_list)

my_list = [1, 4, 3, 4, 5, 6, 7, 4]
my_tuple = tuple(my_list)
print(type(my_tuple), my_tuple)

mountain = tuple('Alps')
print(mountain)

tuple_1 = 'h', 'a', 'p', 'p', 'y'
tuple_2 = 1, 3, 5
print(tuple_1)
print(type(tuple_1))
print(tuple_2)

number = tuple(range(1,11))
print(number, type(number), sep="\n")

even_no = (0, 2, 4)
print(even_no[0])
print(even_no[1])
print(even_no[2])

city_list = ['Tokyo' , 'Istanbul' , 'Moskow', 'Dublin' ]
city_tuple = tuple(city_list)

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
str_six = mix_tuple [2] [2][0]
print(str_six)

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
str_six = mix_tuple[2] [1:3]
print(str_six, type(str_six), sep="\n")

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
last = mix_tuple[-1]
print(last, type(last), sep="\n")

mix_tuple = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
option_1 = mix_tuple[3][1]
option_2 = mix_tuple[-1] [1]
print(option_1, option_2, sep = "\n")  

a = [1,2,3]
b = (1,2,3)
import sys
sys. getsizeof(a)
sys. getsizeof(b)

print('15.000$' .endswith('$'))

phrase = 'What is Soul?'
print(phrase. upper().swapcase())

phrase = 'What is Soul?'
print(phrase. title())

phrase = 'What is Soul?'
new_phrase = phrase. replace('Soul', 'feeliNGS' )
print(new_phrase. title())

s = 'Eggs, spam and eggs'
print (s. count ( ' eggs' ) )

s = 'Spam, eggs, spam and eggs.'
print (s. find('egs' ))

S = 'Eggs, spam and eggs. '
print (s. strip( 'Es. '))
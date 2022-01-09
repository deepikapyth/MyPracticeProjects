"""#All Modules
import math
import statistics
import json


#All Variables



#All Functions"""
#####################################
#LIST CREATE
####################################
def create_list():
    List_init = []
    number_ele_List = int(input("please enter number elements to be available in list"))  
    for element in range(number_ele_List):
        element_n = int(input("please enter the element: "))
        List_init.append(element_n)
    return List_init


def append_list(List):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    List.append(element_to_be_inserted)
    return List

def pop_list(List):
    #Two different types of pop operations
    element_to_be_pop = int(input("Please enter the index element to be pop "))
    List.pop(element_to_be_pop)
    return List
    
def len_list(List):
    return len(List)

def extend(List):
    NEWlist=[]
    n=int(input("enter no.of elemts:"))
    for i in range (1,n+1):
        x=int(input("enter the elemt"))
        NEWlist.append(x)
        List.extend(NEWlist)
    return List


def sort(List):
    List.sort()
    return List


##def remove(List):
   # List.remove()
    #return List

def min_list(List):
    return List
    
def max_list(List):
    return List

def count_list(List):
    y=int(input("enter the elemt to count"))
    z=List.count(y)
    return z


"""def multiply(List):
    print("multiply of two numbers")
    a=int(input("enter 1st element:"))
    b=int(input("enter 2nd element:"))
    return a*b"""
    
def multiply(List):
    result=1
    for i in (List):
        result=result*i
    return result

def reverse(List):
    return List[::-1]

def insert(List):
        x=int(input("enter the element to at index"))
        y=int(input("enter the element to be inserted"))
        z=List.insert(x,y)
        return List

def slice(List):
    x=int(input("enter the starting of element"))
    y=int(input("enter the ending to at index"))
    #z=int(input("enter the step of elemtn"))
    a=List.slice(x,y)
    return List
    
def remove(List):
    x=int(input("enter the number to remove:"))
    y=List.remove(x)
    return List

def conc(List):
    x=int(input("enter the element to concatinate"))
    y=List.concatinate(x)
    return List
###############################################################
#set operations
##############################################################
def create_set():
    s1=set()
    n=int(input("enter number of elements in set_1:"))
    for i in range(n):
        b=int(input("enter the set_1 element:"))
        s1.add(b)
    return s1

def update_set():
    s2=set()
    n=int(input("enter number of elements in set_2:"))
    for i in range(n):
        b=int(input("enter the set_2 element:"))
        s2.add(b)
        set.update(s2)
    return s2

def union():
    s3=s1.union(s2)
    return s3

def intersection():
    s4=s1.intersection(s2)
    return s4
    
def difference():
    s5=s1.difference(s2)
    return s5

def symmetric_difference():
    s6=s1.symmetric_difference(s2)
    return s6


##############################################################################
#DICTIONARY FUNCTION
#############################################################################
def dictionary_create():
    dict_init={}
    n=int(input("number of keyvalue pairs need to be inserted"))
    for i in range(n):
        a=int(input("enter the key vales:"))
        b=int(input("enter the value pairs :"))
        dict_init[a]=b
    return dict_init

def pop(dict_init):
    n=int(input("enter the pop number"))
    x=dict_init.pop(n)
    return dict_init
    

def clear(dict_init):
    x=dict_init.clear()
    return dict_init      


def copy(dict_init):
    x=dict_init.copy()
    return dict_init


def get(dict_init):
    n=int(input("enter the key you want to get value"))
    x=dict_init.get(n)
    return x

def values(dict_init):
    n=int(input("enter the value to get key"))
    x=dict_init.values(n)
    return x



#############################################################
#TUPLE FUNCTION
#############################################################
def tuple_create():
    x=tuple(map(int,input().split(',')))
    return x

def index(x):
    y=int(input("enter the element to find index position"))
    z=x.index(y)
    return z
    
def count(x):
    y=int(input("enter the elemt to count"))
    z=x.count(y)
    return z

def new_tuple():
    nt=()
    x=tuple(map(int,input().split(',')))
    y=nt.append(x)
    return y
    


print("Welcome to Data structure calculator")

print("Please select any operation to proceed \n1.List \n2.Tuple \n3.Set \n4.dictionary..... ")

data_input = int(input("please enter a number between 1 and 4 "))

if data_input == 1:
                 print("Welcome to List operations ")
                 print("Create a List for proceeding List Operations")
                 List_main = create_list()
                 print("The created list is ", List_main)
                 print("Please select any one List operation to proceed (Any number between 1-15)")
                 print("1. Append \n 2. pop \n3.len \n 4.extend \n 5.insert \n 6.remove \n 7.slice \n 8.reverse \n 9.min()&max() \n 10.count \n 11.multiply \n 12.index \n 13.sort \n 14.clear \n 15.concatenate \n16.Max()......")

                 List_operation_input = int(input("please enter any one number ..."))

                 if List_operation_input == 1:
                                        output_append = append_list(List_main)
                                        print("The output after append operations is ", output_append)
                 elif List_operation_input == 3:
                                        output_len = len_list(List_main)
                                        print("The output after len operations is ", output_len)
                 elif List_operation_input ==2:
                                        output_pop = pop_list(List_main)
                                        print("After pop of element ", output_pop)
                 elif List_operation_input ==4:
                                        output_extend = extend(List_main)
                                        print("After extend of element ", output_extend)
                 elif List_operation_input ==13:
                                        output_sort = sort(List_main)
                                        print("After sorting of element ", output_sort)
                 elif List_operation_input ==9:
                                        output_min = min(List_main)
                                        print("This is the MIN(Least element):", output_min)
                 elif List_operation_input ==16:
                                        output_max = max(List_main)
                                        print("This is the MAX(Least element):", output_max)

                 elif List_operation_input ==10:
                                        output_count = count_list(List_main)
                                        print("TOtal number of elements in the List are:", output_count)

                 elif List_operation_input ==11:
                                        output_multiply = multiply(List_main)
                                        print("TOtal number of elements in the List are:", output_multiply)

                 elif List_operation_input ==8:
                                        output_reverse = reverse(List_main)
                                        print("reverse of List List are:", output_reverse)
                 elif List_operation_input ==5:
                                        output_insert = insert(List_main)
                                        print("After inserting element  List are:", output_insert)
                 elif List_operation_input ==5:
                                        output_insert = insert(List_main)
                                        print("After inserting element  List are:", output_insert)
                 elif List_operation_input ==7:
                                        output_slice = slice(List_main)
                                        print("After inserting element  List are:", output_slice)

                 elif List_operation_input ==6:
                                        output_remove = remove(List_main)
                                        print("After removing element  List are:", output_remove)

                 elif List_operation_input ==15:
                                        output_conc = conc(List_main)
                                        print("After inserting element  List are:", output_conc)


if data_input == 3:
                 print("Welcome to List operations ")
                 print("Create a set for proceeding Operations")
                 set_main = create_set()
                 print("The created set1 is ", set_main)
                 set_2=update_set()
                 print("The created set2 is ", set_2)
                 print("Please select any one operation to proceed (Any number between 1-4)")
                 print("1. Union \n 2.Intersection \n3.Difference \n 4.symmetric Difference .....")

                 List_operation_input = int(input("please enter any one number ..."))

                 if List_operation_input == 1:
                                        output_union = set_main.union(set_2)
                                        print("The output after union operations is ", output_union)

                 if List_operation_input == 2:
                                        output_intersection = set_main.intersection(set_2)
                                        print("The output after intersection operations is ", output_intersection)

                 if List_operation_input == 3:
                                        output_difference = set_main.difference(set_2)
                                        print("after difference operations is ", output_difference)
                                        
                 if List_operation_input == 4:
                                        output_symmetric_difference = set_main.symmetric_difference(set_2)
                                        print("after difference operations is ", output_symmetric_difference)

if data_input ==4:
                 print("Welcome to List operations ")
                 print("Create a dictionary for proceeding Operations")
                 dictionary_main = dictionary_create()
                 print("The created dictionary is ", dictionary_main)
                 print("Please select any one operation to proceed (Any number between 1-4)")
                 print("1.pop \n2.clear \n3.copy \n4.gettems \n5.values \n6.clear .....")

                 dict_operation_input = int(input("please enter any one number ..."))

                 if dict_operation_input == 1:
                                        output_pop = pop(dictionary_main)
                                        print("The output after pop operations is ", output_pop)
                
                 if dict_operation_input == 2:
                                        output_clear = clear(dictionary_main)
                                        print("The output after clear operations is ", output_clear)

                 if dict_operation_input == 3:
                                        output_copy=copy(dictionary_main)
                                        print("after copying ", output_copy)

                 if dict_operation_input == 4:
                                        output_get=get(dictionary_main)
                                        print("after selecting particular key ", output_get)

                 if dict_operation_input == 5:
                                        output_values=values(dictionary_main)
                                        print("after selecting particular value ", output_values)

if data_input ==2:
                 print("Welcome to Tuple operations ")
                 print("Create a Tuple for proceeding Operations")
                 tuple_main = tuple_create()
                 print("The created tuple is ", tuple_main)
                 print("Please select any one operation to proceed (Any number between 1-4)")
                 print("1.concatinate \n2.count \n3.index .....")

                 tuple_operation_input = int(input("please enter any one number ..."))

                 if tuple_operation_input == 1:
                                        output_index = new_tuple(tuple_main)
                                        print("The output after pop operations is ", output_index)

                 if tuple_operation_input == 3:
                                        output_index = index(tuple_main)
                                        print("The output after pop operations is ", output_index)

                 if tuple_operation_input == 2:
                                        output_count = count(tuple_main)
                                        print("The output after pop operations is ", output_count)


                                        
"""
#import List
#import Set
#import Dict

w=(input("Welcome to Data structure calculator \nPlease select any one Data structure: \n1. List \n2. Tuple \n3. Set \n4. Dictionary "))
s=(input("selected data structure:"))
n=(input("enter the numbers:"))
a=list(map(int,input().split()))
print(a)
c=(input("select the operation you want to perorm:"))
d=input("pick any number from 0 to 9:")

list
1.append()
2.extend()
3.insert()
4.remove()
5.pop()
6.slice()
7.reverse()
8.len()
9.min()&max()
10.count()
11.concatenate()
12.multiply()
13.index()
14.sort()
15.clear()

tuple
1.access()
2.unpack()
3.join()
4.update()
5.loop()

set
1.intersection()
2.union()
3.differnce()
4.complement()

dictionary
loop
"""



   


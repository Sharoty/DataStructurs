Describe what is a list. 

  - A list is the placing of collected element in an order using squared [] brackets and are separeted by commas. 
  - It takes floats, strings, integers and booleans.

Examples of list used in python are as follows;

- list_of_intergers = [1,2,3,4,5,6,7,8,9,10]

- list_of_strings = ["one","two","three",four","five","ten"]
_  list_of_float = [12.5,33.00,]
3. Booleans this is used to comform if the information is True or False.

 
- Within a list we can create other list.

lay = [[1,2,3,4,5,6,7,8,9,10],["one","two","three",four","five","ten"]

- How to select an item in a list,
    an item can be selected using am index which will help us to select only the identified item in the list.

How we can identify a list;
Always ensure that all the listed items are in squared brackets and are separeted by comas. The nature of the list can be identified by the items listed for example if we are you strings it has to be corded.

           DICTIONARY NOTES
 A dictionary is used to store data values in key : value pairs. They are an unordered sequence of items key-value pairs, which means the order is not preserved. 
 A dictionary is an collection of an unordered items that are placed in the curly {} braces, separated by comas and a paired using keys : values pairs.The keys and the values are separated by full colons. 
The dictionary uses the value to access information .

   Examples of a dictionary
  -num = {1:"one",2:"two",3:"three,4:"four"}
  -print(num[2])
  
  Nested dictionary
  
  _family = {
    "child1":{
         "name" : "ruth",
         "year" : 2013
          },
          "child2":{
            "name":"tina",
            "year" : 2017
            },
            "child3":{
                "name" : "lisa",
                "year" : 2021
                 }
}
print(myfamily["child3"])

In a dictionary strings has to be quoted always and ensure that the identified key is within the dictonary to avoild erros. 
      Examples of errors are ; 
Index error this is the type of error that comes as a result of an index exceeding the number od listed items.
typeError this is the type of error that comes when a value or a key in a dictionary is misspelled.
keyError this is the type of error that comes when you type a key which is not is the dictionary or list given.

Dctionaries can be used when the data has a unique reference that can be associated with the value. It  usually uses numbers or strings.
charlotte = {"name":"charlotte","age":24,"nationality":"zambian"}
print(charlotte["age"])
print(type(charlotte["nationality"]))


mimi = {"country":"zambia","province":"southern","langauge":"tonga"}
print(mimi["province"])

mweemba = {"Name":"charlotte","surname":"mweemba","gender":"female","age":24,"school":"macson"}
print(mweemba["gender"])

mwape = {"name":"david","surname":"mwape","gender":"male","age":45,"school":"chabota"}
print(mwape["age"])

sikoswe = {"name":"fredrick","surname":"sikoswe","gender":"male","age":35,"school":"namalundu"}
print(sikoswe["school"])

myfamily = {
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

sharoty = {"myfamily":[{"child1":{
         "name" : "ruth",
         "year" : 2013
          },"child2":{
            "name":"tina",
            "year" : 2017},"child3":{
                "name" : "lisa",
                "year" : 2021}}]}
print(sharoty["myfamily"][0])

sikoswe1 = {
    'my_family':[
            {
            "name" : "Emil",
            "year" : 2004
        },
        {
            "name" : "Tobias",
            "year" : 2007
        },
        {
            "name" : "Linus",
            "year" : 2011
        }
            
        ]
}
print(sikoswe1['my_family'][2])

num = {1:"one",2:"two",3:"three"}
print(num[2])

{
"first_name": "sharoty",
    "last_name": "mweemba",
    "phone_number": "+260974668477",
    "@mail": "sharotykmweemba@gmail.com",
    "location":"kafue gorge",
    "summary":"i am a registered nurse graduate from makeni school of nursing",

    "education":[
 {
    "school":"macson",
    "duration": "2019-2021",
    "qualification": "diploma"
 },
 {"school":"namalundu secondary school",
"duration":"2012-2014",
"qualification":"school certificate"
 }

],
"skill": [{"skill_name": "python",
"rate": 5
},
{"skill_name": "smcs",
   "rate":5
}
],
"work_exprience":[
   {
  "company":"Airtel zambia",
  "role": "transport manager",
  "duration":"jan 2022-jun 2022",
  "decription":"organise transport for kafue agents"
}
],
"reference":[
   {
    "name":"mr gift musonda",
    "number":"+427751741",
    "email":"giftmusonda@gmail.com",
    "position":"human resorce manager"  
   }
]
}
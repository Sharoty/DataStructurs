person_info = {
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
   }]

}
print(person_info['reference'])
print(person_info['reference'][0]['email'])
print(person_info['skill'][1])
print(person_info['skill'][1]['rate'])
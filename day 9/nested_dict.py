# list inside a dictionary
# travel_log={
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Berlin","Hamburg","Stuttgart"],
#     "netherlands":["Amsterdam","Rotterdam","Utrecht"]
# }
# print(travel_log["France"][1])
# nested list
nested_list=["A","B",["C","D"]]
print(nested_list[2][1])

travel_log={
    "France":{
        "number_of_visits":12,
        "cities_visited":["Paris","Lille","Dijon"]
    },
    "Germany":{
        "number_of_visits":5,
        "cities_visited":["Berlin","Hamburg","Stuttgart"]
    },
    "netherlands":{
        "number_of_visits":3,
        "cities_visited":["Amsterdam","Rotterdam","Utrecht"]
    }
}
# now print stuttgart from germany
print(travel_log["Germany"]["cities_visited"][2])
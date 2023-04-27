dict={"family names":["anwar","fathima","kalam","reshma","rowfa","areef","mobeen","mateen","amanu","ameen"]}
print(dict)



dict1= { "family_members" :["anwar","fathima","kalam","reshma"] ,"relation":["father","mother","brother","sister"]}

dict1["family_members"] [1]
dict1["family_members"] [2]

dict2={"friend_names":["santhosh","abhinay","ameer","nayeem","siraj"],"quality" : ["talk active", "anger", "intelligent", "funny"]}

dict2 ["friend_names"] [1]
dict2 ["friend_names"] [4]

food={"non veg":["mutton biryani","chicken biryani","prawns biryani","fish biryani","chicken 65"],"ratings":[2,1,4,5,4]}
print(food)
food["ratings"] [2]

foodi={"veg items":["veg biryani","veg fried rice","veg noodles","veg manchuria"],"ratings":[3,2,4,1]}
print(foodi)
foodi["ratings"] [4]


fav_destination={"cities":["machilipatnam","vijaywada","hyderabad","mumbai","bangalor","delhi","surat","goa","vizag","ahemadabad"],"ratings":[2,2,1,3,1,4,5,3,6,4]}
print(fav_destination)

fav_destination ["cities"][3]



age=19
if age >20:
    print("teen age")
else:
    print("young age")


income=11
if income >10:
    print("i am profitable")
else:
    print("i lost")


purchase_amount=74

if purchase_amount >100:
    print("30% discount")
elif purchase_amount <50:
    print("10% discount")
else:
    print("20% discount")


mov_rs=50
if mov_rs ==140:
    print("balcony")
elif mov_rs==50:
    print("chair")
elif mov_rs==100:
    print("bench")
else:
    print("not avilable")


vehicle_type="four wheeler"
if vehicle_type =="two wheeler":
    print("bike and scooty")
elif vehicle_type =="four wheeler":
    print("car lorry van and zeep")

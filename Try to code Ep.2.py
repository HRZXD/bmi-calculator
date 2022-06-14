food_list = ["x","y","z","n","m",'p']
food = 4
q = quality_score = [7,4,10,8]
r = popularity_score = [5,9,3,5]
main_course_list = ["fried","ome","kua","chick"]
main = main_course_list
for food in food_list:
    if type(main) == str:
        main_course_list.append("kua")

for food in main_course_list:
    q=2
    r=2
    s= (0.6 * q) + (0.4 * r)


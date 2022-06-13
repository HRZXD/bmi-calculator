food_list = str(fried rice , omelet, x ,y)
main_course_list = []
for food in food_list(4):
    if food.type == 'main':
        main_course_list.append(food)
for food in main_course_list:
    q=food.quality_score
    r=food.popularity_score
    s=(0.6 * q) + (0.4 * r)
    food.ranking_score = s
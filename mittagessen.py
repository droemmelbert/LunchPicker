import json
import random
import argparse

# regularity
veryOften = 10
often = 6
sometimes = 3
seldom = 1

# price
cheap = 4
medium = 3
expensive = 2
veryExpensive = 1

# load mittagessen.json
with open('./mittagessen.json') as f:
    options = json.load(f)

restaurants = options.get('Restaurants')


def getRestaurantsWithPrice(price):
    response = []
    for restaurant in restaurants:
        if restaurant.get('price') == price:
            if restaurant.get('regularity') == 'very often':
                appendList(veryOften, restaurant, response)
            elif restaurant.get('regularity') == 'often':
                appendList(often, restaurant, response)
            elif restaurant.get('regularity') == 'sometimes':
                appendList(sometimes, restaurant, response)
            elif restaurant.get('regularity') == 'seldom':
                appendList(seldom, restaurant, response)

    return response


def getRestaurantsWithRegularity(regularity):
    response = []
    for restaurant in restaurants:
        if restaurant.get('regularity') == regularity:
            if restaurant.get('price') == 'cheap':
                appendList(cheap, restaurant, response)
            elif restaurant.get('price') == 'medium':
                appendList(medium, restaurant, response)
            elif restaurant.get('price') == 'expensive':
                appendList(expensive, restaurant, response)
            elif restaurant.get('price') == 'very expensive':
                appendList(veryExpensive, restaurant, response)
    return response


# function to get random restaurant recommendation
def getRandomRestaurant():
    weightedList = []
    for restaurant in restaurants:
        if restaurant.get('regularity') == 'very often':
            appendList(veryOften, restaurant, weightedList)
        elif restaurant.get('regularity') == 'often':
            appendList(often, restaurant, weightedList)
        elif restaurant.get('regularity') == 'sometimes':
            appendList(sometimes, restaurant, weightedList)
        elif restaurant.get('regularity') == 'seldom':
            appendList(seldom, restaurant, weightedList)
        if restaurant.get('price') == 'cheap':
            appendList(cheap, restaurant, weightedList)
        elif restaurant.get('price') == 'medium':
            appendList(medium, restaurant, weightedList)
        elif restaurant.get('price') == 'expensive':
            appendList(expensive, restaurant, weightedList)
        elif restaurant.get('price') == 'very expensive':
            appendList(veryExpensive, restaurant, weightedList)
    return random.choice(weightedList)


def appendList(amount, restaurant, list):
    while amount > 0:
        list.append(restaurant)
        amount -= 1
    return list


def getAllMealsAsString(restaurant):
    meals = restaurant.get('meals')
    if len(meals) > 1:
        return ' or '.join(meals)
    else:
        return meals[0]


def printRecommendation(recommendation):
    print('\n')
    print('Why don\'t you go to', recommendation.get('name'), 'today?')
    if getAllMealsAsString(recommendation) == 'something':
        print('You could try something new there!')
    else:
        print('You could eat', getAllMealsAsString(recommendation))
    if recommendation.get('menu') != None:
        print('\n')
        print('Check out their menu here:', recommendation.get('menu'))
    print('\n')


def isElementInList(element, list):
    for item in list:
        if item == element:
            return True
    return False


# function to pass system arguments to the script
def main(args):
    arg_price = args.price
    arg_regularity = args.regularity
    recommendation = None
    print('\n')
    # if no arguments are passed, get random restaurant recommendation
    if arg_price == '' and arg_regularity == '':
        recommendation = getRandomRestaurant()
        print('Here is a random recommendation for you:')
        printRecommendation(recommendation)

    elif arg_price != '' and arg_regularity == '':
        recommendation = random.choice(getRestaurantsWithPrice(arg_price))
        print('Here is some', arg_price, 'food for you:')
        printRecommendation(recommendation)

    elif arg_price == '' and arg_regularity != '':
        recommendation = random.choice(getRestaurantsWithRegularity(arg_regularity))
        print('Here is some food that you eat', arg_regularity)
        printRecommendation(recommendation)

    elif arg_price != '' and arg_regularity != '':
        recommendationList = []
        listPrice = getRestaurantsWithPrice(arg_price)
        listRegularity = getRestaurantsWithRegularity(arg_regularity)

        for restaurant in listPrice:
            if isElementInList(restaurant, listRegularity):
                recommendationList.append(restaurant)

        recommendation = random.choice(recommendationList)
        print('Here is some', arg_price, 'and', arg_regularity, 'food for you:')
        printRecommendation(recommendation)


# run main function
if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--price', default='', help='price of the food')
    parser.add_argument('-r', '--regularity', default='', help='regularity of the food')
    args = parser.parse_args()
    # run main function
    main(args)

for i in range(1, 30):
    getRestaurantsWithPrice('cheap')

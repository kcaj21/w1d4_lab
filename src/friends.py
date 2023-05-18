import pdb

def get_name(person):
    name = person["name"]
    return name

def get_favourite_tv_show(person):
    favourite_tv_show = person["favourites"]["tv_show"]
    return favourite_tv_show

# def likes_to_eat(person,food):
#     food = person["favourites"]["snacks"]
#     for snack in food:
#         if snack == food:
#             return True
#     return False


def likes_to_eat(person,food):
    # likes_food = bool
    likes_to_eat = person["favourites"]["snacks"]

    # pdb.set_trace()
    #for loop to check whether "food" = items in likes_to eat
    # if that's true, return "true" else return false
    # food = "bread"
    for item in likes_to_eat:
        if item == food:
            return True
        
    return False
    
def add_friend(person, friend):
    friends_list = person["friends"]
    friends_list.append(friend)
    len(friends_list)
    
def remove_friend(person, friend):
    friends_list = person["friends"]
    friends_list.remove(friend)
    len(friends_list)

def total_money(cash):   
    total_cash = 0
    for coins in cash:
        total_cash += coins["monies"]
    return total_cash

def lend_money(lender, borrower, difference):
    lender_balance = lender["monies"]
    borrower_balance = borrower["monies"]
    lender_balance -= difference
    borrower_balance += difference

    

# def all_favourite_foods(everyone):
#     all_food = []

#     everyones_food = everyone["favourties"]["snacks"]
#     all_food.insert[everyones_food]
#     return all_food






    
    
    
    
    
    # pdb.set_trace()
    #for loop to check whether "food" = items in likes_to eat
    # if that's true, return "true" else return false

    
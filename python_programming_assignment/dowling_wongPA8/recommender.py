# Dowling Wong
# COSI 10a, Fall 2021
# Programming Assignment #8
#
# Description: It is a program recommend and calculate the rate of books. I still have 2 days of extension, so that
#trun in two days late

#main function
#no parameter
#no return
def main():
    lines = open("ratings.txt").readlines()
    open("ratings.txt").close()
    titles = build_text_list(lines)
    users = build_user_dict(lines, titles)
    update_ratings(titles, users)
    process(titles, users)




#this function is to read titles and create a tuple to store title of books
#parameter: line
#return: list of ratings
def build_text_list(lines):
    lines = open("ratings.txt").readlines()
    titles = set()
    for i in range(1, len(lines), 3):
        titles.add(lines[i].strip())
    return list(titles)

#crate a dictionary first
#parameter: lines to identify name, titles for rating points
#return: dictionary of users, build a mapping
def build_user_dict(lines, titles):
    lines = open("ratings.txt").readlines()
    users = {}#users are the names of that guys in the file
    for i in range(0, len(lines), 3):
        if lines[i].strip() not in users.keys(): #if it hasn't been counted, add it
            users[lines[i].strip()] = [0] * len(titles)
    return users

#make update user dictionary ratings
#parameter: titles and users
#return none
def update_ratings(titles, users):
    lines = open("ratings.txt").readlines()
    for i in range(0, len(lines), 3):
        elem = lines[i].strip()
        users[elem][titles.index(lines[i + 1].strip())] = int(lines[i + 2])

#prompt user to choose what to do next
#no parameter
#no return
def prompt_user():
    print("Welcome to the Book Recommender. Type the word in the")
    print("left column to do the action on the right.")
    print("recommend : recommend books for a particular user")
    print("averages : output the average ratings of all books in the system")
    print("quit : exit the program")
    print()

# computer the average rate for each book
#parameter: book, titles, users
#return the average rate
def compute_ave(book, titles, users):
    total = 0
    count = 0
    for elem in users.keys(): #go through every
        if users[elem][titles.index(book)] != 0: #this book has been rated by current person
            total += users[elem][titles.index(book)]
            count += 1
    return float(total / count) #return the average rate

#titles mean rate point of each book, and need to match rate points with usernames
#parameter: titles and users
#return the average tuple
def averages(titles, users):
    average = [] #Creat an empty list for average
    for elem in titles:
        tup = (elem, compute_ave(elem, titles, users)) #match average rate with name
        average.append(tup) #and add a new one
    return average

#regular print function for avarage
#parameter: average
#return none
def print_averages(average):
    for elem in average:
        print(elem[0], elem[1]) #name and average rate

#preparing for similarity building
#parameter: the vector of two people
#return total amount
def dot_prod(a_vec, b_vec):
    total = 0
    for i in range(len(a_vec)):
        total += a_vec[i] * b_vec[i]
    return total

#connections of similarity between users
#parameter: username and users
#return their similarity
def build_similarity(username, users):
    similar = []
    for elem in users.keys():
        if elem != username: #this step is important, we don't want to compare one with himself
            similar.append((dot_prod(users[username], users[elem]), elem))
    return similar

#decide who is the most similar,and return these people
#parameter: similarity
#return the most similar
def get_most_similar(similar):
    most_similar = []
    for i in range(3):
        elem = similar.pop()
        most_similar.append(elem[1])
    return most_similar

#To calculate average of rating
#parameter: most_similar, users, titles
#return ratings
def average_ratings(most_similar, users, titles):
    ratings = [0] * len(titles)
    for i in range(len(ratings)):
        count = 0
        total = 0
        for user in most_similar:
            if users[user][i] != 0:
                total += users[user][i]
                count += 1
        if count != 0:
            ratings[i] = total / count
    return ratings

#to build the recommend list
#parameter: ratings and titles
#return recommendations
def build_rec_list(ratings, titles):
    recommendations = []
    for i in range(len(titles)):
        if ratings[i] > 0:
            recommendations.append((ratings[i], titles[i]))
    return recommendations

#just a regualer print function, print recommend list
#parameter: recommendations
#return none
def print_rec(recommendations):
    recommendations.sort() # we are asked to use sort in our program
    for i in range(len(recommendations)):
        elem = recommendations.pop()
        print(elem[1], elem[0])

#The most important program to process users' command
#parameter titles and users
#return none
def process( titles, users):
    average = averages(titles, users)
    average.sort()
    done = False
    prompt_user()
    while not done:
        response = input("next task? ")
        response = response.lower()
        if response == "averages":
            print_averages(average)
        elif response == "recommend":
            username = input("user? ")
            if username not in users.keys():
                print_averages(average)
            else:
                similar = build_similarity(username, users)
                similar.sort()
                most_similar = get_most_similar(similar)
                ratings = average_ratings(most_similar, users, titles)
                recommendations = build_rec_list(ratings, titles)
                print_rec(recommendations)
        elif response == "quit":
            done = True
        print()


main()
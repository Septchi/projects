# This function is used to create a similarity matrix
def calc_similarity_scores(network):
    similarity_matrix = []
    for x in range(network):
        i = []
        for y in range(network):
            i.append(0)
        similarity_matrix.append(i)
    global similarity_table
    similarity_table = similarity_matrix

# This function is used to create a friends list for every user
def calc_list_of_friends(network):
    for n in range(network):
        globals()['friends_of_user'+str(n)] = []
        return globals()['friends_of_user'+str(n)]

# These functions are used to generate a similarity matrix using the friends lists of users
def return_similarity_scores_a(network, similarity_matrix):
    for n in range(network):
        i = n + 1
        while i in range(network):
            similarity_matrix[n][i] = num_in_common_between_lists(globals()['friends_of_user'+str(n)], globals()['friends_of_user'+str(i)])
            i += 1
    return similarity_matrix

def return_similarity_scores_b(network, similarity_matrix):
    n = network - 1
    while n >= 0:
        i = n - 1
        while i >= 0:
            similarity_matrix[n][i] = num_in_common_between_lists(globals()['friends_of_user'+str(n)], globals()['friends_of_user'+str(i)])
            i -= 1
        n -= 1
    return similarity_matrix

# This function is used to generate a friends list for every user
def return_list_of_friends(user_id, list1, list2):
    friends_of_user = []
    indices = [i for i, li in enumerate(list2) if li == user_id]
    for i in indices:
        friends_of_user.append(list1[i])
    indices = [i for i, li in enumerate(list1) if li == user_id]
    for i in indices:
        friends_of_user.append(list2[i])
    globals()['friends_of_user'+str(user_id)] = friends_of_user

# This function is used to automate the generation of friends lists
def gen_list_of_friends(network):
    for n in range(network):
        return_list_of_friends(n, user_u, user_v)

# This function is used to find the similarities between two lists
def num_in_common_between_lists(list1, list2):
    n = 0
    for a in list1:
        for b in list2:
            if a == b:
                n += 1
    return n

# This function is used to generate a recommendation based on the similarity matrix data
def recommend(user_id, network, similarity_matrix):
    while network > 0:
        if network in similarity_matrix[user_id]:
            a = [i for i, n in enumerate(similarity_matrix[user_id]) if n == network]
            b = [i for i in a if i not in globals()['friends_of_user' + str(user_id)]]
            if b:
                print("User(s) "+str(b)+" has/have the highest similarity score with user "+str(user_id))
                break
        network -= 1

# The dataset provided in the .doc file
user_u = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7]
user_v = [1, 2, 3, 4, 6, 7, 9, 3, 6, 8, 9, 8, 9, 6, 7, 8, 9, 8, 8]

# The definition of network in this project is the number of users in the social network
size = 10

# Creating a similarity matrix
calc_similarity_scores(size)

# Creating a friends list for every user
calc_list_of_friends(size)

# Generating a friends list for every user
gen_list_of_friends(size)

# Generating a similarity matrix using the friends lists of users
return_similarity_scores_a(size, similarity_table)
print(similarity_table)
return_similarity_scores_b(size, similarity_table)
print(similarity_table)

# Generating a recommendation based on the similarity matrix data
recommend(0, size, similarity_table)
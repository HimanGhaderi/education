


# d = {1: "one", 2:"two", "name": "Reza"}


# d[3] = "three" 

# d[1] = "one one"

#  del d[1]


# for item in d:
#     print(d[item])



d = {
    "1": {"team": "arsenal", "num_game": 25, "score": 56},
    "2": {"team": "city", "num_game": 25, "score": 50},
    "3": {"team": "aston vila", "num_game": 25, "score": 47}
}


for item in d:
    print(item, "    ", d[item]["team"], "    game: ", d[item]["num_game"], "     score: ", d[item]["score"])
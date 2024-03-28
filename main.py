# 08- March-28th Morning

# Question  number 6
favorite_movies = [
    ("Pulp fiction", 1994),
    ("Inception", 2010),
    ("x", 2020),
    ("The Shawshank redemption", 1994)
]

new_list = sorted(favorite_movies, key=lambda x: x[1], reverse=True)

counter = 0
for item in new_list:
    counter += 1
    print(f"{counter}. {item}")

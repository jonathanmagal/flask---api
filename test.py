import requests
Base = "http://127.0.0.1:5000/"
# data = [
#     {"narnia": {"auther": "fucking dont know", "category": "fantasy", "stars": 2}},
#     {"harry poter": {"auther": "j.k rolling", "category": "mystery", "stars": 3}},
#     {"james bond": {"auther": "M", "category": "action", "stars": 3}},
#     {"mission impossible": {"auther": "j.b rolling", "category": "action", "stars": 5}},
#     {"steve jobs": {"auther": "s.j", "category": "docu", "stars": 5}}
# ]

# for i in data:
#     for bookname, bookdata in i.items():
#         response = requests.put(Base + "books/" + str(bookname), bookdata)
#         print(response.json())
# input()
response = requests.delete(Base + "books/narnia")
print(response.json())
response = requests.get(Base + "books/narnia")
print(response.json())

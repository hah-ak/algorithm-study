# def solution(new_id):
    
#     new_id = new_id.lower()
#     c_id = ""
#     for s in new_id:
#         if not s.isalpha() and not s.isalnum() and s != '-' and s != '_' and s!='.':
#             continue
#         else:
#             c_id += s
#     if c_id == "":
#         c_id = "a"
#     else:
#         c_id = c_id.split('.')
#         for i in range(len(c_id)):
#             if c_id[i] != "":
#                 c_id[i] += '.'
#         c_id = "".join(c_id)
#         if c_id == "":
#             c_id = "a"
#     if c_id[0] == '.':
#         c_id = c_id[1:]
#     if c_id[-1] == '.':
#         c_id = c_id[:-1]

#     if len(c_id) > 15:
#         c_id = c_id[:15]
#         if c_id[-1] == '.':
#             c_id = c_id[:-1]
#     if len(c_id) <= 2:
#         while len(c_id) != 3:
#             c_id += c_id[-1]

#     return c_id



# s = '456....52'


# print(y)

class Node:
    Next = 1
    def __init__(self, data):
        self.data = data

    def change_next(self):
        self.Next = 8

# class Node:
    
#     def __init__(self, data,Next):
#         self.data = data
#         self.Next = None
a = Node(3)
print(a.Next)
b = Node(4)
a.Next = b
b.Next = 5
# a.change_next()
print(a.Next.Next)
from random import randint as Ri
my_list = [Ri(0,100) for _ in range(10)]
print(my_list)
# new_list []
# new_list = my_list.copy()
new_list = my_list[:]
# flag = True
while True:
    for i in range(len(my_list)):
        k = Ri(len(my_list-1))
        new_list[i], new_list[k] = new_list[k], new_list[i]
    for i in range(len(my_list)):
        if new_list[i] == my_list[i]:
            print('Нашлось повторение')
            break
    else:
        break
        # flag = False


def shuffle_my_list(sm_list):
    import random
    new_list = []
    random_list = []
    for i in range(len(sm_list)):
        gen_index = random.randint(0, len(sm_list) - 1)
        while gen_index in random_list:
            gen_index = random.randint(0, len(sm_list) - 1)
        new_list.append(sm_list[gen_index])
        random_list.append(gen_index)
    return new_list
  

import random
def shuffle_my_list(smlist):
    for _ in range(len(sm_list)):
        k = random.randint(0, (len(sm_list) - 1))
        sm_list.insert(0, sm_list.pop(k))


mylist = [random.randint(0, 100) for _ in range(10)]
print(my_list)


from copy import deepcopy
new_list = deepcopy(my_list)

import copy

# old_dict = {'id' : 1, 'name' : 'inightjar' }

# new_dict = old_dict
# # new_list = old_list
# old_dict['list'] = [4, 4, 4]

# print("Old list:", old_dict)
# print("New list:", new_dict)


old_dict = {'info' : {'id': 1, 'name' : 'inightjar'}, 'address': {'country': 'egypt', 'city' : 'sadat city'}}

new_dict = copy.deepcopy(old_dict)

# new_dict['info'] = 'unknown'
new_dict['info']['name'] = 'muhamed medhat'


print("Old list:", old_dict)
print("New list:", new_dict)

print("Old list:", id(old_dict))
print("New list:", id(new_dict))

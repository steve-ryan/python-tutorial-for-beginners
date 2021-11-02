#recommended way
admin_dict = {'1':'scie/065p','2':'scii/890p'}
#getting value for a key using [] brackets
print(admin_dict['1'])

#not recommended if key is an integer
dict_func = dict(one='1',two='2')

#change value
admin_dict['1'] = 'steve/07'
print(admin_dict['1'])

#adding key value dictionary from one dict to another
admin_name = {'name':'steve','phone':'0756949393'}

admin_name.update(admin_dict)
print(admin_name)
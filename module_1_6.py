my_dict = {'Petia': 1995, 'Masha' : 2001,  'Oksana' : 1990}
print('Dict: ' , my_dict)
print('Existing value: ', my_dict['Petia'])
print('Not existing value: ', my_dict.get('Anatolii'))
my_dict.update({'Sasha' : 2007 ,
                'Roma'  :1954})
delete_ = my_dict.pop('Oksana')
print('Deleted value: ' , delete_)
print('Modified dictionary: ' , my_dict)
print()
my_set = {1,2,3,True,'текст',3.14}
print('Set: ',(my_set))
my_set.discard('текст')
my_set.add((1,2,3))
my_set.add('новый текст')
print('Modified set: ', my_set)
import csv

#use 'Dictwriter()' function to create a writer object
with open('write.csv',mode='w') as file:
    writer = csv.DictWriter(file,fieldnames=['name','age','area'])
    writer.writeheader()
    output_data = [
        {
            'name':'steve',
            'age':50,
            'area':'Nairobi'
        }
    ]
    writer.writerows(output_data)
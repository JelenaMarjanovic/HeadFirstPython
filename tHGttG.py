from pprint import pprint

people = {}

person1 = { 'Name': 'Ford Prefect',
            'Gender': 'Male',
            'Occupation': 'Researcher',
            'Home Planet': 'Betelgeuse Seven' }

person2 = { 'Name': 'Arthur Dent',
              'Gender': 'Male',
              'Occupation': 'Sandwich-Maker',
              'Home Planet': 'Earth' }

person3 = { 'Name': 'Tricia McMillan',
            'Gender': 'Female',
            'Occupation': 'Mathematician',
            'Home Planet': 'Earth' }

person4 = { 'Name': 'Marvin',
            'Gender': 'Unknown',
            'Occupation': 'Paranoid Android',
            'Home Planet': 'Unknown' }

people['Ford'] = person1
people['Arthur'] = person2
people['Trillian'] = person3
people['Robot'] = person4

pprint(people)

print()

print('Tricia is a', people['Trillian']['Occupation'])

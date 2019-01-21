import requests

random_taco = requests.get('http://taco-randomizer.herokuapp.com/random').json()
print(random_taco)
print(random_taco['mixin']['recipe'])

# What about all the parts of a taco?

for part, recipe in random_taco.items():
    title = part.replace('_', ' ').title()
    print(f'\n*************** {title} ***************')
    print(f"\n{recipe['recipe']}")



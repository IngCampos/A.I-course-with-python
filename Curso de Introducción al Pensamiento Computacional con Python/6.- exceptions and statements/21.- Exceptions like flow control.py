# Python

def search_country(countries, country):
    """
    Countries is a dictionary. Country is the key.
    Code with the EAFP(easier to ask for forgiveness than permission) principle.
    """

    try:
        return countries[country]
    except KeyError:
        return None


my_dict = {
    'Mexico': 35,
    'Peru': 12,
    'Brasil': 30,
}
print(search_country(my_dict, 'Mexico'))  # 35
print(search_country(my_dict, 'Chile'))  # None

# Javascript

# function search_country(countries, country) {
#    Countries is a dictionary. Country is the key.
#   Code with the LBYL (look before you leap) principle.
# if(!Object.keys(countries).includes(country)) {
#   return null;
#  }
# return countries[country];
# }

# Pyhton use more the EAFP principle

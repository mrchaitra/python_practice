birthday={
    "name":"John",
    "age":30,
    "city":"New York",      
}
meaning={
    "name":"A word or phrase that describes a person, place, thing, or idea.",
    "age":"The length of time that a person has lived or a thing has existed.",
    "city":"A large town."
}
def  get_birthday_info():
    return birthday
def  get_meaning_info():
    return meaning
def  get_birthday_info_by_key(key):
    if key in birthday:
        return birthday[key]
    else:
        return "Key not found"
def  get_meaning_info_by_key(key):
    if key in meaning:
        return meaning[key]
    else:
        return "Key not found"
def  get_birthday_info_by_value(value):
    for key, val in birthday.items():
        if val == value:
            return key
    return "Value not found"
def  get_meaning_info_by_value(value):
    for key, val in meaning.items():
        if val == value:
            return key
    return "Value not found"
def  get_birthday_info_by_key_value(key, value):
    if key in birthday and birthday[key] == value:
        return True
    else:
        return False
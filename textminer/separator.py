import re


def words(text):
    words = re.findall(r'\d*[a-z-]+', text)
    if len(words):
        return words


def phone_number(string):
    words = {}
    # if len(string < 5):
    #     return False
    matches = re.search(r'(\d{3})\D?(\d{4})$', string)
    num = matches.group(1)+'-'+matches.group(2)
    words["area_code"] = re.search(r'(\d{3})', string).group(1)
    words["number"] = num

    return words


def money(string):
    money = {}
    money["currency"] = re.findall(r'^\$', string)
    money["amount"] = re.findall(r'[\d]+(\,\d\d\d)*\.?(\d\d)?$', string)
    return money

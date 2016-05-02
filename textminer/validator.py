import re


def binary(num):
    return re.match(r'[0-1]+', num)


def binary_even(num):
    return re.match(r'^[0-1]+[^1]$', num)


def hex(stuff):
    return re.findall(r'^[0-9A-F]+$', stuff)


def word(string):
    return re.findall(r'^[0-9]*?[a-z-]+$', string)


def words(string, count=None):
    words = re.findall(r'[\w]*[a-zA-Z-]+', string)

    if count is not None:
        return len(words) == count
    else:
        return len(words) > 0


def phone_number(string):
    return re.findall(r'.?(\d{3}).\s?(\d{3}).?(\d{3})', string)


def money(string):
    return re.findall(r'^\$[\d]+(\,\d\d\d)*\.?(\d\d)?$', string)


def zipcode(zipcode):
    return re.match(r'^\d{5}(-\d{4})?$', zipcode)


def date(date):
    return re.findall(r'(\d+.\d+.\d+)', date)

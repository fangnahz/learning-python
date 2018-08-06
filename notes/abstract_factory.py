# coding: utf-8


# formatters
class FranceDateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (x, m, d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return ("{}/{}/{}".format(d, m, y))


class USADateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y, m, d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return("{}-{}-{}".format(m, d, y))


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(' ')
            digits.append(c)
        base = ''.join(reversed(digits))
        return "{}€{}".format(base, cents)


class USACurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(',')
            digits.append(c)
        base = ''.join(reversed(digits))
        return "${}.{}".format(base, cents)


# factories
# factories does not implement formatters, because formatters maybe reused
# e.g. Canada currency formatter is the same as USA, but has different date formatter
class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()

    def create_currency_formatter(self):
        return USACurrencyFormatter()


class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()


# settings to choose formatter, acting as abstract interface
# singleton objcet can be used here, and can be assigned to each factory as an instance variable
factory_map = {
    'US': USAFormatterFactory,
    'FR': FranceFormatterFactory
}


# use case
country_code = 'US'  # or 'FR'
formatter_factory = factory_map.get(country_code)()


# in practice, the follwing package structure can be considered
'''
localize/
    __init__.py
    backends/
        __init__.py
        USA.py
        France.py
        …
'''
# and put the logic to choose formatters in localize/__init__.py,
# using (usually bad) `from .backends.USA import *`
# then use `localize.format_date`

# Or, use a variable to point to specific module
from .backends import USA, France
if country_code == 'US':
    current_backend = USA
# then use `localize.current_backend.format_date`

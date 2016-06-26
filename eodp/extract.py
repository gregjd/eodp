import re

# needs work
def get_effective_date(string):

    try:
        date = re.search(r"(?:shall.+effective|effective date):?(.+)(?=[\.:]?)",
                         string, re.I | re.M).group(1)
    except AttributeError:
        return None
    else:
        return date.lstrip().rstrip('.:')

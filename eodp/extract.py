import re


def get_effective_date(string):

    dates = re.findall(r"(?:shall.+effective|effective date):?(.+)(?=[\.:]?)",
                       string, re.I | re.M)
    try:
        shortest_date = min(dates, key=(lambda s: len(s)))
    except ValueError:
        return None
    else:
        return shortest_date.lstrip().rstrip('.:')

#    try:
#        date = re.search(r"(?:shall.+effective|effective date):?(.+)(?=[\.:]?)",
#                         string, re.I | re.M).group(1)
#    except AttributeError:
#        return None
#    else:
#        return date.lstrip().rstrip('.:')

def get_portal_paragraph(full_text):

    candidates = []
    for line in full_text.split('\n'):
        if 'shall' in line:
            if ('portal' in line) or ('website' in line):
                if ('establish' in line) or ('maintain' in line):
                    if len(line) <= 2000:
                        candidates.append(line.strip())

    return candidates or None

def get_portal_url(full_text):

    urls = re.findall(r"((?:\w{2,}\.)?\w{2,}\.(?:gov|org|com|net|info|edu|io))",
                      full_text, re.I)

    return set([url.lower() for url in urls]) or None

import re

# detect multiple cities?

# Parts: 0 front matter, 1 preamble, 2 transition,
# 2-main, 3-epilogue

# 'whereas' sections
# numbered sections (with and without the word 'section')

BREAKS = [re.compile(r".+?\n(?=whereas)", re.I | re.DOTALL),
          re.compile(r"^.+(?:therefore|hereby|ordained).+?\n?.+?:\n",
                     re.M | re.I)]

# signed, in witness whereof, issued by, history, dated, final action


def divide_policy(string):

    return _divide(string, _find_all_breaks(string))

def divide_sections(string):

    return _divide(string, _find_section_starts(string))

def _divide(string, list_of_points):

    divided = [string]
    for point in _high_to_low(list_of_points):
        divided[0:1] = divided[0][:point], divided[0][point:]
    if '' in divided:
        divided.remove('')

    return divided

def _find_all_breaks(string):

    #return [_find_break(regex, string) for regex in BREAKS]
    break_list = []
    for regex in BREAKS:
        try:
            br = _find_break(regex, string)
        except AttributeError:
            pass
        else:
            break_list.append(br)

    return break_list

def _find_break(regex, string):

    return regex.search(string).end()

def _find_section_starts(string):

    secs = re.finditer(r"^(?:section)? ?([0-9]|[IVX])+ ?[\.:-] ",
                       string, re.M | re.I)

    return [i.start() for i in secs]

def _high_to_low(list_):

    return reversed(sorted(list_))

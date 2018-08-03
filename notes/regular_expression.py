def match(regex, text):
    if regex[0] == '^':
        regex_1_ = regex[1:] if len(regex) > 1 else ''
        return match_here(regex_1_, text)
    for i in range(len(text)):
        if match_here(regex, text[i:]):
            return True
    return False


def match_here(regex, text):
    regex_1 = regex[1] if len(regex) > 1 else ''
    if not regex:
        return True
    if regex_1 == '*':
        regex_2_ = regex[2:] if len(regex) > 2 else ''
        return match_star(regex[0], regex_2_, text)
    if regex == '$':
        return not text
    if text and (regex[0] == text[0] or regex[0] == '.'):
        regex_1_ = regex[1:] if len(regex) > 1 else ''
        text_1_ = text[1:] if len(text) > 1 else ''
        return match_here(regex_1_, text_1_)
    return False


def match_star(c, regex, text):
    for i in range(len(text)):
        text_i_ = text[i:]
        if text_i_[0] == c or c == '.':
            text_i_1_ = text_i_[1:] if len(text_i_) > 1 else ''
            if match_here(regex, text_i_1_):
                return True
    return False

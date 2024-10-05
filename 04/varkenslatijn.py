def varkenslatijn(word) :
    return varkenswoord(word)
    
def varkenswoord(word) :
    sb = []
    add = ''
    suffix = ''
    for ch in word :
        if not ch.isalpha() :
            add_to_sb(sb, add, suffix)
            sb.append(ch)
            suffix = ''
            add = ''
        elif is_vowel(ch) :
            if (ch in ('u', 'U')) and len(suffix) > 0 and (suffix[0] == 'q' or suffix[0] == 'Q') :
                suffix += ch
            else :
                add += ch
        elif len(add) == 0 :
            suffix += ch
        else :
            add += ch
    add_to_sb(sb, add, suffix)
    return ''.join([str(ch) for ch in sb])

def add_to_sb(sb, add, suffix) :
    if len(add) == 0 and len(suffix) == 0 :
        return
    sb.append(add[0].upper() + add[1:] if len(suffix) > 0 and suffix[0].isupper() else add)
    if len(suffix) > 0 :
        sb.append(suffix if len(add) > 0 and add[0].isupper() else suffix[0].lower() + suffix[1:])
        sb.append('ay')
    else :
        sb.append('way')
def is_vowel(ch) :
    return ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

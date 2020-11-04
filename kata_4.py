#https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
def format_duration(num):
    result = []
    if num == 0:
        return 'now'
    y, d, h, m = 31536000, 86400, 3600, 60
    y_s = d_s = h_s = m_s = s_s = ''
    if num >= y:
        years = num // y
        num %= y
        if years > 1:
            y_s = 's'
        result.append('{} year{}'.format(years, y_s))
    
    if num >= d:
        days = num // d
        num %= d
        if days > 1:
           d_s = 's'
        result.append('{} day{}'.format(days, d_s))

    if num >= h:
        hours = num // h
        num %= h
        if hours > 1:
            h_s = 's'
        result.append('{} hour{}'.format(hours, h_s))
    
    if num >= m:
        minutes = num // m
        num %= m
        if minutes > 1:
            m_s = 's'
        result.append('{} minute{}'.format(minutes, m_s))
    if num >= 1:
        if num > 1:
            s_s = 's'
        result.append('{} second{}'.format(num, s_s))

    if len(result) == 1:
        return str(result[0])
    elif len(result) == 2:
        return '{} and {}'.format(result[0], result[1])
    elif len(result) == 3:
        return '{}, {} and {}'.format(result[0], result[1], result[2])
    elif len(result) == 4:
        return '{}, {}, {} and {}'.format(result[0], result[1], result[2], result[3])
    else :
        return '{}, {}, {}, {} and {}'.format(result[0], result[1], result[2], result[3], result[4])
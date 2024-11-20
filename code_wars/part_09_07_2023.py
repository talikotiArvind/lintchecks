# int in seconds to hour, min, seconds

def format_duration(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'

# print(format_duration(3600))


import re
# Convert PascalCase string into snake_case
def to_underscore(string):
    # your code here
    val = re.findall('[A-Z][a-z]*[0-9]*', string)
    return "_".join(i.lower() for i in val )

print(to_underscore("TestController"))

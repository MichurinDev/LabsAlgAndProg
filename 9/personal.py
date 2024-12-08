# Написать регулярное выражение, определяющее, является ли заданная строка правильным MAC-адресом.
# Пример правильного выражения:     aE:dC:cA:56:76:54
# Пример неправильного выражения:   01:23:45:67:89:Az

import re

mac_right = 'aE:dC:cA:56:76:54'
mac_wrong = '01:23:45:67:89:Az'
test = 'aE'

pattern = r'^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$'

print(bool(re.match(pattern, mac_right)))
print(bool(re.match(pattern, mac_wrong)))

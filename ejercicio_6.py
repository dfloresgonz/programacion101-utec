kw = 130

LIMIT_KW = 100
KW_LESS_100 = 0.4522
KW_OVER_100 = 0.7

last = 0

if kw <= LIMIT_KW:
    last = kw * KW_LESS_100
else:
    tmp = LIMIT_KW * KW_LESS_100
    tmp2 = (kw - LIMIT_KW) * KW_OVER_100
    last = tmp + tmp2

print("last: {}".format(last))
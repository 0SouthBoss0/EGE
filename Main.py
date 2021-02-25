# 1
# ГРАФИКИ

# 2
# Логическая функция

# (⋀) - and
# (V) - or
# (¬) - not
# (≡) - ==
# (→) - <=

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((x <= y) == (z <= w)) or (x and w)) == 0:
                    print(x, y, z, w)

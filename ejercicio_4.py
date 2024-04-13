colors_amount = int(input("How many colors do you want? "))

# 6 12 24

c_24 = colors_amount // 24
colors_amount = colors_amount - (c_24 * 24)

c_12 = colors_amount // 12
colors_amount = colors_amount - (c_12 * 12)

c_6 = colors_amount // 6
colors_amount = colors_amount - (c_6 * 6)

print("{} boxes of 24\n{} boxes of 12\n{} boxes of 6\n{} colors are left"
      .format(c_24,  c_12, c_6, colors_amount))
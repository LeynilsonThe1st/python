from bases_numericas import converter

x = 0
i = 1
while i <= 20 :
	x = (x * 10) + 1
	res = converter(str(x), 2, 10)
	print(x, res, "impar:", res % 2 != 0)
	i += 1

# todo numero binario do tipo 1, 11, 111, 1111...1
# convertido para decimal é impar
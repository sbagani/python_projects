def longest_substring_k_distinct_char(str, k):
	charset ={}

	windowstart = 0
	max_len = 0

	for i in range(len(str)):
		rightchar = str[i]

		if rightchar not in charset:
			charset[rightchar] = 0
		charset[rightchar] += 1

		while len(charset) > k:
			leftchar = str[windowstart]
			charset[leftchar] -= 1
			if charset[leftchar] == 0:
				del charset[leftchar]

			windowstart +=1

		max_len = max(max_len, i - windowstart+1)

	return max_len

 	

res = longest_substring_k_distinct_char("arraci", 2)

print(res)


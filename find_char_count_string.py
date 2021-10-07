# To find a char count in a string

# Time complexity = O(n)

def char_count_string(s,c):
	count = 0

	for i in range(len(s)):
		if s[i] == c:
			count = count+1
	return count

s =" sravanthi bagani"
c = "s"

result = char_count_string(s,c)

print(result)


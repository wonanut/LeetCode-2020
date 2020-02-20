"""
Daily Problem 125
Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.
"""

def flatten_dictionary(d):
	output = {}
	def helper(cur_d, prefix, output):
		for item in cur_d:
			if type(cur_d[item]) == dict:
				helper(cur_d[item], prefix + item + '.', output)
			else:
				output[prefix +item] = cur_d[item]
	helper(d, '', output)
	return output

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
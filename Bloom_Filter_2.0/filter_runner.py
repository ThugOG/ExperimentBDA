import hashlib
from bloom_filter import importFile, BloomFilter
from random import shuffle

def hash_function_1(item):
	return int(hashlib.sha256(str(item).encode()).hexdigest(), 16)

def hash_function_2(item):
	return int(hashlib.md5(str(item).encode()).hexdigest(), 16)

def shuffel(x):
	for y in x:
		shuffle(y)

filter_size = 1000
hash_functions = [hash_function_1, hash_function_2]
bloom_filter = BloomFilter(filter_size, hash_functions)

word_p = importFile('set.txt')
word_a = importFile('test.txt')
idxs = [word_p, word_a]

for element in word_p:
	bloom_filter.add(element)

shuffel(idxs)

test_words = word_a + word_p[:1]
shuffel([idxs, test_words])

for element in test_words:
	if element in bloom_filter:
		if element in word_a:
			print(f"'{element}' is a false positive!!!")
		else:
			print(f"'{element}' is probably present in the set!!!")
	else:
		print(f"'{element}' is surely not present in the set.")


def extract_hashtag(text):
	words = text.split()

	hashtag = []

	for word in words:
		if word[0] == "#":
			hashtag.append(word)

	return hashtag


text = "i am alireza parvaresh  #mcs student at #aut"


hashtags = extract_hashtag(text)

for index ,hashtag in enumerate(hashtags):
	print(f"{index + 1} ---- > {hashtag}")

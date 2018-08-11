from config import *
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

all_hashtags = {}

for post in posts_collection.find():
	try:
		hashes = post["Hashtags"]
		for this_hash in hashes:
			if this_hash.lower() not in all_hashtags:
				all_hashtags[this_hash] = 1
			else:
				all_hashtags[this_hash] += 1
	except:
		pass

print(all_hashtags)
performance = []
objects = []
for key in all_hashtags:
	if all_hashtags[key] >= 500:
	# Gotta make this pour out only the ones with 50 or more
	# otherwise the graph is massive and unreadable
	# Also spit this out into a CSV
		performance.append(all_hashtags[key])
		full_name = "{0}\n({1})".format(key,all_hashtags[key])
		objects.append(full_name)

y_pos = np.arange(len(objects))
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Amount of posts containing this hashtag')
plt.title('Hashtags seen throughout captured tweets')
plt.savefig('graphs/hashtags.png')
plt.show()

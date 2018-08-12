from config import *
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

all_languages = {}

for post in posts_collection.find():
	try:
		lang = post["Language"]
		if lang != "":
			if lang not in all_languages:
				all_languages[lang] = 1
			else:
				all_languages[lang] += 1
		else:
			print("No language defined, moving along")
	except:
		pass

performance = []
objects = []
for key in all_languages:
	performance.append(all_languages[key])
	full_name = "{0}\n({1})".format(key,all_languages[key])
	objects.append(full_name)

y_pos = np.arange(len(objects))
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Amount of posts per language')
plt.title('Languages seen throughout captures posts')
plt.savefig('graphs/languages.png')
plt.show()
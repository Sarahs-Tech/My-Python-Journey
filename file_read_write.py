def count_prints(name):
    with open(name, "r") as file:
        count=0
        for line in file:
            words=line.strip().split()
            # print(words)

            
            for word in words:
                if word.startswith("print"):
                    count+=1
                # print(count)
    return count




import os

folder_path='/workspaces/My-Python-Journey'
names=os.listdir(folder_path)
print(names)

# count_all=0
# for name in names:
#     if name.endswith(".py"):
#         count_all+=count_prints(name)
#         # print(count_all)

# print(count_all)

import re

all_words={}
for name in names:
    if name.endswith(".py"):
        with open(name, "r") as file:
                
                for line in file:
                    words=re.findall(r'\w+', file.read().lower())
                    # print(words)

                    for word in words:
                        if word not in all_words:
                            all_words.update({word:1})

                        else:
                            all_words[word]+=1

# print(all_words)
sorted_words=dict(sorted(all_words.items(), key=lambda item:-item[1]))

print(sorted_words)











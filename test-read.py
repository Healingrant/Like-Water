import random

# Pulls Random Phrase from pool of 133 file 
#  entries (64 best of yin+yang[modified]
#   and 69 original phrases.)

with open("phrases-general-v0.1.5.csv", "rb") as source:
    lines = [line for line in source]
random_choice_general = random.sample(lines, 1)
# with open("new_file.csv", "wb") as sink:
    # sink.write("\n".join(random_choice))
    
with open("phrases-yin-v0.0.0.csv", "rb") as source:
	lines_yin = [line for line in source]
random_yin = random.sample(lines_yin, 1)


with open("phrases-yang-v0.0.0.csv", "rb") as source:
	lines_yang = [line for line in source]
random_yang = random.sample(lines_yang, 1)



print random_choice_general[0]

print 


#Prints random yin + yang combo from pool of 64 yin and 64 yang phrases.
print random_yin[0], random_yang[0]
    
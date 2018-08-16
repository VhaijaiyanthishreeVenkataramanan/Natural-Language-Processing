""" CAP 6640 - Dr. Glinos - University of Central Florida
Please place the input files and the program files on the same location
Python Version - 3.6.4
To run the program, use the following command:
python3 Vhaijaiyanthi_pa3.py
"""


import collections
from collections import defaultdict

END = "  "
START = ""

def distinct_tags(tags):
    print('All Tags Observed:')
    unique_tags = list(tags)
    unique_tags.sort()
    for index, tag in enumerate(unique_tags, 1):
        print("{0}. {1}". format(index, tag))
        


def initial_distribution(unique_tags, total_sentences): 
	print('\n')
	print('Initial Distribution:\n') 	
	sort_tags = sorted(unique_tags.items())
	ordered_tags = collections.OrderedDict(sort_tags)
	for x, y in ordered_tags.items():
		val = y / total_sentences
		print("start [  {0}\t| \t ] {1:.6f}".format(x, val))
		
# def initial_distribution(unique_tags, sentence_list, total_sentences):
# 	print('\n')
#     print('Initial Distribution:\n')
#     a = []
#     init_dist = []
#     count = 0
#     prob = 0
#     for i in sentence_list:
#     	a.append(i.split("\n")) 
#     for tag in unique_tags:
#     	for sentence in a:
#     		if tag == sentence[0].split(" ")[1]:
#     			count += 1
#     	prob = (float(count) / float(total_sentences))
#     	if prob != 0:
#     		init_dist.append("%6f" %prob)
#     	count = 0
#     for i in range(len(init_dist)):
#     	print("start [", unique_tags[i], "| ]", init_dist[i])
    	
def dict_words_and_tags(tags, words):
	words_and_tags = {}
	for w in range(len(tags)):
		words_and_tags[words[w]] = words_and_tags.get(words[w], {})
		words_and_tags[words[w]][tags[w]] = words_and_tags[words[w]].get(tags[w], 0)
		words_and_tags[words[w]][tags[w]] += 1
	return words_and_tags


def emission_probabilities(words_and_tags, tags):
	print('\n')
	print("Emission Probabilities:\n\n")
	emission_prob = {}
	sort_tags = sorted(words_and_tags.items())
	ordered_tags = collections.OrderedDict(sort_tags)
	for word, dict_tag in ordered_tags.items():
		emission_prob[word] = dict_tag
		for tag, count in dict_tag.items():
			tag_repeats = tags.count(tag)
			emission = count / tag_repeats
			emission_prob[word][tag] = float(format(emission, ".6f"))
			print("\t\t{0}\t\t{1}\t\t{2:.6f}".format(word.center(10), tag.center(7), emission))
	return emission_prob


# def emission_probabilities():
#     print("\nEmission Probabilities:\n")
#     uniqueListWords = set(listWords)
#     printEmission = []
#     l = list(uniqueListWords)
#     dictionary = dict((elem[0], []) for elem in l)
#     for tup in listWords:
#         dictionary.setdefault(tup[0], []).append(tup[1])
#     countList = []
# 
#     for myTag in beta:
#         countList.append(tagList.count(myTag))
# 
#     toPrint = []
#     for key in dictionary.keys():
#         temp = dictionary[key]
#         temp1 = list(set(temp))
#         for val in temp1:
#             countList[beta.index(val)]
#             toPrint.append((key, val,"%6f" %(float(float(temp.count(val)) / float(countList[beta.index(val)])))))
# 
#     toPrint.sort(key=lambda x: x[0])
#     for tup in toPrint:
#         i = tup[0]
#         if i.endswith("sses" or "xes" or "ches" or "shes"):
#             i = i[:-2]
#         elif i.endswith("ses" or "zes"):
#             i = i[:-1]
#         elif i.endswith("men"):
#             i = i[:-2] + "an"
#         elif i.endswith("ies"):
#             i = i[:-3] + "y"
#         print("{:>15}".format(str(i)), " ", str(tup[1]), " ", str(tup[2]))
#     counter = 0
#     index = 0
#     prev = ""
#     print("\nTransition Probabilities:\n")
#     a = []
#     myList = []
#     sentence_list = (inputFile.split("\n\n"))
#     for i in sentence_list:
#         a.append(i.split("\n"))
#     count = 0
#     prob = 0
# 
#     for tag in beta:
#         for sentence in a:
#             if tag == sentence[0].split(" ")[1]:
#                 count = count + 1
#         prob = (float(count) / float(len(a)))
#         if prob != 0:
#             myList.append("%6f" %prob)
#         count = 0
#     for i in range(len(myList)):
#         print(" [", beta[i], "|] ", myList[i], end='')
#     for i in beta:
#         while (index < len(beta)):
#             for j in tagList:
#                 if prev == i and j == beta[index]:
#                     counter = counter + 1
#                 prev = j
#             variable = countList[beta.index(i)]
#             prob = float(counter) / float(variable)
#             if prob != 0:
#                 print("[", beta[index], "|", i, "] ", "%6f" %prob, end='')
#             counter = 0
#             index = index + 1
#         index = 0
# 
# emission_probabilities()

		
def lemmatization(words):
	l_words = [''] * len(words)
	for i, w in enumerate(words):
		if w.endswith(("sses", "xes", "ches", "shes")):
			w_new = w[:-2]
		elif w.endswith(("ses", "zes")):
			w_new = w[:-2]
		elif w.endswith("men"):
			w_new = w[:-2] + "an"
		elif w.endswith("ies"):
			w_new = w[:-3] + "y"
		else:
			w_new = w
		l_words[i] = w_new
	return l_words


def dict_tags_and_tags(tags_list):
	tag_tag_dict = {}
	start_tags = list()
	end_tags = list()
	for tags in tags_list:
		start_tags.append(tags[0])
		length = len(tags)
		end_tags.append(tags[length - 1])
		tags.insert(0, START)
		tags.append(END)
		for i in range(len(tags) - 1):
			tag_tag_dict[tags[i]] = tag_tag_dict.get(tags[i], {})
			tag_tag_dict[tags[i]][tags[i + 1]] = tag_tag_dict[tags[i]].get(tags[i + 1], 0)
			tag_tag_dict[tags[i]][tags[i + 1]] += 1
	return tag_tag_dict
	
def transition_probabilities(tags_and_tags):
    print('\n')
    print("Transition Probabilities:")
    transition_prob = {}
    for key, tag_value in tags_and_tags.items():
        transition_prob[key] = tag_value
        counts = sum(tag_value.values())
        for inner_tags, value in tag_value.items():
            transition_prob[key][inner_tags] = float(
                format(transition_prob[key][inner_tags] / counts, ".6f"))
    sort_dict = sorted(transition_prob.items(), key=lambda x: x[0])
    ordered = collections.OrderedDict(sort_dict)
    count = 0
    for key in ordered:
        tag_dict = transition_prob[key]
        count += len(tag_dict)
        print("[{0:.6f}]".format((sum(tag_dict.values()))))
        sorted_tags = sorted(tag_dict.items(), key=lambda x: x[0])
        ord_tags = collections.OrderedDict(sorted_tags)
        for tag, val in ord_tags.items():
            print("[{0}|{1}] {2:.6f}".format(tag, key, val))
        

    return transition_prob, count
		
        
def train(input_train):
	line = list(filter(bool, input_train.split('\n\n')))
	tag_words = defaultdict(list)
	for index, sentence in enumerate(line):
		tag_words[index] = sentence.split('\n')
		
	outer_list = []
	for index, word in tag_words.items():
		inner_list = [[], []]
		for i, v in enumerate(word):
			parts = v.split(" ")
			inner_list[0].append(parts[0])
			inner_list[1].append(parts[1])
			
		outer_list.insert(index, inner_list)
	
	tags = list()
	words = list()
	list_of_tags = []
	unique_tag_counts = defaultdict(int)
	
	for item in outer_list:
		list_of_tags.append(item[1])
		tags += item[1] 
		words += item[0]
		unique_tag_counts[item[1][0]] += 1
	words = [word.lower() for word in words]
	distinct_tags(set(tags))
	initial_distribution(unique_tag_counts, len(line))
	word_lemmatization = lemmatization(words)
	words_and_tags = dict_words_and_tags(tags, word_lemmatization)
	tag_tag_dict = dict_tags_and_tags(list_of_tags)
	emission = emission_probabilities(words_and_tags, tags)
	transition, bigrams = transition_probabilities(tag_tag_dict)
	print("Corpus Features:")
	print("Total # tags:", len(set(tags)))
	print("Total # bigrams:", bigrams)
	print("Total # lexicals:", len(emission))
	print("Total # sentences", len(line))
	return emission, transition

def viterbi(emission, test_words_list, transition):
    final_tags = {}
    test_words = test_words_list[:]
    for word in test_words:
        if word not in emission:
            index = test_words.index(word)
            final_tags[word] = 'NN'
            test_words.pop(index)

    print("Test Set Tokens Found in Corpus: ")
    for word in test_words:
        print("\t\t", word, "  :")
        word_dict = emission.get(word)
        sorted_items = sorted(word_dict.items())
        ord_words = collections.OrderedDict(sorted_items)
        for tag, val in ord_words.items():
            format_value = float(format(val, '.6f'))
            print(tag, "(", format_value, ")")
    print("Intermediate Results of Viterbi Algorithm:")
    viterbi_list = []
    backpointer = []
    first_viterbi = {}
    first_backpointer = {}
    first_word_tags = emission[test_words[0]].keys()
    for tag in first_word_tags:
        if tag == START:
            continue
        sensor_model = emission[test_words[0]][tag]
        init_distribution = transition[START][tag]
        first_viterbi[tag] = init_distribution * sensor_model
        first_backpointer[tag] = None
    total = sum(first_viterbi.values())
    print("Iteration  1 : \t\t", test_words[0], ":")
    sorted_items = sorted(first_viterbi.items())
    ord_dict = collections.OrderedDict(sorted_items)
    for tag, prob in ord_dict.items():
        value = prob / total
        first_viterbi[tag] = value
        format_value = float(format(value, '.6f'))
        print(tag, " (", format_value, ",", first_backpointer[tag], " )")
    print()
    final_tags[test_words[0]] = max(first_viterbi, key=first_viterbi.get)
    viterbi_list.append(first_viterbi)
    backpointer.append(first_backpointer)
    for index, word in enumerate(test_words[1:]):
        corpus_tags = emission[word]
        prev_word_tags = viterbi_list.pop()
        print("Iteration", index + 2, ":", "\t\t", word, ":")
        max_dict = {}
        max_tag_dict = {}
        viterbi_dict = {}
        for tag in corpus_tags:
            best_max = 0
            best_prev_tag = None
            for prev_tag in prev_word_tags:
                prev_prob = prev_word_tags[prev_tag]
                transit_prob = transition[prev_tag].get(tag, 0.0001)
                emission_prob = emission[word][tag]
                current_prob = prev_prob * transit_prob * emission_prob
                if current_prob > best_max:
                    best_max = current_prob
                    best_prev_tag = prev_tag
            max_dict[tag] = best_max
            max_tag_dict[tag] = best_prev_tag
        total = sum(max_dict.values())
        sorted_items = sorted(max_dict.items())
        ord_items = collections.OrderedDict(sorted_items)
        for max_tag, max_prob in ord_items.items():
            value = max_prob / total
            viterbi_dict[max_tag] = value
            format_value = float(format(value, ".6f"))
            print(max_tag, "(", format_value, ",", max_tag_dict[max_tag], ")")

        viterbi_list.append(viterbi_dict)
        final_tags[word] = max(viterbi_dict, key=viterbi_dict.get)
       
    return final_tags


def calculate_prior_distribution_of_tags(tags):
    tag_list = list(filter(bool, tags))
    len_of_tags = len(tag_list)
    tag_dict = defaultdict(int)
    for tag in tag_list:
        tag_dict[tag] += 1
    print(sum(tag_dict.values()))
    print("length:", len_of_tags)
    for tag, count in tag_dict.items():
        print(tag, " ", count / len_of_tags, count)


def test_file(test_content):
    sentences = list(filter(bool, test_content.split('\n')))
    sentence_split = []
    for sentence in sentences:
        lower = sentence.lower()
        sentence_split.append(lower.split())
    return sentence_split


def tagger_output(words, tags):
    for i in range(len(words)):
        print("\t\t", "{0}".format(words[i]).center(7), " ")
        print("{0}".format(tags[words[i]]).center(5))



def main(training, testing):
	print('University of Central Florida')
	print('CAP6640 Spring 2018 - Dr.Glinos')
	print('\n') 
	training = open(training + ".txt")
	testing = open(testing + ".txt")
	input_train = training.read()
	input_test = testing.read()
	emission_dict, transition_dict = train(input_train)
	test_sentences = test_file(input_test)
	for test_words in test_sentences:
		final_tags = viterbi(emission_dict, test_words, transition_dict)
		print("Viterbi Tagger Output: ")
		tagger_output(test_words, final_tags)
	
	
	
main('pos.train', 'sample_3')
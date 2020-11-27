#imports
import wordcloud
from matplotlib import pyplot as plt


#function to calculate frequencies of words
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_|~'''
    # punctuations = ['!','(',')','-','[',']','{','}',';',':','\'','\"',',','<','>','.','/','\\','?','@','#','$','%','^','&','*','_','~']
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","for","to","on",
    "not","I","in"]
    new_string = ""
    
    for character in file_contents:
        if character.lower() not in punctuations:
            new_string += character.lower()
    
    new_words = new_string.split(' ')
    dict = {}
    for word in new_words:
        if word not in uninteresting_words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 0
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict)
    return cloud.to_array()

#openning the file
file1 = open("<file name.txt>","r")
file_contents = file1.read()
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
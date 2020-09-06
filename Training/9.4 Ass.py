sentence= input("Enter a sentence: ")

words= sentence.split(' ')
smallest_word_len=len(sentence)
largest_word_len=0
for i in words:
    if len(i)< smallest_word_len:
        smallest_word_len= len(i)
    if len(i)> largest_word_len:
        largest_word_len= len(i)
        
for i in words:
    if len(i) == smallest_word_len:
        print('Smallest Word', i)
    if len(i) == largest_word_len:
        print('Largest Word', i)

vowels_count=0
consonents_count=0
whitespace_count=0
for x in sentence:
        if  x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            vowels_count+=1
        elif x==' ':
            whitespace_count+=1
        else:
            consonents_count+=1
print("Vowels Count:",vowels_count)
print("Consonents Count",consonents_count)
print("Whitespaces Count",whitespace_count)

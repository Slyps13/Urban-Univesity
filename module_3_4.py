def single_root_words (root_word,*other_words) :
  same_words = []
  root_word_l = root_word.lower()
  for i in range (len(other_words)) :   
    if (root_word_l in other_words[i].lower()) or (root_word_l.count(other_words[i].lower()) > 0 ):
      same_words.append(other_words[i])
  return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

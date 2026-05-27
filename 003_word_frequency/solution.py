def word_frequency(sentence: str) -> dict:
    # Write your solution here
    # create an empty dict then .split() the whole sentence and count how many words are dupes. count goes up by 1 else juse 1, no dupes. 
    
    d = {}
    for word in sentence.lower().split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
        
    return d

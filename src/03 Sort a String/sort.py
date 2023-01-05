def sort_words(strings):
    words = strings.split()
    words.sort(key=str.lower)
    reply = ''
    for word in words:
      reply = reply + word+ " "
    return reply

w = input("Enter strings to sort: ")
print(sort_words(w))
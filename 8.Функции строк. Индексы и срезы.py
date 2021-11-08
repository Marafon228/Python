word = "FootBall, skaTe, baSKetball"
#print(word.count("e"))
#print(word.capitalize())
#print(word.find('pr')) для поиска символов
hobby = word.split(', ')

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ", ".join(hobby)
print(result)


import random
def main():
    if __name__ == '__main__':
        readFile()
def readFile():
    readFile.lines = [line.rstrip('\n') for line in open('words.txt')]

readFile()
print(readFile.lines)

word = random.choice(readFile.lines)
word_size=len(word)
new_word = "*" * word_size
input_letter_list = []
i=""
if len(word) > 10:
    ranges = word_size
else:
    ranges = 10
for x in range(ranges):
    input_letter = input("Enter the one letter word or "+ str(word_size) + " length word" )
    if input_letter in input_letter_list:
        print("You have already entered this letter")
        x+=1
        continue
    input_letter_list.append(input_letter)
    if input_letter == word:
        new_word = word
        break
    occurrences = word.count(input_letter)
    indice = [i for i, a in enumerate(word) if a == input_letter]
    if len(indice) ==0:
        print("input letter is not present in the word, please enter another word")
    for y in indice:
        new_word_2 = new_word[:y]+input_letter+new_word[y+1:]
        new_word = new_word_2
    if(new_word == word):
        print("YOU WON!!")
        break
    print(new_word)

if(new_word==word):
    print("Game finished ", "word : "+word)

if new_word!=word:
    print("YOU LOST!!!!!")




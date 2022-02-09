# Funktio vastaanottaa sanan , laskee sen pituuden, tallentaa sanan väärinpäin uuten muuttujaan ja palauttaa sen
def reverse(word, lowercase):
        word_length = len(word)
        i = 1
        reverse_word = ""
        while word_length >= i:
            reverse_word = reverse_word + word[-(i)]
            i = i+1
        if lowercase == True:
            return reverse_word.casefold()
        else:
            return reverse_word

print(reverse("Kalle", lowercase= True))
print(reverse("Kalle", lowercase= False))
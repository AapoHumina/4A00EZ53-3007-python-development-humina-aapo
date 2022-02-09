# Funktio vastaanottaa sanan , laskee sen pituuden, tallentaa sanan väärinpäin uuten muuttujaan ja palauttaa sen
def is_palindrome(word, lowercase):
    word_length = len(word)
    reverse_word = ""
    if lowercase == True:
        word = word.casefold()
    i = 1
    while word_length >= i:
        reverse_word = reverse_word + word[-(i)]
        i = i+1
    if reverse_word == word:
        return True
    else:
        return False


print(is_palindrome("Saippuakauppias", lowercase= True))
print(is_palindrome("Saippuakauppias", lowercase= False))
print(is_palindrome("Kalle", lowercase= False))
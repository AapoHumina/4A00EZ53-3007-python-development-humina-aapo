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

import unittest

class TestMain(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("Saippuakauppias", lowercase=True), "saippuakauppias")
        self.assertEqual(reverse("AAPO", lowercase=True), "opaa")
        self.assertEqual(reverse("Aapo", lowercase=True), "opaa")
        self.assertEqual(reverse("Aapo", lowercase=False), "opaA")
        self.assertEqual(reverse("OLLI", lowercase=True), "illo")
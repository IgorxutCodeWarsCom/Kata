def disemvowel(string):
    return string.translate(
        {
            ord("a"): "", ord("e"): "", ord("i"): "", ord("o"): "", ord("u"): "",
            ord("A"): "", ord("E"): "", ord("I"): "", ord("O"): "", ord("U"): "",
        }
    )

def let_it_be(n):

    return '\n'.join(['let it be,']*n)

def sing():

    song=let_it_be(4)
    song+='\nthere will be an answer,\n'
    song+=let_it_be(5)
    song+='\nwhisper words of wisdom, let it be'

    return song

print(sing())
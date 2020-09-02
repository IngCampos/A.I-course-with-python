def first_letter(letter_list):
    first_letters = []

    for word in letter_list:
        try:
            assert type(word) == str, f'{word} is not str'
            assert len(word) > 0, 'String empty is not allowed'
            first_letters.append(word[0])
        except AssertionError as e:
            print(e)
    return first_letters


letter_list = ['Martin', 'Campos', '', 123]

print(first_letter(letter_list))

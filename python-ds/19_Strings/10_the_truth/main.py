def decode_word(word):
    decoded_word = ''
    for i_sym in word:
        if i_sym.isupper():
            decoded_word += alphabet[alphabet.index(i_sym.lower()) - 1].upper()
        else:
            decoded_word += alphabet[alphabet.index(i_sym) - 1]
    return decoded_word


def shift_word(word):
    shifted_word = ''
    for i_sym in range(len(word)):
        shifted_word += word[(i_sym - shift) % len(word)]
    if '.' in shifted_word:
        shifted_word += '\n'
    return shifted_word


text = '''vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'''
alphabet = '''abcdefghijklmnopqrstuvwxyz!",-./'(*+'''
shift = 3

text_list = text.split()

decoded_string = [decode_word(i_word) for i_word in text_list]

decoded_text = []

for i_word in decoded_string:
    decoded_text.append(shift_word(i_word))
    if '.' in i_word:
        shift += 1

print(' '.join(decoded_text))

# зачёт!

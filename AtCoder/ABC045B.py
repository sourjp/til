
def my_turn(card_list):
    global cont_game
    global your_turn
    if card_list:
        your_turn = card_list[0]
        card_list.pop(0)
    else:
        cont_game = False

card_a = [ _ for _ in input()]
card_b = [ _ for _ in input()]
card_c = [ _ for _ in input()]

your_turn = 'a'
cont_game = True

while cont_game:
    if your_turn == 'a':
        my_turn(card_a)
    if your_turn == 'b':
        my_turn(card_b)
    if your_turn == 'c':
        my_turn(card_c)

print(your_turn.upper())
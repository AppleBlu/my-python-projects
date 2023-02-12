
def card_picked(card):
  if card >= '1':
    return 'Go higher!' 
  elif card >= '6':
    return 'Go lower!'
  else:
    return 'You need to enter your card'
  

print(card_picked('2'))



card_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,] 
card_list_2 = [6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]

count = card_list.count(range(1, 5))
count_2 = card_list_2.count(range(6, 10))


card_list_3 = range(1, 11)

print(card_list)
print(list(card_list_2))
print(list(card_list_3))



print('There is another ' + str(len(card_list + card_list_2)) + ' cards in the deck')

print(count)
print(count_2)
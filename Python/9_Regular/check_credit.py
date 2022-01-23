
import re
card_no = "3387-7573-8679-3456"  # Given input
card = card_no.split("-")
new_card = ''.join(card)
group = list(set([len(i) for i in card]))

valid = False
if len(new_card) == 16 and len(re.findall("\d",new_card)) == 16 and group[0] == 4: # check length of 16 digits and 16 digits are integer
    if re.findall("\A3", card_no) or re.findall("\A4", card_no) or re.findall("\A9", card_no): # check card start with 3 or 4 or 9
        valid = True
        
c=0
if valid == True:  # if card valid then check it contains more than two consecutive digits. If yes then card is not valid
    for i in range(len(new_card) - 2):
        if new_card[i] == new_card[i + 1] and new_card[i + 1] == new_card[i + 2]:
            c+=1
            if c == 1:
                valid = False
                break

                
if valid == True:
    print("Credit Card is Valid")
else:
    print("Credit Card is not Valid")
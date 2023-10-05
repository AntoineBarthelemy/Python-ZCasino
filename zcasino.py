"""Welcome to the ZCasino, a random wheel game """

"""Explication of the Rules:
The player (you), bets on a number between 0-49 fifty in all. After your bets you should specify how many cash you want to bets. Be Careful !!
to don't loose everythings you have. You start the game with one thousand dollars. Next, the croupier will start to turn run the wheel and launch
the beal. When the wheel has stopped, the croupier recovers the information of the beal's position and compare your choice. If both are identics
low probability 1/50 then the gain is multiply by 3. Else if the both are in the same category (impair, pair) The gain is situated at the middle 50%
of your choice. Finnaly if, nothings match 😢 you loose your bets."""

"""First possibility: You bets 1000 dollars, you will win 3000 dollars, you will be at 4000 dolars 💵.
   Second possibility: You bets 1000 dollars, you will win 500 dollars, you will be at 1500 dollars 😁.
   Third possibility: You bets 1000 dollars, you will loose 1000 dollars, you will be at 0. 😢"""

# Import modules
import random
import math
import time




# Declaration of global variables

user_choice = input("Veuillez saisir un nombre compris entre 0 et 49 inclus ")
pair_array = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48] # Array in Js or List in Python
impair_array =[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49] # Array in Js or List in Python
bank_account = 1000




# Declaration of fonctions




def value_comparaison (user_choice, paid_sum_user, bank_account, result_game): # Fourth treatement
    global pair_array, impair_array

    if user_choice == result_game:
        print(f"Vous avez gagné: {paid_sum_user * 3} euros, car lorsque la roue s'est arrêté, la bille était positionnée sur la case : {result_game}.  Votre crédit s'élève donc à : {(paid_sum_user *3) + paid_sum_user + bank_account} euros.💵 ")
        first_possibility = (paid_sum_user * 3) + paid_sum_user + bank_account
        

    elif user_choice in pair_array and result_game in pair_array or user_choice in impair_array and result_game in impair_array:
        print(f"Vous avez gagné {math.ceil(paid_sum_user * 0.5) } euros, car lorsque la roue s'est arrêté, la bille était positionnée sur la case : {result_game}. Votre crédit s'élève donc à { (math.ceil(paid_sum_user * 0.5)) + paid_sum_user + bank_account} euros.😁  ")
        second_possibility = math.ceil((paid_sum_user * 0.5)) + paid_sum_user + bank_account
        
        
    else:
        print(f"Vous avez perdu {paid_sum_user} euros, car lorsque la roue s'est arrêté, la bille était positionnée sur la case : {result_game}. Votre crédit s'élève donc à : {bank_account - paid_sum_user} euros.😢")
        third_possibility = bank_account - paid_sum_user
       
        
  

def game_start (user_choice, paid_sum_user, bank_account): # Third treatement
    while True:
        display_game = input("Le croupier fait tourner la roulette et lâche la bille ... [press Q for see the result] ")
        
        if display_game == "Q":
            result_game = random.randint(0,49) # Local variable
            value_comparaison(user_choice, paid_sum_user, bank_account, result_game)
           
            break 

        else:
            continue
    


def paid_sum (user_choice, bank_account): # Second treatement
    paid_sum_user = input(f"Veuillez saisir la somme que vous souhaitez miser (crédit: {bank_account}). ") # Local variable

    try:
        paid_sum_user = int(paid_sum_user)
        if paid_sum_user > 0 and paid_sum_user <= bank_account:
            print(f"Vous avez choisi : {paid_sum_user} euros sur votre compte actuelle qui s'éléve à {bank_account} euros")
            game_start(user_choice, paid_sum_user, bank_account)

        else:
          raise ValueError
        
    except ValueError:
        print(f"La valeur saisi n'est pas correcte. Veuillez réessayer ...")
        time.sleep(2)
        paid_sum(user_choice, bank_account)
        
        

   


def choice_number (user_choice, bank_account): # First treatement
    # assert bank_account != 0


    try:
        user_choice = int(user_choice)
        print(bank_account)

        if user_choice <= 49 and user_choice >= 0:
            print(f"Vous avez choisi : {user_choice}")
            paid_sum(user_choice, bank_account)
            
        else:
            raise ValueError
        
        
    except ValueError:
        print("La valeur saisi ne correspond pas aux critères demandés")
       

# Call to the function in the global area

choice_number(user_choice, bank_account)



    














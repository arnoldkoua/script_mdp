"""
Dans cet exercice, vous devez :

Afficher la phrase mdp_trop_court en majuscule si le mot de passe entrÃ© est Ã©gal Ã  0.

Afficher la phrase mdp_trop_court avec une majuscule sur la premiÃ¨re lettre si le mot de passe entrÃ© est plus petit que 8.

Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entrÃ© ne contient que des nombres.

Afficher la phrase "Inscription terminÃ©e." si le mot de passe est valide.

Script de dÃ©part :
"""

"""mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

Questions pour cet exercice
Comment utiliser les structures conditionnelles et 
des mÃ©thodes de chaÃ®nes de caractÃ¨res pour vÃ©rifier 
la validitÃ© du mot de passe ?"""

#Solution

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0 or mdp == "0":
    print(mdp_trop_court.upper())
elif len(mdp) > 0 and len(mdp) < 8:
    print(mdp_trop_court.capitalize())
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")

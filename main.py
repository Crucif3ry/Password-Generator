import random

print("""
__________         ________                
\______   \___.__./  _____/  ____   ____   
 |     ___<   |  /   \  ____/ __ \ /    \  
 |    |    \___  \    \_\  \  ___/|   |  \ 
 |____|    / ____|\______  /\___  >___|  / 
           \/            \/     \/     \/ """) 
print("Par Crucif3ry et SeeZ \n")

lettrefull="azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890$£ù%*µ/!§@#()&-_^;+{}"
nombre="1234567890"

def main():
  while True:
    choix=input("1.Mot de passe\n2.code PIN\nRentrez un nombre : ")
    if choix == "1":
      classic()
      break
    if choix == "2":
      pin()
      break
    print("rentrez un nombre entre 1 et 2")
   
def classic(): 
   while True:
    longeur=int(input("Longeur du mot de passe: "))
    
    motdepasse= "".join(random.sample(lettrefull,longeur))
    
    print("Voici ton mot de passe :",motdepasse)
    
    break

def pin():
  while True:
    longeurpin=int(input("Longeur du code PIN: "))

    codepin= "".join(random.sample(nombre,longeurpin))

    print("Voici ton code pin :",codepin)

    break
  

if __name__ == '__main__':
 main()
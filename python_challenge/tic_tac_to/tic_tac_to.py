def afficher_plateau(plateau):
  s = ""
  for i in range(3):
    print("_____________")
    for j in range(3):
      s += f"| {plateau[i][j]} "
    s+="|"
    print(s)
    s = ""
  print("_____________")


def verifier_victoire(plateau, joueur):
  # Vérification des lignes
  for i in range(3):
    if plateau[i][0] == plateau[i][1] == plateau[i][2] == joueur:
      return True

  # Vérification des colonnes
  for j in range(3):
    if plateau[0][j] == plateau[1][j] == plateau[2][j] == joueur:
      return True

  # Vérification des diagonales
  if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
    return True

  if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
    return True

  return False


def jouertictactoe():
  plateau = [[" " for _ in range(3)] for _ in range(3)]
  joueur = "X"
  tour = 1
  victoire = False

  while tour <= 9 and not victoire:


    print("Tour", tour)
    print("Joueur", joueur)

    ligne = -2
    while True and (ligne > 2 or ligne < 0) :
      if ligne > 2 or ligne < 0:
        print("Enter a valid integer")
      try:
        ligne = int(input("Choisissez la ligne (0, 1, 2) : "))
        print(ligne)
      except ValueError:
        print('Enter a valid integer')


    colonne = -2
    while True and (colonne > 2 or colonne < 0):
      if colonne > 2 or colonne < 0:
        print("Enter a valid integer")
      try:
        colonne = int(input("Choisissez la colonne (0, 1, 2) : "))
        print(colonne)
      except ValueError:
        print('Enter a valid integer')



    if plateau[ligne][colonne] == " ":
      plateau[ligne][colonne] = joueur
      if verifier_victoire(plateau, joueur):
        victoire = True
        print("Joueur", joueur, "a gagné !")
      else:
        joueur = "O" if joueur == "X" else "X"
        tour += 1
    else:
      print("Case déjà occupée !")

    afficher_plateau(plateau)

  if not victoire:
    print("Match nul !")


jouertictactoe()
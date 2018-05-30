
"""
Auteur : NGUYEN Van An  
Date : Dimanche 29 Avril 2018
Titre : Geometrie (Calcul Aire, Perimetre)
Description : Triangles, quadrilatères, cercles,  ellipses
"""
import math

Continuer = True

while(Continuer == True):
      """
      Segment : Affichage du menu de sélection des polygones
      """
      print("1- Triangles")
      print("2- Quadrilatères (Carré, Rectangle, Parallélogramme, Losange, Deltoïde")
      print("3- Cercle")
      print("4- Ellipse", "\n")
      print("5- Polygone régulier a n-côtés")
      Option1 = int(input("Quelle est le type de polygone? "))

      if (Option1 == 1):
            BaseTriangle = int(input("Base du triangle : "))
            HauteurTriangle = int(input("Hauteur du triangle : "))
            AireTriangle = BaseTriangle * HauteurTriangle / 2
            QuestionTriangleRectangle = input("Est-ce un triangle rectangle (o/n)? ")
            if(QuestionTriangleRectangle != "o" or QuestionTriangleRectangle != "n"):
                  if(QuestionTriangleRectangle == "o"):
                  QuestionHypotenuse = input("Voulez-vous connaître la longueur de l'hypoténuse (o/n)? ")
                  if(QuestionHypotenuse == "o"):
                        QuestionHypotenuse2 = input("Est-ce que la hauteur correspondait aux cathètes (o/n)? ")
                          if(QuestionHypotenuse2 == "o"):
                              LongueurHypotenuse = math.sqrt(HauteurTriangle * HauteurTriangle + BaseTriangle * BaseTriangle)
                              print("La longueur de l'hypoténuse du triangle est", LongueurHypotenuse, "unités.")
              print("L'aire du triangle est", AireTriangle, "unités carrés")
        
      elif(Option1 == 2):
            """
            Segment : Affichage du menu de sélection des quadrilatères
            """
            print("1- Carré")
            print("2- Rectangle")
            print("3- Trapèze")
            print("4- Deltoïde")
            print("5- Parallélogramme")
            print("6- Losange")
            Option2 = int(input("Quelle est le type de quadrilatères?"))

            """
            Segment : Carré
            """
            if(Option2 == 1):
                  CoteCarre = int(input("Côté du carré : "))
                  AireCarre = CoteCarre * CoteCarre
                  print("L'aire du carré est", AireCarre, "unités carrés.")

            """
            Segment : Rectangle
            """
             elif(Option2 == 2):
                  BaseRectangle = int(input("Base du rectangle : "))
                  HauteurRectangle = int(input("Hauteur du rectangle : "))
                  AireRectangle = BaseRectangle * HauteurRectangle
                  print("L'aire du rectangle est", AireRectangle, "unités carrés.")

            """
            Segment : Trapèze
            """
             elif(Option2 == 3):
                  PetiteBaseTrapeze = int(input("Petite base du trapèze : "))
                  GrandeBaseTrapeze = int(input("Grande base du trapèze : "))
                  HauteurTrapeze = int(input("Hauteur du trapèze : "))
                  AireTrapeze = (PetiteBase + GrandeBase) * HauteurTrapeze / 2
                  print("L'aire du rectangle est", AireRectangle, "unités carrés")

            """
            Segment : Deltoïde
            """
            elif(Option2 == 4):
                  PetiteHauteurDeltoide = int(input("Petite hauteur du deltoïde : "))
                  GrandeHauteurDeltoide = int(input("Grande hauteur du deltoïde : "))
                  BaseCommuneDeltoide = int(input("Base commune du deltoïde : "))
                  AireDeltoide = BaseCommuneDeltoide * (abs(PetiteHauteurDeltoide - GrandeHauteurDeltoide)) / 2
                  print("L'aire du deltoïde est", AireDeltoide, "unités carrés.")

            """
            Segment : Parallélogramme
            """
            elif(Option2 == 5):
                  BaseParallelo = int(input("Base du parallélogramme : "))
                  HauteurParallelo = int(input("Hauteur du parallélogramme : "))
                  AireParallelo = BaseParallelo * HauteurParallelo
                  print("L'aire du parrallélogramme est", AireParallelo, "unités carrés.")

            """
            Segment : Trapèze
            """
            elif(Option2 == 6):
                  PetiteDiagonaleLosange = int(input("Petite diagonale du losagnge : "))
                  GrandeDiagonaleLosange = int(input("Grande diagonale du losange : "))
                  AireLosange = PetiteDiagonaleLosange * GrandeDiagonaleLosange / 2
                  print("L'aire du losage est", AireLosange, "unités carrés.")

      elif(Option1 == 3):
        RayonCercle = int(input("Rayon du cercle : "))
        Pi = 3.14159
        AireCercle = RayonCercle * RayonCercle * Pi
        CirconférenceCercle = 2 * RayonCercle * Pi
        print("L'aire du cercle est", AireCercle, "unités carrés.")
        print("La circonférence du cercle est", CirconferenceCercle, "unités")

      """
      Segment : Ellipse
      """
      elif(Option1 == 4)
            DistanceFocale = int(input("Demi-focale de l'ellipse :))
            DistanceY = int(input("Semi-mineur de l'ellipse: "))
            Pi = 3.14159
            AireEllipse  = Pi * DistanceFocale * DistanceY
      
      """
      Segment : Polygone régulier à n-côtés
      """
      elif(Option2 == 5):
            nCote = int(input("Nombre de côtés :  "))
            Option2ApotemeCote = input("Avez-vous les mesures de l'apotème et du côté du polygone (o/n)? ")
            if(Option2ApotemeCote == "o"):
                  ApotemePolygone = int(input("Apoteme du polygone : "))
                  CotePolygone = int(input("Côté du polygone : "))
                  AirePolygone = (ApotemePolygone * CotePolygone / 2) * nCote
                  PerimetrePolygone = CotePolygone * nCote
                  
      """   
      Segment : Confirmation de la continuation du processus
      """
    Question = input("Voulez-vous continuer (Oui/ Non)? ")
    while(Question != "Oui" and Question != "Non"):
        Question = input("Veuillez entrer un réponse valide. ")
    if(Question == "o"):
        Continuer = True
    elif(Question == "n"):
        Continuer = False
    CompteurSigne = 0
    while(CompteurSigne < 30):
        print("=",sep='', end='')
        CompteurSigne = CompteurSigne + 1
    print("\n")

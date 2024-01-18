
#1----------------------------------------------------------------
la_liste_films = []

def list_initiale():
    global la_liste_films

    la_liste_films = [{
        'nom': 'Inception',
        'realisateur': 'Christopher Nolan',
        'annee': 2016,
        'budget': 160
    }]

    print("La liste est initialisee a {}:".format(la_liste_films))

#1----------------------------------------------------------------
def create_film():
    print('Entrez nom du film')
    nom = input()
    print('Entrez realisateur du film')
    realisateur = input()

    print('Entrez annee du film')

    try:
        annee = int(input())
        if annee > 2024:
            print("Ce film n\'est pas encore sorti?")
    except ValueError:
        print("L'annee n'est pas valide")
        menu()

    print('Entrez budget du film')

    try:
        budget = float(input())
    except ValueError:
        print("Le budget n'est pas valide")
        menu()

    film = {
        'nom': nom,
        'realisateur': realisateur,
        'annee': annee,
        'budget': budget
    }

    la_liste_films.append(film)

    print('Le film {} a été enregistré.'.format(film['nom']))

    return la_liste_films


#2--------------------------------------------------------
def info_film(film):
    print('Le film {} a été réalisé par {} au cours l\'année {} avec un budget de {} million de dollars.'.format(film['nom'], film['realisateur'], film['annee'], film['budget']))


#3--------------------------------------------------------
def lister_films():
    for film in la_liste_films:
        info_film(film)


#4--------------------------------------------------------
def budget_moyen():
    avg = float(sum(film['budget'] for film in la_liste_films)) / len(la_liste_films)
    print(f'budget moyen est: :', avg)


#5--------------------------------------------------------
def rechercher_film():
    print(' Entrez le titre/nom du film a rechercher')
    nom = input()
    result = None
    for film in la_liste_films:
        if film['nom'].lower() == nom.lower() :
            result = film
            break

    if result:
        info_film(result)
    else:
        print("Le film n'existe pas dans notre liste")


#6----------------------------------------------------------------
def rechercher_selon_budget():
    print("Entrez le budget seuil")
    try:
        budgetSeuil = float(input())
    except TypeError:
        print("Le budget est un montant. veuilez entrer une somme valide")

    filmsDepassantBudgetSeuil = list( filter(lambda x: x['budget'] > budgetSeuil, la_liste_films) )
    
    if not filmsDepassantBudgetSeuil:
        print("Aucun film depassant ce budget de {}".format(budgetSeuil))
        
    for film in filmsDepassantBudgetSeuil:
        info_film(film) 


#7----------------------------------------------------------------
def supprimer_film():
    print(' Entrez le titre/nom du film a supprimer')
    nom = input()
    deleted = False
    
    for i in range(len(la_liste_films)):
        if la_liste_films[i]['nom'] == nom:
            del la_liste_films[i]
            deleted = True
            break

    if deleted:
        print('Le film a bien ete supprime'.format(nom))
        print('Voici la nouvelle liste:')
        lister_films()
    else:
        print("Le film {} n'existe pas dans notre liste, et donc n'a pas ete supprime".format(nom))


#8--------------------------------
def menu():
    choixUser = True
    while choixUser:
        menuList = """
        1 = Ajout d'un nouveau film
        2 = Imprimer tous les films stockés dans liste_films
        3 = Imprimer le budget moyen
        4 = Rechercher un film dont le titre est saisi par l'utilisateur
        5 = Rechercher tous les films dont le budget est supérieur à un montant saisi par l'utilisateur
        6 = Supprimer un film dont le titre est saisi par l'utilisateur
        7 = Réinitialiser la liste comme question 1
        0 =  Quitter"""

        print(menuList)

        try:
            choixUser = int(input())
            print("Votre choix est {}".format(choixUser))
            if choixUser == 0:
                exit()
            elif choixUser == 1:
                create_film()   
            elif choixUser == 2:
                lister_films()   
            elif choixUser == 3:
                budget_moyen()   
            elif choixUser == 4:
                rechercher_film()  
            elif choixUser == 5:
                rechercher_selon_budget()
            elif choixUser == 6:
                supprimer_film()     
            elif choixUser == 7:
                list_initiale()  
            elif choixUser >= 8:
                print("Ce menu n'est pas disponible. Veuillez faire un choix entre les chiffres de 0 a 7")
            else:
                print("choix non valide") 
        except TypeError:
            print("Votre choix n'est pas valide")
            print(type(choixUser))



if __name__ == '__main__':
    #list_initiale()
    #create_film()
    #lister_films()
    #budget_moyen()
    #rechercher_film()
    #rechercher_selon_budget()
    #supprimer_film()
    list_initiale()
    menu()

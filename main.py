import pygame
import time
from random import randint

pygame.init()

# Définir les couleurs utilisées dans le programme
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


#Création d'une fenêtre en plein écran
monEcran = pygame.display.set_mode((1920, 1080))

#Récupération de la résolution de l'écran
width = 1920
height = 1080

pygame.display.set_caption("Starship Savior")

#Chargement de la musique
pygame.mixer.music.load("Sons/interstellar.mp3")
pygame.mixer.music.play(-1)

# Charger les images de fond
images_fond = [
    "Cine/home.gif",
    "Cine/cine1.jpg",
    "Cine/cine2.jpg",
    "Cine/cine3.jpg"
]

# Définir l'index de l'image de fond actuelle
index_fond = 0
fond = 0

# Affichage du fond d'écran
background_image = pygame.image.load("Cine/home.gif")
background_image = pygame.transform.scale(background_image, (width, height))
monEcran.blit(background_image, (0, 0))

GOP = pygame.font.Font("Polices/GearsOfPeace.ttf", 150)
titre = GOP.render("Starship Savior", 1, (255,255,0))
titre_rect = titre.get_rect()
x, y = monEcran.get_rect().center
y-=200
titre_rect.center = (x,y)
monEcran.blit(titre, titre_rect)

GOP = pygame.font.Font("Polices/GearsOfPeace.ttf", 30)
soustitre = GOP.render("Press [SPACE] or [>]", 1, (255,255,0))
soustitre_rect = soustitre.get_rect()
x, y = monEcran.get_rect().center
y += 100
soustitre_rect.center = (x,y)
monEcran.blit(soustitre, soustitre_rect)

texte1 = [
        "Le monde était divisé en deux parties distinctes :",
        "d'un côté, une population pauvre et affamée,",
        "luttant pour survivre dans des conditions de vie",
        "inhumaines, et de l'autre, une élite privilégiée",
        "vivant dans l'opulence.",
        "La technologie n'avait fait qu'aggraver les inégalités.",
        "La vie était devenue un jeu à somme nulle,",
        "où les riches prospéraient et les pauvres mouraient.",
        "L'espoir était faible, car l’élite n'avait aucun",
        "intérêt à partager ses avantages, et les démunis",
        "étaient condamnés à vivre dans une souffrance perpétuelle.",
        "Mais cette société aux tendances dystopiques a disparu du jour",
        "au lendemain pour laisser place à bien pire :",
        "l'attaque des Bâtisseurs.",
        " ",
        "Press [SPACE] or [>]"
          ]

texte2 = [
        "Arrivés par milliers depuis les cieux, les Bâtisseurs",
        "s’étaient rendus sur Terre avec un seul objectif :",
        "y fonder une nouvelle civilisation. Face à cette situation",
        "critique, les gouvernements du monde entier se réunirent",
        "en urgence pour élaborer une stratégie de défense",
        "commune. Des armées furent mobilisées, de nouvelles",
        "armes furent développées et pour la première fois le",
        "monde entier s’unit contre un ennemi commun.",
        "Le conflit entre les Bâtisseurs et l'humanité fut long et sanglant.",
        "Les envahisseurs semblaient dotés d'une technologie bien",
        "supérieure à celle des humains, mais ces derniers avaient une",
        "volonté sans pareille. Des villes furent détruites, des populations",
        "massacrées, mais les humains ne baissèrent pas les bras.",
        " ",
        "Press [SPACE] or [>]"
        ]

texte3 = [
        "L’heure de l’affrontement final est enfin arrivée. Cependant,",
        "alors que votre escouade affrontait les dernières forces des",
        "Bâtisseurs, une riposte de ces derniers a réduit en morceaux",
        "les vaisseaux de vos alliés. Vous devez maintenant vaincre",
        "les derniers bâtisseurs par vos propres moyens !",
        "Mais vous avez trouvé leur faille :",
        "chacun d’entre eux a une zone rouge sur son corps",
        "qui indique son point faible...",
        " ",
        "Press [SPACE] or [>]"
        ]

cinematique = True
# Boucle principale
while cinematique :
    # Gestion des événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            try :
                jeu_en_cours = False
                cinematique = False
                accueil = False
                levels = False
                pygame.quit()
            except :
                pass
        elif evenement.type == pygame.KEYDOWN:  
            if evenement.key == pygame.K_RIGHT:
                fond = 7
                pass
            elif evenement.key == pygame.K_SPACE:
                fond += 1
                # Changer d'image de fond
                index_fond = (index_fond + 1) % len(images_fond)
                
                # Effacer le texte précédent
                monEcran.fill(NOIR)

                background_image = pygame.image.load(images_fond[index_fond])
                background_image = pygame.transform.scale(background_image, (width, height))
                monEcran.blit(background_image, (0, 0))
                break
            
    if fond == 1 :
        BAT = pygame.font.Font("Polices/batman.ttf", 60)
        text = "Terre, an 2154."
        delay = 15  # en millisecondes
        color = pygame.Color('yellow')
        x = 50
        y = 50
        for i in range(len(text)):
            char = text[i]
            text_surface = BAT.render(char, True, color)
            monEcran.blit(text_surface, (x, y))
            pygame.display.update()
            pygame.time.delay(delay)
            x += text_surface.get_width()
        y += 40
        fond += 1
        for ligne in texte1 :
            x = 50
            y += 40
            BAT = pygame.font.Font("Polices/batman.ttf", 20)
            for i in range(len(ligne)):
                char = ligne[i]
                text_surface = BAT.render(char, True, color)
                monEcran.blit(text_surface, (x, y))
                pygame.display.update()
                pygame.time.delay(delay)
                x += text_surface.get_width()
    
    if fond == 3 :
        color = pygame.Color('yellow')
        y = 50
        fond += 1
        for ligne in texte2 :
            x = 50
            y += 40
            BAT = pygame.font.Font("Polices/batman.ttf", 20)
            for i in range(len(ligne)):
                char = ligne[i]
                text_surface = BAT.render(char, True, color)
                monEcran.blit(text_surface, (x, y))
                pygame.display.update()
                pygame.time.delay(delay)
                x += text_surface.get_width()
                
    if fond == 5 :
        color = pygame.Color('yellow')
        y = 50
        fond += 1
        for ligne in texte3 :
            x = 50
            y += 40
            BAT = pygame.font.Font("Polices/batman.ttf", 20)
            for i in range(len(ligne)):
                char = ligne[i]
                text_surface = BAT.render(char, True, color)
                monEcran.blit(text_surface, (x, y))
                pygame.display.update()
                pygame.time.delay(delay)
                x += text_surface.get_width()
                
    if fond == 7 :
        cinematique = False
        jeu_en_cours = True
        
    # Rafraîchir l'affichage de la fenêtre
    pygame.display.flip()























accueil = True
jeu = False
son = True
g = True
difficulty = 'Easy'
levels = False


menu_theme = pygame.mixer.Sound("Sons/smash.mp3")
menu_theme.set_volume(0.5)
menu_theme.play()


#Boucle principale du jeu
while jeu_en_cours :

    # Affichage du fond d'écran
    background_image = pygame.image.load("Autres/fond.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))
    monEcran.blit(background_image, (0, 0))

    if accueil :
        playoff = pygame.image.load("Boutons/PlayOff.png")
        playoff = pygame.transform.scale(playoff, (width/5, height/5))
        monEcran.blit(playoff, (width/2.5, height/2))
        sonoff = pygame.image.load("Boutons/SonOff.png")
        sonoff = pygame.transform.scale(sonoff, (width/8, height/5))
        sonon = pygame.image.load("Boutons/SonOn.png")
        sonon = pygame.transform.scale(sonon, (width/8, height/5))

        if son :
            monEcran.blit(sonon, (100,100))

        else :
            monEcran.blit(sonoff, (100,100))

        playon = pygame.image.load("Boutons/PlayOn.png")
        playon = pygame.transform.scale(playon, (width/5, height/5))

        levelson = pygame.image.load("Boutons/LevelsOn.png")
        levelson = pygame.transform.scale(levelson, (width/5, height/5))

        levelsoff = pygame.image.load("Boutons/LevelsOff.png")
        levelsoff = pygame.transform.scale(levelsoff, (width/5, height/5))
        monEcran.blit(levelsoff, (width - levelsoff.get_width() - 100, 100))

        pygame.display.update()

        monClic = False
        mouseX,mouseY = pygame.mouse.get_pos()

        for evenement in pygame.event.get() :
            if evenement.type == pygame.QUIT:
                try:
                    jeu_en_cours = False
                    cinematique = False
                    accueil = False
                    levels = False
                    pygame.quit()
                except :
                    pass
            # Gestion du clic de la souris
            elif evenement.type == pygame.MOUSEBUTTONDOWN :
                monClic = True

            if monClic :
 
                if 100 < mouseX < 100+sonon.get_width() and  100 < mouseY < 100+sonon.get_height() and g :
                    # Si le bouton est touché
                    monEcran.blit(sonoff, (100,100))
                    pygame.mixer.music.pause()
                    son = False
                    g = False
                    monClic=False
                    menu_theme.stop()
                    pygame.display.update()
                        
                elif 100 < mouseX < 100+sonon.get_width() and  100 < mouseY < 100+sonon.get_height() and not g:
                    # Si le bouton est touché
                    monEcran.blit(sonon, (100,100))
                    pygame.mixer.music.unpause()
                    son = True
                    g = True
                    monClic=False
                    menu_theme.play()
                    pygame.display.update()


                elif width/2.5 < mouseX < width/2.5+playoff.get_width() and height/2 < mouseY < height/2+playoff.get_height():
                    # Si le bouton est touché
                    monEcran.blit(playon, (width/2.5, height/2))
                    pygame.display.update()
                        
                    if difficulty == 'Easy' or 'Hard' or 'Boss':
                        jeu = True
                            
                    monClic=False
                    accueil=False
                        
                elif width - levelsoff.get_width() - 100 < mouseX < width - 100 and 100 < mouseY < 100 + levelsoff.get_height():
                    # Si le bouton est touché
                    monEcran.blit(levelson, (width-levelsoff.get_width()-100, 100))
                    pygame.display.update()
                    levels = True
                    monClic = False
                    accueil = False



    if levels :

        homeoff = pygame.image.load("Boutons/HomeOff.png")
        homeoff = pygame.transform.scale(homeoff, (width/5, height/5))
        monEcran.blit(homeoff, (100, 100))

        homeon = pygame.image.load("Boutons/HomeOn.png")
        homeon = pygame.transform.scale(homeon, (width/5, height/5))

        gooff = pygame.image.load("Boutons/EasyOff.png")
        gooff = pygame.transform.scale(gooff, (width/8, height/5))
        go2off = pygame.image.load("Boutons/HardOff.png")
        go2off = pygame.transform.scale(go2off, (width/8, height/5))
        go3off = pygame.image.load("Boutons/BossOff.png")
        go3off = pygame.transform.scale(go3off, (width/8, height/5))

        monEcran.blit(gooff, (width/3-gooff.get_width()/2, height/3-gooff.get_height()/2))
        monEcran.blit(go2off, (2*width/3-go2off.get_width()/2, height/3-go2off.get_height()/2))
        monEcran.blit(go3off, (width/2-go3off.get_width()/2, height/1.5-go3off.get_height()/2))

        goon = pygame.image.load("Boutons/EasyOn.png")
        goon = pygame.transform.scale(goon, (width/8, height/5))
        go2on = pygame.image.load("Boutons/HardOn.png")
        go2on = pygame.transform.scale(go2on, (width/8, height/5))
        go3on = pygame.image.load("Boutons/BossOn.png")
        go3on = pygame.transform.scale(go3on, (width/8, height/5))

        pygame.display.update()

        monClic = False
        mouseX,mouseY = pygame.mouse.get_pos()
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                try:
                    jeu_en_cours = False
                    cinematique = False
                    accueil = False
                    levels = False
                    pygame.quit()
                except :
                    pass
            # Gestion du clic de la souris
            elif evenement.type == pygame.MOUSEBUTTONDOWN :
                monClic = True
                
            if monClic :
                
                if 100 < mouseX < 100 + homeoff.get_width() and  100 < mouseY < 100 + homeoff.get_height(): #Comparer la position du carré avec la position du pointeur
                        # Si le bouton est touché
                        monEcran.blit(homeon, (100, 100))
                        pygame.display.update()
                        levels = False
                        monClic = False 
                        accueil = True 
                              
                elif width/3-gooff.get_width()/2 < mouseX < width/3+gooff.get_width()/2 and height/3-gooff.get_height()/2 < mouseY < height/3+gooff.get_height():
                        # Si le bouton est touché
                        monEcran.blit(goon, (width/3-gooff.get_width()/2, height/3-gooff.get_height()/2))
                        pygame.display.update()
                        levels = False
                        monClic = False
                        accueil = True
                        difficulty = 'Easy'
                        
                elif 2*width/3-go2off.get_width()/2 < mouseX < 2*width/3+go2off.get_width()/2 and height/3-go2off.get_height()/2 < mouseY < height/3+go2off.get_height():
                        # Si le bouton est touché
                        monEcran.blit(go2on, (2*width/3-go2off.get_width()/2, height/3-go2off.get_height()/2))
                        pygame.display.update()
                        levels = False
                        monClic = False
                        accueil = True
                        difficulty = 'Hard'
                        
                elif width/2-go3off.get_width()/2 < mouseX < width/2+go3off.get_width()/2 and height/1.5-go3off.get_height()/2 < mouseY < height/1.5+go3off.get_height():
                        # Si le bouton est touché
                        monEcran.blit(go3on, (width/2-go3off.get_width()/2, height/1.5-go3off.get_height()/2))
                        pygame.display.update()
                        levels = False
                        monClic = False
                        accueil = True
                        difficulty = 'Boss'





















    #Chargement des images des aliens
    explosion = pygame.image.load('Autres/explosion.png')
    alien1 = pygame.image.load("Aliens/alien1.png")
    alien2 = pygame.image.load("Aliens/alien2.png")
    alien4 = pygame.image.load("Aliens/alien4.png")
    boss = pygame.image.load("Aliens/boss.png")

    #Chargement de la musique et des sons
    if g :
        pygame.mixer.music.load("Sons/fight.mp3")
        pygame.mixer.music.play(-1)
    laser = pygame.mixer.Sound("Sons/laser.mp3")
    boom = pygame.mixer.Sound("Sons/boom.mp3")


    #Chargement des polices d'écriture
    GOP = pygame.font.Font("Polices/GearsOfPeace.ttf", 36)

    #Ajout du timer
    start_time = time.time()
    game_time = 100 # Temps en secondes pour le timer

    #Initialisation des variables
    jeu_en_cours=True
    score = 0
    x = (0,0)
    posx = (0,0)
    posy = (0,0)
    a = 0
    mort = True
    if difficulty == 'Boss' :
        alien = pygame.image.load("Aliens/boss.png")
    else :
        alien = pygame.image.load("Aliens/alien1.png")
    kill = 0
    explo = [(0,0), -1]
    shoot = [(0,0), -1]



    #Boucle principale du jeu
    while jeu:
        menu_theme.stop()

        # Affichage du fond d'écran
        background_image = pygame.image.load("Autres/fond.jpg")
        background_image = pygame.transform.scale(background_image, (width, height))
        monEcran.blit(background_image, (0, 0))

        # Affichage du score
        score_display = GOP.render("Score : "+str(score), 1, (255,255,0))
        monEcran.blit(score_display, (width/2.2, height/20))
        
        #Affichage de la difficulté
        diff_display = GOP.render(difficulty, 1, (255,255,0))
        monEcran.blit(diff_display, (width/1.2, height/20))
        
        # Affichage du vaisseau
        mouseX,mouseY=pygame.mouse.get_pos()
        ship = pygame.image.load("Autres/ship.png")
        ship = pygame.transform.scale(ship, (width/6, height/3.5))
        monEcran.blit(ship, ((mouseX-width/12), height*0.7))


        # Affichage des Bâtisseurs
        spawn = game_time - time.time()
        
        if difficulty == 'Easy' :
            if mort :
                spawn = 3

            if spawn%3 < 0.01 :
                a += 1
                if a > 2 :
                    a = 0
                mort = False
                posx = randint(width/10, width*0.9)
                posy = randint(height/10, height/2)
                x = (width/10,height/6)
                point = False
                L = [pygame.transform.scale(alien1, x),pygame.transform.scale(alien2, x),pygame.transform.scale(alien4, x)]
                alien = L[a]
                kill = 0
                
        elif difficulty == 'Hard' :
            if mort :
                spawn = 2

            if spawn%2 < 0.01 :
                a += 1
                if a > 2 :
                    a = 0
                mort = False
                posx = randint(width/10, width*0.9)
                posy = randint(height/10, height/2)
                x = (width/10,height/6)
                point = False
                L = [pygame.transform.scale(alien1, x),pygame.transform.scale(alien2, x),pygame.transform.scale(alien4, x)]
                alien = L[a]
                kill = 0

        elif difficulty == 'Boss' :
            if time.time()%1 < 0.01 :
                a += 1
                if a > 2 :
                    a = 0
                posx = randint(width/10, width*0.9)
                posy = randint(height/10, height/2)
                x = (width/10,height/6)
                point = False
                alien = boss
                kill = 0

            alien = pygame.transform.scale(alien, (width/6, height/3.5))

        
        monEcran.blit(alien, (posx,posy))


        # Gestion du timer
        elapsed_time = time.time() - start_time

        temps_restant = game_time - elapsed_time
        tr = int(temps_restant//1)
        if tr <= 0 :
            tr = 0
        temps = GOP.render(f"Temps restant : {tr}", 1, (255,255,0))
        monEcran.blit(temps, (width/30,height/20))

        #A la fin du timer
        if tr == 0 :
            monEcran.fill(NOIR)
            background_image = pygame.image.load("Autres/fond.jpg")
            background_image = pygame.transform.scale(background_image, (width, height))
            monEcran.blit(background_image, (0, 0))
            
            pygame.mixer.music.stop()
            
            laser = pygame.mixer.Sound("Sons/silence.mp3")
            ship = pygame.image.load("Autres/empty.png")

            score_display = GOP.render("Score : "+str(score), 1, (255,255,0))
            monEcran.blit(score_display, (width/2.2, height/20))

            homeoff = pygame.image.load("Boutons/HomeOff.png")
            homeoff = pygame.transform.scale(homeoff, (width/5, height/5))
            homeoff_rect = homeoff.get_rect()
            monEcran.blit(homeoff, (width/2.5, height/1.5))

            homeon = pygame.image.load("Boutons/HomeOn.png")
            homeon = pygame.transform.scale(homeon, (width/5, height/5))

            for evenement in pygame.event.get() :
                if evenement.type == pygame.QUIT:
                    try:
                        jeu_en_cours = False
                        cinematique = False
                        accueil = False
                        levels = False
                        pygame.quit()
                    except :
                        pass

                # Gestion du clic de la souris
                elif evenement.type == pygame.MOUSEBUTTONDOWN :
                    monClic = True
            if monClic :
                if width/2.5 < mouseX < width/2.5+homeoff.get_width() and height/1.5 < mouseY < height/1.5+homeoff.get_height():
                    print("L'image a été cliquée !")
                    monEcran.blit(homeon, (width/2.5, height/1.5))
                    jeu, accueil = False, True
                    monClic = False


            if difficulty == 'Easy' :
                if score >= 50 :
                    BAT = pygame.font.Font("Polices/batman.ttf", 40)
                    win_display = BAT.render("Félicitations ! Vous avez repoussé les Bâtisseurs !", 1, (255,255,0))
                    # Définir la nouvelle position du texte au centre de la fenêtre
                    rect_texte = win_display.get_rect()
                    rect_texte.center = monEcran.get_rect().center
                    monEcran.blit(win_display, rect_texte)
                    pass

                else :
                    BAT = pygame.font.Font("Polices/batman.ttf", 40)
                    lose_display = BAT.render("Les Bâtisseurs vous ont vaincu...", 1, (255,255,0))
                    # Définir la nouvelle position du texte au centre de la fenêtre
                    rect_texte = lose_display.get_rect()
                    rect_texte.center = monEcran.get_rect().center
                    monEcran.blit(lose_display, rect_texte)
                    pass
                
            elif difficulty == 'Hard' :
                if score >= 90 :
                    BAT = pygame.font.Font("Polices/batman.ttf", 40)
                    win_display = BAT.render("Félicitations ! Vous avez repoussé les Bâtisseurs !", 1, (255,255,0))
                    # Définir la nouvelle position du texte au centre de la fenêtre
                    rect_texte = win_display.get_rect()
                    rect_texte.center = monEcran.get_rect().center
                    monEcran.blit(win_display, rect_texte)
                    pass

                else :
                    BAT = pygame.font.Font("Polices/batman.ttf", 40)
                    lose_display = BAT.render("Les Bâtisseurs vous ont vaincu...", 1, (255,255,0))
                    # Définir la nouvelle position du texte au centre de la fenêtre
                    rect_texte = lose_display.get_rect()
                    rect_texte.center = monEcran.get_rect().center
                    monEcran.blit(lose_display, rect_texte)
                    pass
            
            elif difficulty == 'Boss' :
                if score >= 100 :
                    BAT = pygame.font.Font("Polices/batman.ttf", 40)
                    win_display = BAT.render("Félicitations ! Vous avez repoussé les Bâtisseurs !", 1, (255,255,0))
                    # Définir la nouvelle position du texte au centre de la fenêtre
                    rect_texte = win_display.get_rect()
                    rect_texte.center = monEcran.get_rect().center
                    monEcran.blit(win_display, rect_texte)
                    pass
                
                else :
                    BAT = pygame.font.Font("Polices/batman.ttf", 40)
                    lose_display = BAT.render("Les Bâtisseurs vous ont vaincu...", 1, (255,255,0))
                    # Définir la nouvelle position du texte au centre de la fenêtre
                    rect_texte = lose_display.get_rect()
                    rect_texte.center = monEcran.get_rect().center
                    monEcran.blit(lose_display, rect_texte)
                    pass

        if difficulty != 'Boss' :    
            if time.time() < (explo[1])+0.5 :
                explosion = pygame.transform.scale(explosion, (width/10, height/6))
                monEcran.blit(explosion,explo[0])

        if time.time() < (shoot[1])+0.2 :
            mouseX,mouseY=pygame.mouse.get_pos()
            ship = pygame.image.load("Autres/shoot.png")
            ship = pygame.transform.scale(ship, (width/6, height/3.5))
            monEcran.blit(ship, ((mouseX-width/12), height*0.7))
            
        # Mise à jour de l'affichage
        pygame.display.update()


        
        # Gestion des événements (souris)
        for evenement in pygame.event.get():
            monClic = False
            
            # Gestion du clic de la souris
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                monClic=True
                laser.play()
                shoot = [(posx,posy),time.time()]

            if monClic:
                # Si la zone rouge est touchée
                if monEcran.get_at(pygame.mouse.get_pos()) == (255,0,0) :
                    monEcran.fill('black')
                    mort = True
                    touche=True
                    score += 1
                    kill += 1
                    explo = [(posx,posy),time.time()]
                    boom.play()

                # Si la zone rouge n'est pas touchée
                else:
                    touche=False

            # Quitter le jeu
            if evenement.type == pygame.QUIT:
                try:
                    jeu_en_cours = False
                    cinematique = False
                    accueil = False
                    levels = False
                    pygame.quit()
                except :
                    pass
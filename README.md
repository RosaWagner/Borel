# Borel, un système typographique pour l'école primaire.

## Apprendre à lire, apprendre à écrire

![Bonjour](documentation/images/Bonjour.jpg)

Comment penser la typographie pour l’apprentissage conjoint de la lecture et de l’écriture? Développé avec des enseignants du primaire et des orthophonistes, ce projet cherche à reconnecter les signes que l'on apprend à lire et ceux que l’on apprend à écrire. 

Un système typographique a donc été pensé dans cette logique, pour établir une continuité entre tracé cursif et forme typographique. **Borel** (nommé en hommage à Suzanne Borel-Maisonny, pionnière de l’orthophonie) est un caractère robuste, peu contrasté, avec une grande hauteur d'x. Les lettres sont ouvertes et bien distinctes, tout en respectant les règles de l’écriture dans les écoles françaises. **Borel Guides**, qui permet d'afficher des lignes de cahier, vient compléter ce système qui met en valeur l'accessibilité, l'adaptabilité et la cohérence.

**Les enseignants sont invités à faire leur retour d'utilisation du Borel après avoir expérimenter avec leur élèves. Idéalement, une étude expérimentale rigoureuse devrait confirmer ou réfuter les hypothèses ci-dessous. Les chercheurs intéressés sont donc aussi invités à contacter Rosalie Wagner s'ils veulent collaborer pour la porduction d'un matériel expérimental adapté à une telle démarche.**

## Utiliser la police
**Vous pouvez télécharger les fonts depuis les dossiers:**
- [Borel/fonts/ttf](./Borel/fonts/ttf/)
- [BorelGuides/fonts/ttf](./BorelGuides/fonts/ttf/)

Sur internet, une recherche rapide vous aidera à installer correctement ces fichiers selon votre machine (Mac, Windows, etc). S'il y a le moindre problème lors de l'installation, s'il vous plait envoyez-moi un message avec le message d'erreur qui est apparu à ce moment.

**Les lettres ne s'accrochent pas les unes aux autres?**
L'utilisation de Borel dépend grandement des "alternatives contextuelles", qui est une option qui permet à la police de choisir la forme appropriée de la lettre en fonction des lettres autour d'elles.

Pour activer les alternatives contextuelles:
- Word sur Mac: barre des menu > "Mise en Page" > Police > Paramètres avancés > [x] Utiliser les alternatives contextuelles.
- Word sur Windows: barre de recherche > tapez "Police" > Paramètres avancés > [x] Utiliser les alternatives contextuelles 
- Dans les autres environnements, les alternatives contextuelles devraient être activées par défaut.

**La police n'apparait pas dans le menu déroulant des applications Mac?** 
Cela arrive sur certaines version, c'est parce que la fonte ne supporte qu'un set limité de caractères. Pour la trouver il suffit d'aller dans le menu: format > police > afficher les polices. 

Une fois selectionnée à cet endroit elle apparaitra ensuite tout en haut du menu déroulant des polices l'application.

**Dans quel contexte utiliser Borel?**
La police est open-source, cela veut dire qu'il est possible de l'utiliser comme bon vous semble, gratuitement, même pour des projets commerciaux. N'hésitez pas à m'envoyer des images de votre utilisation de Borel! Si vous remarquez un problème, il est recommandé d'ouvrir une "issue" dans [l'onglet "issues" de ce repository](https://github.com/RosaWagner/Borel/issues).


## Lexique
Les termes typographiques sont nombreux et imposent de nombreux repères qui peuvent perturber l’attention. Cependant, il est important pour l'adulte de les connaitre pour comprendre le projet Borel et la suite de cette documentation.

![termes typographiques](./documentation/images/height.jpg)

Pour les enfants, on peut simplifier en parlant de « zones ». Cela amène plus de liberté dans l’exercice d’écriture et c’est aussi plus logique par rapport aux différentes tailles des ascendantes qu'on retrouve conventionnellement en typographie. 

![termes adaptés aux enfants](./documentation/images/height2.jpg)

## Proportions

Les polices cursives scolaires traditionnelles sont disprortionnées par rapport au polices d'écriture de l'usage courant — que l'on retrouve dans les livres, sur les écrans ou la signalétique. Si on regarde les cursives scolaires en France, les ascendantes seraient censé faire trois fois la taille de la hauteur d'x. Sachant que la taille des lettres est souvent limitée aux lignes du cahier, cela veut dire que la hauteur d'x est écrasée entre deux lignes qui, le plus souvent, font 1.5 ou 2mm de hauteur. Ces proportions sont héritées de l'utilisation conjointe des fameuses réglures Séyès et d'un style calligraphique propres à l'utilisation des plumes à reservoir des siècles précédents. 

Hors il a plusieurs arguments qui nous poussent à questionner ces canons:

1. C'est la hauteur de la "zone des petites lettres" qui va conditionner la lisibilité du mot. En effet, les lettres qui sont contenues entre la ligne de base et la hauteur d'x constituent environ 65% de notre alphabet (sans compter les lettres accentuées), en plus de cummuler la plus grande fréquence d'apparition dans le français (environ 80%).[^1] Il parait donc absurde de donner autant d'importance aux capitales, ainsi qu'aux ascendantes/descendantes. 

2. La taille perçue d'une police va paraitre plus ou moins grande en fonction du rapport entre hauteur d'x et hauteur d'ascendante. Par exemple, lorsque *Times New Roman* ou *Arial* sont composé en corps 12pt, *Arial* paraitra plus grande car sa hauteur d'x est plus haute.[^2] Pour compenser la perte de lisibilité d'une police cursive qui a une hauteur d'ascendante 3 fois plus grande que la hauteur d'x, il faudra donc augmenter la taille globale de la police. Malheureusement, peu d'enseignants le font, et c'est aussi impossible lorsque les réglures Séyès dictent la composition du texte.

3. Il faudra aussi un interlignage plus grand pour éviter que les ascendantes et les descendantes ne s'entrechoquent d'une ligne à l'autre. Hors, un interlignage trop serré ou trop grand peut impacter négativement la lisibilité.[^3] Lorsque les polices cursives traditionnelles suivent les lignes du cahiers, l'interlignage parait trop serré, et lorsque l'on saute une ligne, il parait trop large.

4. Pour la lecture continue d'un texte à une distance standard de 40cm, par un adulte normolecteur, la hauteur d'x devrait de trouver entre 1.5mm et 14mm pour rester lisible.[^4] 1.5mm est la taille minimum sur le spectre de la lisibilité pour un adulte! Des études ont démontré que les apprentis lecteurs, et particulèrement ceux présentant des troubles dys, bénéficiaient à lire des caractères légèrement plus grand.[^5] L'étude retenue pour soutenir cette thèse fait le cas de Times New Roman donnant de meilleurs resultats de lecture à 18pt jusqu'à la fin du CE1; cela correspond à une hauteur d'x de 2.84mm (ce qui correspond à Borel en 16pt). Ces chiffres ne sont bien sûr pas absolus et général à tous les enfants, mais ça donne une idée.

5. Ces proportions (Hauteur d'x = 1/3 Ascendante) est observée en France mais rarement, voire jamais, à l'étranger.[^6] C'est bien la preuve qu'il n'y a donc pas qu'une manière de faire, et qu'il y a peu de raison à perpétuer un système aussi rigide.

Celi-dit, lors de l'apprentissage de l'écriture, il est important d'entrainer les doigts et les yeux à bien faire la différence entre les petites et les grandes lettres. Il faut arriver à une taille qui permette d'exercer la motricité fine — passer de petites boucles à grande boucles en ne bougeant que les doigts, pas les mains. Il faut donc une claire différence entre hauteur d'x et ascendente, sans pour autant exagérer cette différence au risque d'impacter négativement la lisibilité. De plus, il est pratiquement impossible dans l'enseignement en France de s'abtraire des cahiers d'écriture à réglure Séyès; il faut donc questionner les canons de l'écriture scolaire cursive, sans pour autant passer outre ce facteur.

**Le défi que doit donc relever le projet Borel est celui du juste compromis entre hauteur d'x et ascendante pour permettre:** 
- une lisibilité non contraignante[^7]
- la clarté du déchiffraphe des graphèmes
- l'entrainement au geste d'écriture[^8]
- l'adaptation aux lignes du cahier

J'ai donc adapté les proportions du Borel afin que la hauteur d'x corresponde à deux lignes du cahier, et que la hauteur des grandes boucles corresponde à quatre. Ainsi les proportions sont plus harminieuses avec les caractères romains coventionnels.

![Proportions par rapport aux lignes du cahier](./documentation/images/height3.jpg)

**Pourquoi les capitales sont-elles plus petites que les grandes boucles?** 

Conventionnellement, la hauteur des capitales est la même que la hauteur des ascendantes, ou légèrement plus petites. Ceci dans le cas où les ascendentes sont droites comme dans n'importe quelle Serif (ex. Times New Roman), ou Sans-Serif (ex: Arial, Comic Sans). Dans l'écriture cursive en France, nous utilisons la boucle pour joindre l'ascendante par le haut; l'amplitude de la boucle augmente la hauteur de l'ascendante. Mais les lettres comme t, d, q, ainsi que les capitales qui ne bénéficient pas de cette jonction, sont donc plus petites que les grandes boucles.

## Processus de design
Pour que la police soit un parfait modèle pour l'apprentissage de l'écriture, chaque lettre existe sous forme de 10 variantes contextuelles.

![10 variantes par lettres](./documentation/images/process.jpg)

## Borel Guides

Borel Guides est une police pour tracer des lignes de cahier. Elle se superpose parfaitement à la police Borel. Elle contient différentes palettes de couleurs, pour s'ajuster à la préférence des petits écrivains, mais aussi un grand choix de motifs linéaires pour s'adapter à l'objectif pédagogique, à la police utilisée, etc. L'enseignants est aussi libre d'utiliser Borel Guides avec une autre police que Borel, des motifs ont été pensé à cet égard.

Veuillez trouvez toutes les informations sur Borel Guides dans ce document:
**[Borel Guides Instructions](./documentation/proof/BorelGuides-Instructions.pdf)**.

![Exemple de grilles](./documentation/images/grille.jpg)

**Attention:**
- Pour utiliser Borel et Borel Guides ensemble, il faut bien deux blocs de textes différents à superposer. Dans Word, cela veut dire qu'il faut utiliser la page comme un bloc de texte (jusque là tout est est normal) et ensuite en créer un autre pour la grille de Borel Guides en allant dans le menu: **insertion** > **zone de texte**. Cette zone de texte va se régler comme un bloc image, c'est à dire qu'avec la petite ancre vous pouvez lui dire de se mettre "derrière le texte" de la page principal.

- L’interlignage est déjà réglé pour les logiciels de traitement de text communs comme Word, Page ou TextEdit. Il correspond à un interlignage de taille 1 dans votre logiciel. Si vous voulez resserer les lignes, utilisez un interlignage 0,5 pour que les lignes se superposent parfaitement. Dans Indesign, vous devrez observer un interlignage double pour permettre la parfaite imbrication de la grille d’une ligne à l’autre. Si vous choississez une taille de police 24 pt, choissisez un interlignage de 48 pt.

- Borel Guides est une *Color Font*. C’est un format particulier qui permet à une police de contenir et de rendre à l'écran des palettes de couleurs. Si vous ne voyez pas les couleurs dans votre logiciel de traitement de texte, cela signifie que votre logiciel ne supporte pas cette technologie. 

- Borel Guides est aussi une police *variable*. C’est un format qui permet de modifier la police sur différents axes comme par exemple: la largeur et l’épaisseur. Il est conseillé de ne pas utiliser [la police variable](./BorelGuides/fonts/variable/) dans vos logiciels de traitement de texte, elle est plutôt destinée au web. Utiliser des polices dites [statiques](./BorelGuides/fonts/ttf/). En effet, beacoup de logiciels supportent les polices colorées, et supportent les polices variables, mais pas les polices colorées et variable.

## À venir

À condition de trouver les financements, il est envisagé de developper le projet Borel pour lui permettre de s'adapter encore mieux aux besoins des enseignants et de la recherche.

**Axes de variabilité:**
- [ ] Weight (graisse)
- [ ] Width (chasse) 
- [ ] Spacing (espacement)
- [ ] HyperExpansion (chasse + espacement)
- [ ] Slant (oblique)

![Design Space](./documentation/images/designspace.jpg)

Il pourrait être intéressant de pouvoir faire varier les proportions de la police afin de tester ces différents paramètres:

- [ ] Ascender-height (hauteur des ascendantes)
- [ ] Caps-height (heuteur des capitales)
- [ ] x-height (hauteur d'x)

**Styles:**
- [ ] Dotted (pointillés)
- [ ] Outlined (contours)
- [ ] Guided (guidé)

![Styles pour l'éducation](./documentation/images/styles.jpg)

**Alternates:**
- [ ] Simplified cursive capitals (capitales cursives simplifiées)
- [ ] Swashed capitals (capitales cursives ornées)

![Variantes des capitales](./documentation/images/capitales.jpg)

## Bio

[Rosalie Wagner](http://rosaliewagner.com) est diplômée d'un master des Beaux-Arts de Lyon en 2016, et d'un post-master de l'ANRT Nancy (Atelier National de Recherche typographique) en 2019. Elle s'est formée à l'ingénierie de fonte chez Black Foundry (Paris) et Alphabet Type (Berlin). Elle est basée à Berlin et travaille en tant que Type designer et Font engineer indépendante pour Google Fonts depuis 2020. Elle a collaboré avec des foundries comme 205TF, Fontwerk, NaN et Fatype, ainsi que divers designers indépendants et studios de communication.

- **Présentation du projet Borel à l'ANRT**, 2019, [[Video](https://anrt-nancy.fr/fr/videos#video-325200518)]
- **Baskervville**, 2017, [[Google Fonts](https://fonts.google.com/specimen/Baskervville)] — *conception collaborative, design de l'italique, correction et développement du Romain, production de la fonte.*
- **Arima Greek**, 2018, [[Google Fonts](https://fonts.google.com/specimen/Arima?noto.script=Grek&query=Arima&subset=greek)] — *conception et design du grec d'Arima de NDiscover sous la direction d'Emilios Theofanous et Irene Vlachou.*

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at https://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.

### Notes

[^1]: L'Université de Toulouse a recensé en 2008 [la fréquence des lettres dans tout le Wikipedia français](https://fr.wikipedia.org/wiki/Fréquence_d%27apparition_des_lettres).

[^2]: *[Does print size matter for reading? A review of findings from vision science and typography](https://jov.arvojournals.org/article.aspx?articleid=2191906#88123043)*, Gordon E. Legge; Charles A. Bigelow, Journal of Vision August 2011, Vol.11, 8. doi:https://doi.org/10.1167/11.5.8

[^3]: *[Influence de la typographie sur l’aisance de lecture d’une population d’enfants dyslexiques. Master Thesis.](https://dumas.ccsd.cnrs.fr/dumas-01302521/document)*, Klein V., Bordeaux : Université de Bordeaux, 2010

[^4]: Gordon E. Legge, Charles A. Bigelow, *op. cit.*

[^5]: Klein V., *op. cit.*

[^6]: Pour plus d'information sur le sujet, TypeTogether a entrepris récemment [une recherche globale sur les écritures scolaires dans le monde](https://www.type-together.com/new-research-handwriting).

[^7]: Pour plus d'information sur le sujet, *[Legibility, How and why typography affects ease of reading](https://legible-typography.com/en/)*, Mary C. Dyson, [Design Regression](https://designregression.com), 2023 

[^8]: Pour plus d'informations sur le sujet, *[Le geste d'écriture](https://legestedecriture.fr), Méthode d'apprentissage Cycle 1 • Cycle 2, Différenciation et transversalité*, Danièle Dumont, Hatier, 2016

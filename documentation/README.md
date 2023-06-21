### Find the english version of this documentation: ["How to use Borel"](./README_en.md)

# Utiliser Borel

Borel est une police open source, ce qui signifie que vous avez la liberté de l'utiliser dans tous vos projets, y compris les projets commerciaux, et ce, gratuitement.

## Télécharger les polices

1. **À partir du ["release"](https://github.com/RosaWagner/Borel/releases)** : cliquez sur le fichier `fonts.zip` de la dernière version pour le télécharger.

2. **À partir du dossier "fonts"** :
   - [Borel](../Borel/fonts/ttf/)
   - [Guide Borel](../BorelGuides/fonts/ttf/)

## Installer les polices
### Mac

1. **Ouvrez le Livre des polices** : le Livre des polices est l'outil de gestion de polices par défaut sur macOS. Vous pouvez le trouver en accédant au dossier "Applications" ou en utilisant la recherche Spotlight.

2. **Installez la police** : Double-cliquez sur le fichier de police téléchargé et le Livre des polices s'ouvrira. Cliquez sur le bouton "Installer la police" dans la fenêtre d'aperçu de la police. Alternativement, vous pouvez faire glisser le fichier de police dans la fenêtre du Livre des polices.

3. **Vérifiez l'installation** : Une fois installée, vous pouvez trouver la police répertoriée dans le Livre des polices. Vous pouvez également utiliser la police dans différentes applications sur votre Mac, telles que les éditeurs de texte ou les logiciels de conception.

Si la police n'apparait pas dans le menu déroulant de l'application, vous pouvez toujours la trouver dans le panneau des polices (cmd+T) ou menu: `format > Police > afficher les polices`.

### Windows :

1. **Installez la police** : Double-cliquez sur chaque fichier de police. Une fenêtre d'aperçu s'ouvrira. Cliquez sur le bouton "Installer" en haut de la fenêtre d'aperçu. Alternativement, vous pouvez cliquer avec le bouton droit sur le fichier de police et sélectionner "Installer" dans le menu contextuel.

1. **Vérifiez l'installation** : Après l'installation, la police sera disponible pour une utilisation dans les applications. Vous pouvez confirmer l'installation en vérifiant la liste des polices dans des programmes tels que les logiciels de traitement de texte, les logiciels de conception graphique ou le dossier des polices Windows situé dans le Panneau de configuration.

**Si un message d'erreur apparaît lors de l'installation, veuillez le signaler en [ouvrant une "issue"](https://github.com/RosaWagner/Borel/issues). Pour ce faire, suivez le lien et cliquez sur le bouton vert "New issue" et n'oubliez pas de joindre une capture d'écran du message d'erreur.**

## Activer les alternatives contextuelles

L'utilisation de Borel dépend largement des "alternatives contextuelles", qui est une option permettant à la police de choisir la forme appropriée de la lettre en fonction des lettres environnantes et ainsi de les connecter.

Cette option est activée par défaut dans de nombreuses applications de bureau et web, mais pas dans les applications de Microsoft Office. Si les lettres ne se connectent pas, suivez ces étapes ci-dessous.

###

 Mac

1. Sélectionnez le texte.
2. Allez dans `Format` > `Police`.
3. Recherchez la section `Typographie` ou `Avancé`.
4. Cochez la case `Utiliser les alternatives contextuelles`.

### Windows

1. Sélectionnez le texte.
2. Cliquez avec le bouton droit de la souris et choisissez `Police` ou `Paramètres de police`.
3. Accédez à l'onglet `Avancé`.
4. Cochez la case `Utiliser les alternatives contextuelles`.

## Guide Borel : Police Couleur et Variable 

- Borel Guides est une *fonte couleur*. Il s'agit d'un format spécial qui permet à une police de contenir et d'afficher des palettes de couleurs à l'écran. Si vous ne voyez pas les couleurs dans votre éditeur de texte, cela signifie que votre logiciel ne prend pas en charge cette technologie.

- Borel Guides est également une *fonte variable*. Il s'agit d'un format qui vous permet de modifier la police sur différents axes, tels que la largeur et la graisse. Il est conseillé de ne pas utiliser la [police variable](./BorelGuides/fonts/variable/) dans votre logiciel d'édition de texte, car elle est destinée au web. Utilisez plutôt les [polices statiques](./BorelGuides/fonts/ttf/). De nombreux programmes prennent en charge les polices colorées *ou* les polices variables, mais pas les polices colorées *et* variables simultanément.

## Utiliser de Borel et Borel Guide ensemble

Pour utiliser Borel et Borel Guides ensemble, vous devez superposer deux cadres de texte différents.

Dans MS Word, vous pouvez utiliser Borel pour écrire le texte principal. Ensuite, vous devrez créer une zone de texte pour Borel Guides :

- allez dans le menu : `Insertion` > `Zone de texte` > `Zone de texte simple`. Cette zone de texte fonctionnera comme un cadre d'image, c'est-à-dire que vous pouvez utiliser l'ancre pour le placer "derrière le texte" sur la page principale. Vous pouvez également supprimer les bordures, etc.

- L'espacement entre les lignes est déjà configuré pour les éditeurs de texte courants tels que Word, Page ou TextEdit. Néanmoins, assurez-vous que Borel et Borel Guide ont la même valeur pour qu'ils se superposent parfaitement. Définissez l'interlignage sur `1` pour une meilleure expérience.

- Dans InDesign, vous devrez utiliser un interlignage double pour permettre au quadrillage de s'emboîter parfaitement d'une ligne à l'autre. Par exemple, si vous choisissez une taille de police de `24 pt`, choisissez un espacement des lignes de `48 pt`.
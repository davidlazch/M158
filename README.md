# M158 - Labo Final

## Prerequis

Premierement on doit cloner la repo en local.

Vous pouvez faire ca en untilisant la commande:

```sh
$ git clone https://github.com/davidlazch/M158.git
```

Si vous avez déjà cloné le repo, c'est important a le mettre à jour pour être sûr que vous avez la dernière version en local.

```sh
$ git pull
```

## Les Branches

On va utiliser la notion des branches pour gérér le boulot éffectue dans une manière que ça ne dérange pas le travail des autres.

Pour le faire, premièrement on doit créér une branche en local:

```sh
$ git checkout -B nomprenom/travail-vous-alliez-faire
```

Par exemple, un bon nom pour un branche pourrait être `davidlaz/adding-myself`.

En utilisant git checkout, vous seriez déplacées dans la nouvelle branche automatiquement, mais si vous voulez revenir sûr la branche "master", vous pouvez executer:

```sh
$ git switch nom-de-la-branche
```

## Le Commit & Push

Quand vous avez fini avec vos changements, vous pouvez faire un commit et un push.

Un commit est utilisé pour suivre les changements dans une branche et on peut toujours révenir sûr un commit (révenir sûr un état de projet). Chaque commit contient un UUID et c'est impossible a avoir deux commits avec le même UUID.

Avant qu'on faire le commit on peut vérifier les changements qu'on a éffectue.

```sh
$ git status
```

Si on est sûr et on veut ajouter un fichier dans un commit, on peut faire:

```sh
$ git add ./chemin/relatif/jusqua/fichier
```

Si tous les fichiers sont ajoutées, on peut faire un commit:

```sh
$ git commit -m 'Message du commit'
```

Finalément, on peut faire un push chez la repo publique en créant une nouvelle branche.

```sh
$ git push
```

## Le Merge

Maintenant en allant sûr la repo dans GitHub, on peut voir que on peut "Créer un Pull Request".

On peut faire ça si on est sûr que nos changements sont correct et si on veut ajouter nos changements dans la branche principale (master).

Aprés le PR, on veut que au minimum 1 personne vérifie les changements avant qu'on faire un merge avec la branche principale pour éviter des possibles bug's dans le code qu'on n'as pas vu (et d'autres raisons).

Si au moins une personne a accepté les changements, vous pouvez cliquer sûr "Merge pull request"

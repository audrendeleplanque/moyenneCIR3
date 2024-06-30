def averagePhysics(transformation, mecaSol, probaStat, analyseDesSignaux, automatique):
    try:
        partielTransformation = findValue(transformation, "Partiel")
    except:
        partielTransformation = findValue(transformation, "session")

    averageTransformation = findValue(transformation, "Interrogation")* 0.2 + findValue(transformation, "TP") * 0.4 + partielTransformation * 0.4

    try:
        partielMecaSol = findValue(mecaSol, "Partiel")
    except:
        partielMecaSol = findValue(mecaSol, "session")

    averageMecaSol = findValue(mecaSol, "Epreuve de Contrôle Continu n°1")* 0.2 + findValue(mecaSol, "Epreuve de Contrôle Continu n°2") * 0.2 + partielMecaSol * 0.6

    try:
        partielProbaStat = findValue(probaStat, "Partiel")
    except:
        partielProbaStat = findValue(probaStat, "session")

    averageProbaStat = findValue(probaStat, "TP ")* 0.5 + partielProbaStat * 0.5

    try:
        partielAnalyseDesSignaux = findValue(analyseDesSignaux, "Partiel")
    except:
        partielAnalyseDesSignaux = findValue(analyseDesSignaux, "session")

    averageAnalyseDesSignaux = findValue(analyseDesSignaux, "Travaux Pratiques")* 0.2 + findValue(analyseDesSignaux, "DS") * 0.4 + partielAnalyseDesSignaux * 0.4

    try:
        partielAutomatique = findValue(automatique, "Partiel")
    except:
        partielAutomatique = findValue(automatique, "session")

    averageAutomatique = findValue(automatique, "DS")* 0.3 + findValue(automatique, "TP") * 0.2 + findValue(automatique, "session") * 0.5

    averagePhsics = averageTransformation*0.25 + averageMecaSol*0.15 + averageProbaStat*0.2 + averageAnalyseDesSignaux*0.25 + averageAutomatique*0.15

    return round(averagePhsics, 2)

def findValue(dict, keyWord):
    for cle, valeur in dict.items():
        if keyWord in cle:
            return float(valeur)

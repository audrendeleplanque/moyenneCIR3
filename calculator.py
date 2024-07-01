def averagePhysics(mecaQ, elecNum, projetElec, physiqueSol, ElecAna):
    try:
        partielMecaQ = findValue(mecaQ, "Session")
    except:
        partielMecaQ = findValue(mecaQ, "Partiel")

    averageMecaQ = findValue(mecaQ, "DS") * 0.3 + findValue(mecaQ, "continu") * 0.2 + partielMecaQ * 0.5

    try:
        partielElecNum = findValue(elecNum, "session")
    except:
        partielElecNum = findValue(elecNum, "Partiel")

    averageElecNum = findValue(elecNum, "TP Microcontroleurs") * 0.2 + findValue(elecNum, "DS") + partielElecNum * 0.4

    print("Moyenne elecNum : ", averageElecNum)

    averageProjetElec = findValue(projetElec, "Projet d'électronique (semaine 4)") * 0.6 + findValue(projetElec, "QCM") * 0.4

    try:
        partielPhysiqueSol = findValue(physiqueSol, "Partiel")
    except:
        partielPhysiqueSol = findValue(physiqueSol, "session")

    averagePhysiqueSol = findValue(physiqueSol, "Contrôle continu") * 0.2 + findValue(physiqueSol, "DS") * 0.3 + partielPhysiqueSol * 0.5

    try:
        partielElecAna = findValue(ElecAna, "Partiel")
    except:
        partielElecAna = findValue(ElecAna, "session")

    averageElecAna = findValue(ElecAna, "TP") * 0.2 + findValue(ElecAna, "DS") * 0.4 + partielElecAna * 0.4

    averagePhysics = averageMecaQ * 0.2 + averageElecNum * 0.2 + averageProjetElec * 0.2 + averagePhysiqueSol * 0.2 + averageElecAna * 0.2

    return round(averagePhysics, 2)

def averageMaths(transformation, mecaSol, probaStat, analyseDesSignaux, automatique):
    try:
        partielTransformation = findValue(transformation, "Partiel")
    except:
        partielTransformation = findValue(transformation, "session")

    averageTransformation = findValue(transformation, "Interrogation") * 0.2 + findValue(transformation,
                                                                                         "TP") * 0.4 + partielTransformation * 0.4

    try:
        partielMecaSol = findValue(mecaSol, "Partiel")
    except:
        partielMecaSol = findValue(mecaSol, "session")

    averageMecaSol = findValue(mecaSol, "Epreuve de Contrôle Continu n°1") * 0.2 + findValue(mecaSol,
                                                                                             "Epreuve de Contrôle Continu n°2") * 0.2 + partielMecaSol * 0.6

    try:
        partielProbaStat = findValue(probaStat, "Partiel")
    except:
        partielProbaStat = findValue(probaStat, "session")

    averageProbaStat = findValue(probaStat, "TP ") * 0.5 + partielProbaStat * 0.5

    try:
        partielAnalyseDesSignaux = findValue(analyseDesSignaux, "Partiel")
    except:
        partielAnalyseDesSignaux = findValue(analyseDesSignaux, "session")

    averageAnalyseDesSignaux = findValue(analyseDesSignaux, "Travaux Pratiques") * 0.2 + findValue(analyseDesSignaux,
                                                                                                   "DS") * 0.4 + partielAnalyseDesSignaux * 0.4

    try:
        partielAutomatique = findValue(automatique, "Partiel")
    except:
        partielAutomatique = findValue(automatique, "session")

    averageAutomatique = findValue(automatique, "DS") * 0.3 + findValue(automatique, "TP") * 0.2 + findValue(
        automatique, "session") * 0.5

    averageMaths = averageTransformation * 0.25 + averageMecaSol * 0.15 + averageProbaStat * 0.2 + averageAnalyseDesSignaux * 0.25 + averageAutomatique * 0.15

    return round(averageMaths, 2)

def averageInfo(java, infographie, projetInfo, BDD, reseau, devops):
    try:
        partielJava = findValue(java, "Partiel")
    except:
        partielJava = findValue(java, "session")

    averageJava = findValue(java, "Projet") * 0.25 + findValue(java, "TP") * 0.25 + partielJava * 0.5

    try:
        partielInfographie = findValue(infographie, "Partiel")
    except:
        partielInfographie = findValue(infographie, "session")

    averageInfographie = findValue(infographie, "TP3") * 0.3 + findValue(infographie, "TP2") * 0.3 + partielInfographie * 0.4

    averageProjetInfo = findValue(projetInfo, "Projet")

    try:
        partielBDD = findValue(BDD, "2nde session de Base de données")
    except:
        partielBDD = findValue(BDD, "Partiel")

    averageBDD = findValue(BDD, "pratique") * 0.5 + partielBDD * 0.5

    try:
        partielReseau = findValue(reseau, "Partiel")
    except:
        partielReseau = findValue(reseau, "session")

    averageReseau = partielReseau

    try:
        partielDevops = findValue(devops, "Partiel")
    except:
        partielDevops = findValue(devops, "session")

    averageDevops = partielDevops

    averageInfo = averageJava * 0.22 + averageInfographie * 0.15 + averageProjetInfo * 0.15 + averageBDD * 0.1 + averageReseau * 0.16 + averageDevops * 0.22

    return round(averageInfo, 2)

def findValue(dict, keyWord):
    for cle, valeur in dict.items():
        if keyWord in cle:
            return float(valeur)
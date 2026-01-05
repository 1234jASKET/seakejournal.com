def calculer_cogs(total_demande, noms, pourcentages, prix):
    composants = []
    total_kg = 0
    total_matiere = 0

    for nom, pct, prix_unit in zip(noms, pourcentages, prix):
        if not nom.strip():
            continue

        pct = float(pct)
        prix_unit = float(prix_unit)

        kg = (pct / 100) * total_demande
        cout = kg * prix_unit

        composants.append({
            "nom": nom,
            "kg": round(kg, 3),
            "cout": round(cout, 2),
        })

        total_kg += kg
        total_matiere += cout

    overhead = round(total_kg * 3.5, 2)  # tu peux changer
    cogs = total_matiere + overhead
    cout_par_kg = cogs / total_kg if total_kg > 0 else 0

    return {
        "composants": composants,
        "total_kg": round(total_kg, 3),
        "total_matiere": round(total_matiere, 2),
        "overhead": overhead,
        "cogs": round(cogs, 2),
        "cout_par_kg": round(cout_par_kg, 2),
    }
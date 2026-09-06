"""
Module : Indice d'Équivalence Thérapeutique-Travail (IETT)
Projet : Pacte de Solidarité Vitale (PSV) - La Carte Publique Maladie
Description : Algorithme de conversion des soins reçus en effort productif.
"""

class EvaluateurIETT:
    def __init__(self, cout_base: float, complexite_pathologie: float):
        self.cout_base = cout_base
        self.complexite = complexite_pathologie  # Ex: 1.0 (standard) à 3.0 (soins lourds)
        
    def calculer_iett(self, facteur_restitution: float = 1.0) -> float:
        """
        Calcule la masse de travail ou la valeur due par le citoyen guéri 
        en fonction des ressources médicales investies par la collectivité.
        """
        if facteur_restitution <= 0:
            raise ValueError("Le facteur de restitution doit être supérieur à 0.")
            
        iett_total = (self.cout_base * self.complexite) / facteur_restitution
        print(f"[IETT] Calcul effectué : Base ({self.cout_base}) x Complexité ({self.complexite})")
        print(f"[IETT] Valeur totale de rédemption due : {iett_total} unités de travail")
        return iett_total

    def convertir_en_heures(self, iett_total: float, valeur_horaire_travail: float = 10.0) -> float Convertir en heures:
        """
        Convertit l'IETT en un volume horaire d'effort public (Entropie ou Emploi).
        """
        heures_requises = iett_total / valeur_horaire_travail
        print(f"[IETT] Conversion en effort physique : {heures_requises} heures de travail public.")
        return heures_requises

# --- Simulation d'exécution ---
if __name__ == "__main__":
    # Exemple : Un citoyen ayant reçu des soins complexes évalués à 5000 unités de base
    dossier_soin = EvaluateurIETT(cout_base=5000.0, complexite_pathologie=1.5)
    
    # Calcul de l'IETT
    valeur_due = dossier_soin.calculer_iett(facteur_restitution=1.0)
    
    # Conversion en heures de travail public à effectuer
    dossier_soin.convertir_en_heures(valeur_due, valeur_horaire_travail=15.0)

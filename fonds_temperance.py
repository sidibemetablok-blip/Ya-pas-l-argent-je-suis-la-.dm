"""
Module : Fonds d'Épargne et de Tempérance (FET)
Projet : Pacte de Solidarité Vitale (PSV) - La Carte Publique Maladie
Description : Gestion de l'avance pour le mois de jeûne/méditation et 
calcul du remboursement majoré au coefficient 1.5.
"""

class PacteSolidariteVitale:
    def __init__(self, citoyen_id: str, solde_initial: float = 0.0):
        self.citoyen_id = citoyen_id
        self.solde = solde_initial
        self.dette_active = 0.0
        self.statut = "Actif"

    def demander_allocation_temperance(self, montant_demande: float) -> float:
        """
        Débloque une somme pour sécuriser le mois de jeûne ou de méditation.
        Applique un coefficient de rédemption de 1.5.
        """
        self.solde += montant_demande
        # Application du coefficient de remboursement 1.5
        self.dette_active = montant_demande * 1.5
        print(f"[FET] Citoyen {self.citoyen_id} - Allocation de {montant_demande} versée.")
        print(f"[FET] Dette de rédemption établie à (facteur 1.5) : {self.dette_active}")
        return self.dette_active

    def rembourser_dette(self, montant_verse: float) -> None:
        """
        Remboursement de la dette via l'effort productif ou l'économie générée.
        """
        if montant_verse >= self.dette_active:
            surplus = montant_verse - self.dette_active
            self.dette_active = 0.0
            self.statut = "Soldé / Apuré"
            print(f"[PSV] Dette intégralement remboursée. Surplus de {surplus} réinjecté dans le Fonds Global.")
        else:
            self.dette_active -= montant_verse
            print(f"[PSV] Remboursement partiel reçu. Reste dû : {self.dette_active}")

# --- Simulation d'exécution ---
if __name__ == "__main__":
    # Initialisation pour un citoyen
    citoyen = PacteSolidariteVitale(citoyen_id="MS-2026-001")
    
    # Demande d'allocation pour le mois de jeûne/méditation
    citoyen.demander_allocation_temperance(1000.0)
    
    # Apurement de la dette après la période (remboursement à 1.5 = 1500)
    citoyen.rembourser_dette(1500.0)

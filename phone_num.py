# Importation de la bibliothèque 'requests' pour effectuer des requêtes HTTP
import requests

def localiser_numero(cle_api, numero_telephone):
    """
    Fonction pour obtenir les informations d'un numéro de téléphone via l'API NumVerify.
    
    Args:
        cle_api (str): Clé d'API obtenue depuis numverify.com
        numero_telephone (str): Numéro de téléphone avec l'indicatif international (ex: +33123456789)
    """
    
    # Configuration de l'URL de l'API avec les paramètres nécessaires
    url = f"http://apilayer.net/api/validate?access_key={cle_api}&number={numero_telephone}"
    
    try:
        # Envoi de la requête GET à l'API
        reponse = requests.get(url).json()
        
        # Vérification si le numéro est valide
        if not reponse.get("valid"):
            print("Numéro invalide.")
            return
        
        # Affichage des informations extraites
        print(f"Numéro : {reponse['number']}")
        print(f"Pays : {reponse['country_name']} (Code : {reponse['country_code']})")
        print(f"Opérateur : {reponse['carrier']}")
        print(f"Région : {reponse['location']}")
        print(f"Type de ligne : {reponse['line_type']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Échec de la requête API : {e}")
    except KeyError:
        print("Format de réponse inattendu de l'API.")

# Configuration principale
if __name__ == "__main__":
    # --- IMPORTANT ---
    # Remplacez par votre clé API personnelle (inscription gratuite sur numverify.com)
    CLE_API = "VOTRE_CLE_API"
    
    # Numéro de test de Twilio (ne pas utiliser pour du tracking réel !)
    NUMERO_TEST = "+14158586273"  # Exemple : numéro de test Twilio (États-Unis)
    
    # Appel de la fonction de localisation
    localiser_numero(CLE_API, NUMERO_TEST)

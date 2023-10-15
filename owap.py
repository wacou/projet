print("bienvenu dans notre outil de test!\nVEUILLEZ CHOISIR LE TYPE DE TEST:")
print("1: pour tester le Contrôle d’accès défaillant sur Bwa")
print("2: tester la vulnérabilité Stockage de données non sécurisées")
print("3: pour tester la vulnérabilité Injection SQL")
print("4: pour tester la vulnérabilité Mauvaise configuration de la sécurité")
print("5: falsification de requête côté serveur(SSRF)")


choix = int(input("entrez votre choix : "))

#  tester le Contrôle d’accès défaillant
if choix == 1:
    import requests
    import json

    def test_access_control(url, user, password):
      """
      Test le contrôle d’accès défaillant sur Bwapp

      Args:
        url: L'URL de Bwapp
        user: Le nom d'utilisateur
        password: Le mot de passe

      Returns:
        Le résultat du test
      """

      # Connectez-vous à l'application
      response = requests.post(url + "/login", data={"username": user, "password": password})
      if response.status_code != 200:
        return False

      # Obtenez l'ID de l'utilisateur
      response = requests.get(url + "/user/me")
      user_id = json.loads(response.content)["id"]

      # Essayez d'accéder à une ressource protégée
      response = requests.get(url + "/admin/users")
      if response.status_code == 200:
        return False

      return True


    if __name__ == "__main__":
      # Configurez les paramètres
      url = input("Veuillez entrer l'adresse URL que vous souhaitez tester : ")
      user = "admin"
      password = "admin"

      # Exécutez le test
      result = test_access_control(url, user, password)
      if result:
        print("Le contrôle d’accès est défaillant.")
      else:
        print("Le contrôle d’accès est fonctionnel.")
# tester une vulnérabilité de stockage de données non sécurisées :
elif choix == 2:
    import requests
    import sys

    def main():
        # Demandez à l'utilisateur d'entrer l'adresse Web de l'application cible.
        url = input("Entrez l'adresse Web de l'application cible : ")

        # Connectez-vous à l'application cible.
        session_id = login(url)

        # Trouvez une entrée de données qui est stockée de manière non sécurisée.
        data_to_find = input("Entrez le type de données à trouver : ")

        # Envoyez une requête malveillante pour tenter d'accéder à ces données.
        response = send_malicious_request(url, session_id, data_to_find)

        # Analysez la réponse pour voir si les données sensibles ont été divulguées.
        if data_to_find in response.text:
            print("Données sensibles divulguées !")
        else:
            print("Données sensibles non divulguées.")

    def login(url):
        # Connectez-vous à l'application cible en tant qu'utilisateur authentifié.
        url = "{}/login".format(url)
        data = {"username": "admin", "password": "password"}
        response = requests.post(url, data=data)

        # Récupérez l'identifiant de session de l'utilisateur.
        session_id = response.cookies["session_id"]

        return session_id

    def send_malicious_request(url, session_id, data_to_find):
        # Envoyez une requête malveillante pour tenter d'accéder aux données sensibles.
        url = "{}/profile?session_id={}".format(url, session_id)
        data = {"data_to_find": data_to_find}
        response = requests.get(url, data=data)

        return response

    if __name__ == "__main__":
        main()
#pour tester la vulnérabilité Injection SQL
elif choix == 3:
    import requests
    import sys

    def main():
        # Demandez à l'utilisateur d'entrer l'adresse Web de l'application cible.
        url = input("Entrez l'adresse Web de l'application cible : ")

        # Trouvez une entrée de données qui est susceptible d'être vulnérable à l'injection SQL.
        input_field = input("Entrez le nom du champ d'entrée à tester : ")

        # Envoyez une requête malveillante pour tenter d'accéder aux données sensibles.
        response = send_malicious_request(url, input_field)

        # Analysez la réponse pour voir si les données sensibles ont été divulguées.
        if "password" in response.text:
            print("Données sensibles divulguées !")
        else:
            print("Données sensibles non divulguées.")

    def send_malicious_request(url, input_field):
        # Envoyez une requête malveillante pour tenter d'accéder aux données sensibles.
        url = "{}/?{}".format(url, input_field)
        response = requests.get(url)

        return response

    if __name__ == "__main__":
        main()

#pour tester la vulnérabilité Mauvaise configuration de la sécurité
elif choix == 4:
    import requests
    import sys

    def main():
        # Demandez à l'utilisateur d'entrer l'adresse Web de l'application cible.
        url = input("Si la valeur de configuration est vide, c'est une vulnérabilité potentielle.\nEntrez l'adresse Web de l'application cible : ")

        # Listez les paramètres de configuration de l'application cible.
        response = requests.get(url)
        headers = response.headers

        # Analysez les paramètres de configuration pour détecter les vulnérabilités.
        for header in headers:
            # Recherchez les valeurs de configuration qui peuvent être vulnérables.
            if header.startswith("X-"):
                # Si la valeur de configuration est vide, c'est une vulnérabilité potentielle.
             if headers[header] == "":
                    print("Vulnérabilité potentielle : {} = {}".format(header, headers[header]))

    if __name__ == "__main__":
        main()
#falsification de requête côté serveur(SSRF)
elif choix == 5:
    import requests
    import sys

    def main():
        # Demandez à l'utilisateur d'entrer l'adresse Web de l'application cible.
        url = input("Entrez l'adresse Web de l'application cible : ")

        # Envoyez une requête malveillante à l'application cible.
        response = requests.get(url + "/?query=http://example.com")

        # Analysez la réponse pour voir si l'attaquant a pu contrôler le comportement de l'application.
        if "example.com" in response.text:
            print("Vulnérabilité SSRF détectée !")
        else:
            print("Aucune vulnérabilité SSRF détectée.")

    if __name__ == "__main__":
        main()

# projet

Étape 1: Pour implémenter ce code en Python, nous allons utiliser un paquet appelé boîtier. Tout d'abord, nous allons créer un paquet ARP en utilisant le boîtier scapy. Ici, nous ne créons pas une requête ARP, mais au lieu de cela, nous créons un paquet de réponse ARP. Donc, nous allons nous faire savoir quels domaines nous devons nous fixer afin de faire le paquet ARP en tant que paquet de réponse en Python.
 Pour implémenter ce code en Python, nous allons utiliser un paquet appelé boîtier. Tout d'abord, nous allons créer un paquet ARP en utilisant le boîtier scapy. Ici, nous ne créons pas une requête ARP, mais au lieu de cela, nous créons un paquet de réponse ARP. Donc, nous allons nous faire savoir quels domaines nous devons nous fixer afin de faire le paquet ARP en tant que paquet de réponse en Python comme suit. En boucinage, le paquet ARP est créé en utilisant la syntaxe comme indiqué ci-dessous.

import scapy.all as scapy
 
scapy.ARP()
 
# To list the fields in ARP()
 
print(scapy.ls(scapy.ARP()))

Produit:

 

Étape 2: Maintenant, comprenons le code en obtenant d'abord l'adresse MAC de l'appareil avec son adresse IP avec le code ci-dessous. On utilise tout d'abord le module de boîtier précité pour générer un paquet ARP à l'adresse IP donnée.

# creating an ARP request to the ip address
arp_request = scapy.ARP(pdst=ip)    

Puis créer un message de diffusion avec une adresse MAC pour diffuser MAC qui est « ff:ff:ff:ff:ff:ff:ff» comme indiqué ci-dessous.

# setting the denstination MAC address to broadcast MAC address
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

Ensuite, nous combinons le paquet de diffusion avec la demande ARP.

# combining the ARP packet with the broadcast message
arp_request_broadcast = broadcast / arp_request

On s'envoie ensuite à l'adresse IP de la victime et pour ce faire, nous utilisons scapy.srp() comme indiqué ci-dessous.

answ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

Étape 3: combinons maintenant les mentions d'adresses MAC mentionnées ci-dessus dans une fonction et ensuite vous les avez avec notre boucle pour tromper continuellement les appareils. 

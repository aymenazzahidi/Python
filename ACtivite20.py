ips = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

###Qusetion 1
print("Premiere adresse :", ips[0])

###Qusetion 2
print("Derniere adresse :", ips[len(ips) - 1])

###Qusetion 3
print("Troisieme adresse :", ips[2])

###Qusetion 4
ips.append("172.31.0.1")
print("Liste apres ajout :", ips)

###Qusetion 5
if "200.100.50.1" in ips:
    ips.remove("200.100.50.1")
print("Liste apres suppression :", ips)

###Qusetion 6
nombre = len(ips)
print("Nombre d’adresses restantes :", nombre)

###Qusetion 7
a = "192.168.0.1"
if a in ips:
    print(f"L’adresse {a} est dans la liste.")
else:
    print(f"L’adresse {a} n’est pas dans la liste.")

###Qusetion 8
def classe_ip(ip):
    premier_octet = int(ip.split(".")[0])
    if 1 <= premier_octet <= 126:
        return "A"
    elif 128 <= premier_octet <= 191:
        return "B"
    elif 192 <= premier_octet <= 223:
        return "C"
    else:
        return "Autre"

print("La classe de 10.0.0.1 est :", classe_ip("10.0.0.1"))

###Qusetion 9
ips.sort()
print("Liste triee :", ips)

###Qusetion 10
c = 0
for ip in ips:
    if classe_ip(ip) == "C":
        c += 1
print("Nombre d’adresses de classe C :", c)

###Qusetion 11
def est_publique(ip):
    o1, o2 = map(int, ip.split(".")[:2])
    # Vérification des plages privées
    if o1 == 10:
        return False
    if o1 == 172 and 16 <= o2 <= 31:
        return False
    if o1 == 192 and o2 == 168:
        return False
    if o1 == 169 and o2 == 254:
        return False
    return True

cmp = 0
for ip in ips:
    if est_publique(ip)==True:
        cmp += 1
print("Nombre d’adresses publiques :", cmp)

from pyscript import document
import random

for _ in range(5):
    szam=random.randint(1,10)
    document.getElementById("#kimenet").innerText+=str(szam)+"\n"
    
def beolvas(event):
    felhasznalo = document.getElementById("#beviteli-mezo").value
    document.getElementById("#kimenet1").innerText = felhasznalo
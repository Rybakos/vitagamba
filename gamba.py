import random
import time
symbols=["🍒", "🍋","🍇","🎰", "🍉", "🔔", "🍊", "🍑"]
fraze=["Prohrál si peníze syna", "Měl si radši vsadit tutovku", "Kdo nesází okrádá rodinu", "Každý gambler odchází těsně před svojí výhrou", "Nepřestávej točit", "WE LOVE GAMBLING", 
       "Exekuce na krku frajere"]
penizky = 100
multiplier=0


while penizky>0:
    
    time.sleep(0.50)
    print(f"Zbývá vám: {penizky} chechtáku" )
    time.sleep(0.50)
    bet = int(input("Sázku prosím: "))
    if bet>penizky:
        input("Zadal si moc velkou sázku na, kterou nemáš peníze zkus to znovu")
        time.sleep(0.50)
        continue
    else:
        tocka1 = random.choice(symbols)
        tocka2 = random.choice(symbols)
        tocka3 = random.choice(symbols)
        penizky-=bet
        vyhra=bet*multiplier
        print(f"Výsledky spinu: {tocka1} {tocka2} {tocka3}")
        if tocka1==tocka2==tocka3:
            if tocka1==("🍒"):
                multiplier=5
            elif tocka1==("🍋"):
                multiplier=6
            elif tocka1==("🍇"):
                multiplier=8
            elif tocka1==("🎰"):
                multiplier=20
            elif tocka1==("🍉"):
                multiplier=10      
            elif tocka1==("🔔"):
                multiplier=15
            elif tocka1==("🍊"):
                multiplier=7
            elif tocka1==("🍑"):
                multiplier=9
        else:
            multiplier=0
            vyhra=0
        time.sleep(0.10)
        print(f"Result: {vyhra}")
        time.sleep(0.10)
        print(f"Vsadil si: ${bet}, Multiplier: {multiplier}x")
        time.sleep(0.10)
        print(f"Vyhral si: ${vyhra}")
        time.sleep(0.10)
        print(f"Nyní máš na účtě: ${penizky}")
        time.sleep(0.10)

vybraza_fraze=random.choice(fraze)
print(vybraza_fraze)






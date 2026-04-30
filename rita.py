import turtle

t = turtle.Turtle()
t.speed(5)

# -------- FIGURER --------
def kvadrat(storlek, färg):
    t.color(färg)
    t.begin_fill()
    for _ in range(4):
        t.forward(storlek)
        t.right(90)
    t.end_fill()

def triangel(storlek, färg):
    t.color(färg)
    t.begin_fill()
    for _ in range(3):
        t.forward(storlek)
        t.left(120)
    t.end_fill()

def cirkel(radie, färg):
    t.color(färg)
    t.begin_fill()
    t.circle(radie)
    t.end_fill()

# -------- BLOMMA --------
def blomma(storlek, antal, färg):
    t.color(färg)
    for _ in range(antal):
        kvadrat(storlek, färg)
        t.right(360 / antal)

# -------- MENY --------
def meny():
    print("\n--- MENY ---")
    print("1. Rita kvadrat")
    print("2. Rita triangel")
    print("3. Rita cirkel")
    print("4. Rita blomma")
    print("5. Avsluta")

# -------- HUVUDPROGRAM --------
val = 0

while val != "5":
    meny()
    val = input("Välj alternativ: ")

    färg = input("Ange färg (t.ex. red, blue, green): ")

    if val == "1":
        kvadrat(100, färg)

    elif val == "2":
        triangel(100, färg)
    elif val == "3":
        cirkel(50, färg)

    elif val == "4":
        blomma(80, 12, färg)

    elif val == "5":
        print("Avslutar...")

    else:
        print("Fel val!")

turtle.done()
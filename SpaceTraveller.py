import random

print("You have been lifted off into space!")
print("There are many planets out there.")
print("There are inhabited planets and uninhabited planets.")
print("You have to explore the planets and find the inhabited planets.")

HealthBar = 100
FuelBar = 100
AmmoBar = 1000

print("Health:", HealthBar)
print("Fuel:", FuelBar)
print("Ammo:", AmmoBar)
print("If you run out of health or fuel, game over!")

Planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
Scenarios = [
    'You found food',
    'You found coal',
    'You found inhabitants',
    'You found guns',
    'You found guns and coal',
    'You found guns and food',
    'You found coal and food'
]

while True:
    print(" Planet [Fuel Required]")
    for i in range(len(Planets)):
        print(i+1, ". ", Planets[i], "[", (i+1)*10, "]")
    
    y = int(input("Choose the planet you want to land on (1-8):"))
    
    if y < 1 or y > 8:
        print("Invalid choice. Please choose a planet between 1 and 8.")
        continue

    FuelBar -= y * 10
    if FuelBar <= 0:
        print("You have run out of fuel! Game over!")
        break

    print("You have landed on", Planets[y-1])
    print("Fuel: ", FuelBar)
    
    r = int(input("1. Explore\n2. Return\n"))
    
    if r == 2:
        FuelBar -= y * 10
        if FuelBar <= 0:
            print("You ran out of fuel on the way back! Game over!")
            break
        else:
            print("Returned safely! Fuel: ", FuelBar)
            continue
    else:
        num = random.randint(0, 6)
        print(Scenarios[num])
        
        if num == 0:
            HealthBar += 10
            print("Health increased by 10. Current Health:", HealthBar)
        elif num == 1:
            FuelBar += 10
            print("You found coal! Fuel increased by 10. Current Fuel:", FuelBar)
        elif num == 2:
            print("You found inhabitants! They attack you!")
            strength = random.randint(1, 500)
            if strength >= HealthBar:
                print("They were too strong! You are dead. Game over!")
                HealthBar = 0
                break
            else:
                HealthBar -= strength
                AmmoBar -= strength
                print("You survived the attack! Health:", HealthBar, "Ammo:", AmmoBar)
        elif num == 3:
            AmmoBar += 50
            print("You found guns! Ammo increased by 50. Current Ammo:", AmmoBar)
        elif num == 4:
            FuelBar += 10
            AmmoBar += 50
            print("You found guns and coal! Fuel and Ammo increased. Fuel:", FuelBar, "Ammo:", AmmoBar)
        elif num == 5:
            HealthBar += 10
            AmmoBar += 50
            print("You found guns and food! Health and Ammo increased. Health:", HealthBar, "Ammo:", AmmoBar)
        elif num == 6:
            HealthBar += 10
            FuelBar += 10
            print("You found coal and food! Health and Fuel increased. Health:", HealthBar, "Fuel:", FuelBar)

    if HealthBar <= 0 or FuelBar <= 0:
        print("You ran out of health or fuel! Game over!")
        break

    x = input("Wanna explore another planet? (yes/no): ")
    if x != "yes":
        break

print("Game Over")
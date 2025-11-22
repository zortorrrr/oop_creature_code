class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

        if target.hp < 0:
            target.hp = 0

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"


# ===============================
# FlyingCreature Branch
# ===============================

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power, altitude=0):
        super().__init__(name, hp, attack_power)
        self.altitude = altitude

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!")

        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP is now {target.hp}")


# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")

        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP is now {target.hp}")


# ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = fire_level  # value 0–100

    def emit_fire(self, new_fire_level):
        # keep range between 0 and 100
        if new_fire_level < 0:
            new_fire_level = 0
        if new_fire_level > 100:
            new_fire_level = 100

        self.fire_level = new_fire_level
        print(f"{self.name}'s fire level is now {self.fire_level}")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        
        # fire bonus damage
        bonus = self.fire_level // 10     # every 10 fire level = +1 damage
        total_damage = self.attack_power + bonus

        print(f"{self.name} unleashes a fire blast at {target.name}!")
        print(f"Base damage {self.attack_power} + fire bonus {bonus} = {total_damage}")

        target.hp -= total_damage
        if target.hp < 0:
            target.hp = 0

        print(f"{target.name} HP is now {target.hp}")

# ===========================
# FireCreature Tests
# ===========================

if __name__ == "__main__":
    print("=== FireCreature Tests ===\n")

    pyro = FireCreature("Flame Spirit", 70, 9, fire_level=20)
    dummy = Creature("Practice Dummy", 50, 0)

    pyro.emit_fire(60)
    print(f"Fire level should be 60 → Actual: {pyro.fire_level}")

    pyro.attack(dummy)
    print(f"Dummy HP should be {50 - (9 + 6)} → Actual: {dummy.hp}")
    print()

    print("=== Tests Completed ===")


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

print("=== FireCreature Tests ===\n")

pyro = FireCreature("Flame Spirit", 70, 9, fire_level=20)
dummy = Creature("Practice Dummy", 50, 0)

pyro.emit_fire(60)
print(f"Fire level should be 60 → Actual: {pyro.fire_level}")

pyro.attack(dummy)
print(f"Dummy HP should be {50 - (9 + 6)} → Actual: {dummy.hp}")
print()

print("=== Tests Completed ===")


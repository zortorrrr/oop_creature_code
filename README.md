# Creature Battle Project (OOP + Git Branching Practice)

## Overview
This project is part of OOP Laboratory 4. The objective is to practice:
- Object-Oriented Programming (OOP)
- Inheritance and Method Overriding  
- Code testing with multiple creature types  
- Git branching, merging, and manual merge conflict resolution

Three creature subclasses were created on separate branches and later merged into the **main** branch:
- `flying_creature`
- `swimming_creature`
- `fire_creature`

Each branch adds new abilities and overrides the base class behavior.

---

## Base Class: Creature

### Attributes
- `name`  
- `hp`  
- `attack_power`

### Methods
- `attack(target)`  
  - Deals damage, prevents negative HP, prints attack messages  
- `is_alive()`  
- `__str__()`  

---

## FlyingCreature Class

### Extra Attribute
- `altitude`

### Extra Method
- `fly_to(new_altitude)`

### Overridden Method
- `attack()`  
  - Performs aerial-style attack messages  
  - Includes altitude information

---

## SwimmingCreature Class

### Extra Attribute
- `depth`

### Extra Method
- `dive_to(new_depth)`

### Overridden Method
- `attack()`  
  - Performs underwater-style attacks  
  - Includes depth information  

---

## FireCreature Class

### Extra Attribute
- `fire_level` (0–100)

### Extra Method
- `emit_fire(new_fire_level)`  
  - Adjusts fire power within the valid range

### Overridden Attack Behavior
- Fire damage increases based on fire_level  
- Formula:  

bonus_damage = fire_level // 10
total_damage = attack_power + bonus_damage

---

## Git Workflow Summary

### 1. Setup main project
git init
git add .
git commit -m "Add base Creature class"

### 2. Branch 1: flying_creature
git checkout -b flying_creature
Add FlyingCreature class
git add creature_simulation.py
git commit -m "Add FlyingCreature"

### 3. Branch 2: swimming_creature
git checkout main
git checkout -b swimming_creature
Add SwimmingCreature class
git add creature_simulation.py
git commit -m "Add SwimmingCreature"

### 4. Merge + Resolve Conflict
git checkout main
git merge flying_creature
git merge swimming_creature
Conflict occurs → Manually resolve in creature_simulation.py
git add creature_simulation.py
git commit -m "Resolve merge conflict"

### 5. Branch 3: fire_creature
git checkout -b fire_creature
Add FireCreature
git add creature_simulation.py
git commit -m "Add FireCreature class and tests"

### 6. Merge back to main
git checkout main
git merge fire_creature
git push

---

## How to Run
Simply execute:

python3 creature_simulation.py

All tests for:
- Creature  
- FlyingCreature  
- SwimmingCreature  
- FireCreature  

will automatically display.

---

## Author
**Kasithat Panya**  
Student ID: **6810545450**

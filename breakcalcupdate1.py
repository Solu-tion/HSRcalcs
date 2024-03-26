print("Hello ^^ This calc was made by Solv (@solu.tion on discord) \n When the calc asks you to input the character element refer back to this key:")
print("0 = Physical \n 1= Fire \n 2 = Ice \n 3 = Lightening \n 4 = Wind \n 5 = Quantum \n 6 = Imaginary")
print("Please note: This is only for damage calculating for the break, not the DoT/Entanglement damage")
print("Report any issues to my discord!! Thank you for using <3")

AttackerLvl = 80
EnemyLevel = 95
Defredpercent = float(input("Input def shred here:"))
DefIgnpercent = float(input("Input def ignore here:"))

totalenemylvl = EnemyLevel + 20
totalattackerlvl = AttackerLvl + 20

try:
    Defredpercent = Defredpercent / 100
    DefIgnpercent = DefIgnpercent / 100 
except ZeroDivisionError:
    if Defredpercent >= 0:
        Defredpercent = 0.0
    elif DefIgnpercent >= 0:
        DefIgnpercent = 0.0
    else:
        Defredpercent = 0.0
        DefIgnpercent = 0.0


DefMultiplier = float()

def defmultiplier(DefMultiplier, totalattackerlvl, totalenemylvl, Defredpercent, DefIgnpercent):
    DefMultiplier = (totalattackerlvl) / ((totalenemylvl) * (1 - Defredpercent - DefIgnpercent) + totalattackerlvl)
    if 1.0 < DefMultiplier:
       DefMultiplier = 1.0
    return DefMultiplier

BaseBreakDmg = 3767.5533
MaxToughnessMultiplier = 8.5
Physical = 2
Fire = 2
Ice = 1
Lightening = 1
Wind = 1
Quantum = 0.5
Imaginary = 0.5
BreakElement = [Physical, Fire, Ice, Lightening, Wind, Quantum, Imaginary]
BreakEffectPercent = float(input("Add Break eff here: "))
ResMultiplier = float(input("Add res pen here: "))
BaseDmg = BaseBreakDmg * BreakElement[int(input("input element here: "))]
WeaknessBreakDmg = float()
TotalBreakDmg = float()

def breakdmg(TotalBreakDmg, BaseDmg, BreakEffectPercent, DefMultiplier, ResMultiplier, MaxToughnessMultiplier):
    TotalBreakDmg = BaseDmg * (1 + (BreakEffectPercent / 100)) * defmultiplier(DefMultiplier, totalattackerlvl, totalenemylvl, Defredpercent, DefIgnpercent) * ((ResMultiplier + 100) / 100) * 0.9 * MaxToughnessMultiplier
    return TotalBreakDmg

print(breakdmg(TotalBreakDmg, BaseDmg, BreakEffectPercent, DefMultiplier, ResMultiplier, MaxToughnessMultiplier))
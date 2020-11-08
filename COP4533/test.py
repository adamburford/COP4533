
totalHP = 1000000.0
hp = totalHP
damageTick = 1000000
actualDamage = 0.0
totalRawDamage = 0.0
armor = 0.0

while hp > 0:
	armor = (1 - (hp/totalHP)) / 2
	actualDamage = damageTick * (1.0 - armor)

	if actualDamage > hp:
		actualDamage = hp
		totalRawDamage += actualDamage * (1 + armor)
	else:
		totalRawDamage += damageTick

	hp -= actualDamage

print(totalRawDamage/totalHP)
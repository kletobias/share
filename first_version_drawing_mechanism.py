import numpy as np
from decimal import *

getcontext().prec = 28
np.set_printoptions(precision=6)
single_cards = np.empty(5)
multiple_packs = {}
pack_num_list = []
entire_drawn_list = []
total_dust = []
# Defining rarity colors by integer numbers
common = 0
golden_common = 1
rare = 2
golden_rare = 3
epic = 4
golden_epic = 5
legendary = 6
golden_legendary = 7

# Associated draw chances by data from wiki:
# 70.14% 	21.51% 	4.19% 	1.00% 	3.17% 	1.49% 	1.33% 	0.25% 	0.09%
draw_common = 0.704
draw_golden_common = 0.0139
draw_rare = 0.2141
draw_golden_rare = 0.0133
draw_epic_temp = 0.0415 + (1 - 0.9999899999999998)
draw_epic = draw_epic_temp
print(draw_epic)
draw_golden_epic = 0.0023
draw_legendary = 0.01001
draw_golden_legendary = 0.00088
sum_draw_chances = np.sum([draw_common, draw_rare, draw_epic, draw_legendary, draw_golden_common, draw_golden_rare, draw_golden_epic, draw_golden_legendary])
print(sum_draw_chances)
listed_draw_probabilities = [draw_common, draw_rare, draw_epic, draw_legendary, draw_golden_common, draw_golden_rare, draw_golden_epic, draw_golden_legendary]
listed_draw_probabilities.sort()
print(str(listed_draw_probabilities[7]) + '\n')
# ss = 1
# decision = input('Do you want to input a value for the number of packs that should be simulated? Type either "yes" or "no": ')
# if decision == "yes":
# 	ceiling = input('Please enter an integer number of the number of packs you would like to simulate: ')
# 	ceiling = np.int(ceiling)
# else:
# 	ceiling = 10000
ceiling = 100000
for j in range(0, ceiling, 1):
	cards_in_pack = []
	multiple_packs[j] = []
	for card in range(0, 5, 1):
		draw_result = np.random.uniform(0, 1, 1)
		if draw_result <= listed_draw_probabilities[0]:
			cards_in_pack.append(golden_legendary)
			total_dust.append(1600)
		elif draw_result <= listed_draw_probabilities[1]:
			cards_in_pack.append(golden_epic)
			total_dust.append(400)
		elif draw_result <= listed_draw_probabilities[2]:
			cards_in_pack.append(legendary)
			total_dust.append(400)
		elif draw_result <= listed_draw_probabilities[3]:
			cards_in_pack.append(golden_rare)
			total_dust.append(100)
		elif draw_result <= listed_draw_probabilities[4]:
			cards_in_pack.append(golden_common)
			total_dust.append(50)
		elif draw_result <= listed_draw_probabilities[5]:
			cards_in_pack.append(epic)
			total_dust.append(100)
		elif draw_result <= listed_draw_probabilities[6]:
			cards_in_pack.append(rare)
			total_dust.append(20)
		else:
			cards_in_pack.append(common)
			total_dust.append(5)
		if (card == 4) and (max(cards_in_pack) < 2):
			cards_in_pack[card] = 2
			total_dust.append(20)
	# print("Total dust in this pack is: %s" % total_dust)
	multiple_packs[j].append(cards_in_pack)
	entire_drawn_list.append(cards_in_pack)
# print("Total dust in all packs is: %s" % total_dust)
print(max(entire_drawn_list))
out_array = np.asarray(entire_drawn_list)
unique_vals, freq = np.unique(out_array, return_counts=True)
print("In the simulation, the different rarity classes are from \"common\" to \"golden legendary\": %s" % unique_vals)
print("In the simulation the absolute drop count, for each of the respective rarity classes is: %s" % freq)



def percentage_droprate(listi):
	pct_list = []
	for x in listi:
		if type(x) != np.int64:
			pct = np.float((Decimal(x * 100) / Decimal(ceiling * 5)))
			pct_list.append(pct)
		else:
			pct = np.float(((x * 100) / Decimal(ceiling * 5)))
			pct_list.append(pct)
	return pct_list


print("In the simulation the drop rate, in percent of the respective rarity class is: %s" % percentage_droprate(freq))
avg_dust = np.average(total_dust)
avg_dust = avg_dust * 5
print("The average dust value per pack is: %s" % avg_dust)
dust_for_golden_legendary_packs = Decimal(3200) / Decimal(avg_dust)
print("The number of packs needed to craft that \"Golden Zephrys\" is: %s" % dust_for_golden_legendary_packs)

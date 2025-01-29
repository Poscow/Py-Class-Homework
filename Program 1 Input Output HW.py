#Input Data
slices_per_pizza = 8
family_members = 4
slices_per_person = input("How many slices per person \n")
#Calculate total slices needed
total_slices_needed = family_members * int(slices_per_person)
#Calculate numbers of pizzas needed
whole_pizza_needed = total_slices_needed // int(slices_per_pizza)
#Calculate leftover slices
leftover_slices = total_slices_needed % int(slices_per_pizza)
whole_pizza_needed, leftover_slices
#Output Data
print(f"You will need, {whole_pizza_needed} pizza(s) and, {leftover_slices} leftover slices.")

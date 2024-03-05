# current stock of medical/Pharmacy supplies
medical_supplies = [
  {"item_name": "Syringes", "quantity": 1500, "reorder_point": 500}, 
  {"item_name": "Sodium Chloride 0.9 % 1 Liter Bags", "quantity": 500,"reorder_point": 250},
  {"item_name": "Heparin Syrings", "quantity": 500, "reorder_point": 250},
  {"item_name": "Metformin 100 Tabs", "quantity": 1000, "reorder_point": 500},
  {"item_name": "Lisinopril 10mg Tabs", "quantity": 100, "reorder_point": 15},
  {"item_name": "Levothyroxine 50mcg Tabs", "quantity": 100, "reorder_point": 30},
  {"item_name": "Warfarin 3mg Tabs", "quantity": 100, "reorder_point": 25},
  {"item_name": "Syringe Needles", "quantity": 500, "reorder_point": 150 }, 
  {"item_name": "Intravenous Catheters", "quantity": 200, "reorder_point": 50},                                                      
  {"item_name": "Empty vials", "quantity": 100, "reorder_point": 50}
  ]
# Extracting information
warfarin_item = [x for x in medical_supplies if x["item_name"] == "Warfarin 3mg Tabs"]
print(warfarin_item)

warfarin_item = [x for x in medical_supplies if x["reorder_point"] == 15]
print(warfarin_item)

#User input trying to find the item being updated
user_input = input("Enter the item name being updated: ")
# find the item
item_found = False
for i, item in enumerate(medical_supplies):
  if item["item_name"] == user_input:
    item_found = True
    break
if item_found:
  #if item is found then get input for the new quantity being updated
  new_quantity = int(input("Enter new quantity: "))

  #update the quantity in the dictionary
  medical_supplies[i]["quantity"] = new_quantity
  #print confirmation message
  print(f"{user_input} quantity updated to {new_quantity}. ")
else:
  print(f"Item {user_input} not found in the list.")
        


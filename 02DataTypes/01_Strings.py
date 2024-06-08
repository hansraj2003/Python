chai = "Masala Chai"
first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)

num_list = "0123456789"
print(num_list[0:7:2])   
# this 2 tells the hoping of the digits in the required data.       if its 2, one number is skipped. If its 3, 2 digits are skipped.

print(chai.lower())
print(chai.upper())

chai = "   Masala Chai   "
print(chai)
print(chai.strip())

chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split())
print(chai.split(", "))

chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("chai"))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)
print(", ".join(chai_variety))

chai = "Masala Chai" 
print(len(chai))
for letter in chai:
    print(letter)

chai = "He said, \"Masala chai is awesome\""
print(chai)

chai = "Masala\nChai"
print(chai)

chai = r"Masala\nChai"
print(chai)

chai = "Masala Chai"
print("Masala" in chai)
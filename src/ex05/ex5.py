name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_in_cms = round(height * 2.54)
weight_in_kgs = round(weight / 2.2)

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"That is {height_in_cms} cm.")
print(f"He's {weight} pounds heavy.")
print(f"That is {weight_in_kgs} kg.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

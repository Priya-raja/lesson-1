"""Make a set and filter"""

recipes = {
    "Masala Chai":["ginger","cardamom","clove"],
    "Elaichi Chai": ["milk","cardamom"],
    "Spicy chai":["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
def display_stars(stars):
    print("*"*stars, end="\n")
display_stars(5)

def display_stars_and_space(stars, spaces):
    print(" "*spaces,"*"*stars , end="\n")
display_stars_and_space(5,4)

def display_pyramid(height):
    for i in range(0, height):
        stars = 1 + (2*i)
        space = (height)-(i)
        display_stars_and_space(stars, space)
display_pyramid(5)
display_pyramid(10)
display_pyramid(15)
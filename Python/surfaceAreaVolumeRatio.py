while True:

    print("Type 'x' to exit")

    #Used to find get the side length of the shape
    sideLength = input("Input the side length as cm: ")

    #Breaking out of the loop
    if sideLength.upper() == "X":
        break

    #Getting the volume
    volume = float(sideLength) * float(sideLength) * float(sideLength)

    #Getting the surface area
    surfaceArea = 6 * (float(sideLength) * float(sideLength))

    #Getting the surface area ratio
    surfaceAreaRatio = float(surfaceArea) / float(volume)

    print(f"\nThe volume is {volume}cm^3")
    print(f"The surface area is {surfaceArea}cm^2")
    print(f"The surface area ratio is {surfaceAreaRatio}\n\n")
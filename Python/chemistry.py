atomicList = []
atomicInput = ""
finalAtomic = 0.0

massInput = 0.0

result = 0.0

while True:
    atomicInput = input("Enter atomic mass (float): ")

    if atomicInput == "stop" or atomicInput == "":
        break
    else:
        atomicList.append(float(atomicInput))

if atomicInput == "":
    massInput = float(input("Enter mass of substance: "))
    
    for i in range(len(atomicList)):
        print(atomicList[i])

        finalAtomic = finalAtomic + atomicList[i]

    result = float(massInput) / float(finalAtomic)

    print(f"\n\nMr of substance: {str(finalAtomic)}")
    print(f"Final calculation for moles: {str(result)}")

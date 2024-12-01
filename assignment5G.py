def AMCount():
    try:
        with open("article.txt", "r") as file:
            count_a = 0
            count_m = 0

            for line in file:
                for char in line:
                    if char.lower() == 'a':
                        count_a += 1
                    elif char.lower() == 'm':
                        count_m += 1

        print(f"Occurrences of 'A/a': {count_a}")
        print(f"Occurrences of 'M/m': {count_m}")

    except FileNotFoundError:
        print("Error: The file 'STORY.TXT' was not found.")

AMCount()
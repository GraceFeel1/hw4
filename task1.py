
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")

                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count

        return total, average

    except FileNotFoundError:
        print("File not found.")
        return 0, 0

    except (ValueError, OSError):
        print("Error reading file.")
        return 0, 0


total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

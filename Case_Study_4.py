file_path = "CS4.txt"

with open(file_path, "r") as f:
    content = f.read()

with open(file_path, "r") as f:
    first_line = f.readline()
    second_line = f.readline()

with open(file_path, "r") as f:
    lines = f.readlines()

print("---- Task 1 Output ----")
print("Total number of lines:", len(lines))

print("\nFirst 2 lines:")
print(first_line, end="")
print(second_line, end="")

print("\nLast 2 lines:")
print(lines[-2], end="")
print(lines[-1], end="")

# -------- Task 2: Log Classification --------
log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for line in lines:
    if "INFO" in line:
        log_counts["INFO"] += 1
    if "WARNING" in line:
        log_counts["WARNING"] += 1
    if "ERROR" in line:
        log_counts["ERROR"] += 1

print("\n---- Task 2 Output ----")
print("Log counts:", log_counts)

# -------- Task 3: Write Filtered Files --------
info_lines = []
warning_lines = []
error_lines = []

for line in lines:
    if "INFO" in line:
        info_lines.append(line)
    if "WARNING" in line:
        warning_lines.append(line)
    if "ERROR" in line:
        error_lines.append(line)

with open("info_logs.txt", "w") as f:
    f.writelines(info_lines)

with open("warning_logs.txt", "w") as f:
    f.writelines(warning_lines)

with open("error_logs.txt", "w") as f:
    f.writelines(error_lines)

print("\n---- Task 3 Output ----")
print("Filtered files created successfully.")

# -------- Task 4: Search Feature --------
keyword = input("\nEnter keyword to search (INFO/WARNING/ERROR): ")

matching_lines = []

for line in lines:
    if keyword in line:
        print(line, end="")
        matching_lines.append(line)

with open("search_result.txt", "w") as f:
    f.writelines(matching_lines)

print("\nSearch results saved in search_result.txt")

# -------- File Pointer Operations --------
print("\n---- File Pointer Operations ----")

with open(file_path, "rb") as f:
    # First 50 chars
    print("\nFirst 50 characters:\n", f.read(50).decode())

    # Beginning
    f.seek(0)
    print("\nAfter seek(0):\n", f.read(50).decode())

    # Middle
    f.seek(len(content) // 2)
    print("\nFrom middle:\n", f.read(50).decode())

    # Last 100 chars
    f.seek(-100, 2)
    print("\nLast 100 characters:\n", f.read().decode())
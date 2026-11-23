failed_count=0 
with open("sample.log", "r", encoding="utf-8") as file:
    for line in file: 
         if "LOGIN_FAILED" in line:
                failed_count += 1 
                print(line, end="")
print(failed_count)

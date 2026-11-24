failed_count = 0            #count for amount of "failed" times
failures_by_ip = {}     #count for certain IPs
file_path = input("Enter the path to your file ").strip()
try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:       #for loop that'll go thru each line and check for "failed"
            if "LOGIN_FAILED" in line: 
                failed_count += 1 
                parts = line.split()     #splits the text into sections 
                ip_field = parts[3]      #grabs the 'Ip' part of the section that we need 
                ip_parts = ip_field.split("=") 
                ip_address = ip_parts[1]
                current_count = failures_by_ip.get(ip_address, 0)
                failures_by_ip[ip_address] = current_count + 1

except FileNotFoundError:
    print("Error: That file could not be found. Check the path and try againn")
except PermissionError:
    print("Error: You do not have permission to read this file.")
else:
    for ip, count in failures_by_ip.items(): # .items() allows for the loop to grab 'ip', and 'count'" 
        print(ip, count)
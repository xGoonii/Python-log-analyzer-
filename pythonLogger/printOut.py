failed_count = 0            #count for amount of "failed" times
failures_by_ip = {}         #count for certain IPs
with open("sample.log", "r", encoding="utf-8") as file:     #this is opening the file 
    for line in file:       #for loop that'll go thru each line and check for "failed"
         if "LOGIN_FAILED" in line: 
                failed_count += 1 
                parts = line.split()     #splits the text into sections 
                ip_field = parts[3]      #grabs the 'Ip' part of the section that we need 
                ip_parts = ip_field.split("=") 
                ip_address = ip_parts[1]
                current_count = failures_by_ip.get(ip_address, 0)
                failures_by_ip[ip_address] = current_count + 1
print(failed_count)
print(failures_by_ip)

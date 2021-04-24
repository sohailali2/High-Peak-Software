
input_file =open("input.txt","r")
output_file = open("output.txt","w+")
goodies={}
output_list=[]

for f in input_file:
    index_toRead_price=f.index(":")
    print(f[index_toRead_price+1:].strip())
    print(f[:index_toRead_price])
    goodies[f[:index_toRead_price]]=f[index_toRead_price+1:].strip()

print(goodies)
prices_only=list(goodies.values())

prices_only=[int (i) for i in prices_only]
prices_only.sort(reverse=True)
print(prices_only)
no_of_employees=int(input("Enter number of employees :"))

length_considered=(len(prices_only)-no_of_employees)
print(length_considered)


for i in range(length_considered):
    maxPrice=prices_only[i]
    minPrice=prices_only[no_of_employees+i]
    if i == 0:
        difference=maxPrice-minPrice
        choosen_index=i
    elif (maxPrice-minPrice)<difference:
        difference=maxPrice-minPrice
        choosen_index=i


choosen_prices=prices_only[choosen_index:no_of_employees+choosen_index]
difference=max(choosen_prices)-min(choosen_prices)
print("difference",difference)


count=0
for key,value in goodies.items():
    prices_only[count]
    print(value)
    if int(value)in choosen_prices and count<no_of_employees:
        strl=key+": "+value

        output_list.append(strl)
        count+=1
        print(strl)

output_file.write("The goodies selected for distribution are:")
output_file.write("\n")

for i in output_list:
    output_file.write(i)
    output_file.write("\n")
output_file.write("And the difference between the chosen goodies with highest price and the lowest price is  "+str(difference))

input_file.close()
output_file.close()

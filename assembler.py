ins_bin = [
    0b0010_0000, # Load next value in RAM to R0
    0b0000_0010, # Number 2
    0b0010_0001, # Load next value in RAM to R1
    0b0000_0001, # Number 1
    0b1000_0001, # Add regsiter R0 to R1 and store in R1
]

for ins_hex in map(hex, ins_bin):
    print(ins_hex)

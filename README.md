# Toy CPU

To run code, go to `programs/` to find programs, which can be loaded into the memory.
To load into memory, go to `CPU` and from there jump inside of `RAM 256`. Right click on the RAM
and select `Load Image`.

## Intruction Set

### LOAD/STORE Instructions

Load/Store information from/to the RAM to/from a register.

Bits:
* Bit 7, 6, 5: 0 0 0
* Bit 4: 0 means LOAD, 1 means STORE
* Bit 3, 2: Reg A
* Bit 1, 0: Reg B

Reg A = Contains Destination/Source RAM address
Reg B = Source/Destination Register

### Data Instructions

Load next 8 bits from the next RAM address into a register.

Bits:
* Bit 7, 6, 5, 4:  0 0 1 0
* Bit 3, 2: Irrelevant
* Bit 1, 0: Destination Register

### Jump Register Instruction

Jump to memory location pointed by a register.

Bits:
* Bit 7, 6, 5, 4: 0 0 1 1
* Bit 3, 2: Irrelevant
* Bit 1, 0: RAM address source register

### Jump Address Instruction

Jump to next byte in the RAM.

Bits:
* Bit 7, 6, 5, 4: 0 1 0 0
* Bit 3, 2, 1, 0: Irrelevant

### Jump If Instruction

Jump to address in next RAM location if flags set.

Bits:
* Bit 7, 6, 5, 4: 0 1 0 1
* Bit 3 (C): Carry Flag
* Bit 2 (A): A > B
* Bit 1 (E): A = B
* Bit 0 (Z): Zero

| Flags | Jump condition |
| ----- | -------------- |
| 0000  | No Jump |
| 0001  | JZ (Jump Zero) |
| 0010  | JE (jump if A=B) |
| 0011  | JEZ (jump if A=B OR Zero) |
| 0100  | JA (jump if A>B) |
| 0101  | JAZ (jump if A>B OR Zero|
| 0110  | JAE (jump if A>=B) |
| 0111  | JAEZ (jump if A>=B OR Zero) |
| 1000  | JC (Jump if Carry) |
| 1001  | JCZ (Jump if Carry OR Zero) |
| 1010  | JCE (Jump if Carry OR A=B) |
| 1011  | JCEZ (Jump if Carry OR A=B OR Zero ) |
| 1100  | JCA (Jump if Carry OR A>B) |
| 1101  | JCAZ (Jump if Carry OR A>B OR Zero) |
| 1110  | JCAE (Jump if Carry OR A>=B) |
| 1111  | JCAEZ (Jump if Carry OR A>=B OR Zero) |

### Clear Flags Instruction

Sets all the flags to 0.

Bits:
* Bit 7, 6, 5, 4: 0 1 1 0
* Bit 3, 2, 1, 0: Irrelevant

### ALU Instructions

* Bit 7: 1 (identifies as an ALU instruction)
* Bit 6, 5, 4: ALU Op Code
* Bit 3, 2: Reg A
* Bit 1, 0: Reg B

#### Op Codes

| Instruction | Bits |
|---|---|
| ADD | 0 0 0 |
| SHR | 0 0 1 |
| SHL | 0 1 0 |
| NOT | 0 1 1 |
| AND | 1 0 0 |
| OR  | 1 0 1 |
| XOR | 1 1 0 |
| CMP | 1 1 1 |

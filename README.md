# Toy CPU

## Intruction Set

### LOAD/STORE Instruction

Bits:
* Bit 7: 0 (identifies as a LOAD/STORE instruction)
* Bit 6, 5: EMPTY
* Bit 4: 0 means LOAD, 1 means STORE
* Bit 3, 2: Reg A
* Bit 1, 0: Reg B

Reg A = Destination/Source RAM address
Reg B = Source/Destination Register

### ALU Instruction

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

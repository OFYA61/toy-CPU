# Toy CPU

## Intruction Set

### LOAD/STORE Instruction

Bit 7: 0 (identifies as a LOAD/STORE instruction)
Bit 6, 5: EMPTY
Bit 4: 0 means LOAD, 1 means STORE
Bit 3, 2: Reg A
Bit 1, 0: Reg B

| 1 | _ | _ | OP | REG_A1 | REG_A0 | REG_B1 | REG_B0 |

#### Op Codes

| Instruction | Bits
| ADD | 0 0 0 |
| SHR | 0 0 1 |
| SHL | 0 1 0 |
| NOT | 0 1 1 |
| AND | 1 0 0 |
| OR  | 1 0 1 |
| XOR | 1 1 0 |
| CMP | 1 1 1 |

### ALU Instruction

Bit 7: 1 (identifies as an ALU instruction)
Bit 6, 5, 4: ALU Op Code
Bit 3, 2: Reg A
Bit 1, 0: Reg B

| 1 | OP_2 | OP_1 | OP_0 | REG_A1 | REG_A0 | REG_B1 | REG_B0 |

#### Op Codes

| Instruction | Bits
| ADD | 0 0 0 |
| SHR | 0 0 1 |
| SHL | 0 1 0 |
| NOT | 0 1 1 |
| AND | 1 0 0 |
| OR  | 1 0 1 |
| XOR | 1 1 0 |
| CMP | 1 1 1 |

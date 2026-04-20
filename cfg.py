# Simple Control Flow Graph + Data Flow

def build_cfg(statements):
    cfg = {}
    
    for i in range(len(statements)):
        cfg[i] = []
        
        # Normal flow
        if i + 1 < len(statements):
            cfg[i].append(i + 1)
    
    return cfg


def data_flow_analysis(statements):
    print("\nData Flow Analysis:")

    for i, stmt in enumerate(statements):
        parts = stmt.split("=")
        
        if len(parts) == 2:
            defined = parts[0].strip()
            used = parts[1].strip()

            print(f"Line {i}:")
            print(f"  Defined → {defined}")
            print(f"  Used    → {used}")


# Input
n = int(input("Enter number of statements: "))
statements = []

for _ in range(n):
    statements.append(input())

# CFG
cfg = build_cfg(statements)

print("\nControl Flow Graph:")
for node in cfg:
    print(f"{node} -> {cfg[node]}")

# Data Flow
data_flow_analysis(statements)
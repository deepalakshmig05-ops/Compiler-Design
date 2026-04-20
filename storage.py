# Simulating Stack, Heap, Static allocation

# Static memory
static_memory = {"x": 10}

# Stack simulation
stack = []

# Heap simulation
heap = {}

heap_address = 1000


def push_stack(value):
    stack.append(value)
    print(f"Stack PUSH → {value}")


def pop_stack():
    if stack:
        val = stack.pop()
        print(f"Stack POP → {val}")


def allocate_heap(value):
    global heap_address
    heap[heap_address] = value
    print(f"Heap Allocated → Address {heap_address}, Value {value}")
    heap_address += 1


def show_memory():
    print("\nStatic Memory:", static_memory)
    print("Stack:", stack)
    print("Heap:", heap)


# Demo
push_stack(5)
push_stack(10)
pop_stack()

allocate_heap(50)
allocate_heap(100)

show_memory()
# Compiler
CC = gcc
# Compiler Flags
CFLAGS = -Wall -g
# Source and Output Files
SRC = main.c
OBJ = main.o
ASM = main.s
PREPROC = main.i
EXEC = main

# Default target
all: preprocess compile assemble link run

# Step 1: Preprocessing
preprocess:
	$(CC) $(CFLAGS) -E $(SRC) -o $(PREPROC)
	@echo "Preprocessing done."

# Step 2: Compilation (Convert C to Assembly)
compile:
	$(CC) $(CFLAGS) -S $(SRC) -o $(ASM)
	@echo "Compilation to Assembly done."

# Step 3: Assembling (Convert Assembly to Object file)
assemble:
	$(CC) $(CFLAGS) -c $(SRC) -o $(OBJ)
	@echo "Assembling done."

# Step 4: Linking (Generate Executable)
link:
	$(CC) $(OBJ) -o $(EXEC)
	@echo "Linking done. Executable created."

# Step 5: Running the executable
run: link
	./$(EXEC)

# Cleanup generated files
clean:
	rm -f $(OBJ) $(ASM) $(PREPROC) $(EXEC)
	@echo "Cleanup done."


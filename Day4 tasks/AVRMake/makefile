# AVR Toolchain
CC = avr-gcc
OBJCOPY = avr-objcopy
AVRDUDE = avrdude

# MCU Settings (Modify as needed)
MCU ?= atmega328p      # Change for different AVR chips (e.g., attiny85, atmega16)
F_CPU ?= 16000000UL    # Clock speed (16MHz default, change as needed)
PROGRAMMER ?= arduino  # Programmer type (usbasp, arduino, avr109, etc.)
PORT ?= /dev/ttyUSB0   # Serial port (Windows: COMx, Linux/macOS: /dev/ttyUSBx)

# Compilation Flags
CFLAGS = -Wall -g -Os -mmcu=$(MCU) -DF_CPU=$(F_CPU)

# File Names
SRC = main.c
OBJ = main.o
ELF = main.elf
HEX = main.hex

# Default target: Build and Upload
all: compile link hex upload

# Step 1: Compile C to Object File
compile:
	$(CC) $(CFLAGS) -c $(SRC) -o $(OBJ)
	@echo "Compilation completed (Created $(OBJ))."

# Step 2: Link Object File to ELF
link: compile
	$(CC) $(CFLAGS) $(OBJ) -o $(ELF)
	@echo "Linking completed (Created $(ELF))."

# Step 3: Convert ELF to HEX
hex: link
	$(OBJCOPY) -O ihex -R .eeprom $(ELF) $(HEX)
	@echo "HEX file generated (Created $(HEX))."

# Step 4: Upload HEX to AVR
upload: hex
	$(AVRDUDE) -c $(PROGRAMMER) -p $(MCU) -P $(PORT) -U flash:w:$(HEX):i
	@echo "Upload completed. Your AVR is now running the program!"

# Cleanup
clean:
	rm -f $(OBJ) $(ELF) $(HEX)
	@echo "Cleanup done."

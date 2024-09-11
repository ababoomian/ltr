import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# LTR390 I2C address is 0x53
LTR390_ADDR = 0x53

try:
    bus.write_byte(LTR390_ADDR, 0x00)
    print("Successfully communicated with the sensor.")
except OSError as e:
    print(f"Failed to communicate: {e}")


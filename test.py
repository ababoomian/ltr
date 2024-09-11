import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# LTR390 I2C address is 0x53
LTR390_ADDR = 0x53

def read_uv_index():
    # Set mode to UVS (UV sensing mode)
    bus.write_byte_data(LTR390_ADDR, 0x00, 0x0A)
    time.sleep(0.1)
    
    # Read 2 bytes of UV data
    uv_data = bus.read_i2c_block_data(LTR390_ADDR, 0x08, 2)
    
    # Combine the two bytes and return the UV index
    uv_index = (uv_data[1] << 8) | uv_data[0]
    return uv_index

try:
    while True:
        uvi = read_uv_index()
        print(f"UV Index: {uvi}")
        time.sleep(1)
except KeyboardInterrupt:
    pass


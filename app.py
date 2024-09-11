from light_sensor import LightSensor

import time

def main():
    """
    Main application function to read data from the light sensor.
    """
    # Initialize the light sensor
    sensor = LightSensor()

    if sensor.working:
        print("Light sensor initialized and ready.")
    else:
        print("Light sensor is not working or initialized.")

    try:
        # Continuously read sensor data in a loop
        while True:
            data = sensor.read_data()
            uv = data.get("uv")
            lux = data.get("lux")

            if uv is not None and lux is not None:
                print(f"UV Index: {uv}, Lux: {lux}")
            else:
                print("Failed to read valid sensor data.")

            # Sleep for 10 seconds before the next read
            time.sleep(10)

    except KeyboardInterrupt:
        print("Application terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()


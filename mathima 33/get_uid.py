import os

try:
    uid = os.getuid()
    print("User ID:", uid)
except AttributeError:
    print("os.getuid() is not supported on this platform.")
except OSError as e:
    print(f"An error occurred: {e}")

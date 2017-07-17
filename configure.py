# import os


# Takes user inputs to get necessary information about the user's setup.
# Only has to be run once.

input("""This is a one-time configuration for your mirror setup.
Please just answer a few questions to get started.\n
Press Enter to continue""")

height = input("""How high above your target is the center of your mirror? """)
distance = input("""What is the distance between your target and your mirror, measured horizontally? """)
angle = input("""Standing on the target spot, what direction is the mirror from where you are?\nAnswer in degrees, and be as precise as possible.\nNote that 0° is due north and 90° is due east. """)
lat = input('Enter your latitude: ')
lon = input('Enter your longitude: ')

with open('configuration.csv', 'w') as f:
    f.write(",".join([height, distance, angle, lat, lon]))

print("Success!")
input("Press Enter to quit")

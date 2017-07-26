# import os


# Takes user inputs to get necessary information about the user's setup.
# Only has to be run once.

def config():
    input("This is a one-time configuration for your mirror setup."
          "\nPress Enter to continue.\n")

    height = input("How high above your target is the center of your mirror? ")
    distance = input("\nWhat is the distance between your target"
                     " and your mirror, measured horizontally? ")
    angle = input("\nStanding on the target spot, what direction is the"
                  " mirror from where you are?\nAnswer in degrees, and be as"
                  " precise as possible.\n"
                  "Note that 0° is due north and 90° is due east. ")
    lat = input('\nEnter your latitude: ')
    lon = input('\nEnter your longitude: ')

    with open('configuration.csv', 'w') as f:
        f.write(",".join([height, distance, angle, lat, lon]))

    print("Success!")


if __name__ == '__main__':
    config()
    input("Press Enter to quit")

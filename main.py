""" Main class for character creation """

from koikatsu_child_generator.chara import Child

# Add path to mother character and father character
child = Child(mother="", father="", output_name="new_child")


if __name__ == "__main__":
    # creates child character (True == Female, False == Male, defaults to Female)
    child.create(False)

    # creates child character with random gender
    #child.create_random()

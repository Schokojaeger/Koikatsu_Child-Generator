""" Main class for character creation """

from koikatsu_child_generator.chara import Child

# Add path to mother character and father character
child = Child(mother="", father="", output_name="new_child")

# TODO make it cli-usable ya doofus
if __name__ == "__main__":
    # creates child character (True == Female, False == Male, defaults to Female)
    child.create()

    # creates child character with random gender
    #child.create_random()

""" base class for character creation/manipulation """

import copy
import random
from kkloader import KoikatuCharaData
from koikatsu_child_generator import constants
from koikatsu_child_generator.mother import Mother
from koikatsu_child_generator.father import Father


class Child:
    """ base class for creating children """

    def __init__(self, mother, father, output_name):
        if not isinstance(mother, str) and isinstance(father, str):
            raise TypeError("Both 'Mother' and 'Father' Files must be the "\
                            "filename of the corresponding .png file in String Format")

        if not isinstance(output_name, str):
            raise TypeError("Parameter 'output_name' should be a string with "\
                            "the name the file should be called after creation")

        self.motherc = Mother(f"./{mother}.png")
        self.mother = KoikatuCharaData.load(f"./{mother}.png")
        self.fatherc = Father(f"./{father}.png")
        self.father = KoikatuCharaData.load(f"./{father}.png")

        self.child = KoikatuCharaData()
        self.child.image = self.mother.image
        self.child.face_image = self.mother.image
        self.child.product_no = 100
        self.child.header = "【KoiKatuChara】".encode("utf-8")
        self.child.version = "0.0.0".encode("ascii")
        self.child.blockdata = copy.deepcopy(self.mother.blockdata)
        # TODO try moving the block below to the specific methods to use the correct KKEx
        #      for the respective gender
        # if hasattr(self.mother, "KKEx"):
        #     self.child["KKEx"] = copy.deepcopy(self.mother["KKEx"])
        self.child["Custom"] = copy.deepcopy(self.mother["Custom"])
        self.child["Coordinate"] = copy.deepcopy(self.mother["Coordinate"])
        self.child["Parameter"] = copy.deepcopy(self.mother["Parameter"])
        self.child["Status"] = copy.deepcopy(self.mother["Status"])
        self.output_name = output_name

        # Because of all the different kinds of accessories (vanilla or modded), and all the things
        # they can fuck up, children will not inherit any accessories whatsoever
        # NOTE perhaps in the future you'll be able to select which ones to carry over
        c = 0
        while c < 7:
            for i in self.child["Coordinate"][c]["accessory"]["parts"]:
                i["type"] = 0
            c += 1


    def modify_value(self, base_value, percentage_change) -> float:
        """ change current value randomly within a certain range """
        min_value = base_value - (base_value * percentage_change)
        max_value = base_value + (base_value * percentage_change)
        new_value = random.uniform(min_value, max_value)
        # TODO add minimum and maximum values here for the sliders
        # or you'll get very ugly integer overflows
        # e.g. both have the maximum value or minimum value for sliders, it
        # could modify the value upwards, which would result in a very
        # low slider value

        return new_value

    # inherit_face() does not need a gender boolean. The face will be put together from both
    # parents in the same way, regardless of gender
    def inherit_face(self) -> None:
        """ take faceslider values of parent characters, modify and save as child facesliders """

        # loop through facesliders and modify all values to a random degree
        # (currently 50% up or down from base)
        for i in constants.list_faceslider:
            currm = constants.getv(self.mother, i)
            currf = constants.getv(self.father, i)
            if currm == 0.0 and currf == 0.0:       # TODO test this with 0 values, non-zero values
                continue                            # and alternating (currm == 0 but currf != 0)
            middle_value = (currm + currf) / 2
            # changing the randomization of head size to 20% (can get pretty fucked)
            # we only use the mother's head size here to determine if the current
            # item really is the head size
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][1]:
                newitem = self.modify_value(middle_value, 0.2)
                constants.setv(self.child, i, newitem)
            else:
                newitem = self.modify_value(middle_value, 0.5)
                # set resulting value as corresponding faceslider value of child
                constants.setv(self.child, i, newitem)

        # Inherit nose from parents
        nose_options = (self.mother["Custom"]["face"]["noseId"],
                        self.father["Custom"]["face"]["noseId"])

        self.child["Custom"]["face"]["noseId"] = random.choice(nose_options)
        if self.child["Custom"]["face"]["noseId"] == self.mother["Custom"]["face"]["noseId"]:
            print("Nose: Mother")
        else:
            print("Nose: Father")

        # Set Lip Line Type to either inherit from parents or 0
        lipline_options = (self.mother["Custom"]["face"]["lipLineId"],
                           self.father["Custom"]["face"]["lipLineId"], 0)

        self.child["Custom"]["face"]["lipLineId"] = random.choice(lipline_options)

        if self.child["Custom"]["face"]["lipLineId"] == self.mother["Custom"]["face"]["lipLineId"]:
            print("Lip Line: Mother")

        elif (self.child["Custom"]["face"]["lipLineId"] ==
              self.father["Custom"]["face"]["lipLineId"]):
            print("Lip Line: Father")

        elif self.child["Custom"]["face"]["lipLineId"] == 0:
            print("Lip Line: None")
        # TODO set Lip Line color according to inherited skin color (Black Skin with
        # white line could look really weird for example)

        # Mole selection from parents and no mole
        mole_options = (self.father["Custom"]["face"]["moleId"],
                        self.mother["Custom"]["face"]["moleId"], 0)
        # Set mole for child
        self.child["Custom"]["face"]["moleId"] = random.choice(mole_options)

        if self.child["Custom"]["face"]["moleId"] == self.mother["Custom"]["face"]["moleId"]:
            self.child["Custom"]["face"]["moleColor"] = self.mother["Custom"]["face"]["moleColor"]
            self.child["Custom"]["face"]["moleLayout"] = self.mother["Custom"]["face"]["moleLayout"]
            print("Mole: Mother")

        elif self.child["Custom"]["face"]["moleId"] == self.father["Custom"]["face"]["moleId"]:
            self.child["Custom"]["face"]["moleColor"] = self.father["Custom"]["face"]["moleColor"]
            self.child["Custom"]["face"]["moleLayout"] = self.father["Custom"]["face"]["moleLayout"]
            print("Mole: Father")

        elif self.child["Custom"]["face"]["moleId"] == 0:
            print("Mole: None")

        # Set all makeup to empty
        # NOTE Some vanilla options for various makeup can look a bit weird at times. So
        # as to not create some abominations and to give the users a "clean" version of
        # their character, we'll just leave all makeup options empty
        self.child["Custom"]["face"]["baseMakeup"]["eyeshadowId"] = 0
        self.child["Custom"]["face"]["baseMakeup"]["cheekId"] = 0
        self.child["Custom"]["face"]["baseMakeup"]["lipId"] = 0
        self.child["Custom"]["face"]["baseMakeup"]["paintId"][0] = 0
        self.child["Custom"]["face"]["baseMakeup"]["paintId"][1] = 0


    # Parameter "gender": True == Female, False == Male
    def inherit_body(self, gender: bool) -> None:
        """ take bodyslider values of parent characters, modify and save as child bodysliders """

        # loop through bodysliders and modify all values to a random degree
        for i in constants.list_bodyslider:
            currm = constants.getv(self.mother, i)
            currf = constants.getv(self.father, i)
            if currm == 0.0 and currf == 0.0:       # TODO test this check
                continue
            # changing the randomization of breast size
            # Using the mother's breast size since using a middle value of both parents would likely
            # always result in a small chest size (father will usually have a very small size)
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][4]:
                if not gender:
                    # for male children, breast size is irrelevant
                    constants.setv(self.child, i, 0) # TODO check if 0 is actually correct for males, perhaps use 'currf' instead
                    print("Male: No Boobs")
                    continue
                # using a modifier of 50% to not always get basically the same size as the mother
                newitem = self.modify_value(currm, 0.5)
                print("Boobs", newitem)
                constants.setv(self.child, i, newitem)
                continue
            # changing the randomization of butt angle (can get really fucked up)
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][27]:
                # For male children, butt size will be determined by the father's
                if not gender:
                    newitem = self.modify_value(currf, 0.15)
                    constants.setv(self.child, i, newitem)
                    continue
                # Using the mother's butt size for female children
                newitem = self.modify_value(currm, 0.15)
                constants.setv(self.child, i, newitem)
                continue

            middle_value = (currm + currf) / 2
            newitem = self.modify_value(middle_value, 0.3)
            # set resulting value as corresponding bodyslider value of child
            constants.setv(self.child, i, newitem)


    # Parameter "gender": True == Female, False == Male
    # TODO add functionality for male children, mainly look for all hairstyles
    # associated with male characters
    def inherit_hair(self, gender: bool) -> None:
        """ use either mother's or father's haircolor (or in combination)
            to determine the child's hair color and choose random
            hair options from the vanilla selection """

        # Vanilla female hairstyles for Back Hair
        # TODO add male hair selection
        # For some reason, the vanilla back hairstyles end at 58 and pick back up at 200?????
        back_hair_options = list(range(0, 59)) + list(range(200, 210))
        # Set random Back Hair
        self.child["Custom"]["hair"]["parts"][0]["id"] = random.choice(back_hair_options)
        print("Back Hair ID: " , self.child["Custom"]["hair"]["parts"][0]["id"])

        # Vanilla female hairstyles for Front Hair
        # And here, the vanilla hairstyles end at 20, pick back up at 70, stop again,
        # and then start again at 200?????
        front_hair_options = list(range(1, 21)) + list(range(31, 71)) + list(range(200, 210))
        # Set random Front Hair

        # NOTE Below, certain strings from the "KKEx" Data Block of a card get deleted.
        # In case of one of my tested cards, some modded front and back hair.
        # Whenever I tried to just change the ID of the hair, it wouldn't work because
        # those two strings override whatever I set. By deleting them,
        # I can set the hair to whatever I want

        # Empty several KKEx attributes that can potentially fuck up a new character
        # NOTE if any new ones appear that concern hair, add them here
        try:
            del self.child["KKEx"]["com.deathweasel.bepinex.hairaccessorycustomizer"][1]
        except KeyError:
            pass

        # TODO Check if this is really needed here. Probably has nothing to do with hair
        # Was relevant for Card: YN
        try:
            del self.child["KKEx"]["org.njaecha.plugins.objimport"]
        except KeyError:
            pass

        # reverse loop through the info block of a card to delete all instances of custom hair
        try:
            counter = -1
            for _ in self.child["KKEx"]["com.bepis.sideloader.universalautoresolver"][1]["info"]:
                counter += 1

            while counter >= 0:
                if b'hair' in (self.child["KKEx"]["com.bepis.sideloader.universalautoresolver"]
                               [1]["info"][counter].lower()):

                    del (self.child["KKEx"]["com.bepis.sideloader.universalautoresolver"]
                         [1]["info"][counter])
                    counter -= 1

                else:
                    counter -= 1

        except KeyError:
            pass

        self.child["Custom"]["hair"]["parts"][1]["id"] = random.choice(front_hair_options)
        print("Front Hair ID: ", self.child["Custom"]["hair"]["parts"][1]["id"])

        # Vanilla Hairstyles for Side Hair
        # TODO add male hair selection
        side_hair_options = [0, 1, 2, 3, 5, 6, 7]
        # Set random Side Hair
        self.child["Custom"]["hair"]["parts"][2]["id"] = random.choice(side_hair_options)
        print("Side Hair ID: ", self.child["Custom"]["hair"]["parts"][2]["id"])

        # Vanilla Extensions (eg. Ahoge)
        # We give a 50/50 chance of extensions or else almost every character will get one
        # because of the amount of them ingame compared to just one option of having none
        do_ahoge = random.choice([True, False])
        if do_ahoge:
            extensions_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 200]
            # Set random Extension
            self.child["Custom"]["hair"]["parts"][3]["id"] = random.choice(extensions_options)
            print("Extensions ID: ", self.child["Custom"]["hair"]["parts"][3]["id"])
        else:
            self.child["Custom"]["hair"]["parts"][3]["id"] = 0
            print("No Extensions")

        # Vanilla Eyebrows
        # NOTE I have currently decided to inherit the eyebrows directly from the parents.
        #      Should I decide against that in the future, or should I add an option to
        #      randomise these, I will use the eyebrow options below again
        #eyebrow_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 200, 201]
        eyebrow_options = [self.father["Custom"]["face"]["eyebrowId"],
                           self.mother["Custom"]["face"]["eyebrowId"]]

        # Set random Eyebrows
        self.child["Custom"]["face"]["eyebrowId"] = random.choice(eyebrow_options)
        print("Eyebrows ID: ", self.child["Custom"]["face"]["eyebrowId"])

        # Getting hair colors of parents
        color_m = self.mother["Custom"]["hair"]["parts"][0]["baseColor"]
        color_f = self.father["Custom"]["hair"]["parts"][0]["baseColor"]
        color_options = [color_m, color_f]

        # Back Hair Color
        self.child["Custom"]["hair"]["parts"][0]["baseColor"] = random.choice(color_options)
        self.child["Custom"]["hair"]["parts"][0]["startColor"] = random.choice(color_options)
        self.child["Custom"]["hair"]["parts"][0]["endColor"] = random.choice(color_options)
        if self.child["Custom"]["hair"]["parts"][0]["baseColor"] == color_m:
            self.child["Custom"]["hair"]["parts"][0]["acsColor"][0] = color_f
        else:
            self.child["Custom"]["hair"]["parts"][0]["acsColor"][0] = color_m

        # Front Hair
        self.child["Custom"]["hair"]["parts"][1]["baseColor"] = (self.child["Custom"]["hair"]
                                                                 ["parts"][0]["baseColor"])

        # looks really fucking weird if back and front hair root don't match up
        self.child["Custom"]["hair"]["parts"][1]["startColor"] = (self.child["Custom"]["hair"]
                                                                  ["parts"][0]["startColor"])
        self.child["Custom"]["hair"]["parts"][1]["endColor"] = random.choice(color_options)
        if self.child["Custom"]["hair"]["parts"][1]["baseColor"] == color_m:
            self.child["Custom"]["hair"]["parts"][1]["acsColor"][0] = color_f
        else:
            self.child["Custom"]["hair"]["parts"][1]["acsColor"][0] = color_m

        # Side Hair
        self.child["Custom"]["hair"]["parts"][2]["baseColor"] = (self.child["Custom"]["hair"]
                                                                 ["parts"][0]["baseColor"])
        self.child["Custom"]["hair"]["parts"][2]["startColor"] = random.choice(color_options)
        self.child["Custom"]["hair"]["parts"][2]["endColor"] = random.choice(color_options)
        # TODO insert accessory color here

        # Extension Color
        self.child["Custom"]["hair"]["parts"][3]["baseColor"] = (self.child["Custom"]["hair"]
                                                                 ["parts"][0]["baseColor"])
        self.child["Custom"]["hair"]["parts"][3]["startColor"] = random.choice(color_options)
        self.child["Custom"]["hair"]["parts"][3]["endColor"] = random.choice(color_options)
        # TODO insert accessory color here

        # Eyebrow Color
        self.child["Custom"]["face"]["eyebrowColor"] = (self.child["Custom"]["hair"]
                                                        ["parts"][0]["baseColor"])


    # Parameter "gender": True == Female, False == Male
    def inherit_eyes(self, gender: bool) -> None:
        """ inherit eyes in a (somewhat) believable way """

        # Sclera will be inherited from either one of the parents
        # Parent's Scleras
        sclera_options = (self.father["Custom"]["face"]["whiteId"],
                          self.mother["Custom"]["face"]["whiteId"])
        # Inherit Sclera from parents
        self.child["Custom"]["face"]["whiteId"] = random.choice(sclera_options)
        if self.child["Custom"]["face"]["whiteId"] == self.mother["Custom"]["face"]["whiteId"]:
            print("Sclera Type: Mother")
        else:
            print("Sclera Type: Father")

        # Vanilla Pupil options
        pupil_options = list(range(0, 77)) + list(range(200, 217))
        # Set random pupils
        self.child["Custom"]["face"]["pupil"][0]["id"] = random.choice(pupil_options)

        # We want to use the same pupils for now.
        # Will maybe add an option for 2 different ones later
        self.child["Custom"]["face"]["pupil"][1]["id"] = (self.child["Custom"]["face"]
                                                          ["pupil"][0]["id"])
        print("Pupils Eye 1 ID: ", self.child["Custom"]["face"]["pupil"][0]["id"])
        print("Pupils Eye 2 ID: ", self.child["Custom"]["face"]["pupil"][1]["id"])

        # Pupil Color
        # Parents' eyecolors
        primary_eyecolors = (self.father["Custom"]["face"]["pupil"][0]["baseColor"],
                             self.mother["Custom"]["face"]["pupil"][0]["baseColor"])

        secondary_eyecolors = (self.father["Custom"]["face"]["pupil"][0]["subColor"],
                               self.mother["Custom"]["face"]["pupil"][0]["subColor"])

        # Set random mix of primary eyecolor and secondary eyecolor chosen from parents
        self.child["Custom"]["face"]["pupil"][0]["baseColor"] = random.choice(primary_eyecolors)

        # Again, we want to use the same color for both eyes
        self.child["Custom"]["face"]["pupil"][1]["baseColor"] = (self.child["Custom"]["face"]
                                                                 ["pupil"][0]["baseColor"])
        self.child["Custom"]["face"]["pupil"][0]["subColor"] = random.choice(secondary_eyecolors)

        # Again, we want to use the same color for both eyes
        self.child["Custom"]["face"]["pupil"][1]["subColor"] = (self.child["Custom"]["face"]
                                                                ["pupil"][0]["subColor"])

        if (self.child["Custom"]["face"]["pupil"][0]["baseColor"] ==
            self.father["Custom"]["face"]["pupil"][0]["baseColor"]):

            print("Pupil base color Father")

        elif (self.child["Custom"]["face"]["pupil"][0]["baseColor"] ==
              self.mother["Custom"]["face"]["pupil"][0]["baseColor"]):

            print("Pupil base color Mother")

        if (self.child["Custom"]["face"]["pupil"][0]["subColor"] ==
            self.father["Custom"]["face"]["pupil"][0]["subColor"]):

            print("Pupil sub color Father")

        elif (self.child["Custom"]["face"]["pupil"][0]["subColor"] ==
              self.mother["Custom"]["face"]["pupil"][0]["subColor"]):

            print("Pupil sub color Mother")

        # Eye Gradient
        # Selection of Vanilla eye gradients
        gradient_options = [0, 1, 2, 3]

        # Set random eye gradient
        self.child["Custom"]["face"]["pupil"][0]["gradMaskId"] = random.choice(gradient_options)

        # Set same eye gradient for both eyes
        self.child["Custom"]["face"]["pupil"][1]["gradMaskId"] = (self.child["Custom"]["face"]
                                                                  ["pupil"][0]["gradMaskId"])

        print("Gradient: ", self.child["Custom"]["face"]["pupil"][0]["gradMaskId"])

        # Set gradient strength, vertical position and size to default
        # values to not create weird ass looking eyes
        self.child["Custom"]["face"]["pupil"][0]["gradBlend"] = 0.46
        self.child["Custom"]["face"]["pupil"][1]["gradBlend"] = 0.46
        self.child["Custom"]["face"]["pupil"][0]["gradOffsetY"] = 0.48
        self.child["Custom"]["face"]["pupil"][1]["gradOffsetY"] = 0.48
        self.child["Custom"]["face"]["pupil"][0]["gradScale"] = 0.58
        self.child["Custom"]["face"]["pupil"][1]["gradScale"] = 0.58

        # Eye Highlights

        # Parent's upper highlights
        upper_hl_options = [self.mother["Custom"]["face"]["hlUpId"],
                            self.father["Custom"]["face"]["hlUpId"]]

        self.child["Custom"]["face"]["hlUpId"] = random.choice(upper_hl_options)

        if self.child["Custom"]["face"]["hlUpId"] == self.mother["Custom"]["face"]["hlUpId"]:
            self.child["Custom"]["face"]["hlDownId"] = self.mother["Custom"]["face"]["hlDownId"]
            print("Highlights: Mother")
        else:
            self.child["Custom"]["face"]["hlDownId"] = self.father["Custom"]["face"]["hlDownId"]
            print("Highlights: Father")

        # Upper and lower eyeliner will be taken from the respective parent of the same gender.
        # This is done to retain a certain degree of likeness to the parents, instead of
        # essentially just creating a random new character
        if gender:
            self.child["Custom"]["face"]["eyelineUpId"] = (self.mother["Custom"]["face"]
                                                           ["eyelineUpId"])
            self.child["Custom"]["face"]["eyelineDownId"] = (self.mother["Custom"]["face"]
                                                         ["eyelineDownId"])
        else:
            self.child["Custom"]["face"]["eyelineUpId"] = (self.father["Custom"]["face"]
                                                           ["eyelineUpId"])
            self.child["Custom"]["face"]["eyelineDownId"] = (self.father["Custom"]["face"]
                                                         ["eyelineDownId"])

        # Setting eyeliner color according to haircolor
        if (self.child["Custom"]["hair"]["parts"][0]["baseColor"] ==
            self.mother["Custom"]["hair"]["parts"][0]["baseColor"]):

            self.child["Custom"]["face"]["eyelineColor"] = (self.mother["Custom"]["face"]
                                                            ["eyelineColor"])
            print("Eyeliner Color: Mother")

        else:
            self.child["Custom"]["face"]["eyelineColor"] = (self.father["Custom"]["face"]
                                                            ["eyelineColor"])
            print("Eyeliner Color: Father")

        # Set Eyes and Eyebrows to not show through hair
        self.child["Custom"]["face"]["foregroundEyes"] = 1
        self.child["Custom"]["face"]["foregroundEyebrow"] = 1


    def create_child(self, gender: bool) -> None:
        """ create a new character with specified gender """

        if gender:
            print("Creating female character...")
            if hasattr(self.mother, "KKEx"):
                self.child["KKEx"] = copy.deepcopy(self.mother["KKEx"])
        else:
            print("Creating male character...")
            if hasattr(self.father, "KKEx"):
                self.child["KKEx"] = copy.deepcopy(self.father["KKEx"])

        self.inherit_face()
        self.inherit_hair(gender)
        self.inherit_body(gender)
        self.inherit_eyes(gender)
        self.save()
        print("Done!")


    def create_random_child(self) -> None:
        """ create character with random gender """

        gender = random.choice([True, False])

        if gender:
            print("Creating female character...")
            if hasattr(self.mother, "KKEx"):
                self.child["KKEx"] = copy.deepcopy(self.mother["KKEx"])
        else:
            print("Creating male character...")
            if hasattr(self.father, "KKEx"):
                self.child["KKEx"] = copy.deepcopy(self.father["KKEx"])

        self.inherit_face()
        self.inherit_hair(gender)
        self.inherit_body(gender)
        self.inherit_eyes(gender)
        self.save()
        print("Done!")


    def save(self) -> None:
        """ save created character as a new card """

        # calls the 'save()' method of KoikatuCharaData
        self.child.save(f"./{self.output_name}.png")

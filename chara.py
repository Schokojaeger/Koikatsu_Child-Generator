""" base class for character creation/manipulation. This is supposed to make accessing members of cards easier """

import copy
import random
from kkloader import KoikatuCharaData
import _globals as _g
from mother import Mother
from father import Father


class Child:

    def __init__(self, mother, father, output_name):
        if not isinstance(mother, str) and isinstance(father, str):
            raise TypeError("Both 'Mother' and 'Father' Files must be the filename of the corresponding .png file in String Format")

        if not isinstance(output_name, str):
            raise TypeError("Parameter 'output_name' should be a string with the name the file should be called after creation")

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
        if hasattr(self.mother, "KKEx"):
            self.child["KKEx"] = copy.deepcopy(self.mother["KKEx"])
        self.child["Custom"] = copy.deepcopy(self.mother["Custom"])
        self.child["Coordinate"] = copy.deepcopy(self.mother["Coordinate"])
        self.child["Parameter"] = copy.deepcopy(self.mother["Parameter"])
        self.child["Status"] = copy.deepcopy(self.mother["Status"])
        self.output_name = output_name


    # ---------------------------------------------------------------------------------------------
    def modify_value(self, base_value, percentage_change):
        """ change current value randomly within a certain range """
        min_value = base_value - (base_value * percentage_change)
        max_value = base_value + (base_value * percentage_change)
        new_value = random.uniform(min_value, max_value)

        return new_value

    # ---------------------------------------------------------------------------------------------
    def inherit_face(self):
        """ take faceslider values of parent characters, modify and save as child facesliders """

        # loop through facesliders and modify all values to a random degree (currently 50% up or down from base)
        for i in _g.list_faceslider:
            currm = _g.getv(self.mother, i)
            currf = _g.getv(self.father, i)
            if currm == self.mother["Custom"]["face"]["pupil"][0]["gradOffsetY"]:
                print("HERE IT IS")
            if currm == 0.0:
                continue
            middle_value = (currm + currf) / 2
            # changing the randomization of head size (can get pretty fucked)
            # we only use the mother's head size here to determine if the current item really is the head size
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][1]:
                newitem = self.modify_value(middle_value, 0.2)
                _g.setv(self.child, i, newitem)
            else:
                newitem = self.modify_value(middle_value, 0.5)
                # set resulting value as corresponding faceslider value of child
                _g.setv(self.child, i, newitem)

    # ---------------------------------------------------------------------------------------------
    def inherit_body(self):
        """ take bodyslider values of parent characters, modify and save as child bodysliders """

        # loop through bodysliders and modify all values to a random degree
        for i in _g.list_bodyslider:
            currm = _g.getv(self.mother, i)
            currf = _g.getv(self.father, i)
            if currm == 0.0:
                continue
            # changing the randomization of breast size
            # Using the mother's breast size since using a middle value of both parents would likely
            # always result in a small chest size (father will normally have a very small size)
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][4]:
                # using a modifier of 50% to not always get basically the same size as the mother
                newitem = self.modify_value(currm, 0.5)
                print("Boobs", newitem)
                _g.setv(self.child, i, newitem)
                continue
            # changing the randomization of butt angle (can get really fucked up)
            # Using the mother's butt size since the father should normally have a small butt
            if currm == self.mother["Custom"]["body"]["shapeValueBody"][27]:
                newitem = self.modify_value(currm, 0.15)
                _g.setv(self.child, i, newitem)
                continue

            middle_value = (currm + currf) / 2
            newitem = self.modify_value(middle_value, 0.3)
            # set resulting value as corresponding bodyslider value of child
            _g.setv(self.child, i, newitem)

    # ---------------------------------------------------------------------------------------------
    def inherit_hair(self):
        """ use either mother's or father's haircolor (or in combination) to determine the child's hair color.
            Will also choose random hair options from the vanilla selection """

        # Vanilla Hairstyles for Back Hair
        back_hair_options = list(range(0, 59)) + list(range(200, 210))                              # For some reason, the vanilla back hairstyles end at 58 and pick back up at 200?????
        # Set random Back Hair
        self.child["Custom"]["hair"]["parts"][0]["id"] = random.choice(back_hair_options)
        print("Back Hair ID: " , self.child["Custom"]["hair"]["parts"][0]["id"])

        # Vanilla Hairstyles for Front Hair
        front_hair_options = list(range(1, 21)) + list(range(31, 71)) + list(range(200, 210))       # And here, the vanilla hairstyles end at 20, pick back up at 70, stop again, and then start again at 200?????
        # Set random Front Hair
        self.child["Custom"]["hair"]["parts"][1]["id"] = random.choice(front_hair_options)
        print("Front Hair ID: ", self.child["Custom"]["hair"]["parts"][1]["id"])

        # Vanilla Hairstyles for Side Hair
        side_hair_options = [0, 1, 2, 3, 5, 6, 7]
        # Set random Side Hair
        self.child["Custom"]["hair"]["parts"][2]["id"] = random.choice(side_hair_options)
        print("Side Hair ID: ", self.child["Custom"]["hair"]["parts"][2]["id"])

        # Vanilla Extensions (eg. Ahoge)
        extensions_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 200]
        # Set random Extension
        self.child["Custom"]["hair"]["parts"][3]["id"] = random.choice(extensions_options)
        print("Extensions ID: ", self.child["Custom"]["hair"]["parts"][3]["id"])

        # Vanilla Eyebrows
        # NOTE I have currently decided to inherit the eyebrows directly from the parents. Should I decide against that in the future,
        #      or should I add an option to randomise these, I will use the eyebrow options below again
        #eyebrow_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 200, 201]
        eyebrow_options = [self.father["Custom"]["face"]["eyebrowId"], self.mother["Custom"]["face"]["eyebrowId"]]
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
        self.child["Custom"]["hair"]["parts"][1]["baseColor"] = self.child["Custom"]["hair"]["parts"][0]["baseColor"]
        self.child["Custom"]["hair"]["parts"][1]["startColor"] = self.child["Custom"]["hair"]["parts"][0]["startColor"]     # looks really fucking weird if back and front hair root don't match up
        self.child["Custom"]["hair"]["parts"][1]["endColor"] = random.choice(color_options)
        if self.child["Custom"]["hair"]["parts"][1]["baseColor"] == color_m:
            self.child["Custom"]["hair"]["parts"][1]["acsColor"][0] = color_f
        else:
            self.child["Custom"]["hair"]["parts"][1]["acsColor"][0] = color_m

        # Side Hair
        self.child["Custom"]["hair"]["parts"][2]["baseColor"] = self.child["Custom"]["hair"]["parts"][0]["baseColor"]
        self.child["Custom"]["hair"]["parts"][2]["startColor"] = random.choice(color_options)
        self.child["Custom"]["hair"]["parts"][2]["endColor"] = random.choice(color_options)
        #insert accessory color here

        # Extension Color
        self.child["Custom"]["hair"]["parts"][3]["baseColor"] = self.child["Custom"]["hair"]["parts"][0]["baseColor"]
        self.child["Custom"]["hair"]["parts"][3]["startColor"] = random.choice(color_options)
        self.child["Custom"]["hair"]["parts"][3]["endColor"] = random.choice(color_options)
        #insert accessory color here

        # Eyebrow Color
        self.child["Custom"]["face"]["eyebrowColor"] = self.child["Custom"]["hair"]["parts"][0]["baseColor"]

    # ---------------------------------------------------------------------------------------------
    def inherit_eyes(self):
        """ inherit eyes in a (somewhat) believable way """

        # Sclera will be inherited from either one of the parents
        # Parent's Scleras
        sclera_options = (self.father["Custom"]["face"]["whiteId"], self.mother["Custom"]["face"]["whiteId"])
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
        self.child["Custom"]["face"]["pupil"][1]["id"] = self.child["Custom"]["face"]["pupil"][0]["id"]         # We want to use the same pupils for now. Will maybe add an option for 2 different ones later
        print("Pupils Eye 1 ID: ", self.child["Custom"]["face"]["pupil"][0]["id"])
        print("Pupils Eye 2 ID: ", self.child["Custom"]["face"]["pupil"][1]["id"])

        # Pupil Color
        # Parents' eyecolors
        primary_eyecolors = (self.father["Custom"]["face"]["pupil"][0]["baseColor"], self.mother["Custom"]["face"]["pupil"][0]["baseColor"])
        secondary_eyecolors = (self.father["Custom"]["face"]["pupil"][0]["subColor"], self.mother["Custom"]["face"]["pupil"][0]["subColor"])

        # Set random mix of primary eyecolor and secondary eyecolor chosen from parents
        self.child["Custom"]["face"]["pupil"][0]["baseColor"] = random.choice(primary_eyecolors)
        self.child["Custom"]["face"]["pupil"][1]["baseColor"] = self.child["Custom"]["face"]["pupil"][0]["baseColor"]           # Again, we want to use the same color for both eyes
        self.child["Custom"]["face"]["pupil"][0]["subColor"] = random.choice(secondary_eyecolors)
        self.child["Custom"]["face"]["pupil"][1]["subColor"] = self.child["Custom"]["face"]["pupil"][0]["subColor"]             # Again, we want to use the same color for both eyes

        if self.child["Custom"]["face"]["pupil"][0]["baseColor"] == self.father["Custom"]["face"]["pupil"][0]["baseColor"]:
            print("Base Color Father")
        elif self.child["Custom"]["face"]["pupil"][0]["baseColor"] == self.mother["Custom"]["face"]["pupil"][0]["baseColor"]:
            print("Base Color Mother")
        
        if self.child["Custom"]["face"]["pupil"][0]["subColor"] == self.father["Custom"]["face"]["pupil"][0]["subColor"]:
            print("Sub Color Father")
        elif self.child["Custom"]["face"]["pupil"][0]["subColor"] == self.mother["Custom"]["face"]["pupil"][0]["subColor"]:
            print("Sub Color Mother")
        
        # Eye Gradient
        # Selection of Vanilla eye gradients
        gradient_options = [0, 1, 2, 3]

        # Set random eye gradient
        self.child["Custom"]["face"]["pupil"][0]["gradMaskId"] = random.choice(gradient_options)
        self.child["Custom"]["face"]["pupil"][1]["gradMaskId"] = self.child["Custom"]["face"]["pupil"][0]["gradMaskId"]         # Set same eye gradient for both eyes

        print("Gradient: ", self.child["Custom"]["face"]["pupil"][0]["gradMaskId"])

        # Set gradient strength, vertical position and size to default values to not create weird ass looking eyes
        self.child["Custom"]["face"]["pupil"][0]["gradBlend"] = 0.46
        self.child["Custom"]["face"]["pupil"][1]["gradBlend"] = 0.46
        self.child["Custom"]["face"]["pupil"][0]["gradOffsetY"] = 0.48
        self.child["Custom"]["face"]["pupil"][1]["gradOffsetY"] = 0.48
        self.child["Custom"]["face"]["pupil"][0]["gradScale"] = 0.58
        self.child["Custom"]["face"]["pupil"][1]["gradScale"] = 0.58

        # Eye Highlights

        # Parent's upper highlights
        upper_hl_options = [self.mother["Custom"]["face"]["hlUpId"], self.father["Custom"]["face"]["hlUpId"]]

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
        self.child["Custom"]["face"]["eyelineUpId"] = self.mother["Custom"]["face"]["eyelineUpId"]  # currently strictly taking the eyeliner from the mother since there are no male children yet
        self.child["Custom"]["face"]["eyelineDownId"] = self.mother["Custom"]["face"]["eyelineDownId"]
        # TODO add logic for eyeliners for male and female characters here when
        # implementing male children.

        # Setting eyeliner color according to haircolor
        # NOTE currently using the eyeliner color of the parent, whose base haircolor has been inherited
        # Will test this and then make a final decision
        if self.child["Custom"]["hair"]["parts"][0]["baseColor"] == self.mother["Custom"]["hair"]["parts"][0]["baseColor"]:
            self.child["Custom"]["face"]["eyelineColor"] = self.mother["Custom"]["face"]["eyelineColor"]
            print("Eyeliner Color: Mother")
        else:
            self.child["Custom"]["face"]["eyelineColor"] = self.father["Custom"]["face"]["eyelineColor"]
            print("Eyeliner Color: Father")

    # ---------------------------------------------------------------------------------------------
    def save(self):
        """ call .save() method of KoikatuCharaData with desired output name """

        self.child.save(f"./{self.output_name}.png")

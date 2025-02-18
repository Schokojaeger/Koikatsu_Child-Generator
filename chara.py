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
            if currm == 0.0:
                continue
            middle_value = (currm + currf) / 2
            # changing the randomization of head size
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
        back_hair_options = list(range(0, 21)) + list(range(31, 71)) + list(range(200, 210))
        # Set random Back Hair
        self.child["Custom"]["hair"]["parts"][0]["id"] = random.choice(back_hair_options)
        print("Back Hair ID: " , self.child["Custom"]["hair"]["parts"][0]["id"])

        # Vanilla Hairstyles for Front Hair
        front_hair_options = list(range(1, 21)) + list(range(31, 71)) + list(range(200, 210))       # For some reason, the vanilla hairstyles end at 20, pick back up at 70, stop again, and then start again at 200?????
        # Set random Front Hair
        self.child["Custom"]["hair"]["parts"][1]["id"] = random.choice(front_hair_options)
        print("Front Hair ID: ", self.child["Custom"]["hair"]["parts"][1]["id"])

        # Vanilla Hairstyles for Side Hair
        side_hair_options = [0, 1, 2, 3, 4, 6, 7]
        # Set random Side Hair
        self.child["Custom"]["hair"]["parts"][2]["id"] = random.choice(side_hair_options)
        print("Side Hair ID: ", self.child["Custom"]["hair"]["parts"][2]["id"])

        # Vanilla Extensions (eg. Ahoge)
        extensions_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 200]
        # Set random Extension
        self.child["Custom"]["hair"]["parts"][3]["id"] = random.choice(extensions_options)
        print("Extensions: ", self.child["Custom"]["hair"]["parts"][3]["id"])

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

    # ---------------------------------------------------------------------------------------------
    def save(self):
        """ call .save() method of KoikatuCharaData with desired output name """
        self.child.save(f"./{self.output_name}.png")

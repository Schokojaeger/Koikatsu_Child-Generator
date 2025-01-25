""" class for mother character and its values """

from kkloader import KoikatuCharaData

class Mother():
    def __init__(self, mother):
        if isinstance(mother, str):
            self.mother = KoikatuCharaData.load(mother)
        else:
            raise TypeError("passed mother file is not of type String (should just be filename)")

        self.face_width = self.mother["Custom"]["face"]["shapeValueFace"][0]
        self.upper_face_depth = self.mother["Custom"]["face"]["shapeValueFace"][1]
        self.upper_face_height = self.mother["Custom"]["face"]["shapeValueFace"][2]
        self.upper_face_size = self.mother["Custom"]["face"]["shapeValueFace"][3]
        self.lower_face_depth = self.mother["Custom"]["face"]["shapeValueFace"][4]
        self.lower_face_width = self.mother["Custom"]["face"]["shapeValueFace"][5]
        self.lower_jaw_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][6]
        self.lower_jaw_depth = self.mother["Custom"]["face"]["shapeValueFace"][7]
        self.jaw_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][8]
        self.jaw_width = self.mother["Custom"]["face"]["shapeValueFace"][9]
        self.jaw_depth = self.mother["Custom"]["face"]["shapeValueFace"][10]
        self.chin_tip = self.mother["Custom"]["face"]["shapeValueFace"][11]
        self.chin_depth = self.mother["Custom"]["face"]["shapeValueFace"][12]
        self.chin_width = self.mother["Custom"]["face"]["shapeValueFace"][13]
        self.cheekbone_width = self.mother["Custom"]["face"]["shapeValueFace"][14]
        self.cheekbone_depth = self.mother["Custom"]["face"]["shapeValueFace"][15]
        self.cheek_width = self.mother["Custom"]["face"]["shapeValueFace"][16]
        self.cheek_depth = self.mother["Custom"]["face"]["shapeValueFace"][17]
        self.cheek_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][18]
        self.eyebrow_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][19]
        self.eyebrow_spacing = self.mother["Custom"]["face"]["shapeValueFace"][20]
        self.eyebrow_angle = self.mother["Custom"]["face"]["shapeValueFace"][21]
        self.inner_eyebrow_shape = self.mother["Custom"]["face"]["shapeValueFace"][22]
        self.outer_eyebrow_shape = self.mother["Custom"]["face"]["shapeValueFace"][23]
        self.upper_eyelid_shape1 = self.mother["Custom"]["face"]["shapeValueFace"][24]
        self.upper_eyelid_shape2 = self.mother["Custom"]["face"]["shapeValueFace"][25]
        self.upper_eyelid_shape3 = self.mother["Custom"]["face"]["shapeValueFace"][26]
        self.lower_eyelid_shape1 = self.mother["Custom"]["face"]["shapeValueFace"][27]
        self.lower_eyelid_shape2 = self.mother["Custom"]["face"]["shapeValueFace"][28]
        self.lower_eyelid_shape3 = self.mother["Custom"]["face"]["shapeValueFace"][29]
        self.eye_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][30]
        self.eye_spacing = self.mother["Custom"]["face"]["shapeValueFace"][31]
        self.eye_depth = self.mother["Custom"]["face"]["shapeValueFace"][32]
        self.eye_rotation = self.mother["Custom"]["face"]["shapeValueFace"][33]
        self.eye_height = self.mother["Custom"]["face"]["shapeValueFace"][34]
        self.eye_width = self.mother["Custom"]["face"]["shapeValueFace"][35]
        self.inner_eye_corner_height = self.mother["Custom"]["face"]["shapeValueFace"][36]
        self.outer_eye_corner_height = self.mother["Custom"]["face"]["shapeValueFace"][37]
        self.nose_tip_height = self.mother["Custom"]["face"]["shapeValueFace"][38]
        self.nose_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][39]
        self.nose_ridge_height = self.mother["Custom"]["face"]["shapeValueFace"][40]
        self.mouth_vertical_position = self.mother["Custom"]["face"]["shapeValueFace"][41]
        self.mouth_width = self.mother["Custom"]["face"]["shapeValueFace"][42]
        self.mouth_depth = self.mother["Custom"]["face"]["shapeValueFace"][43]
        self.upper_lip_depth = self.mother["Custom"]["face"]["shapeValueFace"][44]
        self.lower_lip_depth = self.mother["Custom"]["face"]["shapeValueFace"][45]
        self.mouth_corner_shape = self.mother["Custom"]["face"]["shapeValueFace"][46]
        self.ear_size = self.mother["Custom"]["face"]["shapeValueFace"][47]
        self.ear_angle_y = self.mother["Custom"]["face"]["shapeValueFace"][48]
        self.ear_angle_z = self.mother["Custom"]["face"]["shapeValueFace"][49]
        self.upper_ear_shape = self.mother["Custom"]["face"]["shapeValueFace"][50]
        self.lower_ear_shape = self.mother["Custom"]["face"]["shapeValueFace"][51]

        self.list_faceslider = [self.face_width, self.upper_face_depth, self.upper_face_height, self.upper_face_size, self.lower_face_depth, 
                                self.lower_face_width, self.lower_jaw_vertical_position, self.lower_jaw_depth, self.jaw_vertical_position, 
                                self.jaw_width, self.jaw_depth, self.chin_tip, self.chin_depth, self.chin_width, self.cheekbone_width, 
                                self.cheekbone_depth, self.cheek_width, self.cheek_depth, self.cheek_vertical_position, self.eyebrow_vertical_position, 
                                self.eyebrow_spacing, self.eyebrow_angle, self.inner_eyebrow_shape, self.outer_eyebrow_shape, self.upper_eyelid_shape1, 
                                self.upper_eyelid_shape2, self.upper_eyelid_shape3, self.lower_eyelid_shape1, self.lower_eyelid_shape2, 
                                self.lower_eyelid_shape3, self.eye_vertical_position, self.eye_spacing, self.eye_depth, self.eye_rotation, 
                                self.eye_height, self.eye_width, self.inner_eye_corner_height, self.outer_eye_corner_height, 
                                self.nose_tip_height, self.nose_vertical_position, self.nose_ridge_height, self.mouth_vertical_position, 
                                self.mouth_width, self.mouth_depth, self.upper_lip_depth, self.lower_lip_depth, self.mouth_corner_shape, 
                                self.ear_size, self.ear_angle_y, self.ear_angle_z, self.upper_ear_shape, self.lower_ear_shape]

    def save(self, name):
        # Beim Aufrufen dieser Methode wurden zuvor nie die eigentlichen Werte der Originalkarte verändert, weil sie oben nur einer neuen Variable zugewiesen werden
        self.mother.save(f"./{name}.png")
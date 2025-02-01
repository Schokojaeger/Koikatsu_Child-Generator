""" class for mother character and its values """

from kkloader import KoikatuCharaData

class Mother():
    def __init__(self, mother):
        if isinstance(mother, str):
            self.mother = KoikatuCharaData.load(mother)
        else:
            raise TypeError("passed mother file is not of type String (should just be filename)")

        # Facesliders ------------------------------------------------------------------------------------
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
        self.head_size = self.mother["Custom"]["body"]["shapeValueBody"][1]

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
                                self.ear_size, self.ear_angle_y, self.ear_angle_z, self.upper_ear_shape, self.lower_ear_shape, self.head_size]
        
        # Bodysliders ------------------------------------------------------------------------------------
        self.body_height = self.mother["Custom"]["body"]["shapeValueBody"][0]
        self.neck_width = self.mother["Custom"]["body"]["shapeValueBody"][2]
        self.neck_thickness = self.mother["Custom"]["body"]["shapeValueBody"][3]
        self.breast_size = self.mother["Custom"]["body"]["shapeValueBody"][4]
        self.breast_vertical_position = self.mother["Custom"]["body"]["shapeValueBody"][5]
        self.breast_spacing = self.mother["Custom"]["body"]["shapeValueBody"][6]
        self.breast_horizontal_position = self.mother["Custom"]["body"]["shapeValueBody"][7]
        self.breast_vertical_angle = self.mother["Custom"]["body"]["shapeValueBody"][8]
        self.breast_depth = self.mother["Custom"]["body"]["shapeValueBody"][9]
        self.breast_roundness = self.mother["Custom"]["body"]["shapeValueBody"][10]
        self.areola_depth = self.mother["Custom"]["body"]["shapeValueBody"][11]
        self.nipple_thickness = self.mother["Custom"]["body"]["shapeValueBody"][12]
        self.nipple_depth = self.mother["Custom"]["body"]["shapeValueBody"][13]
        self.upper_body_shoulder_width = self.mother["Custom"]["body"]["shapeValueBody"][14]
        self.upper_body_shoulder_thickness = self.mother["Custom"]["body"]["shapeValueBody"][15]
        self.upper_torso_width = self.mother["Custom"]["body"]["shapeValueBody"][16]
        self.upper_torso_thickness = self.mother["Custom"]["body"]["shapeValueBody"][17]
        self.lower_torso_width = self.mother["Custom"]["body"]["shapeValueBody"][18]
        self.lower_torso_thickness = self.mother["Custom"]["body"]["shapeValueBody"][19]
        self.waist_position = self.mother["Custom"]["body"]["shapeValueBody"][20]
        self.belly_thickness = self.mother["Custom"]["body"]["shapeValueBody"][21]
        self.waist_width = self.mother["Custom"]["body"]["shapeValueBody"][22]
        self.waist_thickness = self.mother["Custom"]["body"]["shapeValueBody"][23]
        self.hip_width = self.mother["Custom"]["body"]["shapeValueBody"][24]
        self.hip_width_2 = self.mother["Custom"]["body"]["shapeValueBody"][25]
        self.butt_size = self.mother["Custom"]["body"]["shapeValueBody"][26]
        self.butt_angle = self.mother["Custom"]["body"]["shapeValueBody"][27]
        self.upper_thigh_width = self.mother["Custom"]["body"]["shapeValueBody"][28]
        self.upper_thigh_thickness = self.mother["Custom"]["body"]["shapeValueBody"][29]
        self.lower_thigh_width = self.mother["Custom"]["body"]["shapeValueBody"][30]
        self.lower_thigh_thickness = self.mother["Custom"]["body"]["shapeValueBody"][31]
        self.knee_width = self.mother["Custom"]["body"]["shapeValueBody"][32]
        self.knee_thickness = self.mother["Custom"]["body"]["shapeValueBody"][33]
        self.calves = self.mother["Custom"]["body"]["shapeValueBody"][34]
        self.ankle_width = self.mother["Custom"]["body"]["shapeValueBody"][35]
        self.ankle_thickness = self.mother["Custom"]["body"]["shapeValueBody"][36]
        self.arms_shoulder_width = self.mother["Custom"]["body"]["shapeValueBody"][37]
        self.arms_shoulder_thickness = self.mother["Custom"]["body"]["shapeValueBody"][38]
        self.upper_arm_width = self.mother["Custom"]["body"]["shapeValueBody"][39]
        self.upper_arm_thickness = self.mother["Custom"]["body"]["shapeValueBody"][40]
        self.elbow_width = self.mother["Custom"]["body"]["shapeValueBody"][41]
        self.elbow_thickness = self.mother["Custom"]["body"]["shapeValueBody"][42]
        self.forearm_thickness = self.mother["Custom"]["body"]["shapeValueBody"][40]
        self.breast_softness = self.mother["Custom"]["body"]["bustSoftness"]
        self.breast_weight = self.mother["Custom"]["body"]["bustWeight"]

        self.list_bodyslider = [self.body_height, self.neck_width, self.neck_thickness, self.breast_size, self.breast_vertical_position, self.breast_spacing, self.breast_horizontal_position, self.breast_vertical_angle, 
                               self.breast_depth, self.breast_roundness, self.areola_depth, self.nipple_thickness, self.nipple_depth, self.upper_body_shoulder_width, self.upper_body_shoulder_thickness, self.upper_torso_width, 
                               self.upper_torso_thickness, self.lower_torso_width, self.lower_torso_thickness, self.waist_position, self.belly_thickness, self.waist_width, self.waist_thickness, self.hip_width, self.hip_width_2, 
                               self.butt_size, self.butt_angle, self.upper_thigh_width, self.upper_thigh_thickness, self.lower_thigh_width, self.lower_thigh_thickness, self.knee_width, self.knee_thickness, self.calves, self.ankle_width, 
                               self.ankle_thickness, self.arms_shoulder_width, self.arms_shoulder_thickness, self.upper_arm_width, self.upper_arm_thickness, self.elbow_width, self.elbow_thickness, self.forearm_thickness, 
                               self.breast_softness, self.breast_weight]

    def save(self, name):
        """ call .save method of KoikatuCharaData with chosen output name """
        self.mother.save(f"./{name}.png")

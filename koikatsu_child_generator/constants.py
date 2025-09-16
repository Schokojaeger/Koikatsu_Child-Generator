""" global constants to be used by chara classes """
from functools import reduce

# Facesliders
face_width = ["Custom", "face", "shapeValueFace", 0]
upper_face_depth = ["Custom", "face", "shapeValueFace", 1]
upper_face_height = ["Custom", "face", "shapeValueFace", 2]
upper_face_size = ["Custom", "face", "shapeValueFace", 3]
lower_face_depth = ["Custom", "face", "shapeValueFace", 4]
lower_face_width = ["Custom", "face", "shapeValueFace", 5]
lower_jaw_vertical_position = ["Custom", "face", "shapeValueFace", 6]
lower_jaw_depth = ["Custom", "face", "shapeValueFace", 7]
jaw_vertical_position = ["Custom", "face", "shapeValueFace", 8]
jaw_width = ["Custom", "face", "shapeValueFace", 9]
jaw_depth = ["Custom", "face", "shapeValueFace", 10]
chin_tip = ["Custom", "face", "shapeValueFace", 11]
chin_depth = ["Custom", "face", "shapeValueFace", 12]
chin_width = ["Custom", "face", "shapeValueFace", 13]
cheekbone_width = ["Custom", "face", "shapeValueFace", 14]
cheekbone_depth = ["Custom", "face", "shapeValueFace", 15]
cheek_width = ["Custom", "face", "shapeValueFace", 16]
cheek_depth = ["Custom", "face", "shapeValueFace", 17]
cheek_vertical_position = ["Custom", "face", "shapeValueFace", 18]
eyebrow_vertical_position = ["Custom", "face", "shapeValueFace", 19]
eyebrow_spacing = ["Custom", "face", "shapeValueFace", 20]
eyebrow_angle = ["Custom", "face", "shapeValueFace", 21]
inner_eyebrow_shape = ["Custom", "face", "shapeValueFace", 22]
outer_eyebrow_shape = ["Custom", "face", "shapeValueFace", 23]
upper_eyelid_shape1 = ["Custom", "face", "shapeValueFace", 24]
upper_eyelid_shape2 = ["Custom", "face", "shapeValueFace", 25]
upper_eyelid_shape3 = ["Custom", "face", "shapeValueFace", 26]
lower_eyelid_shape1 = ["Custom", "face", "shapeValueFace", 27]
lower_eyelid_shape2 = ["Custom", "face", "shapeValueFace", 28]
lower_eyelid_shape3 = ["Custom", "face", "shapeValueFace", 29]
eye_vertical_position = ["Custom", "face", "shapeValueFace", 30]
eye_spacing = ["Custom", "face", "shapeValueFace", 31]
eye_depth = ["Custom", "face", "shapeValueFace", 32]
eye_rotation = ["Custom", "face", "shapeValueFace", 33]
eye_height = ["Custom", "face", "shapeValueFace", 34]
eye_width = ["Custom", "face", "shapeValueFace", 35]
inner_eye_corner_height = ["Custom", "face", "shapeValueFace", 36]
outer_eye_corner_height = ["Custom", "face", "shapeValueFace", 37]
nose_tip_height = ["Custom", "face", "shapeValueFace", 38]
nose_vertical_position = ["Custom", "face", "shapeValueFace", 39]
nose_ridge_height = ["Custom", "face", "shapeValueFace", 40]
mouth_vertical_position = ["Custom", "face", "shapeValueFace", 41]
mouth_width = ["Custom", "face", "shapeValueFace", 42]
mouth_depth = ["Custom", "face", "shapeValueFace", 43]
upper_lip_depth = ["Custom", "face", "shapeValueFace", 44]
lower_lip_depth = ["Custom", "face", "shapeValueFace", 45]
mouth_corner_shape = ["Custom", "face", "shapeValueFace", 46]
ear_size = ["Custom", "face", "shapeValueFace", 47]
ear_angle_y = ["Custom", "face", "shapeValueFace", 48]
ear_angle_z = ["Custom", "face", "shapeValueFace", 49]
upper_ear_shape = ["Custom", "face", "shapeValueFace", 50]
lower_ear_shape = ["Custom", "face", "shapeValueFace", 51]
head_size = ["Custom", "body", "shapeValueBody", 1]     # head size would normally be in bodysliders
                                                        # but I think it makes more sense to also
                                                        # change the head size when creating or
                                                        # altering a face


list_faceslider = [face_width, upper_face_depth, upper_face_height, upper_face_size, lower_face_depth, lower_face_width, lower_jaw_vertical_position, lower_jaw_depth,
                   jaw_vertical_position, jaw_width, jaw_depth, chin_tip, chin_depth, chin_width, cheekbone_width, cheekbone_depth, cheek_width, cheek_depth, cheek_vertical_position,
                   eyebrow_vertical_position, eyebrow_spacing, eyebrow_angle, inner_eyebrow_shape, outer_eyebrow_shape, upper_eyelid_shape1, upper_eyelid_shape2,
                   upper_eyelid_shape3, lower_eyelid_shape1, lower_eyelid_shape2, lower_eyelid_shape3, eye_vertical_position, eye_spacing, eye_depth, eye_rotation, eye_height,
                   eye_width, inner_eye_corner_height, outer_eye_corner_height, nose_tip_height, nose_vertical_position, nose_ridge_height, mouth_vertical_position, mouth_width,
                   mouth_depth, upper_lip_depth, lower_lip_depth, mouth_corner_shape, ear_size, ear_angle_y, ear_angle_z, upper_ear_shape, lower_ear_shape, head_size]

# Bodysliders
body_height = ["Custom", "body", "shapeValueBody", 0]
neck_width = ["Custom", "body", "shapeValueBody", 2]
neck_thickness = ["Custom", "body", "shapeValueBody", 3]
breast_size = ["Custom", "body", "shapeValueBody", 4]
breast_vertical_position = ["Custom", "body", "shapeValueBody", 5]
breast_spacing = ["Custom", "body", "shapeValueBody", 6]
breast_horizontal_position = ["Custom", "body", "shapeValueBody", 7]
breast_vertical_angle = ["Custom", "body", "shapeValueBody", 8]
breast_depth = ["Custom", "body", "shapeValueBody", 9]
breast_roundness = ["Custom", "body", "shapeValueBody", 10]
areola_depth = ["Custom", "body", "shapeValueBody", 11]
nipple_thickness = ["Custom", "body", "shapeValueBody", 12]
nipple_depth = ["Custom", "body", "shapeValueBody", 13]
upper_body_shoulder_width = ["Custom", "body", "shapeValueBody", 14]
upper_body_shoulder_thickness = ["Custom", "body", "shapeValueBody", 15]
upper_torso_width = ["Custom", "body", "shapeValueBody", 16]
upper_torso_thickness = ["Custom", "body", "shapeValueBody", 17]
lower_torso_width = ["Custom", "body", "shapeValueBody", 18]
lower_torso_thickness = ["Custom", "body", "shapeValueBody", 19]
waist_position = ["Custom", "body", "shapeValueBody", 20]
belly_thickness = ["Custom", "body", "shapeValueBody", 21]
waist_width = ["Custom", "body", "shapeValueBody", 22]
waist_thickness = ["Custom", "body", "shapeValueBody", 23]
hip_width = ["Custom", "body", "shapeValueBody", 24]
hip_width_2 = ["Custom", "body", "shapeValueBody", 25]
butt_size = ["Custom", "body", "shapeValueBody", 26]
butt_angle = ["Custom", "body", "shapeValueBody", 27]
upper_thigh_width = ["Custom", "body", "shapeValueBody", 28]
upper_thigh_thickness = ["Custom", "body", "shapeValueBody", 29]
lower_thigh_width = ["Custom", "body", "shapeValueBody", 30]
lower_thigh_thickness = ["Custom", "body", "shapeValueBody", 31]
knee_width = ["Custom", "body", "shapeValueBody", 32]
knee_thickness = ["Custom", "body", "shapeValueBody", 33]
calves = ["Custom", "body", "shapeValueBody", 34]
ankle_width = ["Custom", "body", "shapeValueBody", 35]
ankle_thickness = ["Custom", "body", "shapeValueBody", 36]
arms_shoulder_width = ["Custom", "body", "shapeValueBody", 37]
arms_shoulder_thickness = ["Custom", "body", "shapeValueBody", 38]
upper_arm_width = ["Custom", "body", "shapeValueBody", 39]
upper_arm_thickness = ["Custom", "body", "shapeValueBody", 40]
elbow_width = ["Custom", "body", "shapeValueBody", 41]
elbow_thickness = ["Custom", "body", "shapeValueBody", 42]
forearm_thickness = ["Custom", "body", "shapeValueBody", 43]
breast_softness = ["Custom", "body", "bustSoftness"]
breast_weight = ["Custom", "body", "bustWeight"]


list_bodyslider = [body_height, neck_width, neck_thickness, breast_size, breast_vertical_position, breast_spacing, breast_horizontal_position, breast_vertical_angle, 
                   breast_depth, breast_roundness, areola_depth, nipple_thickness, nipple_depth, upper_body_shoulder_width, upper_body_shoulder_thickness, upper_torso_width, 
                   upper_torso_thickness, lower_torso_width, lower_torso_thickness, waist_position, belly_thickness, waist_width, waist_thickness, hip_width, hip_width_2, 
                   butt_size, butt_angle, upper_thigh_width, upper_thigh_thickness, lower_thigh_width, lower_thigh_thickness, knee_width, knee_thickness, calves, ankle_width, 
                   ankle_thickness, arms_shoulder_width, arms_shoulder_thickness, upper_arm_width, upper_arm_thickness, elbow_width, elbow_thickness, forearm_thickness, 
                   breast_softness, breast_weight]


def getv(c, path):
    """ get value """
    return reduce(lambda c, key: c[key] if isinstance(c, dict) else c[key], path, c)


def setv(c, path, value):
    """ set value """
    target = reduce(lambda c, key: c[key] if isinstance(c, dict) else c[key], path[:-1], c)
    target[path[-1]] = value

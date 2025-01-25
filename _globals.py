""" global constants to be used by chara classes """
from functools import reduce

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

list_faceslider = [face_width, upper_face_depth, upper_face_height, upper_face_size, lower_face_depth, lower_face_width, lower_jaw_vertical_position, lower_jaw_depth,
                   jaw_vertical_position, jaw_width, jaw_depth, chin_tip, chin_depth, chin_width, cheekbone_width, cheekbone_depth, cheek_width, cheek_depth, cheek_vertical_position,
                   eyebrow_vertical_position, eyebrow_spacing, eyebrow_angle, inner_eyebrow_shape, outer_eyebrow_shape, upper_eyelid_shape1, upper_eyelid_shape2,
                   upper_eyelid_shape3, lower_eyelid_shape1, lower_eyelid_shape2, lower_eyelid_shape3, eye_vertical_position, eye_spacing, eye_depth, eye_rotation, eye_height,
                   eye_width, inner_eye_corner_height, outer_eye_corner_height, nose_tip_height, nose_vertical_position, nose_ridge_height, mouth_vertical_position, mouth_width,
                   mouth_depth, upper_lip_depth, lower_lip_depth, mouth_corner_shape, ear_size, ear_angle_y, ear_angle_z, upper_ear_shape, lower_ear_shape]

def getv(c, path):
    return reduce(lambda c, key: c[key] if isinstance(c, dict) else c[key], path, c)

def setv(c, path, value):
    target = reduce(lambda c, key: c[key] if isinstance(c, dict) else c[key], path[:-1], c)
    target[path[-1]] = value

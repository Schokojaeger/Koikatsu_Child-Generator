""" test class for creating new characters """

from koikatsu_child_generator.chara import Child


child = Child(mother="", father="", output_name="new_child")
child.create_child(True)
#child.create_child(False)
#child.create_random_child()

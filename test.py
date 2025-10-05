""" test class for creating new characters """

from koikatsu_child_generator.chara import Child


child = Child(mother="", father="", output_name="new_child")

child.create(True)
#child.create_random()

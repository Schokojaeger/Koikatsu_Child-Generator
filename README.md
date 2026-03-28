# Koikatsu Child Generator
This is a tool for generating a child character from two pre-existing parent characters.

This tool will use the physical feature values of both parents and a bit of variance, to create a unique look for a new child character.
This process may result in some wacky creations, mostly when parent characters are using extremes for their sliders or have vastly different artstyles.

- Modded parent characters are supported, but depending on which mods they use, the result may not be as expected!

# Usage

## Running from CLI

The general syntax for the generator is:

```bash
python child_generator.py [command] [options]
```

### Commands

#### create: 
- Create a new character from two parent characters

Syntax:
```bash
python child_generator.py create <mother> <father> [-g | --gender <female | male>] [-fn | --filename <filename>] [-v | --verbose]
```

Arguments:

**\<mother>**: path to the female parent character\
**\<father>**: path to the male parent character

Options:

**[--gender, -g <female | male>]**: specify gender of new character (choose from 'female' or 'male'). Will choose a random gender, if omitted.\
**[--filename, -fn \<filename>]**: specify filename of new character (don't include file extension)\
**[--verbose, -v]**: print information about some attributes of the new character
#
Example:
```bash
python child_generator.py create ./mother.png ./father.png --gender female --filename new_child --verbose
```

It will spit out a new character with a placeholder image, called *"new_child.png"*.

<br>

# Acknowledgements
- [great-majority/KoikatuCharaLoader](https://github.com/great-majority/KoikatuCharaLoader)
# opsdroid skill skill-thefappening

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) created with cookiecutter.

## skill-thefappening
opsdroid> fappening [celebname] will generate URLS for nude celebrity pictures

## Setting Up
Our __init__.py init file will contain one function, a function that opsdroid will use to generate a bunch of URLS for the specified celebrity.

## Building the Skill
We are ready to start working on our skills. First, you need to create a folder for the fappening skill. Choose a location and name it skill-fappening.

mkdir /path/to/my/skill-fappening


## Requirements

None.

## Configuration

Now, let's open opsdroid configuration.yaml file and add our fappening skill to the skills section.

skills:
  ## Fappening ##
  skill-fappening:
    name: skill-fappening
    path: /path/to/my/skill-fappening
    no-cache: true
    
Note: We will need to set no-cache to true, in order to tell opsdroid to install the skill on every opsdroid run.

Fappening Skill
	Now that our skill has all the configuration details set up in the configuration.yaml file, let's create the __init__.py inside our skill-fappening folder and start working on the skill.
	
The first thing we need to do is to import the Skill class and the regex_matcher. Your __init__.py file should look like this:	
	from opsdroid.skill import Skill
	from opsdroid.matchers import match_regex
	
Now we need to write the fappening class to generate urls.  Let's create a class that inherits from the Skill class to contain the function.

Let's create an asynchronous function.

We need to create a regular expression that will trigger opsdroid running the fappening function. 

We also will need to pass the message that the user sends in order to determine how opsdroid will respond.
	
## Usage

opsdroid> fappening [celebname] will generate URLS for nude celebrity pictures.  Can accept up to names with 5 words ie. a b c d e

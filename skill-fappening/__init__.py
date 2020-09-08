from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class SkillthefappeningSkill(Skill):
   # group 			|			option
   # fappening			|			required
   # any character		|			required to create URL
   # any character		|			optional
   # any character		|			optional
   # ie. fappening <-- next line
   #     fappening a <-- baseurl + a + /
   #     fappening a b <-- baseurl + a + - + b + /
   #     fappening a b c <-- baseurl + a + - + b + - + c + /
   #     fappening a b c d <-- baseurl + a + - + b + - + c + - + d + /
   #  baseurl = "https://thefappening.plus/category/"
   #  await message.respond(baseurl + str(c_fname) + "-" + str(c_lname) + "/")

   @match_regex(r'fappening (\S+)(\s\S+)?(\s\S+)?(\s\S+)?(\s\S+)?')
   async def thefappening_getimages(self, message):
   	baseurl = "https://thefappening.plus/category/"
   	if (message.regex.group(2)):
   		if (message.regex.group(3)):  	
   			if (message.regex.group(4)): 
   				if (message.regex.group(5)):
   					await message.respond(baseurl + str(message.regex.group(1)) + "-" + str(message.regex.group(2)).strip() + "-" + str(message.regex.group(3)).strip() + "-" + str(message.regex.group(4)).strip() + "-" + str(message.regex.group(5)).strip() +"/")
   				else:
   					await message.respond(baseurl + str(message.regex.group(1)) + "-" + str(message.regex.group(2)).strip() + "-" + str(message.regex.group(3)).strip() + "-" + str(message.regex.group(4)).strip() +"/")
   			else:
   				await message.respond(baseurl + str(message.regex.group(1)) + "-" + str(message.regex.group(2)).strip() + "-" + str(message.regex.group(3)).strip() + "/")     				   
   		else:
   			await message.respond(baseurl + str(message.regex.group(1)) + "-" + str(message.regex.group(2)).strip() + "/")   		
   	else:
   		await message.respond(baseurl + str(message.regex.group(1)) + "/")

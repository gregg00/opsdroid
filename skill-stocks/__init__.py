from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class SkillstocksSkill(Skill):


    #https://www.marketwatch.com/investing/stock/aapl

    @match_regex(r'stocks (\S+)')
    async def getstock(self, message):
    	baseurl = "https://www.marketwatch.com/investing/stock/"
    	await message.respond(baseurl + str(message.regex.group(1)))

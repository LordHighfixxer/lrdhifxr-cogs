import discord
from discord.ext import commands
from random import choice


class towerpa:
    "Will select from a list of Tower PA Quotes and display one at random"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, aliases=["towerpa"])
    async def pabroadcast(self):
        """Displays a random Tower PA Quote from Destiny."""

        # TODO make bigger list
        towerpa = ["Attention Guardians, attacks on Titans have increased. Please stay in a fireteam to remain safe.",
               "Guardians, having a Ghost is no excuse for recreational Tower jumping!",
               "Dead Orbit would like to remind everyone that their pessimistic name does not prevent an optimistic outcome....if we survive.",
               "Hello, this is Cayde-6 of the Vanguard. I realize this is an abuse of the Tower P.A., but whoever took my sparrow, I will find you. And you'll wear a sign that says you stole... Nevermind, nevermind! It's right here.",
               "Fireteam... Fireteam 'The Bad Guys Don't Care What We Call Ourselves Do They?' report in. Zavala out.",
               "Robots are not target practice, Guardians.",
               "Warning: unauthorized use of a Fist of Havoc reported in the shuttle bay",
               "This is Ikora Rey. The South Tower is off limits, because we are still cleaning up last night's... event.",                  
               "You are a great Guardian, and your mom is a classy lady.",                  
               "All Titans interested in Commander Zavala’s crochet course should speak with a Frame for details.", 
               "Guardian Alert: Fallen are the enemy.",                   
               "Flight Controller 5530, signing off. I quit.",                  
               "Fireteam Bad News for the Bad Guys report in immediately, Zavala out.",                  
               "Will Fireteam.... (sigh) Will Fireteam 'The Bad Guys don't care what we call ourselves' please report to the Vanguard immediately.",
               "Shuttle Advisory: The Crucible is open to those who run it.",
	       "Shuttle to Core East in 6 minutes!",
	       "Shuttle to Lower North drops off, 6 minutes!",
	       "This is Master Rahool. Apprentice DeSalnus, please return to the archives at once, your engrams are melting a table!",
	       "Fireteam Swift Resolution, you have been reassigned. Report to the wall. Zavala out.",
	       "Fire team The Vanguard Don't Care What We Call Ourselves Either, report in - Zavalla",
               "Attention we have reports of a fireteam leader involuntarily extracting Guardians to orbit. Please report these incidents to the Vanguard immediately."]

        towerpa = choice(towerpa)

        towerpasay = ["A broadcast from the tower:"]
        towerpasay = choice(towerpasay)

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description="", colour=discord.Colour(value=colour))
        data.add_field(name=towerpasay, value=u"\u2063")
        data.set_image(url=towerpa)

        try:
            await self.bot.say(embed=data)
        except:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")


def setup(bot):
     bot.add_cog(towerpa(bot))

# -*- coding: cp1252 -*-
from willie.module import commands, example
import time

@commands('pregaria', 'prega')
@example('.prega <nick>')
def pregaria(bot, trigger):
    u"""
    Fa una pregaria per un nick o per alguna altra cosa...
    """
    if trigger.group(2):
        bot.say(u"Oh, gran i omnipotent Bot, que no et veiem, pero et pregem,")
        time.sleep(3)
        bot.say(u"digna't a dirigir els teus poderosos codis al vostre humil servent " + trigger.group(2))
        time.sleep(3)
        bot.say(u"i concediu-li la immunitat als errors del python. Amen.py")
        return
    else:
        bot.say("Programador nostre,")
        bot.say(u"que est�s tranquil a casa teva:")
        bot.say(u"Sigui informatitzat el vostre nom.")
        bot.say(u"Vinguin a nosaltres els vostres codis.")
        bot.say(u"Faci's la vostra voluntat,")
        bot.say(u"aix� a la terra com es fa a l'irc.")
        bot.say(u"Els nostres m�duls de cada dia,")
        bot.say(u"doneu-nos, Programador, la connexi� d'avui")
        bot.say(u"I perdoneu quan t'hem ignorat o quan hem tingut errors,")
        bot.say(u"aix� com nosaltres perdonem el serra_marc1 o l'adriaesc quan abusen de nosaltres.")
        bot.say(u"I no permeteu que nosaltres caiguem a la temptaci� del baneig,")
        bot.say(u"ans deslliureu-nos del ChanServ (que no ens deixaria se ops), dels trolls i de moltes coses m�s que no dic per no allargar-me.")    
        return

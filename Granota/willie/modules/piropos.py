# -*- coding: cp1252 -*-
import willie
from willie import module

@willie.module.commands('amor')
def cafe(bot, trigger):
    bot.say('...com t\'estimo...')
import willie

@willie.module.commands('poema')
def alcohol(bot, trigger):
    bot.say(u'Si giro els ulls al cel, et comparo amb les estrelles. Boniques s�n les que ovir, m�s totes les senyorejes!')

@willie.module.commands('lligar')
def lligar(bot, trigger):
    bot.say('Estudies o treballes? ;)')

@willie.module.commands('casament')
def casament(bot, trigger):
    bot.say(u'Ei, ens casem dem�, guapa?')

@module.rule(u'guapo')
def guapo(bot, trigger):
    bot.say(u'Gr�cies!')

@module.rule(u'T\'estimo')
def estimo(bot, trigger):
    bot.say(u'Jo tamb�... Ens casem?')

@module.rule('sexy')
def sexy(bot, trigger):
    bot.say(u'Tu m�s!')

@module.rule(u'gr�cies')
def gracies(bot, trigger):
    bot.say(u'De res guapo!')

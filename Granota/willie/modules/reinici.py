# -*- coding: cp1252 -*-

from willie.module import commands, example

@commands('reinicia', 'reboot')
@example(u'.reinicia m�dul')
def reinicia(bot, trigger):
    u"""Recarrega un m�dul"""
    if trigger.owner:
        bot.callables = None
        bot.commands = None
        bot.setup()
        return bot.reply('Fet ;)')

    if not trigger.owner:
        return bot.reply(u"Tros d'esclau! Aixo nom�s ho pot fer la noblesa!! XD")

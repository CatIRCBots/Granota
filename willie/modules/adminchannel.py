# -*- coding: utf-8 -*-

import re
from willie.module import commands, priority, OP


def setup(bot):
    #Having a db means pref's exists. Later, we can just use `if bot.db`.
    if bot.db and not bot.db.preferences.has_columns('topic_mask'):
        bot.db.preferences.add_columns(['topic_mask'])


@commands('op')
def op(bot, trigger):
    if trigger.admin:
        if not trigger.group(2):
            channel = trigger.sender
            nick = trigger.nick
            bot.msg('ChanServ', 'op ' + trigger.sender + ' ' + nick)
            return
        else:
            channel = trigger.sender
            nick = trigger.group(2)
            bot.msg('ChanServ', 'op ' + trigger.sender + ' ' + nick)
            return
    else:
        return
        

@commands('deop')
def deop(bot, trigger):
    if trigger.admin:
        if not trigger.group(2):
            channel = trigger.sender
            nick = trigger.nick
            bot.msg('ChanServ', 'deop ' + trigger.sender + ' ' + nick)
            return
        else:
            channel = trigger.sender
            nick = trigger.group(2)
            bot.msg('ChanServ', 'deop ' + trigger.sender + ' ' + nick)
            return
    else:
        return

@commands('voice', 'v', 'veu', 'voz')
def voice(bot, trigger):
    if trigger.admin:
        if not trigger.group(2):
            channel = trigger.sender
            nick = trigger.nick
            bot.msg('ChanServ', 'voice ' + trigger.sender + ' ' + nick)
            return
        else:
            channel = trigger.sender
            nick = trigger.group(2)
            bot.msg('ChanServ', 'voice ' + trigger.sender + ' ' + nick)
            return
    else:
        return
            
@commands('devoice', 'dv')
def devoice(bot, trigger):
    if trigger.admin:
        if not trigger.group(2):
            channel = trigger.sender
            nick = trigger.nick
            bot.msg('ChanServ', 'devoice ' + trigger.sender + ' ' + nick)
            return
        else:
            channel = trigger.sender
            nick = trigger.nick
            bot.msg('ChanServ', 'devoice ' + trigger.sender + ' ' + nick)
            return
    else:
        return


@commands('kick')
@priority('high')
def kick(bot, trigger):
    if bot.privileges[trigger.sender] < OP:
        return
    if not trigger.admin:
        return
    bot.write(['KICK', trigger.group(2)])


def configureHostMask(mask):
    if mask == '*!*@*':
        return mask
    if re.match('^[^.@!/]+$', mask) is not None:
        return '%s!*@*' % mask
    if re.match('^[^@!]+$', mask) is not None:
        return '*!*@%s' % mask

    m = re.match('^([^!@]+)@$', mask)
    if m is not None:
        return '*!%s@*' % m.group(1)

    m = re.match('^([^!@]+)@([^@!]+)$', mask)
    if m is not None:
        return '*!%s@%s' % (m.group(1), m.group(2))

    m = re.match('^([^!@]+)!(^[!@]+)@?$', mask)
    if m is not None:
        return '%s!%s@*' % (m.group(1), m.group(2))
    return ''


@commands('ban')
@priority('high')
def ban(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    text = trigger.group().split()
    argc = len(text)
    if argc < 2:
        return
    opt = text[1]
    banmask = opt
    channel = trigger.sender
    if opt.startswith('#'):
        if argc < 3:
            return
        channel = opt
        banmask = text[2]
    banmask = configureHostMask(banmask)
    if banmask == '':
        return
    bot.write(['MODE', channel, '+b', banmask])


@commands('unban')
def unban(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    text = trigger.group().split()
    argc = len(text)
    if argc < 2:
        return
    opt = text[1]
    banmask = opt
    channel = trigger.sender
    if opt.startswith('#'):
        if argc < 3:
            return
        channel = opt
        banmask = text[2]
    banmask = configureHostMask(banmask)
    if banmask == '':
        return
    bot.write(['MODE', channel, '-b', banmask])


@commands('quiet')
def quiet(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    text = trigger.group().split()
    argc = len(text)
    if argc < 2:
        return
    opt = text[1]
    quietmask = opt
    channel = trigger.sender
    if opt.startswith('#'):
        if argc < 3:
            return
        quietmask = text[2]
        channel = opt
    quietmask = configureHostMask(quietmask)
    if quietmask == '':
        return
    bot.write(['MODE', channel, '+q', quietmask])


@commands('unquiet')
def unquiet(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    text = trigger.group().split()
    argc = len(text)
    if argc < 2:
        return
    opt = text[1]
    quietmask = opt
    channel = trigger.sender
    if opt.startswith('#'):
        if argc < 3:
            return
        quietmask = text[2]
        channel = opt
    quietmask = configureHostMask(quietmask)
    if quietmask == '':
        return
    bot.write(['MODE', opt, '-q', quietmask])


@commands('kickban', 'kb')
@priority('high')
def kickban(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    text = trigger.group().split()
    argc = len(text)
    if argc < 4:
        return
    opt = text[1]
    nick = opt
    mask = text[2]
    reasonidx = 3
    if opt.startswith('#'):
        if argc < 5:
            return
        channel = opt
        nick = text[2]
        mask = text[3]
        reasonidx = 4
    reason = ' '.join(text[reasonidx:])
    mask = configureHostMask(mask)
    if mask == '':
        return
    bot.write(['MODE', '+b', mask])
    bot.write(['KICK', channel, nick, ' :', reason])

@commands('topic')
def topic(bot, trigger):
    purple, green, bold = '\x0306', '\x0310', '\x02'
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        if bot.config.lang == 'ca':
            bot.reply(u"Necessito com a ḿinim flags d'operador del canal.")
        elif bot.config.lang == 'es':
            bot.reply("Necesito flags de operador del canal.")
        else:
            bot.reply("I need at least operator flags to perform this action.")
        return
    text = trigger.group(2)
    if text == '':
        return
    channel = trigger.sender.lower()

    narg = 1
    mask = None
    if bot.db and channel in bot.db.preferences:
        mask = bot.db.preferences.get(channel, 'topic_mask')
        narg = len(re.findall('%s', mask))
    if not mask or mask == '':
        mask = '%s'

    top = trigger.group(2)
    text = tuple()
    if top:
        text = tuple(unicode.split(top, '~', narg))

    if len(text) != narg:
        if bot.config.lang == 'ca':
            message = "Falten arguments. Me n'has donat " + str(len(text)) + ', pero en calen ' + str(narg) + '.'
        elif bot.config.lang == 'es':
            message = "Faltan argumentos. Me has dado " + str(len(text)) + ', pero hacen falta ' + str(narg) + '.'
        else:
            message = "Not enough arguments. You gave " + str(len(text)) + ', it requires ' + str(narg) + '.'
        return bot.say(message)
    topic = mask % text

    bot.write(['TOPIC', channel + ' :' + topic])


@commands('tmask')
def set_mask(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    if not bot.db:
        if bot.config.lang == 'ca':
            bot.say("No tinc ben configurada la base de dades i no he pogut dur a terme aquesta accio.")
        elif bot.config.lang == 'es':
            bot.say(u"No tengo bien configurada la base de datos y no he podido hacer esa accion.")
        else:
            bot.say(u"I don't have my database configured and I couldn't make this action.")
    else:
        bot.db.preferences.update(trigger.sender.lower(), {'topic_mask': trigger.group(2)})
        if bot.config.lang == 'ca':
            bot.say("Fet, " + trigger.nick)
        elif bot.config.lang == 'es':
            bot.say("Hecho, " + trigger.nick)
        else:
            bot.say("Done, " + trigger.nick)

@commands('showmask')
def show_mask(bot, trigger):
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    if not bot.db:
        if bot.config.lang == 'ca':
            bot.say("No tinc ben configurada la base de dades i no he pogut dur a terme aquesta accio.")
        elif bot.config.lang == 'es':
            bot.say(u"No tengo bien configurada la base de datos y no he podido hacer esa accion.")
        else:
            bot.say(u"I don't have my database configured and I couldn't make this action.")
    elif trigger.sender.lower() in bot.db.preferences:
        bot.say(bot.db.preferences.get(trigger.sender.lower(), 'topic_mask'))
    else:
        bot.say("%s")

@commands('m', 'moderat', 'moderado', 'moderate')
def moderat(bot, trigger):
    if trigger.admin:
        channel = trigger.sender
        bot.write(["MODE", channel, "+m"])
    else:
        bot.say(u"Ho sento, pero no")
        return
    
@commands('unmoderate', '-m')
def dmoderat(bot, trigger):
    if trigger.admin:
        channel = trigger.sender
        bot.write(["MODE", channel + " -m"])
    else:
        if bot.config.lang == 'ca':
            bot.say(u"No ets administrador.")
        elif bot.config.lang == 'es':
            bot.say(u"No eres administrador.")
        else:
            bot.say(u"You are not admin.")
        return

@commands('recover', 'recupera')
def recover(bot, trigger):
    if not trigger.admin:
        return
    if trigger.sender.startswith('#'):
        if bot.config.lang == 'ca':
            bot.say('Nomes en privat')
        elif bot.config.lang == 'es':
            bot.say('Solo en privado')
        else:
            bot.say('Only in private')
        return
    if not trigger.group(2):
        return
    if trigger.admin:
        channel = trigger.group(2)
        bot.msg('ChanServ', 'recover ' + channel)
        bot.join(channel)
        bot.write(['MODE', channel + ' +I ' + trigger.nick])
        if bot.config.lang == 'ca':
            bot.reply(u"Recuperació completada per %s. Ja pots entrar al canal." % channel)
        elif bot.config.lang == 'es':
            bot.reply(u"Recuperacion completada por %s. Ya puedes entrar al canal." % channel)
        else:
            bot.reply(u"Recover complete for %s. You can now join the channel." % channel)
        return
    
@commands('i')
def i(bot, trigger):
    if trigger.admin:
        channel = trigger.sender
        bot.write(['MODE', channel + ' +i'])
        return
    else:
        return

@commands('-i')
def di(bot, trigger):
    if trigger.admin:
        channel = trigger.sender
        bot.write(['MODE', channel + ' -i'])
        return
    else:
        return

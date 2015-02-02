# -*- coding: cp1252 -*-
from willie import module
from willie.module import commands
import random
import re
import respostes

ligns = []
rmencionormal = [u"Et penses que et repondr�? Bah!",u"Digues, amor meu!",
                 u"Dieu algo?",u"Vigila amb el que dius, que no saps qui s�c jo!",
                 u"Bah",u"%s, per qu� dius aix�? No m'ofenguis!",u"Aqu� la bot-central. Digui?",
                 u"pssss (faig pipi)",u"hola!",u"Calla, que estic ocupat!",u"No siguis burro!",
                 u"mmmmmhhh",u"Tu creus?",u"un segon",u"hi hi hi",
                 u"Al m�n hi ha 10 tipus de bot: els que saben binari i els que no.",
                 u"Al m�n hi ha 3 tipus de bot: els que saben comptar i els que no.",
                 u"Calculant l'�ltima xifra del nombre pi. Esperi si us plau...",
                 u"�ltimes not�cies: La tecla 'Control' ha detingut la tecla 'Escape' que ha quedat sota cust�dia de la tecla 'Bloquejar Despla�ament'.",
                 u"Un hotel infinit ple pot acollir infinits clients m�s. Per� un bot infinitament perfecte (Com jo) pot respondre a les teves peticions *finites*.",
                 u"Carpe diem et quid pro quo ut non habeas corpus mutatis mutandis.",
                 u"Menteixes quan dius que menteixes?",
                 u"Ho diuen les enquestes: cinc de cada deu bots... s�n la meitat.",
                 u"Jo mai oblido un nick... per� en el teu cas far� una excepci�.",
                 u"[<Espai reservat per a publicitat>]"]
rmenciowner = [u"Totalment d'acord!",u"L'amo sap guiar-nos molt b�...",
               u"S�, amo, el que tu diguis.",u"A la �rden!",
               u"per servir-lo",u"servidor",u"Senyor meu, m'omple de joia sentir el meu nom en el teu admirable discurs.",
               u":)",u"Els meus respectes, majestat",
               u"Oh, majestat, �s evident que us recolzar� sempre, en totes les vostres decisions!",
               u"El jefe �s un pesat, que alg� el faci fora del xat!!! >:D",
               u"Un favor personal... dona els privilegis d'owner a alg� altre!"]
#rhola = [u"Benvingut %s", u"Ei %s!",u"Bon dia %s",u"All� %s!",
#	u"bip... bip... detectant un intr�s al canal... %s",
#	u"Ei tio, que passa %s?",u"Hello %s, how are you?",u"Hola %s, qu� tal?"]
radeu = [u'Ad�u... que far� jo, sense tu? snif snif...', u'Ad�u!',
         u'A reveure!', u'Que vagi b�!', u'Cuida\'t!',
         u'Per fi se\'n va, aquest! XD', u'No em deixis sol amb aquesta colla de bandarres! :)',
         u'Au revoir!']
rtonto = [u'Gr�cies!', u'Aix� tu, carallot!', u'Mira que em xibo a en NeoMahler!',
          u':P :P', u'Me\'n vaig plorant...']
rllengua = [u'Ets m�s maleducat que jo (i mira que �s dif�cil) XD',
            u'Ensenyar la llengua �s de mala educaci�!! :P :P :P']
rperfect = [u'Com jo XD', u'Ai que m\'emociono...', u'Com ha de ser!',
            u'Me\'n alegro!!']

@module.rule(u'ad�u')
def adeu(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(random.choice(radeu))

#@module.rule('hola')
#def hola(bot, trigger):
#    hola = random.choice(rhola)
#    bot.say(hola % trigger.nick)

@module.rule(u':P')
def llengua(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(random.choice(rllengua))

@module.rule('.*$nickname.*')
def mencio(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        if trigger.owner:
            dau = random.choice(['owner','nowner'])
            if dau == 'owner':
                bot.say(random.choice(rmenciowner))
                return
            else:
                bot.say(random.choice(rmencionormal))
        else:
            bot.say(random.choice(rmencionormal))

@module.rule(u'perfect')
def perfecte(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(random.choice(rperfect))

@module.rule(u'tonto')
def tonto(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(random.choice(rtonto))

@module.rule(u'visca')
def visca(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(u'VISCAAAAA!!!!!!!!!!!!!!!')

@module.rule(u'mor')
def mor(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(u"No!!!! No s�c un assass� en s�rie, si vols alguna mort more't tu, " + trigger.nick)

@module.rule('Bot')
def bot(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say(u'Aix� tu, tros d\'hum�!!')

@module.rule(r'(?i).*(Fuck|Screw|shit|mierda|ilipoll|merda|puta|puto).*')
def rude(bot, trigger):
    if trigger.nick in ligns:
        return
    else:
        bot.say('Vigilem aquesta boqueta...')

@commands('ign')
def ign(bot, trigger):
    if trigger.admin:
        if not trigger.group(2):
            return
        else:
            ligns.append(trigger.group(2))
            bot.reply(u"Ignorant a " + trigger.group(2))
    else:
        return

@commands('unign')
def unign(bot, trigger):
    if trigger.admin:
        if not trigger.group(2):
            return
        else:
            if trigger.group(2) in ligns:
                ligns.remove(trigger.group(2))
            else:
                bot.reply(trigger.group(2) + u" no est� a la llista. Escriu \".igns\" per veure la llista d'ignorats")
                return
    else:
        return

@commands('igns')
def igns(bot, trigger):
    if not trigger.admin:
        return
    else:
        bot.msg(trigger.nick, u"Llista de nick ignorats: " + str(ligns))
        return

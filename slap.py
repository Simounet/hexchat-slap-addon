from __future__ import print_function

from random import choice

import hexchat

__module_name__ = 'Slap'
__module_version__ = '2.2'
__module_description__ = 'Slaps specified users'
__author__ = 'Douglas Brunal (AKA) Frankity'

slaps = {
    'trout': 'slaps {} around a bit with a large trout',
    'WeeChat': 'gives {} a clout round the head with a fresh copy of WeeChat',
    'smelly trout': 'slaps {} with a large smelly trout',
    'sternly': 'breaks out the slapping rod and looks sternly at {}',
    'bottom': 'slaps {}\'s bottom and grins cheekily',
    'times': 'slaps {} a few times',
    'carried away': 'slaps {} and starts getting carried away',
    'not violent': 'would slap {}, but is not being violent today',
    'hearty': 'gives {} a hearty slap',
    'large object': 'finds the closest large object and gives {} a slap with it',
    'randomly picks': 'likes slapping people and randomly picks {} to slap',
    'kitchen towel': 'dusts off a kitchen towel and slaps it at {}'
}


def slap_cb(word, word_eol, userdata):
    wordLen = len(word)
    if wordLen > 0:
        if wordLen == 3:
            nick = word[2]
            slapSelected = slaps[word[1]]
        else:
            nick = word[1]
            slapSelected = slaps[choice(slaps.keys())]
        hexchat.command('me ' + slapSelected.format(nick))
    else:
        hexchat.command('help slap')
    return hexchat.EAT_ALL

def slap_menu():
    hexchat.command("MENU -p4 ADD \"$NICK/Slap\"")
    for i in slaps:
        hexchat.command("MENU ADD \"$NICK/Slap/" + i + "\" \"slap " + i + " %s\"")

def unload_cb(userdata):
    print(__module_name__, 'version', __module_version__, 'unloaded.')

hexchat.hook_command('slap', slap_cb, help=("Random slap:\n"
                                            "/slap <nick>\n"
                                            "Specific slap:\n"
                                            "/slap <key> <nick>"))
slap_menu()
hexchat.hook_unload(unload_cb)
print(__module_name__, 'version', __module_version__, 'loaded.')

from tools import *
from databank import *


def main ():
    montrez_bienvenue_message ()
    while user_continues:
     entrez_code_pin ()
    if pin_good:
         montrez_menu ()
    else :
        message_erreur()

   



print "Au revoir !"

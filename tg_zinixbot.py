import telegram
from time import sleep
#import random
from random import SystemRandom
import urllib.request as urllib2
import sys
import re

ran = SystemRandom()

token = sys.argv[1]

regex = re.compile(r"w[huaioe]*t +d[iaoeu]*stor", re.IGNORECASE)

bot = telegram.Bot(token = token)
rekt = ['Rekt', 'Really Rekt', 'Tyrannosaurus Rekt', 'Cash4Rekt.com', 'Grapes of Rekt', 'Ship Rekt', 'Rekt markes the spot', 'Caught rekt handed', 'The Rekt Side Story', 'Singin\' In The Rekt', 'Painting The Roses Rekt', 'Rekt Van Winkle', 'Parks and Rekt', 'Lord of the Rekts: The Reking of the King', 'Star Trekt', 'The Rekt Prince of Bel-Air', 'A Game of Rekt', 'Rektflix', 'Rekt it like it\'s hot', 'RektBox 360', 'The Rekt-men', 'School Of Rekt', 'I am Fire, I am Rekt', 'Rekt and Roll', 'Professor Rekt', 'Catcher in the Rekt', 'Rekt-22', 'Harry Potter: The Half-Rekt Prince', 'Great Rektspectations', 'Rekt Paper Scissors', 'RektCraft', 'Grand Rekt Auto V', 'Call of Rekt: Modern Reking 2', 'Legend Of Zelda: Ocarina of Rekt', 'Rekt It Ralph', 'Left 4 Rekt', 'Pokemon: Fire Rekt', 'The Shawshank Rektemption', 'The Rektfather', 'The Rekt Knight', 'Fiddler on the Rekt', 'The Rekt Files', 'The Good, the Bad, and The Rekt', 'Forrekt Gump', 'The Silence of the Rekts', 'The Green Rekt', 'Gladirekt', 'Spirekted Away', 'Terminator 2: Rektment Day', 'The Rekt Knight Rises', 'The Rekt King', 'REKT-E', 'Citizen Rekt', 'Requiem for a Rekt', 'REKT TO REKT ass to ass', 'Star Wars: Episode VI - Return of the Rekt', 'Braverekt', 'Batrekt Begins', '2001: A Rekt Odyssey', 'The Wolf of Rekt Street', 'Rekt\'s Labyrinth', '12 Years a Rekt', 'Gravirekt', 'Finding Rekt', 'The Arekters', 'There Will Be Rekt', 'Christopher Rektellston', 'Hachi: A Rekt Tale', 'The Rekt Ultimatum', 'Shrekt', 'Rektal Exam', 'Rektium for a Dream', 'The Hunt for Rekt October', 'Oedipus rekt', 'The Tesserekt', 'REKT! REKT! HELP ME! 123 Cavendon Road. Looking forward to hearing from you. Yours truly, Maurice Moss']
dastor = ["AAAARCHARCHARCHARCH", "Install Gentoo", "ARCH! ARCH! ARCH!", "INSTALL GENTOO", "GEN2","AAAAAAAAAAAAARCH", "HANNAHMONTANALINUX", "gan2", "m'lady"]

def distro(msg):
    distrourl = "http://distrowatch.com/"
# if no arguments, gives random distro
    if msg == "":
        site = urllib2.urlopen(distrourl + "random.php")  # uses random.php to give random distro
        distro = site.readlines()[1][24:-9]  # gets distro name from title
        url = site.geturl()  # gets url from the distro page
        return distro.decode("utf-8") + " - " + url  # returns distroname and url
    else:
        # only uses first argument ie damn returns Damn Small
        a = msg[:15]
        site = urllib2.urlopen(distrourl + "table.php?distribution=%s" % a)  # uses table.php to be directed to a distro page
        distro = site.readlines()[1][24:-9]  # gets distro from title
        url = site.geturl()  # gets url from the page
        if distro != "":  # if distro name is empty returns not found
            return str(distro) + " - " + url
#       else:
            return "Did not find distro named %s." % a

#    return "AAAARCHARCHARCHARCHARCHARCH"

print(bot.getMe())

def main():
  try:
    update_id = bot.getUpdates()[0].update_id
  except IndexError:
    update_id = None
  while True:
    sleep(1)

    updates = bot.getUpdates()
    if len(updates) >= 10:
      update_id += (len(updates) - 2)
      #print(update_id, len(updates))

    try:
      update_id = parse(bot, update_id)
    except telegram.TelegramError as e:
      # These are network problems with Telegram.
      if e.message in ("Bad Gateway", "Timed out"):
        sleep(1)
      elif e.message == "Unauthorized":
        # The user has removed or blocked the bot.
        update_id += 1
      else:
         raise e

    #try:
      #print([u.message.text for u in updates])
      #print([u.message.sticker.file_id for u in updates])
    #except AttributeError:
      #dfsajkldfsjlk = 0

def parse(bot, update_id):
  # Request updates after the last update_id
  for update in bot.getUpdates(offset=update_id, timeout=10):
    # chat_id is required to reply to any message
    if update is not None:
        chat_id = update.message.chat_id

    update_id = update.update_id + 1
    message = update.message.text

    #sleep(2)

    if message:
      # Reply to the message
      if message[0] == '/':
        cmd = message[1:].split(' ')
        commander = update.message.from_user.first_name
#        if 'test' in cmd[0]:
#          bot.sendMessage(chat_id=chat_id, text="Hello world!")
        if 'credits@tanZinixBot' in cmd[0]:
          bot.sendMessage(chat_id=chat_id, text="Originally coded by HolyGNU, unixbird, and Alinea169. Telegram version by zinn, forked by Whovian9369. This implementation by junatt. Much love to Streetwalrus for helping out with the tg bot code.")
        if 'highfive@tanZinixBot' in cmd[0]:
          bot.sendMessage(chat_id=chat_id, text="*zinixbot gives %s a highfive*" % commander, parse_mode=telegram.ParseMode.MARKDOWN)
        if "interject@tanZinixBot" in cmd[0]:
          bot.sendMessage(chat_id=chat_id, text="I'd just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.")
        if "rekt@tanZinixBot" in cmd[0]:
            #ran.seed()
            rektmsg = ran.choice(rekt)
            bot.sendMessage(chat_id=chat_id, text="%s" % rektmsg)
        if "shrug@tanZinixBot" in cmd[0]:
          bot.sendSticker(chat_id=chat_id, sticker="BQADBAADegADJkm4A_GsmQiGTg6lAg")
        if 'distro@tanZinixBot'  in cmd[0]:
#          bot.sendMessage(chat_id=chat_id, text="AAAAARCHARCHARCHARCHARCH")
          if len(cmd) == 1:
            mydist = distro("")
          else:
            mydist = distro(cmd[1])
          bot.sendMessage(chat_id=chat_id, text="%s" % mydist)
      else:
        if regex.search(message) is not None:
            #random.seed()
            dastormsg = ran.choice(dastor)
            bot.sendMessage(chat_id=chat_id, text=dastormsg)
            #if message.lower() == "wat distor":
        elif "what distro" in message.lower():
            #random.seed()
            dastormsg = ran.choice(dastor)
            bot.sendMessage(chat_id=chat_id, text=dastormsg)

        f = open('messageslog.txt', 'a')
        f.write(update.message.from_user.name + ":" + message + "\n")
        filecounter = 0
        filecounter+=1
        if filecounter % 10 == 0:
            f.close()
            f = open('messageslog.txt', 'a')

  return update_id

main()

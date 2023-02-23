import requests
import os
import colorama
from colorama import Fore
colorama.init()

os.system('title Made by Azakiwlex')


print (Fore.BLUE + f""" 

    :::     :::::::::       ::::::::  :::::::::     :::     ::::    ::::  ::::    ::::  :::::::::: :::::::::  
  :+: :+:        :+:       :+:    :+: :+:    :+:  :+: :+:   +:+:+: :+:+:+ +:+:+: :+:+:+ :+:        :+:    :+: 
 +:+   +:+      +:+        +:+        +:+    +:+ +:+   +:+  +:+ +:+:+ +:+ +:+ +:+:+ +:+ +:+        +:+    +:+ 
+#++:++#++:    +#+         +#++:++#++ +#++:++#+ +#++:++#++: +#+  +:+  +#+ +#+  +:+  +#+ +#++:++#   +#++:++#:  
+#+     +#+   +#+                 +#+ +#+       +#+     +#+ +#+       +#+ +#+       +#+ +#+        +#+    +#+ 
#+#     #+#  #+#           #+#    #+# #+#       #+#     #+# #+#       #+# #+#       #+# #+#        #+#    #+# 
###     ### #########       ########  ###       ###     ### ###       ### ###       ### ########## ###    ### 

""" )
webhook = input (Fore.RED + 'Webhook url: ')
print("Spameando la Webhook. CTRL + C para detener")


while True:
  data = {
    'avatar_url': 'https://cdn.discordapp.com/attachments/990801275962679296/1078037397482258576/MOSHED-2023-2-22-12-26-53.png',
    'username': 'KugelBlitz Destroyer',
    'Content': 'Hello',
    'embeds': [{
    'title': 'GET REKT',
    'description': 'GET REKT'
    
    }]


}
  x = requests.post(webhook, json=data)


  
 
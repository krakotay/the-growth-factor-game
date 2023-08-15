# Вы можете расположить сценарий своей игры в этом файле.
define config.hard_rollback_limit = 0

# Определение персонажей игры.
define ee = Character('[name]', color="#28e928")
define e = Character('[name], thoughts:', color="#02aadd")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
python:
    flag = True
init:
    image buyactive:
        "buyactive.png"
        zoom 0.1
    image buyactive2:
        "buyactive2.png"
        zoom 0.1
    image buynotactive:
        "buynotactive.png"
        zoom 0.1
    image gg1:
        "gg1.png"
        align (.5, 0.3)
    image gg2:
        "gg2.png"
        align (.5, 0.3)
    image gg3:
        "gg3.png"
        align (.5, 0.3)
    image gg4:
        "gg4.png"
        align (.5, 0.3)
    image gg5:
        "gg5.png"
        align (.5, 0.3)
    image gg6:
        "gg6.png"
        align (.5, 0.3)
    image gg7:
        "gg7.png"
        align (.5, 0.3)
    image gg8:
        "gg8.png"
        align (.5, 0.3)
default mass = 50
default stamina_base = 20
default experience = 0
default exp_stam = 0
default stamina = 20
default time = 17
default exp_stam_max = 5
default fill = 20
default fill_max = 20
default fill_level = 1 + (mass - 50) // 10
default health = 20
default health_max = 20
default money = 500
default clocks = 24 - time
default exg = 2

default cam = False
default gluttony = False
default dds = False
default measure_tape = False
default scales = False
default tape = False
default cafe_text = False
default gym_text = False
default wc_count = False
default adrenalin = False

default stadia1_selfie = ["gg1"]
default stadia2_selfie = ["gg2"]
default stadia3_selfie = ["gg3"]
default stadia4_selfie = ["gg4"]

default week = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default week_count = 0
######################################
#Мои скрины###########################
######################################
screen stats:
    frame:
        xalign 1.0
        vbox:
            $ exp_max = - 45 + mass
            $ exp_stam_max = (stamina_base - 15)
            if scales == False:
                text "Weight, kg: ???"
            if scales == True:
                text "Weight, kg: [mass]"
            text "Money: [money]$"
screen stats_bar:
        $ exp_max = - 45 + mass
        $ exp_stam_max = (stamina_base - 15)
        vbox:
            yalign 0.1
            xalign 1.0
            bar:
                left_bar Frame("gui/bar/left green.png")
                value experience
                range exp_max
                xysize(350, 40)
            bar:
                left_bar Frame("gui/bar/left green.png")
                value exp_stam
                range exp_stam_max
                xysize(350, 40)
screen stats_bar_text:
    $ exp_max = - 45 + mass
    $ exp_stam_max = (stamina_base - 15)
    vbox:
        yalign 0.1
        xalign 1.0
        text "Mass Experience [experience]/[exp_max]"
        text "Energy Experience [exp_stam]/[exp_stam_max]"
screen time_text:
    frame:
        $ clocks = 24 - time
        $ week_day = week[week_count]
        text " [week_day], [clocks]:00"
screen fill_status:
        vbox:
            spacing 3
            yalign 0.1
            bar:
                left_bar Frame("gui/bar/left yellow.png")
                value stamina
                range stamina_base
                xysize(300, 40)
            bar:
                left_bar Frame("gui/bar/left orange.png")
                value fill
                range fill_max
                xysize(300, 40)
            bar:
                left_bar Frame("gui/bar/left red.png")
                style_group 'health'
                value health
                range health_max
                xysize(300, 40)
screen fill_status_text:
        vbox:
            yalign 0.1
            spacing 3
            text "Energy: [stamina]/[stamina_base]" 
            text "Satiety: [fill]/[fill_max]" 
            text "Health: [health]/[health_max]"
screen phone_button_active:
    imagebutton:
        xalign .993
        yalign 0.2
        idle "phone call.png"
        hover "phone call small.png"
        action [Hide('phone_button_active'), Show("phone_screen"), Show("gallery_button"), Show("stats_button"), Show("market_button"), Show("chat_button"), Show("chat_screen")]
screen phone_button:
    imagebutton:
        xalign .993
        yalign 0.2
        idle "phone.png"
        hover "phone small.png"
        action [Show("phone_screen"), Show("gallery_button"), Show("stats_button"), Show("market_button"), Show("chat_button")]

screen phone_screen:
    modal True
    imagemap:
        ground "phone big.png" xalign 0.5 yalign 0.5
        hover "phone button.png"
        hotspot (185, 730, 57, 57) action [Hide("phone_screen"), Hide('stats_screen'), Hide('chat_screen'), Hide("stats_button"), Hide("market_button"), Hide("chat_button"), Hide("gallery_button"), Hide("phone_photos")]
screen stats_button:
    imagebutton:
        xalign 0.43
        yalign 0.24
        idle "stats.png"
        hover "stats big.png"
        action [Hide("phone_photos"), Hide("e_shop"), Hide('chat_screen'),  Show("stats_screen")]
screen market_button:
    imagebutton:
        xalign 0.4766
        yalign 0.24
        idle "market.png"
        hover "market big.png"
        action [Hide("phone_photos"), Hide('chat_screen'), Hide('stats_screen'), Show("e_shop")]
screen gallery_button:
    imagebutton:
        xalign 0.5222
        yalign 0.24
        idle "gallery small.png"
        hover "gallery.png"
        action [Hide('stats_screen'), Hide('chat_screen'), Show("phone_photos")]
screen chat_button:
    imagebutton:
        xalign 0.5688
        yalign 0.24
        idle "chat.png"
        hover "chat big.png"
        action [Show("chat_screen"),  Hide('stats_screen'), Hide("phone_photos")]
screen phone_photos:
    $ available_selfies = stadia1_selfie
    if mass >= 55:
        $ available_selfies = available_selfies + stadia2_selfie
    if mass >= 62:
        $ available_selfies = available_selfies + stadia3_selfie
    if mass >= 68:
        $ available_selfies = available_selfies + stadia4_selfie
    


    frame:
        align (.5, .6)
        xsize 300
        ysize 450
        vbox:
            viewport:
                xsize 300
                ysize 450
                yinitial 1.0
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 20
                    for i in reversed(range(0, len(available_selfies))):
                        $ selfie_image = available_selfies[i]
                        add selfie_image xalign 0.4 zoom .5

screen e_shop():
    modal True
    imagemap:
        ground "phonemarket" align (.5, .5)
        hover "phone button.png"
        hotspot (190, 735, 47, 47) action [Hide("phone_screen"), Hide('stats_screen'), Hide('chat_screen'), Hide("e_shop"), Hide("stats_button"), Hide("market_button"), Hide("chat_button"), Hide("gallery_button"), Hide("phone_photos")]
    if tape == False:
        imagebutton:
            align (.57, .29)
            idle "buyactive" 
            hover "buyactive2" 
            action [Hide("e_shop"), Hide("phone_screen"), Hide('chat_screen'), Hide("stats_button"), Hide("market_button"), Hide("chat_button"), Hide("gallery_button"), Hide("phone_photos"), Call("eshop.buy_tape", from_current=True)]
    if tape == True:
        imagebutton:
            align (.57, .29)
            idle "buynotactive"
            hover "buynotactive" 
            action NullAction()
    if scales == False:
        imagebutton:
            align (.57, .37)
            idle "buyactive" 
            hover "buyactive2" 
            action [Hide("e_shop"), Hide("phone_screen"), Hide("stats_button"), Hide('chat_screen'), Hide("market_button"), Hide("chat_button"), Hide("gallery_button"), Hide("phone_photos"), Call("eshop.buy_scales", from_current=True)]
    if scales == True:
        imagebutton:
            align (.57, .37)
            idle "buynotactive"
            hover "buynotactive" 
            action NullAction()
    if cam == False:
        imagebutton:
            align (.57, .45)
            idle "buyactive" 
            hover "buyactive2" 
            action [Hide("e_shop"), Hide("phone_screen"), Hide("stats_button"), Hide("market_button"), Hide("chat_button"), Hide("gallery_button"), Hide("phone_photos"), Hide('chat_screen'), Call("eshop.buy_cam", from_current=True)]
    if cam == True:
        imagebutton:
            align (.57, .45)
            idle "buynotactive"
            hover "buynotactive" 
            action NullAction()
screen stats_screen:
    frame:
        align(.5, .5)
        vbox: 
            if tape == True:
                $ measure =  94 + ((mass - 50) * 0.76) // 1
                $ measure = int(measure)
                text "Shoulders: [measure] cm"
                $ measure = 80 + ((mass - 50) * 0.88) // 1
                $ measure = int(measure)
                text "Chest: [measure] cm"
                $ measure = 60 + ((mass - 50) * 0.2) // 1
                $ measure = int(measure)
                text "Waist: [measure] cm"
                $ measure = 86 + ((mass - 50) * 0.84) // 1
                $ measure = int(measure)
                text "Buttocks: [measure] cm"
                $ measure = 50 + ((mass - 50) * 0.48) // 1
                $ measure = int(measure)
                text "Thighs: [measure] cm"
                $ measure = 34 + ((mass - 50) * 0.28) // 1
                $ measure = int(measure)
                text "Calves: [measure] cm"
                $ measure = 24 + ((mass - 50) * 0.48) // 1
                $ measure = int(measure)
                text "Biceps: [measure] cm"
                $ measure = 20 + ((mass - 50) * 0.36) // 1
                $ measure = int(measure)
                text "Forearms: [measure] cm"
            else:
                text "I need a measuring tape to measure myself. I should buy one..."
screen chat_screen():
    frame:
        align(.5, .53)
        viewport:
            xsize 300
            ysize 450
            yinitial 1.0
            #mousewheel True
            draggable True
            scrollbars "vertical"
            vbox:
                text "Anna: Hey, is this [name]?"
                text "[name]: Hello! Yes I'm [name], and I assume this is Anna?"
                text "Anna: Yep, you got that right. It was great meeting you! We should totally hang out some time!"
                text "[name]: That's a great idea! I'll let you know when I'm free so we can set something up!"
######################################
#Мои скрины###########################
######################################

######################################
#Мои функции##########################
######################################

python early:
    def eat(spend, eat_fill, health, hours):
        global fill, fill_max, time, money, time
        if fill >= fill_max:
            o = "I\'m stuffed! I probably shouldn't eat anymore right now..."
        elif money < spend:
            o = "I can't buy this, I\'m broke."
        elif time - hours < 1:
            o = "It's too late in the day to eat. I should wait until morning."
        else:
            time -= hours
            if time <= 0:
                o = "It's too late in the day to eat. I should wait until morning."
            else:
                o = "Yum, tasty and filling!" 
                if fill >= fill_max:
                    fill = fill_max
                else:
                    fill += eat_fill
                money -= spend
        if health + 1 > 20:
            health = 20
        return (fill, money, o, health)
    def spend_money(money, spend):
        if money < spend:
            o = "I can't buy this, I\'m broke."
            result = 0
        else:
            o = "Alright!"
            money -= spend
            result = 1
        return (o, money, result)
######################################
#Мои функции##########################
######################################


label start:

    Character('Disclaimer', color="#000") "This is a work of fiction. Names, characters, business, events and incidents are the products of the author's imagination. Any resemblance to actual persons, living or dead, or actual events is purely coincidental."

    Character('Disclaimer', color="#000") "All characters are adults!"
    scene black #чёрный фон

    "Are you really 18 years or older?"

    menu:
        "Yes!":
            jump intro # переход в главное меню

        "No...":
            $ renpy.quit() # выход из игры

label intro:
    show screen stats
    show screen time_text
    $ name = renpy.input('What is the main character\'s name?').strip()

    e "Hello, world. Nice to see you again."

    e "I'm just your run-of-the-mill college girl."

    e "Well, maybe I'm not so average. I don't really have any hobbies, nor do I get out very often. I mostly just stay in my room and study."

    e "It's kind of an obsession at this point. Sure, my grades are solid, but it has its downsides."
    
    e "I just turned 19. Suffice to say, my birthday was spent hitting the books. No real party to speak of."

    e "I think I'm decently cute and cuddly, but guys don't pay attention to me. Like I said, I don't get out much."

    e "Something has to change."
    
    e "I guess I just need to find something that interests me and plunge headlong into it..."

    e "Here's my room. Home sweet home."
    show bg room
label home:
    stop sound
    play music "Moar BGM.mp3"
    
    show screen stats
    show screen fill_status
    show screen fill_status_text 
    show screen stats_bar
    show screen stats_bar_text
    image icons = "icons.png"
    show icons
    show screen phone_button
    $ gym_go = False
label .home:
    if time < 5:
        scene bg room night
    else:
        scene bg room
label .home_menu:    
    menu home_menu:   
        "Look in the mirror":
            e "Let's see how I look."
            if mass <= 54:
                e "There I am, plain ol' me."
                show expression "gg1" as mc
            elif mass >= 55 and mass < 62:
                e "I feel like I have real muscles!"
                show expression "gg2" as mc
            elif mass >= 62 and mass < 68:
                e "It seems my muscles are bigger than before!"
                show expression "gg3" as mc    
            elif  mass >= 68:
                e "Looks like I\'m getting strong!"
                show expression "gg4" as mc    
            window hide
            pause
            window show
            hide mc
            jump home.home
        "Relax (1h)":
            if time <= 1:
                e "It\'s getting late, I should go to bed."
            else:
                $ time -= 1
                $ fill -= 1
                $ stamina += 2
                if stamina >= stamina_base:
                    $ stamina = stamina_base
                if fill <= 0:
                    $ health -= 1
                if health < 1:
                    e "I died. I should've paid more attention to my health. Game over."
                    return
            jump home.home
        "Eat (1h)":
            menu eat_home_menu:
                "Sandwich with turkey and cheese, 1$":
                    if fill < fill_max:
                        $ fill, money, answer, health = eat(1, 3, health, 1)
                        e "[answer]"
                    else:
                        e "I'm not hungry. No need to overeat."
                    jump eat_home_menu
                "Fried chicken with rice and vegetables, 2$" if mass >= 55:
                    if fill < fill_max:
                        $ fill, money, answer, health = eat(2, 5, health, 1)
                        e "[answer]"                 
                    else:
                        e "I'm not hungry. No need to overeat."
                    jump eat_home_menu
                "Lasagna, 3$"  if mass >= 62:
                    if fill < fill_max:
                        $fill, money, answer, health = eat(3, 7, health, 1)
                        e "[answer]"
                    else:
                        e "I'm not hungry. No need to overeat."
                    jump eat_home_menu
                "Back":    
                    jump home.home

        "Sleep (8h)":
            if time <= 1:            
                e "Good night, world. I'll see you in the morning!"
                if experience + 45 - mass >= 0:
                    $ mass += 1
                    $ experience = experience + 45 - mass + 1
                if mass >= 68:
                    $ mass = 68
                    "That's the end of the Demo! Thank you for playing! Please wait for the full version of the game."
                if exp_stam >= 5 + (stamina_base - 20):
                    $ stamina_base += 1
                    $ exp_stam_max = (stamina_base - 15)
                    $ exp_stam = exp_stam - exp_stam_max + 1
                $ stamina = stamina_base
                $ time = 17
                $ fill_max = 20 + mass - 50
                $ exg = 2
                $ wc_count = False
                $ gluttony = False
                $ adrenalin = False
                $ fill_level = 1 + (mass - 50) // 10
                $ fill -= 4
                if fill < 0:
                    $ health -= 1
                if health <= 0:
                    e "..or not. I died in my sleep. Game over."
                    return
                if dds == True:
                    $ exp_stam += 16
                    $ experience += 16
                    $ fill -= 32
                    $ dds = False
                $ week_count += 1
                if week_count == 7:
                    $ week_count = 0
                if fill > 0:
                    $ health += 4
                if health > 20:
                    $ health = 20
            else:
                e "It's too early to sleep just yet. There's plenty of day left!"
            jump home.home
        "Webcam (1h)" if cam == True and mass >= 55 and wc_count == False:
            if time >= 2:
                $ time -= 1
                $ wc_count = True
                $ money += (mass - 40) * 3
                e "How... unusual. Still, the money is too good to ignore..."
                jump home.home
            else:
                e "I don\'t have time to cam today."
                jump home.home
        "Go outside":
            jump street
label street():
    stop sound
    show icons
    play music "Destiny.mp3"
    jump street.street
    
    
label .street:
    if time > 4:
        scene bg street
    else:
        play sound "night.mp3"
        scene bg street night
    menu street_menu:
        "Gym":
            if time > 1:
                $ gym_go = True
                jump gym
            if time <= 1:
                e "It\'s late, I should head back home. I don't want to fall asleep mid-rep!"
                jump street.street
        "Cafe":
            jump cafe
        "Health+":
            jump health_plus
        "Jogging in the park (1h)":
            if time > 4:
                scene bg park
            else:
                scene bg park night
            pause
            if stamina > 3 and time > 1 and fill > 3 + fill_level // 3:
                if health <= 0:
                    e "I died. I should've paid more attention to my health. Game over."
                    return
                #e "Хорошо позанималась!"
                $ exp_stam += 1
                $ fill -= 2
                $ stamina -= 4
                $ time -= 1
                if gluttony == True:
                    $ experience += 1
                    $ fill -= 1
                
                jump street.street
            if (fill <= 2 + fill_level // 3) and stamina > 3:
                $ fill -= 2 + fill_level // 3
                e "I worked out, but now I\'m dizzy. I should eat something."
                $ time -= 1
                $ exp_stam += 1
                $ stamina -= 4
                if gluttony == True:
                    $ experience += 1
                    $ fill -= 1
                if fill <= 0:
                    $ health -= 1
                    jump street.street
                if health <= 0:
                    e "I died. I should've paid more attention to my health. Game over."
                    return
                jump street.street
            else:
                e "That was a nice jog. Time to head back."
                jump street.street
        "Come back home":
            jump home
label cafe():
    stop sound
    jump .cafe
label .cafe():
    $ clocks = 24 - time
    scene bg cafe
    show icons
    if cafe_text == False:
        '''
        The cafe is stylishly minimalist yet cozy. The delicate pastel shades on the walls, coupled with the homey and soft wooden furniture, create a comfortable and warm atmosphere. Huge windows flood the space with natural light.'''
        '''
        Along the walls are cozy sofas and tables with cushy chairs, ideal for relaxing and chatting. The floral arrangements and candles on the tables are also charming and romantic.'''
        $ cafe_text = True
    menu cafe_menu:           
        "Work (8h)" if clocks == 8:
            $ time -= 8
            $ money += 30 + (fill_level * 10) - 10
            $ fill -= 4
            if fill <= 0:
                $ health -= 4
            if health <= 0:
                e "I died. I should've paid more attention to my health. Game over."
                return
            e "Another shift spent making drinks and serving food."    
            jump cafe
        "Cheesecake, 4$":
            $ fill, money, answer, health = eat(4, 3, health, 0)
            e "[answer]"
            jump cafe_menu
                
        "Roll with chicken, 6$":
            $ fill, money, answer, health = eat(6, 5, health, 0)
            e "[answer]"
            jump cafe_menu

        "Bolognese pasta, 8$":
            $ fill, money, answer, health = eat(8, 7, health, 0)
            e "[answer]"
            jump cafe_menu

        "Double burger with fries, $10":
            $ fill, money, answer, health = eat(10, 9, health, 0)
            e "[answer]"
            jump cafe_menu
        "Greek salad, 6$":
            $ fill, money, answer, health = eat(6, 2, health + 1, 0)
            e "[answer]"
            jump cafe_menu
        "Back":
            jump street
label gym():
    stop sound
    play sound "gym.mp3"
    jump .gym
    label .gym:
        show screen stats
        scene bg gym
        show icons
        menu gym_menu:         
            "Exercise":
                menu train_menu:
                    "Strength training (1h)":
                        if time > 1 and fill > 2 + fill_level // 3 and stamina > 3:
                            if health <= 0:
                                e "I died. I should've paid more attention to my health. Game over."
                                return
                            #e "Тренировка была тяжёлой"  
                            $ time -= 1
                            $ experience += 1
                            $ fill -= 2 + fill_level // 3
                            $ stamina -= 4
                            if mass >= 76:
                                $ stamina -= 1
                            if fill <= 0:
                                $ health -= 1
                            if gluttony == True:
                                $ experience += 1
                                $ fill -= 1
                            jump train_menu
                        if (fill <= 2 + fill_level // 3) and stamina > 3:
                            $ time -= 1
                            $ fill -= 2 + fill_level // 3
                            $ experience += 1
                            $ stamina -= 4
                            e "I worked out, but now I\'m dizzy. I should eat something."
                            if gluttony == True:
                                $ experience += 1
                                $ fill -= 1
                            if fill <= 0:
                                $ health -= 1
                            jump train_menu

                        if health <= 0:
                            e "I died. I should've paid more attention to my health. Game over."
                            return
                            jump train_menu
                        else:
                            e "I don't feel good. I should go home and take it easy."
                            jump train_menu
                    "Personal training, $20 (1h)":
                        $ answer, money, result = spend_money(money, 20)
                        if result == 1:
                            if time > 1 and fill > 2 + fill_level // 3 and stamina > 3:

                                if health <= 0:
                                    e "I died. I should've paid more attention to my health. Game over."
                                    return
                                #e "Тренировка была тяжёлой"  
                                $ time -= 1
                                $ experience += 2
                                $ fill -= 2 + fill_level // 3
                                $ stamina -= 4
                                if fill <= 0:
                                    $ health -= 1
                                if gluttony == True:
                                    $ experience += 2
                                    $ fill -= 1
                                jump train_menu
                            if (fill <= 2 + fill_level // 3) and stamina > 3:
                                $ time -= 1
                                $ fill -= 2 + fill_level // 3
                                $ experience += 1
                                $ stamina -= 4
                                e "I worked out, but now I\'m dizzy. I should eat something."
                                if gluttony == True:
                                    $ experience += 1
                                    $ fill -= 1
                                if fill <= 0:
                                    $ health -= 1
                                jump train_menu

                            if health <= 0:
                                e "I died. I should've paid more attention to my health. Game over."
                                return
                                jump train_menu
                            else:
                                e "I don't feel good. I should go home and take it easy."
                                jump train_menu
                        else:
                            e "[answer]"
                            jump train_menu
                    "Cardio (1h)":
                        if stamina > 3 and time > 1 and fill > 3 + fill_level // 3:
                            if health <= 0:
                                e "I died. I should've paid more attention to my health. Game over."
                                return
                            #e "Хорошо позанималась!"
                            $ exp_stam += 1
                            $ fill -= 2
                            $ stamina -= 4
                            $ time -= 1
                            if gluttony == True:
                                $ experience += 1
                                $ fill -= 1
                            jump train_menu
                        
                        if (fill <= 2 + fill_level // 3) and stamina > 3:
                            $ fill -= 2 + fill_level // 3
                            e "I worked out, but now I\'m dizzy. I should eat something."
                            $ time -= 1
                            $ exp_stam += 1
                            $ stamina -= 4
                            if gluttony == True:
                                $ experience += 1
                                $ fill -= 1
                            if fill <= 0:
                                $ health -= 1
                                jump train_menu
                            if health <= 0:
                                e "I died. I should've paid more attention to my health. Game over"
                                return
                            jump train_menu
                        else:
                            e "Time to head home."
                            jump gym_menu
                    "Check strength maximums":
                        e "Let's see how much I can squat."
                        $ result = int(40 + ((mass - 50) * 5.6) // 1)
                        e "[result] kg!"
                        e "Now let's see how much I can bench press."
                        $ result = int( 20 + ((mass - 50) * 4) // 1)
                        e "[result] kg!"
                        e "How about about I see how much I can bicep curl?"
                        $ result = int(30 + ((mass - 50) * 1.4) // 1)
                        e "[result] kg!"
                        e "And now for my grip strength!"
                        $ result = int(40 + ((mass - 50) * 1.2) // 1)
                        e "[result] kg!"
                        jump gym_menu
                    "Back":
                        jump gym_menu
            "Relax (1h)":
                if time <= 1:
                    e "It\'s late, I should head back home."
                else:
                    $ time -= 1
                    $ stamina += 2
                    $ fill -= 1
                    if stamina >= stamina_base:
                        $ stamina = stamina_base
                    if fill <= 0:
                        $ health -= 1
                    if health < 1:
                        e "I died. I should've paid more attention to my health. Game over."
                        return
                jump gym_menu
            "Protein shake, $8":
                $ fill, money, answer, health = eat(8, 5, health, 0)
                jump gym_menu 
            "Go outside":
                jump street
label health_plus():
    play music "Otome90.mp3"
    jump .health_plus
label .health_plus:
    scene bg health plus
    
    menu health_plus_menu:     
        "Buy drugs":
            menu hp_preparates:
                "Drive, 30$":
                    "There's a luminous orange liquid in this test tube."
                    $ answer, money, result = spend_money(money, 30)
                    e "[answer]"
                    if result == 1:
                        $ stamina += 10
                        $ health -= 3
                    jump hp_preparates
                "Adrenaline X, $50" if adrenalin == False:
                    "The liquid in this flask seems potent but poisonous"
                    $ answer, money, result = spend_money(money, 30)
                    e "[answer]"
                    if result == 1:
                        $ stamina += 1000
                        $ health -= 10
                        $ adrenalin = True
                    jump hp_preparates
                "Gluttony, $80" if gluttony == False:
                    "This white tablet is huge! It looks like it's difficult to swallow."
                    $ answer, money, result = spend_money(money, 80)
                    e "[answer]"
                    if result == 1:
                        $ gluttony = True
                    jump hp_preparates
                "GCI (Growth Cells Injection), $100":
                    "This syringe holds a clear solution containing live growth cells."
                    $ answer, money, result = spend_money(money, 100)
                    e "[answer]"
                    if result == 1:
                        $ exp_stam += 10
                        $ experience += 10
                        $ fill -= 10
                    jump hp_preparates
                "DDs+ (deep dreams), $100" if dds == False:
                    "This a round candy is neatly packaged in a bright wrapper. It supposedly tastes like chocolate."
                    $ answer, money, result = spend_money(money, 100)
                    e "[answer]"
                    if result == 1:
                        $ dds = True
                    jump hp_preparates
                "Back":
                    jump health_plus_menu
        "Undergo a procedure":
            menu hp_procedures:
                "Restore health, $100":
                    $ answer, money, result = spend_money(money, 100)
                    if result == 1:
                        $ health = 20
                    e "[answer]"
                    jump hp_procedures
                "ExG procedure, $150" if exg > 0:
                    $ answer, money, result = spend_money(money, 150)
                    if result == 1:
                        $ experience += 10
                        $ exp_stam += 10
                        $ exg -= 2
                    e "[answer]"
                    jump hp_procedures
                "Back":
                    jump health_plus_menu
        "Go outside":
            jump street
label eshop:
label .buy_cam():
    $ answer , money, result = spend_money(money, 100)
    window hide
    show screen phone_screen
    show screen gallery_button
    show screen stats_button
    show screen market_button
    show screen chat_button
    show screen e_shop 
    if result == 1:
        $ cam = True
        pause
        e "[answer]"
        e "I bought a webcam. Maybe I can make some money with it."
        return
    else:
        pause
        e "[answer]"
        return
label .buy_scales():
    $ answer , money, result = spend_money(money, 30)
    window hide
    show screen phone_screen
    show screen gallery_button
    show screen stats_button
    show screen market_button
    show screen chat_button
    show screen e_shop 
    if result == 1:
        $ scales = True
        pause
        e "[answer]" 
        e "I bought a scale. I can measure my weight now."
        return
    else:
        pause
        e "[answer]"            
        return
label .buy_tape():
    $ answer , money, result = spend_money(money, 5)
    window hide
    show screen phone_screen
    show screen gallery_button
    show screen stats_button
    show screen market_button
    show screen chat_button
    show screen e_shop   
    if result == 1:
        $ tape = True
        pause
        e "[answer]" 
        e "I bought a measuring tape. I can measure myself now. That kind of goes without saying..." 
        return
    else:
        pause
        e "[answer]"
        return

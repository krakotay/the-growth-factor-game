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
                text "Thigh: [measure] cm"
                $ measure = 34 + ((mass - 50) * 0.28) // 1
                $ measure = int(measure)
                text "Calves: [measure] cm"
                $ measure = 24 + ((mass - 50) * 0.48) // 1
                $ measure = int(measure)
                text "Biceps: [measure] cm"
                $ measure = 20 + ((mass - 50) * 0.36) // 1
                $ measure = int(measure)
                text "Forearm: [measure] cm"
            else:
                text "I have no\n measure tape"
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
                text "Anna: Hello, how are you?"
                text "[name]: Hello, well, so-so. And what?"
                text "Anna: Oh how. And blow to me! I will be glad to meet you!"
                text "[name]: Great idea, I\'m on my way!"
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
            o = "I\'m already full"
        elif money < spend:
            o = "I have no money"
        elif time - hours < 1:
            o = "I don\'t have time to eat"
        else:
            time -= hours
            if time <= 0:
                o = "It\'s getting late, what\'s the food?"
            else:
                o = "Well ate!" 
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
            o = "I have no money"
            result = 0
        else:
            o = "Ready!"
            money -= spend
            result = 1
        return (o, money, result)
######################################
#Мои функции##########################
######################################


label start:

    Character('Disclaimer', color="#000") "All events are fictitious, all coincidences are random."

    Character('Disclaimer', color="#000") "All characters are adults!"
    scene black #чёрный фон

    "Are you really 18 years old?"

    menu:
        "Yes!":
            jump intro # переход в главное меню

        "No!":
            $ renpy.quit() # выход из игры

label intro:
    show screen stats
    show screen time_text
    $ name = renpy.input('What is the name of the main character?').strip()

    e "Who am I?"

    e "I\'m a girl who just turned 19"

    e "I don\'t have any particular hobbies because I\'m obsessed with studying."

    e "My appearance may be cute and cuddly, but I\'m not that popular with guys because of my introversion."

    e "If any area interests me, I\'m ready to plunge headlong"
    e "Here is my room"
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
        "look in the mirror":
            e "This is how I look"
            if mass <= 54:
                show expression "gg1" as mc
            elif mass >= 55 and mass < 62:
                e "I feel like I have muscles!"
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
                e "It\'s getting late, gotta go to bed"
            else:
                $ time -= 1
                $ fill -= 1
                $ stamina += 2
                if stamina >= stamina_base:
                    $ stamina = stamina_base
                if fill <= 0:
                    $ health -= 1
                if health < 1:
                    e "I died. End of the game"
                    return
            jump home.home
        "Eat (1h)":
            menu eat_home_menu:
                "Sandwich with turkey and cheese 1$":
                    $ fill, money, answer, health = eat(1, 3, health, 1)
                    e "[answer]"
                    jump eat_home_menu
                "Fried chicken with rice and vegetables 2$" if mass >= 55:
                    if fill < fill_max:
                        $ fill, money, answer, health = eat(2, 5, health, 1)
                        e "[answer]"                 
                    else:
                        e "I am not hungry"
                    jump eat_home_menu
                "Lasagna 3$"  if mass >= 62:
                    if fill < fill_max:
                        $fill, money, answer, health = eat(3, 7, health, 1)
                        e "[answer]"
                    else:
                        e "I am not hungry"
                    jump eat_home_menu
                "Back":    
                    jump home.home

        "Sleep (8h)":
            if time <= 1:            
                e "I slept and feel great"
                if experience + 45 - mass >= 0:
                    $ mass += 1
                    $ experience = experience + 45 - mass + 1
                if mass >= 68:
                    $ mass = 68
                    'Demo version is finished. Please wait for the full version of the game'
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
                    e "I died in my sleep"
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
                e "Too early to sleep"
            jump home.home
        "Webcam (1h)" if cam == True and mass >= 55 and wc_count == False:
            if time >= 2:
                $ time -= 1
                $ wc_count = True
                $ money += (mass - 40) * 3
                e "How... unusual"
                jump home.home
            else:
                e "I don\'t have time for webcam today"
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
                e "It\'s late, what rocking?"
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
                    e "I died. Game over"
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
                e "I worked out, but I\'m too hungry and I\'m dizzy"
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
                    e "I died. Game over"
                    return
                jump street.street
            else:
                e "Gotta go home"
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
        The interior of the cafe combines stylish minimalism with a cozy atmosphere. Delicate pastel shades on the walls create calmness, and soft wooden furniture gives warmth and comfort. Huge windows fill the room with light.'''
        '''
        Along the walls are cozy sofas and tables with soft chairs, ideal for relaxing and chatting. On the tables, floral arrangements and candles create a romantic atmosphere and add charm.'''
        $ cafe_text = True
    menu cafe_menu:           
        "Work (8h)" if clocks == 8:
            $ time -= 8
            $ money += 30 + (fill_level * 10) - 10
            $ fill -= 4
            if fill <= 0:
                $ health -= 4
            if health <= 0:
                e "I died. Game over"
                return
            jump cafe
        "Cheesecake 4$":
            $ fill, money, answer, health = eat(4, 3, health, 0)
            e "[answer]"
            jump cafe_menu
                
        "Roll with chicken 6$":
            $ fill, money, answer, health = eat(6, 5, health, 0)
            e "[answer]"
            jump cafe_menu

        "Bolognese pasta 8$":
            $ fill, money, answer, health = eat(8, 7, health, 0)
            e "[answer]"
            jump cafe_menu

        "Double burger with fries $10":
            $ fill, money, answer, health = eat(10, 9, health, 0)
            e "[answer]"
            jump cafe_menu
        "Greek salad 6$":
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
            "exercise":
                menu train_menu:
                    "Strength training (1h)":
                        if time > 1 and fill > 2 + fill_level // 3 and stamina > 3:
                            if health <= 0:
                                e "I died. Game over"
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
                            e "I worked out, but I\'m too hungry and I\'m dizzy"
                            if gluttony == True:
                                $ experience += 1
                                $ fill -= 1
                            if fill <= 0:
                                $ health -= 1
                            jump train_menu

                        if health <= 0:
                            e "I died. Game over"
                            return
                            jump train_menu
                        else:
                            e "Something is wrong with me. Gotta go home"
                            jump train_menu
                    "Personal training, $20 (1h)":
                        $ answer, money, result = spend_money(money, 20)
                        if result == 1:
                            if time > 1 and fill > 2 + fill_level // 3 and stamina > 3:

                                if health <= 0:
                                    e "I died. Game over"
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
                                e "I worked out, but I\'m too hungry and I\'m dizzy"
                                if gluttony == True:
                                    $ experience += 1
                                    $ fill -= 1
                                if fill <= 0:
                                    $ health -= 1
                                jump train_menu

                            if health <= 0:
                                e "I died. Game over"
                                return
                                jump train_menu
                            else:
                                e "Something is wrong with me. Gotta go home"
                                jump train_menu
                        else:
                            e "[answer]"
                            jump train_menu
                    "Cardio (1h)":
                        if stamina > 3 and time > 1 and fill > 3 + fill_level // 3:
                            if health <= 0:
                                e "I died. Game over"
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
                            e "I worked out, but I\'m too hungry and I\'m dizzy"
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
                                e "I died. Game over"
                                return
                            jump train_menu
                        else:
                            e "Gotta go home"
                            jump gym_menu
                    "Check strength indicators":
                        e "I\'ll try to squat with a barbell"
                        $ result = int(40 + ((mass - 50) * 5.6) // 1)
                        e "[result] kg!"
                        e "I\'ll try to lift the barbell lying down"
                        $ result = int( 20 + ((mass - 50) * 4) // 1)
                        e "[result] kg!"
                        e "I\'m trying to lift the bar for biceps"
                        $ result = int(30 + ((mass - 50) * 1.4) // 1)
                        e "[result] kg!"
                        e "I\'ll try dynamometry"
                        $ result = int(40 + ((mass - 50) * 1.2) // 1)
                        e "[result] kg!"
                        jump gym_menu
                    "Back":
                        jump gym_menu
            "Relax (1h)":
                if time <= 1:
                    e "It\'s getting late, gotta go to bed"
                else:
                    $ time -= 1
                    $ stamina += 2
                    $ fill -= 1
                    if stamina >= stamina_base:
                        $ stamina = stamina_base
                    if fill <= 0:
                        $ health -= 1
                    if health < 1:
                        e "I died. End of the game"
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
                    "This is a transparent test tube with an orange luminous liquid."
                    $ answer, money, result = spend_money(money, 30)
                    e "[answer]"
                    if result == 1:
                        $ stamina += 10
                        $ health -= 3
                    jump hp_preparates
                "Adrenaline X, $50" if adrenalin == False:
                    "This is a flask with a poisonous liquid"
                    $ answer, money, result = spend_money(money, 30)
                    e "[answer]"
                    if result == 1:
                        $ stamina += 1000
                        $ health -= 10
                        $ adrenalin = True
                    jump hp_preparates
                "Gluttony, $80" if gluttony == False:
                    "It is a large white tablet that is difficult to swallow due to its size."
                    $ answer, money, result = spend_money(money, 80)
                    e "[answer]"
                    if result == 1:
                        $ gluttony = True
                    jump hp_preparates
                "GCI (Growth cells injection), $100":
                    "This is a syringe with a clear solution containing live growth cells."
                    $ answer, money, result = spend_money(money, 100)
                    e "[answer]"
                    if result == 1:
                        $ exp_stam += 10
                        $ experience += 10
                        $ fill -= 10
                    jump hp_preparates
                "DDs+ (deep dreams), $100" if dds == False:
                    "This is a round candy in a bright wrapper that tastes like chocolate."
                    $ answer, money, result = spend_money(money, 100)
                    e "[answer]"
                    if result == 1:
                        $ dds = True
                    jump hp_preparates
                "Back":
                    jump health_plus_menu
        "Go through the procedure":
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
        e "I bought a webcam. I hope I can make money with it."
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
        e "I bought scales. Now I can measure my weight."
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
        e "I bought a measuring tape. Now I can measure myself." 
        return
    else:
        pause
        e "[answer]"
        return

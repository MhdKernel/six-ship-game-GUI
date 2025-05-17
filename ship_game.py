from tkinter import *
from PIL import ImageTk , Image
from playsound import playsound

#-------------------Root------------------------

root = Tk()
root.title('Ship Game')
root.geometry('700x700')
root.iconbitmap('images/ship_games_ico.ico')
root.resizable(width=False , height=False)

#-----------------Frames------------------------

black_frames_dic ={'bg' : 'red' , 'heigh' : 100 , 'width' : 100 , 'bd' : 3 , 'relief' : 'solid'}
frames_dic ={'bg' : 'white' , 'heigh' : 100 , 'width' : 100  , 'bd' : 3 , 'relief' : 'solid'}
winner_1_dic = {'bg' : 'cyan' , 'heigh' : 100 , 'width' : 100  , 'bd' : 3 , 'relief' : 'solid'}
winner_2_dic = {'bg' : 'green' , 'heigh' : 100 , 'width' : 100  , 'bd' : 3 , 'relief' : 'solid'}


main_fram = Frame(root , bg = 'black' , height=700 , width=700)
frame1 = Frame(root , black_frames_dic)    
frame5 = Frame(root , black_frames_dic)
frame21 = Frame(root , black_frames_dic)    
frame25 = Frame(root , black_frames_dic)
frame2 = Frame(root , frames_dic)
frame3 = Frame(root , frames_dic)
frame4 = Frame(root , frames_dic)
frame6 = Frame(root , frames_dic)
frame7 = Frame(root , frames_dic)
frame8 = Frame(root , frames_dic)
frame9 = Frame(root , frames_dic)
frame10 = Frame(root , winner_1_dic)
frame11 = Frame(root , frames_dic)
frame12 = Frame(root , frames_dic)
frame13= Frame(root , frames_dic)
frame14 = Frame(root , frames_dic)
frame15 = Frame(root , winner_1_dic)
frame16 = Frame(root , frames_dic)
frame17 = Frame(root , frames_dic)
frame18 = Frame(root , frames_dic)
frame19 = Frame(root , frames_dic)
frame20 = Frame(root , winner_1_dic)
frame22 = Frame(root , winner_2_dic)
frame23= Frame(root , winner_2_dic)
frame24 = Frame(root , winner_2_dic)

main_fram.place(x=0 , y=0)
frame1.place(x=100 , y=100)
frame5.place(x=500 , y=100)
frame21.place(x=100 , y=500)
frame25.place(x=500 , y=500)
frame2.place(x = 200 , y = 100)
frame3.place(x = 300 , y = 100)
frame4.place(x = 400 , y = 100)
frame6.place(x = 100 , y = 200)
frame7.place(x = 200 , y = 200)
frame8.place(x = 300 , y = 200)
frame9.place(x = 400 , y = 200)
frame10.place(x = 500 , y = 200)
frame11.place(x = 100 , y = 300)
frame12.place(x = 200 , y = 300)
frame13.place(x = 300 , y = 300)
frame14.place(x = 400 , y = 300)
frame15.place(x = 500 , y = 300)
frame16.place(x = 100 , y = 400)
frame17.place(x = 200 , y = 400)
frame18.place(x = 300 , y = 400)
frame19.place(x = 400 , y = 400)
frame20.place(x = 500 , y = 400)
frame22.place(x = 200 , y = 500)
frame23.place(x = 300 , y = 500)
frame24.place(x = 400 , y = 500)

win_frame = Frame(root , bg = 'black' , height=100 , width=700)
win_frame.place(x=0 , y=600)
player11_start_fram = Frame(root , bg = 'black' , height=100 , width=100)
player11_start_fram.place(x=0 , y=200)
player12_start_fram = Frame(root , bg = 'black' , height=100 , width=100)
player12_start_fram.place(x=0 , y=300)
player13_start_fram = Frame(root , bg = 'black' , height=100 , width=100)
player13_start_fram.place(x=0 , y=400)
player21_start_fram = Frame(root , bg = 'black' , height=100 , width=100)
player21_start_fram.place(x=200 , y=0)
player22_start_fram = Frame(root , bg = 'black' , height=100 , width=100)
player22_start_fram.place(x=300 , y=0)
player23_start_fram = Frame(root , bg = 'black' , height=100 , width=100)
player23_start_fram.place(x=400 , y=0)

#------------------Images----------------------

ship1_img = ImageTk.PhotoImage(Image.open('images/ship_1.jpg'))
ship2_img = ImageTk.PhotoImage(Image.open('images/ship_2.jpg'))
start_button_img = ImageTk.PhotoImage(Image.open('images/start.jpg'))
player_11_img = ImageTk.PhotoImage(Image.open('images/player_11.jpg'))
player_12_img = ImageTk.PhotoImage(Image.open('images/player_12.jpg'))
player_13_img = ImageTk.PhotoImage(Image.open('images/player_13.jpg'))
player_21_img = ImageTk.PhotoImage(Image.open('images/player_21.jpg'))
player_22_img = ImageTk.PhotoImage(Image.open('images/player_22.jpg'))
player_23_img = ImageTk.PhotoImage(Image.open('images/player_23.jpg'))

#------------------Lists-----------------------

player1_list = [[frame6 , frame7 , frame8 ,frame9 , frame10] , [frame11 , frame12 , frame13 , frame14 , frame15] , [frame16 , frame17 , frame18 , frame19 , frame20]]
player2_list = [[frame2 , frame7 , frame12 , frame17 , frame22] , [frame3 , frame8 , frame13 , frame18 , frame23] , [frame4 , frame9 , frame14 , frame19 ,frame24]]
list1 = [0 , 0 , 0]
list2 = [0 , 0 , 0]

#------------------Ships------------------------

ship1_1 = Button( frame6 , image=ship1_img , command= lambda : player1(1))     
ship1_2 = Button(frame11 , image=ship1_img , command= lambda : player1(2)) 
ship1_3 = Button(frame16 , image=ship1_img , command= lambda : player1(3)) 
ship1_1.place(x=25 , y=25)
ship1_2.place(x=25 , y=25)
ship1_3.place(x=25 , y=25)
ship2_1 = Button(frame2 , image=ship2_img , command= lambda : player2(1)) 
ship2_2 = Button(frame3 , image=ship2_img , command= lambda : player2(2)) 
ship2_3 = Button(frame4 , image=ship2_img , command= lambda : player2(3)) 
ship2_1.place(x=25 , y=25)
ship2_2.place(x=25 , y=25)
ship2_3.place(x=25 , y=25)

#----------------Functions----------------------

def players_turn(turnnn):
    global can_11 , can_12 , can_13 , can_21 , can_22 , can_23
    if turnnn == 1:
        can_11 = Button(player11_start_fram , image = player_11_img)
        can_12 = Button(player12_start_fram , image = player_12_img)
        can_13 = Button(player13_start_fram , image = player_13_img)
        can_11.place(x=0,y=0)
        can_12.place(x=0,y=0)
        can_13.place(x=0,y=0)
    elif turnnn == 2:
        can_21 = Button(player21_start_fram , image = player_21_img)
        can_22 = Button(player22_start_fram , image = player_22_img)
        can_23 = Button(player23_start_fram , image = player_23_img)
        can_21.place(x=0,y=0)
        can_22.place(x=0,y=0)
        can_23.place(x=0,y=0)
        
def player1(player_p):
    playsound('musics/2.mp3')

def player2(player_p):
    playsound('musics/3.mp3')
    
def check_ship_existence(fram):
    global code 
    buttons = fram.winfo_children()
    for button in buttons:
        if isinstance(button, Button):
            return True
    return False

def check_ship_existence_img(frame, button_image):
    buttons = frame.winfo_children()
    for button in buttons:
        if isinstance(button, Button) and button.cget('image') == button_image:
            return True
    return False

def loosing_turn():
    global code , player_1 , player_2
    if play == 1:
        if player_1 == 1:
            if check_ship_existence(frame15) == True and check_ship_existence(frame20) == True:
                if check_ship_existence_img(frame6 , 'pyimage1') == True and check_ship_existence_img(frame7 , 'pyimage2') == True and check_ship_existence_img(frame8 , 'pyimage2') == True:
                    code = 4
                elif check_ship_existence_img(frame7 , 'pyimage1') == True and check_ship_existence_img(frame8 , 'pyimage2') == True and check_ship_existence_img(frame9 , 'pyimage2') == True:
                    code = 4
                else:
                    ending_error()
            else:
                ending_error()
        elif player_1 == 2:
            if check_ship_existence(frame10) == True and check_ship_existence(frame20) == True:
                if check_ship_existence_img(frame11 , 'pyimage1') == True and check_ship_existence_img(frame12 , 'pyimage2') == True and check_ship_existence_img(frame13 , 'pyimage2') == True:
                    code = 4
                elif check_ship_existence_img(frame12 , 'pyimage1') == True and check_ship_existence_img(frame13 , 'pyimage2') == True and check_ship_existence_img(frame14 , 'pyimage2') == True:
                    code = 4
                else:
                    ending_error()
            else:
                ending_error()
        elif player_1 == 3:
            if check_ship_existence(frame10) == True and check_ship_existence(frame15) == True:
                if check_ship_existence_img(frame16 , 'pyimage1') == True and check_ship_existence_img(frame17 , 'pyimage2') == True and check_ship_existence_img(frame18 , 'pyimage2') == True:
                    code = 4
                elif check_ship_existence_img(frame17 , 'pyimage1') == True and check_ship_existence_img(frame18 , 'pyimage2') == True and check_ship_existence_img(frame19 , 'pyimage2') == True:
                    code = 4
                else:
                    ending_error()
            else:
                ending_error()
        else:
            ending_error()
    elif play == 2:
        if player_2 == 1:
            if check_ship_existence(frame23) == True and check_ship_existence(frame24) == True:
                if check_ship_existence_img(frame2 , 'pyimage2') == True and check_ship_existence_img(frame7 , 'pyimage1') == True and check_ship_existence_img(frame12 , 'pyimage1') == True:
                    code = 4
                elif check_ship_existence_img(frame7 , 'pyimage2') == True and check_ship_existence_img(frame12 , 'pyimage1') == True and check_ship_existence_img(frame17 , 'pyimage1') == True:
                    code = 4
                else:
                    ending_error()
            else:
                ending_error()
        elif player_2 == 2:
            if check_ship_existence(frame22) == True and check_ship_existence(frame24) == True:
                if check_ship_existence_img(frame3 , 'pyimage2') == True and check_ship_existence_img(frame8 , 'pyimage1') == True and check_ship_existence_img(frame13 , 'pyimage1') == True:
                    code = 4
                elif check_ship_existence_img(frame8 , 'pyimage2') == True and check_ship_existence_img(frame13 , 'pyimage1') == True and check_ship_existence_img(frame18 , 'pyimage') == True:
                    code = 4
                else:
                    ending_error()
            else:
                ending_error()
        elif player_2 == 3:
            if check_ship_existence(frame22) == True and check_ship_existence(frame23) == True:
                if check_ship_existence_img(frame4 , 'pyimage2') == True and check_ship_existence_img(frame9 , 'pyimage1') == True and check_ship_existence_img(frame14 , 'pyimage1') == True:
                    code = 4
                elif check_ship_existence_img(frame9 , 'pyimage2') == True and check_ship_existence_img(frame14 , 'pyimage1') == True and check_ship_existence_img(frame19 , 'pyimage1') == True:
                    code = 4
                else:
                    ending_error()
            else:
                ending_error()
        else:
            ending_error()
            
def ending_error():
    global code , player_1 , player_2           
    if play == 1:
        if player_1 == 1:
            if check_ship_existence(frame10) == True:
                code = 3
            else:
                valid_moves()
        elif player_1 == 2:
            if check_ship_existence(frame15) == True:
                code = 3
            else:
                valid_moves()
        elif player_1 == 3:
            if check_ship_existence(frame20) == True:
                code = 3
            else:
                valid_moves()
        else:
            code = 3
    elif play == 2:
        if player_2 == 1:
            if check_ship_existence(frame22) == True:
                code = 3
            else:
                valid_moves()
        elif player_2 == 2:
            if check_ship_existence(frame23) == True:
                code = 3
            else:
                valid_moves()
        elif player_2 == 3:
            if check_ship_existence(frame24) == True:
                code = 3
            else:
                valid_moves()
        else:
            code = 3

def where_am_i():
    global turn , player_1 , player_2
    if play == 1:
        if player_1 == 1:
            for index , i in enumerate(player1_list[0]):
                if check_ship_existence_img(i , 'pyimage1') == True:
                    turn = index
                    break
        elif player_1 == 2:
            for index , i in enumerate(player1_list[1]):
                if check_ship_existence_img(i , 'pyimage1') == True:
                    turn = index
                    break
        elif player_1 == 3:
            for index , i in enumerate(player1_list[2]):
                if check_ship_existence_img(i , 'pyimage1') == True:
                    turn = index
                    break
    elif play == 2:
        if player_2 == 1:
            for index , i in enumerate(player2_list[0]):
                if check_ship_existence_img(i , 'pyimage2') == True:
                    turn = index
                    break
        elif player_2 == 2:
            for index , i in enumerate(player2_list[1]):
                if check_ship_existence_img(i , 'pyimage2') == True:
                    turn = index
                    break
        elif player_2 == 3:
            for index , i in enumerate(player2_list[2]):
                if check_ship_existence_img(i , 'pyimage2') == True:
                    turn = index
                    break
        
def valid_moves():
    global code , player_1 , player_2
    if play == 1:
        if player_1 == 1:
            where_am_i()
            if turn == 3:
                code = 1
            elif check_ship_existence(player1_list[0][turn+1]) == False and check_ship_existence(player1_list[0][turn+2]) == False:
                code = 1
            elif check_ship_existence(player1_list[0][turn+1]) == False and check_ship_existence(player1_list[0][turn+2]) == True:
                code = 1
            elif check_ship_existence(player1_list[0][turn+1]) == True and check_ship_existence(player1_list[0][turn+2]) == False:
                code = 2
            elif check_ship_existence(player1_list[0][turn+1]) == True and check_ship_existence(player1_list[0][turn+2]) == True:
                code = 3
        elif player_1 == 2:
            where_am_i()
            if turn == 3:
                code = 1
            elif check_ship_existence(player1_list[1][turn+1]) == False and check_ship_existence(player1_list[1][turn+2]) == False:
                code = 1
            elif check_ship_existence(player1_list[1][turn+1]) == False and check_ship_existence(player1_list[1][turn+2]) == True:
                code = 1
            elif check_ship_existence(player1_list[1][turn+1]) == True and check_ship_existence(player1_list[1][turn+2]) == False:
                code = 2
            elif check_ship_existence(player1_list[1][turn+1]) == True and check_ship_existence(player1_list[1][turn+2]) == True:
                code = 3
        elif player_1 == 3:
            where_am_i()
            if turn == 3:
                code = 1
            elif check_ship_existence(player1_list[2][turn+1]) == False and check_ship_existence(player1_list[2][turn+2]) == False:
                code = 1
            elif check_ship_existence(player1_list[2][turn+1]) == False and check_ship_existence(player1_list[2][turn+2]) == True:
                code = 1
            elif check_ship_existence(player1_list[2][turn+1]) == True and check_ship_existence(player1_list[2][turn+2]) == False:
                code = 2
            elif check_ship_existence(player1_list[2][turn+1]) == True and check_ship_existence(player1_list[2][turn+2]) == True:
                code = 3
    elif play == 2:
        if player_2 == 1:
            where_am_i()
            if turn == 3:
                code = 1
            elif check_ship_existence(player2_list[0][turn+1]) == False and check_ship_existence(player2_list[0][turn+2]) == False:
                code = 1
            elif check_ship_existence(player2_list[0][turn+1]) == False and check_ship_existence(player2_list[0][turn+2]) == True:
                code = 1
            elif check_ship_existence(player2_list[0][turn+1]) == True and check_ship_existence(player2_list[0][turn+2]) == False:
                code = 2
            elif check_ship_existence(player2_list[0][turn+1]) == True and check_ship_existence(player2_list[0][turn+2]) == True:
                code = 3
        elif player_2 == 2:
            where_am_i()
            if turn == 3:
                code = 1
            elif check_ship_existence(player2_list[1][turn+1]) == False and check_ship_existence(player2_list[1][turn+2]) == False:
                code = 1
            elif check_ship_existence(player2_list[1][turn+1]) == False and check_ship_existence(player2_list[1][turn+2]) == True:
                code = 1
            elif check_ship_existence(player2_list[1][turn+1]) == True and check_ship_existence(player2_list[1][turn+2]) == False:
                code = 2
            elif check_ship_existence(player2_list[1][turn+1]) == True and check_ship_existence(player2_list[1][turn+2]) == True:
                code = 3
        elif player_2 == 3:
            where_am_i()
            if turn == 3:
                code = 1
            elif check_ship_existence(player2_list[2][turn+1]) == False and check_ship_existence(player2_list[2][turn+2]) == False:
                code = 1
            elif check_ship_existence(player2_list[2][turn+1]) == False and check_ship_existence(player2_list[2][turn+2]) == True:
                code = 1
            elif check_ship_existence(player2_list[2][turn+1]) == True and check_ship_existence(player2_list[2][turn+2]) == False:
                code = 2
            elif check_ship_existence(player2_list[2][turn+1]) == True and check_ship_existence(player2_list[2][turn+2]) == True:
                code = 3

def moves():
    global ship1_1 , ship1_2 , ship1_3 , ship2_1 , ship2_2 , ship2_3 , player_1 , player_2
    if play == 1 and code == 1:
        if player_1 == 1:
            counter_1 = list1[0]
            ship1_1.destroy()
            ship1_1 = Button( player1_list[0][counter_1 + 1] , image=ship1_img , command= lambda : player1(1))
            ship1_1.place(x=25 , y=25)
            counter_1 += 1 
            list1[0] = counter_1
        elif player_1 == 2:
            counter_2 = list1[1]
            ship1_2.destroy()
            ship1_2 = Button( player1_list[1][counter_2 + 1] , image=ship1_img , command= lambda : player1(2))
            ship1_2.place(x=25 , y=25)
            counter_2 += 1 
            list1[1] = counter_2
        elif player_1 == 3:
            counter_3 = list1[2]
            ship1_3.destroy()
            ship1_3 = Button( player1_list[2][counter_3 + 1] , image=ship1_img , command= lambda : player1(3))
            ship1_3.place(x=25 , y=25)
            counter_3 += 1 
            list1[2] = counter_3
    elif play == 1 and code == 2:
        if player_1 == 1:
            counter_1 = list1[0]
            ship1_1.destroy()
            ship1_1 = Button( player1_list[0][counter_1 + 2] , image=ship1_img , command= lambda : player1(1))
            ship1_1.place(x=25 , y=25)
            counter_1 += 2
            list1[0] = counter_1
        elif player_1 == 2:
            counter_2 = list1[1]
            ship1_2.destroy()
            ship1_2 = Button( player1_list[1][counter_2 + 2] , image=ship1_img , command= lambda : player1(2))
            ship1_2.place(x=25 , y=25)
            counter_2 += 2
            list1[1] = counter_2
        elif player_1 == 3:
            counter_3 = list1[2]
            ship1_3.destroy()
            ship1_3 = Button( player1_list[2][counter_3 + 2] , image=ship1_img , command= lambda : player1(3))
            ship1_3.place(x=25 , y=25)
            counter_3 += 2
            list1[2] = counter_3 
       
    elif play == 2 and code == 1:
        if player_2 == 1:
            counter_21 = list2[0]
            ship2_1.destroy()
            ship2_1 = Button(player2_list[0][counter_21 + 1] , image=ship2_img , command= lambda : player2(1)) 
            ship2_1.place(x=25 , y=25)
            counter_21 += 1 
            list2[0] = counter_21  
        elif player_2 == 2:
            counter_22 = list2[1]
            ship2_2.destroy()
            ship2_2 = Button(player2_list[1][counter_22 + 1] , image=ship2_img , command= lambda : player2(2)) 
            ship2_2.place(x=25 , y=25)
            counter_22 += 1 
            list2[1] = counter_22
        elif player_2 == 3:
            counter_23 = list2[2]
            ship2_3.destroy()
            ship2_3 = Button(player2_list[2][counter_23 + 1] , image=ship2_img , command= lambda : player2(3)) 
            ship2_3.place(x=25 , y=25)
            counter_23 += 1 
            list2[2] = counter_23
    elif play == 2 and code == 2:
        if player_2 == 1:
            counter_21 = list2[0]
            ship2_1.destroy()
            ship2_1 = Button(player2_list[0][counter_21 + 2] , image=ship2_img , command= lambda : player2(1)) 
            ship2_1.place(x=25 , y=25)
            counter_21 += 2
            list2[0] = counter_21  
        elif player_2 == 2:
            counter_22 = list2[1]
            ship2_2.destroy()
            ship2_2 = Button(player2_list[1][counter_22 + 2] , image=ship2_img , command= lambda : player2(2)) 
            ship2_2.place(x=25 , y=25)
            counter_22 += 2
            list2[1] = counter_22
        elif player_2 == 3:
            counter_23 = list2[2]
            ship2_3.destroy()
            ship2_3 = Button(player2_list[2][counter_23 + 2] , image=ship2_img , command= lambda : player2(3)) 
            ship2_3.place(x=25 , y=25)
            counter_23 += 2
            list2[2] = counter_23

def winning():
    global winning_code
    if check_ship_existence(frame10) == True and check_ship_existence(frame15) == True and check_ship_existence(frame20) == True:
        winning_code = 1
    elif check_ship_existence(frame22) == True and check_ship_existence(frame23) == True and check_ship_existence(frame24) == True:
        winning_code = 2
    else:
        winning_code = 0


def banners(icode):
    global win1image , win2image , invm_image , legm_image
    if icode == 1:
        root_1 = Toplevel()
        root_1.geometry('700x434')
        win1image = ImageTk.PhotoImage(Image.open('images/win_1.jpg'))
        root_1.title('Player 1 Win')
        win_1_can = Button(root_1 , image= win1image)
        win_1_can.place(x=0 , y=0)
        root_1.after(5000 , lambda:root_1.destroy())
        root.after(5000 , lambda : root.destroy())
    elif icode == 2:
        root_2 = Toplevel()
        root_2.geometry('700x434')
        win2image = ImageTk.PhotoImage(Image.open('images/win_2.jpg'))
        root_2.title('Player 2 Win')
        win_2_can = Button(root_2 , image= win2image)
        win_2_can.place(x=0 , y=0)
        root_2.after(5000 , lambda:root_2.destroy())
        root.after(5000 , lambda : root.destroy())
    elif icode == 3:
        root_3 = Toplevel()
        root_3.geometry('700x574')
        invm_image = ImageTk.PhotoImage(Image.open('images/inv_move.jpg'))
        root_3.title('invalid move')
        inv_move_can = Button(root_3 , image= invm_image)
        inv_move_can.place(x=0 , y=0)
        root_3.after(750 , lambda:root_3.destroy())
    elif icode == 4:
        root_3 = Toplevel()
        root_3.geometry('700x393')
        legm_image = ImageTk.PhotoImage(Image.open('images/leg_move.jpg'))
        root_3.title('legal move')
        inv_move_can = Button(root_3 , image= legm_image)
        inv_move_can.place(x=0 , y=0)
        root_3.after(750 , lambda:root_3.destroy())

def start_game():
    global play , start_button
    play = 1
    enter_1.config(state='normal')
    enter_2.config(state='disabled')
    players_turn(1)
    start_button.destroy()
    start_button = Button(win_frame, text='Start Game', image=start_button_img)
    start_button.place(x=280, y=25)
    playsound('musics/1.wav')
    
def next_turn():
    global player_1, player_2, enter_1, enter_2
    global play
    if play == 1:
        players_turn(2)
        entered_value = enter_1.get()
        if not entered_value.isdigit():
            banners(3)
            return

        player_1 = int(entered_value)
        enter_1.config(state='disabled')
        enter_2.config(state='normal')
        loosing_turn()
        if code == 1 or code == 2:
            moves()
        elif code == 4:
            banners(4)
        elif code == 3:
            banners(3)
            enter_1.config(state='normal')
            enter_2.config(state='disabled')
            return 
        else:
            banners(3)
        winning()
        if winning_code == 1 or winning_code == 2:
            banners(winning_code)
            return

        play = 2
    elif play == 2:
        entered_value = enter_2.get()
        if not entered_value.isdigit():
            banners(3)
            return

        player_2 = int(entered_value)
        enter_2.config(state='disabled')
        enter_1.config(state='normal')
        loosing_turn()
        if code == 1 or code == 2:
            moves()
        elif code == 4:
            banners(4)
        elif code == 3:
            banners(3)
            enter_2.config(state='normal')
            enter_1.config(state='disabled')
            return
        else:
            banners(3)
        winning()
        if winning_code == 1 or winning_code == 2:
            banners(winning_code)
            return
        play = 1 
        
#-------------------Main-------------------------

enter_1 = Entry(win_frame , font=5, relief='solid', bg='yellow', state='disabled')
enter_1.place(x=25, y=25)

enter_2 = Entry(win_frame, font=3, relief='solid', bg='orange', state='disabled')
enter_2.place(x=375, y=25)

player_1_label = Label(win_frame , text='Player 1' , font=5 , bg='cyan')
player_1_label.place(x=100 , y=60)

player_2_label = Label(win_frame , text='Player 2' , font=10 , bg='green')
player_2_label.place(x=450 , y=60)

start_button = Button(win_frame, text='Start Game', command=start_game , image=start_button_img)
start_button.place(x=280, y=25)

next_turn_button = Button(win_frame, text='Next Turn', command=next_turn)
next_turn_button.place(x=280, y=60)

root.mainloop()

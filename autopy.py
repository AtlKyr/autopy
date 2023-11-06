import pyautogui
import pyautogui as auto
import time
import tkinter
from pynput.keyboard import Key, Listener
import keyboard
import pyperclip
from pynput.mouse import Button, Controller
import os












class myclass:












    def __init__(self):
        keyboard.add_hotkey("f7", self.startclick)

        self.FirstHex = "#818282"
        self.SecondHex = "#6e6e6e"



        self.main = tkinter.Tk()
        self.main.geometry("450x300")
        self.main.title("atilkayar AutoClicker")
        self.main.resizable(True, True)
        self.main.configure(bg="#8a8a8a")

        self.namelabel = tkinter.Label(self.main, text="atilkayar Auto Clicker", font=("Ariel", 22), bg="#6e6e6e", width=30)
        self.namelabel.pack(pady=5)



        self.amountlabelofclick = tkinter.Label(self.main, text="Click Amount:            ", font=("Ariel", 13, "bold"), bg="#6e6e6e", width=17)
        self.amountlabelofclick.place(x=10,y=60)

        self.amountbox = tkinter.Text(self.main, height=1, font=("Ariel",13), width=4,bg="#818282")
        self.amountbox.bind("<KeyPress>", self)
        self.amountbox.place(x=125,y=61)



        self.cpsclockcooldown = tkinter.Label(self.main, text="Cps:              ", font=("Ariel", 13, "bold"), bg="#6e6e6e", width=17)
        self.cpsclockcooldown.place(x=10, y=100)

        self.cpsamountbox = tkinter.Text(self.main, height=1, font=("Ariel", 13), width=4, bg="#818282")
        self.cpsamountbox.bind("<KeyPress>", self)
        self.cpsamountbox.place(x=125, y=101)



        self.firstdelay = tkinter.Label(self.main, text="First Click Delay:      ", font=("Ariel", 13, "bold"), bg="#6e6e6e", width=20)
        self.firstdelay.place(x=10 , y=140)

        self.boxfirstdelay = tkinter.Text(self.main, font=("Ariel",13), height=1,width=4, bg="#818282")
        self.boxfirstdelay.place(x=165 , y=141)




        self.doubleclicklabel = tkinter.Label(self.main, text="Double Click:      ", font=("Ariel",13,"bold"), bg="#6e6e6e", width=15)
        self.doubleclicklabel.place(x=10, y=180)

        self.islecked = tkinter.IntVar()

        self.checkdoubleclick = tkinter.Checkbutton(self.main, variable=self.islecked,bg="#6e6e6e")
        self.checkdoubleclick.place(x=140,y=180)




        self.doubleclicklabelr = tkinter.Label(self.main, text="Left Click:      ", font=("Ariel", 13, "bold"),
                                              bg="#6e6e6e", width=15)
        self.doubleclicklabelr.place(x=250, y=60)

        self.ischecked = tkinter.IntVar()

        self.checkdoubleclickr = tkinter.Checkbutton(self.main, variable=self.ischecked, bg="#6e6e6e")
        self.checkdoubleclickr.place(x=390, y=60)




        self.setposlabel = tkinter.Label(self.main,text="  Set Position:  ", font=("Ariel",13,"bold"),bg="#6e6e6e")
        self.setposlabel.place(x=250,y=100)

        self.ispossetyt = tkinter.IntVar()

        self.checkpossetlabel = tkinter.Checkbutton(self.main, variable=self.ispossetyt, bg="#6e6e6e")
        self.checkpossetlabel.place(x=370,y=100)

        self.writedownposses = tkinter.Text(self.main, font=("Ariel", 13, "bold"),height=1,width=16, bg="#818282")
        self.writedownposses.place(x=250,y=125)





        self.colorboxlabel = tkinter.Label(self.main, text="Set Theme:                 ", font=("Ariel",13,"bold"), bg="#6e6e6e")
        self.colorboxlabel.place(x=250, y=155)

        self.boxcolortext = tkinter.Text(self.main, font=("Ariel", 13, "bold"),height=1,width=5, bg="#818282")
        self.boxcolortext.place(x=345, y=156)

        self.setthemebutton = tkinter.Button(self.main, text="Set", font=("Ariel", 7, "bold"), height=1, bg="#6e6e6e",command=self.changetheme)
        self.setthemebutton.place(x=402, y=158)















        self.saveposer = tkinter.Button(self.main, text="Save Position", font=("Ariel", 10, "bold"), height=1, width=11, bg="#6e6e6e", command=self.savepos)
        self.saveposer.place(x=30, y=260)




        self.posfinder = tkinter.Button(self.main, text="Get Postion", font=("Ariel", 10, "bold"), height=1,width=11,bg="#6e6e6e", command=self.getpos)
        self.posfinder.place(x=325,y=260)




        self.startbutton = tkinter.Button(self.main, text="Start", font=("Ariel",18,"bold"),height=1,width=7, bg="#6e6e6e",command=self.startclick)
        self.startbutton.place(x=170,y=245)






        self.macroeditor = tkinter.Button(self.main, text="Macro Editor      ", font=("Ariel",16,"bold"), bg="#6e6e6e", command=self.macropageopeninging)
        self.macroeditor.place(x=249, y=192)

        self.ismacromode = tkinter.IntVar()

        self.macromodechanger = tkinter.Checkbutton(self.main, variable=self.ismacromode, bg="#6e6e6e")
        self.macromodechanger.place(x=400, y= 200)






        self.main.mainloop()






    def savepos(self):

        self.savenerr = tkinter.Toplevel()
        self.savenerr.geometry("400x80")
        self.savenerr.title("atilkayar Pos Saver")
        self.savenerr.configure(bg=self.FirstHex)
        self.savenerr.resizable(True, True)


        self.poslabel = tkinter.Label(self.savenerr, text="Insert Pos Here", font=("Ariel", 11, "bold"), bg=self.SecondHex, width=32)
        self.poslabel.place(x=8,y=8)



        self.sendpostotext = tkinter.Text(self.savenerr, font=("Ariel", 14, "bold"),height=1,width=22)
        self.sendpostotext.place(x=9, y=40)



        self.pastestatposof = tkinter.Button(self.savenerr,font=("Ariel", 9,"bold"), text="Paste", bg=self.SecondHex, command=self.pastestuffaspos)
        self.pastestatposof.place(x=260, y=40)




        self.savedaposss = tkinter.Button(self.savenerr, font=("Ariel", 9, "bold"), text="Save", bg=self.SecondHex, width=10, command=self.saveposbookwrite)
        self.savedaposss.place(x=310,y=7)



        self.loaddaposss = tkinter.Button(self.savenerr, font=("Ariel", 9, "bold"), text="Load", bg=self.SecondHex, width=10, command=self.loadposbookwrite)
        self.loaddaposss.place(x=310, y=40)





    def changetheme(self):



        self.listofrgb = [int(i) for i in str(self.boxcolortext.get("1.0", "end-1c"))]


    #    self.listofrgb = [1,2,3,4]


        self.redderred = self.listofrgb[0] * 25
        self.greenergreen = self.listofrgb[1] * 25
        self.bluerblue = self.listofrgb[2] * 25


        print(self.redderred)
        print(self.greenergreen)
        print(self.bluerblue)


        self.SecondHex = self.rgb_to_hex(self.redderred+5, self.greenergreen+5, self.bluerblue+5)

        self.FirstHex = self.rgb_to_hex(self.redderred+25 , self.greenergreen+25 , self.bluerblue+25 )


        self.main.configure(bg=self.FirstHex)
        self.namelabel.configure(bg=self.SecondHex)
        self.amountlabelofclick.configure(bg=self.SecondHex)
        self.amountbox.configure(bg=self.FirstHex)
        self.cpsclockcooldown.configure(bg=self.SecondHex)
        self.cpsamountbox.configure(bg=self.FirstHex)
        self.firstdelay.configure(bg=self.SecondHex)
        self.boxfirstdelay.configure(bg=self.FirstHex)
        self.doubleclicklabel.configure(bg=self.SecondHex)
        self.checkdoubleclick.configure(bg=self.SecondHex)
        self.setposlabel.configure(bg=self.SecondHex)
        self.checkpossetlabel.configure(bg=self.SecondHex)
        self.writedownposses.configure(bg=self.FirstHex)
        self.checkdoubleclickr.configure(bg=self.SecondHex)
        self.doubleclicklabelr.configure(bg=self.SecondHex)
        self.setthemebutton.configure(bg=self.SecondHex)
        self.colorboxlabel.configure(bg=self.SecondHex)

        self.macromodechanger.configure(bg=self.SecondHex)
        self.macroeditor.configure(bg=self.SecondHex)

        self.macroeditor.configure(bg=self.SecondHex)

        self.boxcolortext.configure(bg=self.FirstHex)
        self.saveposer.configure(bg=self.SecondHex)
        self.startbutton.configure(bg=self.SecondHex)
        self.posfinder.configure(bg=self.SecondHex)


        self.macropage.configure(bg=self.FirstHex)









        self.loaddaposss.configure(bg=self.SecondHex)
        self.savedaposss.configure(bg=self.SecondHex)
        self.pastestatposof.configure(bg=self.SecondHex)
        self.poslabel.configure(bg=self.SecondHex)
        self.savenerr.configure(bg=self.FirstHex)












    def rgb_to_hex(self,r, g, b):

        return '#{:02x}{:02x}{:02x}'.format(r, g, b)





    def getpos(self):

        global cordormor

        self.opnener = tkinter.Toplevel()
        self.opnener.geometry("350x90")
        self.opnener.resizable(True, True)
        self.opnener.title("atilkayar Pos Finder")
        self.opnener.configure(bg=self.FirstHex)


        self.xposzone = tkinter.Label(self.opnener,text="X Position:", font=("Ariel",18,"bold"),bg=self.SecondHex)
        self.xposzone.place(x=10,y=10)
        self.xposzone.configure(text="Mouse Position = " + str(Controller().position))


        self.ctclipboardbut = tkinter.Button(self.opnener,text="Copy To Clipboard", font=("Ariel", 10, "bold"), bg=self.SecondHex, command=self.copytoclipboard)
        self.ctclipboardbut.place(x=113,y=55)



        time.sleep(2)

        cordormor = Controller().position


        self.xposzone.configure(text="Mouse Position = " + str(cordormor))







    def startclick(self):

        time.sleep(int(self.boxfirstdelay.get("1.0", "end-1c")))

        if self.ispossetyt.get():
            print("gggg")

            a, b = self.writedownposses.get("1.0", "end-1c").split(" ")
            print(a)
            print(b)
            lasta = str(a).replace("(", "")
            lastlasta = lasta.replace(",", "")
            lastb = str(b).replace(")", "")

            print(lastlasta)
            print(lastb)

            pyautogui.moveTo(int(lastlasta), int(lastb) ,duration=0)
        else:
            print("asasasa")



        if not self.ismacromode.get() == True:



            if self.ischecked.get():
                if self.islecked.get():

                    for i in range(0, int(self.amountbox.get("1.0", "end-1c"))):
                        Controller().click(Button.left, 2)
                        time.sleep(1 / int(self.cpsamountbox.get("1.0", "end-1c")))
                        if keyboard.is_pressed("f8"):
                            break


                elif not self.islecked.get():

                    for i in range(0, int(self.amountbox.get("1.0", "end-1c"))):
                        Controller().click(Button.left)
                        time.sleep(1 / int(self.cpsamountbox.get("1.0", "end-1c")))
                        if keyboard.is_pressed("f8"):
                            break

            elif not self.ischecked.get():
                if self.islecked.get():

                    for i in range(0, int(self.amountbox.get("1.0", "end-1c"))):
                        Controller().click(Button.right, 2)
                        time.sleep(1 / int(self.cpsamountbox.get("1.0", "end-1c")))
                        if keyboard.is_pressed("f8"):
                            break


                elif not self.islecked.get():

                    for i in range(0, int(self.amountbox.get("1.0", "end-1c"))):
                        Controller().click(Button.right)
                        time.sleep(1 / int(self.cpsamountbox.get("1.0", "end-1c")))
                        if keyboard.is_pressed("f8"):
                            break
        else:

            self.MacroMode()








    def copytoclipboard(self):

        pyperclip.copy(str(cordormor))



    def saveposbookwrite(self):
        saveposbook = open("saveposses.txt", "a")
        print("hgeeeeaelooo")
        saveposbook.write(str(self.sendpostotext.get("1.0", "end-1c")) + "\n\n-----------------\n\n")
        print("hgelooo")



    def loadposbookwrite(self):
        os.startfile("saveposses.txt")

    def savemacrobookwrite(self):
        saveposbook = open("savemacros.txt", "a")
        print("hgeeeeaelooo")
        saveposbook.write(str(self.macrowritebox.get("1.0", "end-1c")) + "\n\n\n----------------------------------------\n\n\n")
        print("hgelooo")

    def loadmacrobookwrite(self):
        os.startfile("savemacros.txt")


    def pastestuffaspos(self):

        pyautogui.write(pyperclip.paste())





    def macropageopeninging(self):




        self.macropage = tkinter.Toplevel()
        self.macropage.geometry("550x260")
        self.macropage.title("atilkayar Macro Maker")
        self.macropage.configure(bg=self.FirstHex)



        self.macrowritebox = tkinter.Text(self.macropage, font=("Courier",14,"bold"), height=3, width=48)
        self.macrowritebox.place(x=8, y=10)



        self.macrosavebuttons = tkinter.Button(self.macropage, text="Save Macro",font=("Courier",14,"bold"),bg=self.SecondHex, command=self.savemacrobookwrite)
        self.macrosavebuttons.place(x=14, y=93)




        self.macroloadbuttons = tkinter.Button(self.macropage, text="Load Macro",font=("Courier",14,"bold"),bg=self.SecondHex, command=self.loadmacrobookwrite)
        self.macroloadbuttons.place(x=210, y=93)




        self.macropastebuttons = tkinter.Button(self.macropage, text="Paste Macro", font=("Courier",14,"bold"),bg=self.SecondHex, command=self.pastestuffaspos)
        self.macropastebuttons.place(x=396, y=93)




        self.replyamountmacrolabel = tkinter.Label(self.macropage, text="Repeat Amount:      ", font=("Courier",14,"bold"), bg=self.SecondHex)
        self.replyamountmacrolabel.place(x=14,y=153)

        self.boxreplyamountmacrobox = tkinter.Text(self.macropage, font=("Courier",11,"bold"), height=1, width=6)
        self.boxreplyamountmacrobox.place(x=165, y=156)





        self.startdelayformacro = tkinter.Label(self.macropage, text="Delay Between Repeats:    ", font=("Courier",14,"bold"), bg=self.SecondHex)
        self.startdelayformacro.place(x=252,y=153)

        self.boxstartdelayformacro = tkinter.Text(self.macropage, font=("Courier", 11, "bold"), height=1, width=4)
        self.boxstartdelayformacro.place(x=497, y=156)

































    def MacroMode(self):

        print(str(self.macrowritebox.get("1.0", "end-1c")))


        self.macro_value = self.macrowritebox.get("1.0", "end-1c")

        self.string_macro_value = str(self.macro_value)

        self.list_of_macro_words = self.string_macro_value.split(":")






        for r in range(1,int(self.boxreplyamountmacrobox.get("1.0", "end-1c")) + 1):

            for self.fs in self.list_of_macro_words:

                if "setpos" in self.fs:

                    self.real_pos_whic_no_end = str(self.fs).replace("setpos", "")[-1]

                    self.pos_seted_rn_pos = str(self.fs).replace("setpos", "")[:-1]

                    pos_split_x, pos_split_y = self.pos_seted_rn_pos.split(" ")

                    self.lastar = str(pos_split_x).replace("(", "")
                    self.lastlastar = self.lastar.replace(",", "")
                    self.lastbr = str(pos_split_y).replace(")", "")

                    pyautogui.moveTo(int(self.lastlastar), int(self.lastbr), duration=float(self.real_pos_whic_no_end))



                elif "press" in self.fs:

                    self.key_of_fs_equals = str(self.fs).replace("press", "")

                    self.nt_key_of_fs_equals = self.key_of_fs_equals[-1]

                    self.fabriano_key_of_fs_equals = self.key_of_fs_equals[0]

                    self.ty_key_of_fs_equals = self.key_of_fs_equals[:-1]

                    self.last_ty_key_of_fs_equals = self.ty_key_of_fs_equals[1:]

                    print(self.nt_key_of_fs_equals)
                    print(self.fabriano_key_of_fs_equals)
                    print(self.last_ty_key_of_fs_equals)

                    for i in range(1, int(self.nt_key_of_fs_equals) + 1):
                        pyautogui.press(self.last_ty_key_of_fs_equals)
                        time.sleep(int(self.fabriano_key_of_fs_equals))





                elif "wait" in self.fs:

                    self.rn_timenumber = str(self.fs.replace("wait", ""))

                    time.sleep(float(self.rn_timenumber))


                elif "click" in self.fs:
                    if "lclick" in self.fs:

                        self.lclick_amount = str(self.fs).replace("lclick", "")

                        self.getlc_minusone = self.lclick_amount[-1]
                        self.norm_sit_at_lc = self.lclick_amount[:-1]

                        for i in range(1, int(self.getlc_minusone) + 1):
                            pyautogui.leftClick()
                            time.sleep(int(self.norm_sit_at_lc))




                    elif "rclick" in self.fs:

                        self.rclick_amount = str(self.fs).replace("rclick", "")
                        self.getrc_minusone = self.rclick_amount[-1]
                        self.norm_sit_at_rc = self.rclick_amount[:-1]

                        for i in range(1, int(self.getrc_minusone) + 1):
                            pyautogui.rightClick()
                            time.sleep(int(self.norm_sit_at_rc))



                elif "write" in self.fs:

                    self.writed_part_in_macrocode = str(self.fs).replace("write", "")

                    pyautogui.write(self.writed_part_in_macrocode)


            time.sleep(int(self.boxstartdelayformacro.get("1.0", "end-1c")))










































































































myclass()







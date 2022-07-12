from tkinter import *
from PIL import Image, ImageTk
import random
import json
import time
import re
import os
import pickle
import getpass
import pyperclip
from threading import Timer
from tkinter import messagebox

""" -- Create list for store character color """

Character_color = {'A': '#b6b6b6', 'B': '#adb2ff', 'C': '#ffa87d', 'D': '#f27a3e', 'E': '#f98888', 'F': '#ff6161',
                   'G': '#ffcd87', 'H': '#f3a231', 'I': '#f0ee75', 'J': '#cae86f', 'K': '#b4e61e', 'L': '#a5dd76',
                   'M': '#88e53c', 'N': '#79dd89', 'O': '#37e254', 'P': '#68ddb0', 'Q': '#03e48e', 'R': '#74d7c3',
                   'S': '#00e6b8', 'T': '#a992d9', 'U': '#9165f0', 'W': '#b573cb', 'X': '#e9a7ff', 'Y': '#a100d6',
                   'Z': '#ca88c6', '1': '#ff71b5', '2': '#ff7171', '3': '#f5acac', '4': '#8a8a8a', '5': '#e89b00'}

""" --- Set Path list for Searching --- 
    --- Path name consists two value 1 Path name | 2 Active or Disable attributes value """

# Main machine username
Main_username = getpass.getuser()

# Create List for store path list
Path_name_list = []


def Set_path():
    # -- Open path list pickle file for store path list

    Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'rb')
    Read_data = pickle.load(Pathlist)
    print(Read_data)

    # -- Clear Path_name list
    Path_name_list.clear()

    # -- Add Path name in Path name list
    for item in Read_data:

        path = str(item).split('*')[0]
        path_value = str(item).split('*')[1]

        if path_value == 'Active':
            Path_name_list.append(path)
        else:
            pass
    Pathlist.close()


Set_path()

""" ----------- EXTENSION FRAME FUNCTION ------------------- """

# List for store current file name

Select_filename = []

# List for store Folder in | Folder show attributes

Select_filename_function_data = []

# List for store extension value of particular file

Extension_list = []

#  List for store file name in first phase of searching

Dir_data = {}

#  List for store Folder name in first phase of searching

Folder_list = []

#  List for store only Sub folder name

Subfolder_list = []

#  Dic for store File in data

Folder_data = {}

""" --- Extension list file name main button function --- """


def Set_extension_list(filename, extension_list):
    """ Function is connected with extension frame file name button is
        set file name , folder in and folder show attributes , extension list attributes in list """

    # Add file name in list
    Select_filename.clear()
    Select_filename.append(filename)

    # Read folder in and folder show attributes from folder data pickle file

    file = open(f'C:\\Users\\{Main_username}\\Lion manager\Folderdata.pkl', 'rb')
    Read_data = pickle.load(file)
    Read_data = Read_data[Select_filename[0]]
    file.close()

    # Add folder in and folder show attributes in list
    Select_filename_function_data.clear()
    Select_filename_function_data.append(Read_data[0])
    Select_filename_function_data.append(Read_data[1])

    # Clear extension list
    Extension_list.clear()

    # -- Set all extension value in Extension list
    for item in extension_list:
        Extension_list.append(item)

    # Call phase 1 searching function
    Set_main_data()


""" --- FIRST PHASE OF SEARCHING --- """


def Set_main_data():
    """ Function is check file data in particular file path and finding data in list
        -- File data add in Dir data
        -- Folder data add in Folder_list """

    # -- Clear Dic_data | Folder_list
    Dir_data.clear()
    Folder_list.clear()

    for Path_name in Path_name_list:

        # -- Get List of particular path
        Main_list = os.listdir(Path_name)

        # Create path name division in Dir data list
        Dir_data[Path_name] = []

        for Extension_file in Main_list:

            global Extension

            try:
                # -- Get extension of file
                Extension = os.path.splitext(Extension_file)[1]

            except:
                pass

            if Extension in Extension_list:

                # -- Add this file data in Dir data

                Dir_data[Path_name].append(Extension_file)

            else:
                pass

            #  Check folder available or not in path

            if os.path.isdir(f'{Path_name}\\{Extension_file}'):

                # -- Skip some folder which already available in Path list

                if Extension_file == 'Downloads':
                    pass

                elif Extension_file == 'Desktop':
                    pass

                elif str(Extension_file[0:1]) == '$':
                    pass

                elif Extension_file == 'AppData':
                    pass

                elif str(Extension_file[0:1]) == '.':
                    pass

                else:

                    # Add Folder name in Folder list
                    Folder_list.append(f'{Path_name}\\{Extension_file}')

            else:
                pass

    # Call option frame function for set option frame
    Set_option_frame_function()

    # Call Main screen function for set Main screen data
    Set_main_file_data_function(Main_width - 28)

    # Call phase 2 searching function is attributes is active

    if Select_filename_function_data[0] == 'ACTIVE':
        Checkfolder_data()
    else:
        pass


""" --- SECOND PHASE OF SEARCHING --- """


def Checkfolder_data():
    # --> Clear Folder data dic
    Folder_data.clear()

    # --> Clear Sub folder name list
    Subfolder_list.clear()

    for Folder_name in Folder_list:

        global Folder_data_list, Setvalue

        # If we get particular folder list than this var use
        Setvalue = 0

        Create_solt = 0

        try:

            # --> Try to get Folder listdir

            Folder_data_list = os.listdir(Folder_name)

            # --> Set value

            Setvalue = 1

        except:

            pass

        if Setvalue == 1:

            for Folder_sub in Folder_data_list:

                # -- Check if any folder is available or not in Folder data list

                if os.path.isdir(f'{Folder_name}//{Folder_sub}'):

                    Subfolder_list.append(f'{Folder_name}\\{Folder_sub}')

                else:
                    pass

                # --> Get Extension of file

                Extension = os.path.splitext(Folder_sub)[1]

                if Extension in Extension_list:

                    if Create_solt == 0:

                        # --> Create Folder name solt in dic

                        Folder_data[Folder_name] = []

                    else:
                        pass

                    # --> Add this Path name in Folder data

                    Folder_data[Folder_name].append(f'{Folder_sub}')

                    Create_solt = 1

                else:
                    pass


        else:
            pass

    # -- Call Set folder file function
    Set_folder_file_in_main_canvas(Main_width - 28)


""" --- Hover and Dehover effect --- """


# Hover effect function
def Enter_frame(event, widget):
    """ This function work as hover effect for extension frame
        -- Function for Extension frame """

    # -- Set frame color
    widget.config(bg=Color_list['Extension_frame_hover'])

    for data in widget.winfo_children():
        data.config(bg=Color_list['Extension_frame_hover'],
                    activebackground=Color_list['Extension_frame_hover'])


# Dehover effect function
def Unhover_frame(event, widget):
    """ This function work as unhover effect for extension  frame
        --  Function for Extension frame """

    # -- Set frame color
    widget.config(bg=Color_list['Extension'])

    for data in widget.winfo_children():
        data.config(bg=Color_list['Extension'],
                    activebackground=Color_list['Extension'])


# Function which call finding file data function for find file data
def Extension_frame_function(event, filename, extension_list):
    """ Button 1 event function of extension frame
        purpose When user click on extension frame than search related extension file data"""

    # -- Call set extension list function
    Set_extension_list(filename, extension_list)


""" ---------- FUNCTION FOR SHOW EXTENSION FILE FUNCTIONALITY FRAME -------------- """

# Create List for store file data screen name
File_data_screen_name = []


# Function which call show file data screen
def Call_file_data_screen_function(event, filename):
    """ Function which call show file data screen """

    if len(File_data_screen_name) == 0:
        File_data_screen(filename)
    else:
        File_data_screen_name[0].destroy()
        File_data_screen(filename)


# Function which show Folder in | Folder show attributes frame for particular file

def File_data_screen(file):
    """ This function is show extension list with particular extension frame
        | Eye image in Extension frame """

    # Create dic for store all file data

    All_folder_data = {}

    # Create list for store current open file data

    File_data = []

    # Open folder data pickle file for read folder and folder show attributes value
    Folder_data = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'rb')
    Read_data = pickle.load(Folder_data)

    # Add This all folder data in All folder data dic
    All_folder_data.clear()
    All_folder_data.update(Read_data)

    # Read particular file data
    Read_data = Read_data[file]

    # Clear Folder data list
    File_data.clear()

    for item in Read_data:
        File_data.append(item)

    Folder_data.close()

    # Folder in active button function
    def Folder_in_active_function():
        """ Function for folder in active button """
        File_data.pop(0)
        File_data.insert(0, 'ACTIVE')

        # Set button color
        Folder_in_active.config(fg='#f4ca22', activeforeground='#f4ca22')
        Folder_in_disable.config(fg='#9c9c9c', activeforeground='#9c9c9c')

    # Folder in disable button function

    def Folder_in_disable_function():
        """ Function for folder in disable button """
        File_data.pop(0)
        File_data.insert(0, 'DISABLE')

        # set button color
        Folder_in_disable.config(fg='#f4ca22', activeforeground='#f4ca22')
        Folder_in_active.config(fg='#9c9c9c', activeforeground='#9c9c9c')

    # Folder show active button function

    def Folder_show_active_function():
        """ Folder show active button function """

        File_data.pop(1)
        File_data.insert(1, 'ACTIVE')

        # Set button color
        Folder_show_active.config(fg='#f4ca22', activeforeground='#f4ca22')
        Folder_show_disable.config(fg='#9c9c9c', activeforeground='#9c9c9c')

    # Folder show disable button function

    def Folder_show_disable_function():
        """ Folder show disable button function """

        File_data.pop(1)
        File_data.insert(1, 'DISABLE')

        # Set button color
        Folder_show_disable.config(fg='#f4ca22', activeforeground='#f4ca22')
        Folder_show_active.config(fg='#9c9c9c', activeforeground='#9c9c9c')

    # Set button function

    def Set_button_function():
        """ Set button function """

        # Write in Extension data pickle file
        Folder_data = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'wb')

        del All_folder_data[file]

        Data = {file: File_data}
        All_folder_data.update(Data)

        pickle.dump(All_folder_data, Folder_data)
        Folder_data.close()

        # Close this screen
        File_data_screen_name.clear()
        Attributes.destroy()

    # Close button function

    def Close_button_function():
        """ Function for close this screen """
        File_data_screen_name.clear()
        Attributes.destroy()

    """ --- Start screen --- """

    Attributes = Toplevel()

    # Set Height and Width
    Attributes_height = 230
    Attributes_width = 500

    Attributes_x = (Attributes.winfo_screenwidth() // 2) - (Attributes_width // 2)
    Attributes_y = (Attributes.winfo_screenheight() // 2) - (Attributes_height // 2)

    # Set geometry
    Attributes.geometry('{}x{}+{}+{}'.format(Attributes_width, Attributes_height, Attributes_x, Attributes_y))

    # Set background color and other value
    Attributes.config(bg=Color_list['Base_color'], highlightbackground='#9c9c9c', highlightthickness=1,
                      highlightcolor='#9c9c9c')

    # Set minimize attributes
    Attributes.wm_transient(Mainwindow)

    # Set Logo
    Attributes.iconbitmap(r"Logo.ico")

    # Set title
    Attributes.title('FILE DATA')

    # Set resizable off
    Attributes.resizable(False, False)

    # Set close button property
    Attributes.wm_protocol('WM_DELETE_WINDOW', Close_button_function)

    # Create File name information label
    File_name_information = Label(Attributes, text=f'{file.upper()}', bg=Color_list['Base_color'], fg='#8cfffb',
                                  font=('calibri', 13, 'bold'),
                                  bd=0)
    File_name_information.place(x=10, y=5)

    """ --- Folder in value related data --- """

    Main_folder_in_frame = Frame(Attributes, height=40, width=475, bg=Color_list['Base_color'], highlightthickness=1,
                                 highlightcolor='#4c4c4c', highlightbackground='#4c4c4c')
    Main_folder_in_frame.place(x=10, y=45)

    # Create Folder information label
    Folder_in_information = Label(Main_folder_in_frame, text='FOLDER IN', bg=Color_list['Base_color'], fg='white',
                                  font=('calibri', 12), bd=0)
    Folder_in_information.place(x=10, y=8)

    # Folder in active button
    Folder_in_active = Button(Main_folder_in_frame, text='ACTIVE', bg=Color_list['Base_color'],
                              activebackground=Color_list['Base_color'],
                              fg='#f4ca22', activeforeground='#f4ca22', font=('calibri', 12), bd=0,
                              command=Folder_in_active_function)
    Folder_in_active.place(x=135, y=4)

    # Folder in disable button
    Folder_in_disable = Button(Main_folder_in_frame, text='DISABLE', bg=Color_list['Base_color'],
                               activebackground=Color_list['Base_color'],
                               bd=0, font=('calibri', 12),
                               command=Folder_in_disable_function)
    Folder_in_disable.place(x=205, y=4)

    """ --- Folder show value related data --- """

    Main_folder_show_frame = Frame(Attributes, height=40, width=475, bg=Color_list['Base_color'], highlightthickness=1,
                                   highlightcolor='#4c4c4c', highlightbackground='#4c4c4c')
    Main_folder_show_frame.place(x=10, y=95)

    # Folder show active button
    Folder_show_information = Label(Main_folder_show_frame, text='FOLDER SHOW', bg=Color_list['Base_color'], fg='white',
                                    font=('calibri', 12), bd=0)
    Folder_show_information.place(x=10, y=8)

    # Folder show active button
    Folder_show_active = Button(Main_folder_show_frame, text='ACTIVE', bg=Color_list['Base_color'],
                                activebackground=Color_list['Base_color'],
                                fg='#f4ca22', activeforeground='#f4ca22', font=('calibri', 12), bd=0,
                                command=Folder_show_active_function)

    Folder_show_active.place(x=135, y=4)

    # Folder show disable button
    Folder_show_disable = Button(Main_folder_show_frame, text='DISABLE', bg=Color_list['Base_color'],
                                 activebackground=Color_list['Base_color'],
                                 fg='#9c9c9c', activeforeground='#9c9c9c', bd=0, font=('calibri', 12),
                                 command=Folder_show_disable_function)
    Folder_show_disable.place(x=205, y=4)

    # Set Button color foreground color

    # Set Folder in Button color

    if File_data[0] == 'ACTIVE':
        Folder_in_active.config(fg='#f4ca22', activeforeground='#f4ca22')
        Folder_in_disable.config(fg='#9c9c9c', activeforeground='#9c9c9c')
    else:
        Folder_in_active.config(fg='#9c9c9c', activeforeground='#9c9c9c')
        Folder_in_disable.config(fg='#f4ca22', activeforegropund='#f4ca22')

    # Set Folder show button color

    if File_data[1] == 'ACTIVE':
        Folder_show_active.config(fg='#f4ca22', activeforeground='#f4ca22')
        Folder_show_disable.config(fg='#9c9c9c', activeforeground='#9c9c9c')
    else:
        Folder_show_active.config(fg='#9c9c9c', activeforeground='#9c9c9c')
        Folder_show_disable.config(fg='#f4ca22', activeforeground='#f4ca22')

    """ --- Create Set and Cancel button --- """

    # Set button start here....
    Set_button_frame = Frame(Attributes, height=30, width=60, bg=Color_list['Base_color'], highlightthickness=1,
                             highlightbackground=Color_list['Button_background'],
                             highlightcolor=Color_list['Button_background'], bd=0)
    Set_button_frame.place(x=310, y=175)

    Set_button = Button(Set_button_frame, text='SET', bg=Color_list['Base_color'],
                        activebackground=Color_list['Base_color'],
                        fg=Color_list['Button_background'], activeforeground=Color_list['Button_background'],
                        font=('calibri', 12), bd=0,
                        command=Set_button_function)
    Set_button.place(x=12, y=7, relheight=0.50)

    # Cancel button start here....

    Cancel_button_frame = Frame(Attributes, height=30, width=90, bg=Color_list['Base_color'], highlightthickness=1,
                                highlightcolor='#9c9c9c', highlightbackground='#9c9c9c', bd=0)
    Cancel_button_frame.place(x=385, y=175)

    Cancel_button = Button(Cancel_button_frame, text='CANCEL', bg=Color_list['Base_color'],
                           activebackground=Color_list['Base_color'],
                           fg='#9c9c9c', activeforeground='#9c9c9c', font=('calibri', 12), bd=0,
                           command=Close_button_function)
    Cancel_button.place(x=12, y=7, relheight=0.50)

    Attributes.mainloop()


# Function which disable Extension functionality frame when click on Button-3
def Disable_show_extension(event):
    """ Function for disable show extension frame in Mainwindow """
    Show_extension.place_forget()


""" --- FUNCTION FOR OPEN EXTENSION FILE DATA PICKLE FILE --- """

#  Create dic for store extension list data
Extension_data = {}

# List for store extension file data when need
# Search bar button work for update Extension data with search data that time value Disable
Extension_call = ['Active']


def Open_extension_file_function():
    """ Function for open extension.pkl file """

    # -- Read Extension list pickle file
    Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
    Read_data = pickle.load(Extension_file)

    # -- Clear Extension data dic
    Extension_data.clear()
    Extension_data.update(Read_data)

    # -- Close Extension frame
    Extension_file.close()


"""" --- EXTENSION FRAME SEARCH BUTTON FUNCTION --- """

# -- Create Dic for store finding data
Extension_search_data = {}


def Extension_search_button_function():
    """ Extension search button function """

    if Search_entry.get() == '':
        messagebox.showinfo('Lion manager', 'Please,Enter search file name entry widget')
    else:

        # -- Get Search value

        Search_value = Search_entry.get()

        for file_name, extension_list in Extension_data.items():

            if str(Search_value).lower() in str(file_name).lower():

                # -- Add data in extension file name and extension list in Extension data dic
                Extension_search_data[file_name] = extension_list

            else:
                pass

        # -- Check Search data dic

        if len(Extension_search_data) == 0:

            # -- Clear all widget in Extension frame
            for widget in Extension_Frame.winfo_children():
                widget.destroy()

            # -- Create Not found any data frame
            Not_found_any_data_frame = Frame(Extension_Frame, height=35, width=257,
                                             bg=Color_list['File_show_canvas_color'],
                                             bd=0)
            Not_found_any_data_frame.grid(row=0, column=0, padx=10, pady=5)

            # -- Create Not found data information label
            Information_label_found = Label(Not_found_any_data_frame, text='Not found any data',
                                            bg=Color_list['File_show_canvas_color'],
                                            fg='#ffa200', font=('calibri', 12), bd=0)
            Information_label_found.place(x=57, y=6)

            # -- Call Timer function for reset extension file data
            Reset_extension_data = Timer(2, Reset_main_extension_data)
            Reset_extension_data.start()

            # -- Delete Search entry value
            Search_entry.delete(0, END)

        else:

            # -- Call Main screen function
            for widget in Extension_Frame.winfo_children():
                widget.destroy()

            # -- Change Extension_call list value
            Extension_call.clear()
            Extension_call.append('Disable')

            # -- Clear Extension data dic
            Extension_data.clear()

            # -- Add Search data dic value in Extension data dic
            Extension_data.update(Extension_search_data)

            # -- Call set extension function
            Main_extension_set_function()

            # -- Clear Extension search data dic
            Extension_search_data.clear()

            # -- Call Open extension file function for set data
            Open_extension_file_function()

            # -- Delete Search entry widget
            Search_entry.delete(0, END)

            # -- Change extension call list value
            Extension_call.clear()
            Extension_call.append('Active')


""" --- EXTENSION FRAME BACK BUTTON FUNCTION --- """


# Function which reset extension frame data
# Threading time function
def Reset_main_extension_data():
    try:
        Extension_back_button_function()
    except:
        pass


# Function for reset extension frame data
def Extension_back_button_function():
    """ Extension frame back button function """

    # -- Set Extension data function

    for widget in Extension_Frame.winfo_children():
        widget.destroy()

    # -- Call function
    Main_extension_set_function()


""" --- Function for close button and Escape event function --- 
    --- Main screen function """

# List for store current canvas name
Current_canvas = []


# Main screen close button function
def Main_close_button():
    """ This function is close canvas of every canvas and Set Mainwindow canvas """

    Mainwindow_canvas.pack(fill=BOTH)

    if len(Current_canvas) == 0:
        pass

    else:
        Current_canvas[0].pack_forget()


# Main screen escape event function
def Escape_function(event):
    """ This function is set Mainwindow_canvas in Mainwindow
        Escape button function and set current canvas name in List"""

    # -- Close widget which we store in Current canvas list

    if len(Current_canvas) == 0:
        pass

    else:
        Current_canvas[0].pack_forget()

    Mainwindow_canvas.pack(fill=BOTH)


""" --------------------- ADD EXTENSION DATA FUNCTION ----------------------- """


# Function which set Add extension main canvas in Main screen
def Add_extension_button():
    """ Function is set Add canvas base in Mainwindow and
        Disable Mainwindow canvas """

    # -- Disable Mainwindow canvas
    Mainwindow_canvas.pack_forget()

    Add_details.pack(fill=BOTH)

    # -- Add name in current canvas list
    Current_canvas.clear()
    Current_canvas.append(Add_details)


# Function is add Extension file data in database
def Set_extension_button_function():
    """ This function is set filename and extension in database """

    if File_name_entry.get() == "":
        messagebox.showinfo('ADD EXTENSION', 'Please,enter file name ')

    elif Extension_name_entry.get() == "":
        messagebox.showinfo('ADD EXTENSION', 'Please,enter extension value')

    else:

        """ -- Write in Extension.pkl file -- """

        # -- Create Dic for store extension data
        Extension_data = {}

        # -- Open extension list pickle file

        Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
        Read_data = pickle.load(Extension_file)

        # -- Add data in extension data dic
        Extension_data.update(Read_data)
        Extension_file.close()

        # -- Check data

        if File_name_entry.get() in Extension_data.items():

            messagebox.showinfo('Lion manager', 'You already add this file name.')

        else:

            # -- Write data in Extension data
            Extension_data[File_name_entry.get()] = [Extension_name_entry.get()]

            # -- Write data in Extension list pickle file

            Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'wb')
            pickle.dump(Extension_data, Extension_file)
            Extension_file.close()

            # -- Clear Extension data dic
            Extension_data.clear()

            """ -- Write in Folderdata.pkl file -- """

            # -- Create dic for store folder data
            Folder_dic = {}

            # -- Add this file data in Folder data pickle file

            Folder_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'rb')
            Read_data = pickle.load(Folder_file)
            Folder_dic.update(Read_data)
            Folder_file.close()

            # -- Add new file data

            Folder_dic[File_name_entry.get()] = ['ACTIVE', 'DISABLE']

            # -- Write in Folder data pickle file
            Folder_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'wb')
            pickle.dump(Folder_dic, Folder_file)
            Folder_file.close()

            # -- Clear Folder dic
            Folder_dic.clear()

        # -- Delete Both Entry widget value
        File_name_entry.delete(0, END)
        Extension_name_entry.delete(0, END)

        # -- Clear all widget in Extension Frame
        for widget in Extension_Frame.winfo_children():
            widget.destroy()

        # -- Call Mainwindow set extension list function
        # -- For update extension list

        Main_extension_set_function()

        # -- Call Close button function
        Main_close_button()


""" ---------------------- ENABLE PATH | DISABLE PATH CANVAS ----------------- """

""" -- ENABLE | DISABLE PATH CANVAS FUNCTION  -- """


# Function which set enable and disable path canvas in main screen
def Add_enable_disable_path_button():
    """ Function which set Enable path list canvas in Mainwindow and Mainwindow canvas """

    # -- Disable Mainwindow canvas
    Mainwindow_canvas.pack_forget()

    # -- Set Enable canvas
    Enable_path_canvas.pack(fill=BOTH)

    # -- Add this canvas name in current canvas list
    Current_canvas.clear()
    Current_canvas.append(Enable_path_canvas)


# Path frame hover effect function
def Enable_path_hover_effect(event):
    """ Function is hover effect of enable path frame """

    Widget = event.widget
    Widget.config(bg='#43434a')

    for sub_widget in Widget.winfo_children():
        sub_widget.config(bg='#43434a', activebackground='#43434a')


# Path frame dehover effect function
def Enable_path_dehover_effect(event):
    """ Function is set dehover effect with enable path list frame """

    Widget = event.widget

    Widget.config(bg=Color_list['File_show_canvas_color'])

    for sub_widget in Widget.winfo_children():
        sub_widget.config(bg=Color_list['File_show_canvas_color'],
                          activebackground=Color_list['File_show_canvas_color'])


# Function which disable and active path in database
def Set_enable_path_list():
    """ Function is set enable path list Main screen for  Enable path and Disable path"""

    def Enable_path(filepath):

        """ Function is enable path """

        # -- List for store path list
        Path_data = []

        # -- Open Pathlist pickle file

        Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'rb')
        Read_data = pickle.load(Pathlist)

        # -- Clear Path data list
        Path_data.clear()

        for item in Read_data:
            Path_data.append(item)
        Pathlist.close()

        # -- Get Position of path
        Call_function = Path_data.index(filepath)

        # -- Remove Path name in List
        Path_data.remove(filepath)

        # -- Get Path name
        Path_name = str(filepath).split('*')[0]

        # -- Get Active and Disable value

        Path_value = str(filepath).split('*')[1]

        if Path_value == 'Active':

            Add_path = f'{Path_name}*Disable'

            Path_data.insert(Call_function, Add_path)

        else:

            Add_path = f'{Path_name}*Active'

            Path_data.insert(Call_function, Add_path)

        # -- Set that path button in

        Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'wb')
        pickle.dump(Path_data, Pathlist)
        Pathlist.close()

        # -- Clear Path data list
        Path_data.clear()

        # -- Call Main screen set path function
        # -- For Reset path list

        Set_path()

        # -- Call Set path function

        Set_enable_path_list()

    def Delete_path_function(filepath):

        """ Function is delete path in database """

        path = str(filepath).split('*')[0]

        answer = messagebox.askquestion('Delete path', 'Are sure you want to delete this path ?\n'
                                                       f'{path}')

        if answer == 'yes':

            # -- Create List for store path name

            Path_data = []

            # -- Open Path list pickle file

            Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'rb')
            Read_data = pickle.load(Pathlist)

            Path_data.clear()

            for item in Read_data:
                Path_data.append(item)

            Pathlist.close()

            # -- Remove this Path name in list

            Path_data.remove(filepath)

            # -- Write this data in Pathlist pickle file

            Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'wb')
            pickle.dump(Path_data, Pathlist)
            Pathlist.close()

            # -- Call set enable and disable path function

            Set_enable_path_list()

            Set_path()

        else:

            pass

    # -- Create list for store path name
    Path_data = []

    # -- Open pathlist pickle file

    Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'rb')
    Read_data = pickle.load(Pathlist)

    # -- Clear Path data
    Path_data.clear()

    for item in Read_data:
        Path_data.append(item)

    # -- Close Pathlist pickle file
    Pathlist.close()

    # -- Delete all widget in Enable-frame

    for widget in Enable_frame.winfo_children():
        widget.destroy()

    # -- Create raw variable

    Path_raw = 0

    for path in Path_data:

        # -- Get path name
        path_1 = str(path).split('*')[0]

        value = str(path).split('*')[1]

        # -- Create Frame
        Path_frame = Frame(Enable_frame, height=45, width=Enable_frame.winfo_screenwidth() - 275,
                           bg=Color_list['File_show_canvas_color'],
                           bd=0)
        Path_frame.grid(row=Path_raw, column=0, pady=10, padx=5)

        # -- Bind Enter event for Hover effect
        Path_frame.bind('<Enter>', Enable_path_hover_effect)

        # -- Bind Leave event for dehover effect
        Path_frame.bind('<Leave>', Enable_path_dehover_effect)

        # -- Create delete path button
        Delete_path = Button(Path_frame, image=Delete_image, bd=0, bg=Color_list['File_show_canvas_color'],
                             activebackground=Color_list['File_show_canvas_color'],
                             command=lambda file=path: Delete_path_function(file))
        Delete_path.place(x=5, y=11)

        # -- Create path name button
        Path_name = Button(Path_frame, text=path_1, bg=Color_list['File_show_canvas_color'], bd=0,
                           fg='#61ed8b', font=('calibri', 13), activebackground=Color_list['File_show_canvas_color'],
                           command=lambda file=path: Enable_path(file), anchor='nw')
        Path_name.place(x=30, y=8)

        # -- Set High light background color
        if Path_raw % 2 == 0:
            Path_frame.config(highlightbackground='#ffce47', highlightthickness=1, highlightcolor='#ffce47')

        else:
            Path_frame.config(highlightbackground='#61ed8b', highlightthickness=1, highlightcolor='#61ed8b')

        # -- Set Path name button foreground color

        if value == 'Active':

            if Path_raw % 2 == 0:

                Path_name.config(fg='#ffce47', activeforeground='#ffce47')

            else:

                Path_name.config(fg='#61ed8b', activeforeground='#61ed8b')

        else:
            Path_name.config(fg='#9c9c9c', activeforeground='#9c9c9c')

        # -- Update Path_raw value
        Path_raw = Path_raw + 1

    # -- Clear Path data list
    Path_data.clear()


def Enable_path_mousewheel_function(event):
    Enable_List_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


""" --- ADD NEW PATH CANVAS FUNCTION --- """


def Enable_add_new_path():
    """ Function for add new path in database """

    # Function which add new path in database
    def Set_path_in_database():

        """ Function is add new path Pathlist pickle file this is function
           of Set path button"""

        # -- List for store path list
        Path_data = []

        # -- Open Pathlist pickle file

        Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'rb')
        Read_data = pickle.load(Pathlist)

        # -- Clear Path data list
        Path_data.clear()

        for item in Read_data:
            Path_data.append(item)
        Pathlist.close()

        # -- Get User enter path
        User_path = Path_entry.get()

        # -- Create system path
        System_path = os.path.normpath(User_path)
        System_path = re.escape(System_path)

        # -- Create Check path
        Check_path_1 = f'{System_path}*Active'
        Check_path_2 = f'{System_path}*Disable'

        if Check_path_1 in Path_data:
            messagebox.showinfo('Lion manager', 'You already add this path.\n'
                                                'Working status = Active. ')
        elif Check_path_2 in Path_data:
            messagebox.showinfo('Lion manager', 'You already add this path.\n'
                                                'Working status = Disable.')
        elif os.path.exists(System_path) == False:
            messagebox.showerror('Lion manager', 'Path not exists.\n'
                                                 'Please,Check your path.')
        else:

            # -- Add Path in Path data list
            Path_data.append(Check_path_1)

            # -- Write path data in Pathlist pickle file
            Pathlist = open(f'C:\\Users\\{Main_username}\\Lion manager\\Pathlist.pkl', 'wb')
            pickle.dump(Path_data, Pathlist)
            Pathlist.close()

            # -- Clear Path_data list
            Path_data.clear()

            # -- Call Set path list function
            # -- For Set all path list frame
            Set_enable_path_list()

            # -- Call Set path function
            Set_path()

    # -- Clear all widget in Enable frame

    for widget in Enable_frame.winfo_children():
        widget.destroy()

    # -- Create Frame

    Path_frame = Frame(Enable_frame, height=150, width=750, bg=Color_list['File_show_canvas_color'],
                       bd=0)
    Path_frame.grid(row=0, column=0)

    # -- Create Path add information label

    Add_path_information = Label(Path_frame, text='Enter path here', bg=Color_list['File_show_canvas_color'],
                                 font=('calibri', 13), bd=0, fg='white')

    Add_path_information.place(x=5, y=5)

    # -- Create Path entry widget

    Path_entry = Entry(Path_frame, bg=Color_list['File_show_canvas_color'], width=55,
                       highlightbackground=Color_list['Entry_color'], highlightthickness=1,
                       highlightcolor=Color_list['Entry_color'], font=('calibri', 13), fg='white',
                       insertbackground='white')
    Path_entry.focus_set()
    Path_entry.place(x=5, y=40)

    """ -- Create Set path button -- """

    Set_path_frame = Frame(Enable_frame, height=30, width=92, bg=Color_list['Base_color'], highlightthickness=1,
                           highlightbackground=Color_list['Button_background'])
    Set_path_frame.place(x=5, y=85)

    # -- Create Set path button
    Set_path_button = Button(Set_path_frame, text='Set Path', bg=Color_list['File_show_canvas_color'],
                             activebackground=Color_list['File_show_canvas_color'], bd=0,
                             fg=Color_list['Button_background'],
                             activeforeground=Color_list['Button_background'], font=('calibri', 13),
                             command=Set_path_in_database)
    Set_path_button.place(x=10, y=7, relheight=0.50)


""" ------------- STORAGE FILE OPTION BUTTON FUNCTION -------------- """

# Create list for storage screen name
Storage_screen_name = []


# Function which set Storage canvas in Main screen
def Store_file_main_button_function():
    """ Store file main button function to show store file """

    if len(Storage_screen_name) == 0:
        Storage_screen_function()
    else:
        Storage_screen_name[0].wm_attributes('-topmost', True)
        Storage_screen_name[0].wm_attributes('-topmost', False)


""" --- Storage screen ---"""


def Storage_screen_function():
    """ ----------- HOVER AND DEHOVER STORE FRAME FUNCTION ------------ """

    # Hover effect function
    def Store_file_frame_hover_effect(event):
        """ Function is set hover effect of Storage file frame """

        Widget = event.widget
        Widget.config(bg='#43434a')

        for sub_widget in Widget.winfo_children():
            sub_widget.config(bg='#43434a', activebackground='#43434a')

    # Dehover effect function
    def Store_file_frame_unhover_effect(event):
        """ Function is set unhover effect of storage file frame """

        Widget = event.widget
        Widget.config(bg=Color_list['File_show_canvas_color'])

        for sub_widget in Widget.winfo_children():
            sub_widget.config(bg=Color_list['File_show_canvas_color'],
                              activebackground=Color_list['File_show_canvas_color'])

    # Function which delete storage file in database
    def Store_delete_file(filename):
        """ Function is delete store file  """

        # -- Create List for store file name
        Store_file_data = []

        # -- Open store file json file
        Store = open(f'C:\\Users\\{Main_username}\\Lion manager\\Store\\Storefile.json', 'r')
        Read_data = json.load(Store)

        # -- Add data ib Store file data list
        Store_file_data.clear()

        for item in Read_data:
            Store_file_data.append(item)

        Store.close()

        # -- Delete this file
        Store_file_data.remove(filename)

        # -- Write data in Json file
        Store = open(f'C:\\Users\\{Main_username}\\Lion manager\\Store\\Storefile.json', 'w')
        json.dump(Store_file_data, Store)
        Store.close()

        # -- Call Set Store file function
        Set_store_file_screen()

    """ --- Canvas scrolling function --- """

    # Enter event function
    def Enter_storage_file_frame(event):
        Display_file_canvas.bind_all('<MouseWheel>', Storage_file_canvas_mousewheel_function)
        Display_file_canvas.bind_all('<Up>', Storage_file_canvas_up_event_function)
        Display_file_canvas.bind_all('<Down>', Storage_file_canvas_down_event_function)

    # Leave event function
    def Leave_storage_file_frame(event):
        Display_file_canvas.unbind_all('<MouseWheel>')
        Display_file_canvas.unbind_all('<Up>')
        Display_file_canvas.unbind_all('<Down>')

    # Mousewheel event function
    def Storage_file_canvas_mousewheel_function(event):
        """ Function for Storage file mousewheel key function """

        Display_file_canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    # Up arrow key function
    def Storage_file_canvas_up_event_function(event):
        """ Up direction event function """
        Display_file_canvas.yview_scroll(1, "units")

    # Down arrow key function
    def Storage_file_canvas_down_event_function(event):
        """ Canvas down arrow event function """
        Display_file_canvas.yview_scroll(-1, "unit")

    # Storage file screen close button function
    def Close_storage_screen():
        """ Function for close this store file screen """

        Storage_screen_name.clear()

        Storage_file_screen.destroy()

    Storage_file_screen = Toplevel(Mainwindow)

    # Set screen height and width
    Storage_height = 600
    Storage_width = 850

    X = (Storage_file_screen.winfo_screenwidth() // 2) - (Storage_width // 2)
    Y = (Storage_file_screen.winfo_screenheight() // 2) - (Storage_height // 2)
    Storage_file_screen.geometry('{}x{}+{}+{}'.format(Storage_width, Storage_height, X, Y))

    # Set title
    Storage_file_screen.title('Store file')

    # Add screen name in list
    Storage_screen_name.clear()
    Storage_screen_name.append(Storage_file_screen)

    # Set resizable off
    Storage_file_screen.resizable(False, False)

    # Set background color
    Storage_file_screen.config(highlightthickness=1, highlightbackground='#9c9c9c', highlightcolor='#9c9c9c')

    # Set screen logo
    Storage_file_screen.iconbitmap(r'Logo.ico')

    # Set Delete attributes for screen
    Storage_file_screen.wm_protocol('WM_DELETE_WINDOW', Close_storage_screen)

    # Set minimize attributes
    Storage_file_screen.wm_transient(Mainwindow)
    """ --- MAIN CANVAS --- """
    Storage_canvas = Canvas(Storage_file_screen, height=Storage_height - 2, width=Storage_width - 2,
                            bg=Color_list['Base_color'],
                            highlightthickness=0)
    Storage_canvas.place(x=0, y=0)

    """ --- CREATE SCROLLING BASE --- """

    # Base-main-frame
    Display_Store_file = Frame(Storage_canvas, height=Storage_height,
                               width=Storage_width,
                               bg=Color_list['File_show_canvas_color'], bd=0)
    Display_Store_file.place(x=0, y=0)

    # Base-canvas
    Display_file_canvas = Canvas(Display_Store_file, height=Storage_height,
                                 width=Storage_width,
                                 bg=Color_list['File_show_canvas_color'], highlightthickness=0)
    Display_file_canvas.place(x=0, y=0)

    # Base-scroll-frame
    Display_frame = Frame(Display_file_canvas, bg=Color_list['File_show_canvas_color'])
    Display_file_canvas.create_window((0, 0), window=Display_frame, anchor='nw')

    def Scroll_function(event):
        Display_file_canvas.configure(scrollregion=Display_file_canvas.bbox('all'))

    Display_frame.bind('<Configure>', Scroll_function)

    # Bind enter and leave event function for binding scrolling function
    Display_frame.bind('<Enter>', Enter_storage_file_frame)
    Display_frame.bind('<Leave>', Leave_storage_file_frame)

    """ --- Open delete image icon --- """

    Delete_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Delete.ico')
    Delete_image = Delete_image.resize((18, 18))
    Delete_image = ImageTk.PhotoImage(Delete_image)

    """ --- FUNCTION WHICH SET STORE FILE FRAME IN Main screen --- """

    def Set_store_file_screen():
        """ Function which set store file in Mainscreen """

        # -- Clear all widget in Enable frame

        for widget in Display_frame.winfo_children():
            widget.destroy()

        # -- Open Store file json file

        Store_data = []

        Storefile = open(f'C:\\Users\\{Main_username}\\Lion manager\\Store\\Storefile.json', 'r')
        Read_data = json.load(Storefile)

        # -- Clear store data list
        Store_data.clear()

        for item in Read_data:
            Store_data.append(item)
        Storefile.close()

        # -- Create var for raw variable
        Store_raw = 0

        if len(Store_data) == 0:

            # Create storage frame
            Store_frame = Frame(Display_frame, height=40, width=838, bg=Color_list['File_show_canvas_color'], bd=0,
                                highlightbackground='#9c9c9c', highlightthickness=1, highlightcolor='#9c9c9c')
            Store_frame.grid(row=Store_raw, column=0, padx=5, pady=8)

            # Create not any file store information label

            Information_label = Label(Store_frame, text='NOT STORE ANY FILE', bg=Color_list['File_show_canvas_color'],
                                      bd=0,
                                      fg='#3bfddc', font=('calibri', 13))
            Information_label.place(x=10, y=6)

        else:
            for store_file in Store_data:

                # -- Get Base file name
                Base_file = os.path.basename(store_file)

                # -- Create Store frame
                Store_frame = Frame(Display_frame, height=40, width=838, bg=Color_list['File_show_canvas_color'], bd=0,
                                    )
                Store_frame.grid(row=Store_raw, column=0, padx=5, pady=8)

                # -- Bind enter event for hover effect
                Store_frame.bind('<Enter>', Store_file_frame_hover_effect)

                # -- Bind Leave event for dehover effect
                Store_frame.bind('<Leave>', Store_file_frame_unhover_effect)

                # -- Create Delete button

                Store_file_delete = Button(Store_frame, image=Delete_image, bg=Color_list['File_show_canvas_color'],
                                           activebackground=Color_list['File_show_canvas_color'], bd=0,
                                           command=lambda path=store_file: Store_delete_file(path))
                Store_file_delete.place(x=5, y=8)
                Store_file_delete.image = Delete_image

                # -- Create store file name button

                Store_file_name = Button(Store_frame, text=f'{Store_raw + 1} {Base_file}',
                                         bg=Color_list['File_show_canvas_color'],
                                         activebackground=Color_list['File_show_canvas_color'], fg='#6ee48f',
                                         activeforeground='#6ee48f', font=('calibri', 13), bd=0,
                                         command=lambda path=store_file: Open_file(path))
                Store_file_name.place(x=30, y=1)

                if Store_raw % 2 != 0:
                    Store_frame.config(highlightbackground='#6ee48f', highlightthickness=1, highlightcolor='#6ee48f')
                    Store_file_name.config(fg='#6ee48f', activeforeground='#6ee48f')

                else:
                    Store_frame.config(highlightbackground='#55e5d7', highlightthickness=1, highlightcolor='#55e5d7')
                    Store_file_name.config(fg='#55e5d7', activeforeground='#55e5d7')

                # -- Update Store raw value
                Store_raw = Store_raw + 1

    Set_store_file_screen()

    Storage_file_screen.mainloop()


""" ------ SETTING SCREEN FUNCTION ------- """

# List for store setting screen name
Setting_screen_name = []


# Function which call setting screen function
def Main_setting_button_function():
    if len(Setting_screen_name) == 1:
        Setting_screen_name[0].wm_attributes('-topmost', True)
        Setting_screen_name[0].wm_attributes('-topmost', False)
    else:
        Setting_screen_code()


# Function which consists setting screen code
def Setting_screen_code():
    """ Function for Setting button --
        -- Which Set Setting screen """

    # close button function
    def Close_Setting_screen_function():
        """ Function for close setting screen """

        Setting_screen_name.clear()

        Setting_screen.destroy()

    def Show_extension_button_function():
        """ Function is set Extension file name in Main screen """

        """ --- CREATE CANVAS BASE --- """

        # Base-main-frame

        Showframe_f1 = Frame(Setting_canvas, height=Height,
                             width=Width - 236,
                             bg=Color_list['Base_color'], bd=0)
        Showframe_f1.place(x=232, y=0)

        # Base-canvas
        Showextension_List_canvas = Canvas(Showframe_f1, width=Width - 236,
                                           height=Height,
                                           bg=Color_list['Base_color'], highlightthickness=0, bd=0)
        Showextension_List_canvas.pack(side="left")

        # Base scrolling frame
        Mainfilefunction_frame = Frame(Showextension_List_canvas, bg=Color_list['Base_color'], height=Height)
        Showextension_List_canvas.create_window((0, 0), window=Mainfilefunction_frame, anchor='nw')

        # Create scrolling function
        def Scroll_function(event):
            Showextension_List_canvas.configure(scrollregion=Showextension_List_canvas.bbox("all"))

        Mainfilefunction_frame.bind("<Configure>", Scroll_function)

        """ --- MOUSEWHEEL SCROLLING FUNCTION --- """

        def Up_direction_function(event):
            """ Function for Going on Up direction function """
            Showextension_List_canvas.yview_scroll(-1, 'unit')

        def Down_direction_function(event):
            """ Function for Going on down direction function """

            Showextension_List_canvas.yview_scroll(1, 'unit')

        def Show_canvas_mouseWheel_function(event):

            """ Function for MouseWheel event for Show canvas """
            Showextension_List_canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

        """ --- BIND SCROLLING FUNCTION ON ENTER AND LEAVE EVENT --- """

        # Enter event function
        def Canvas_enter_function(event):
            """ Enter event function """

            # -- Bind MouseWheel function
            Showextension_List_canvas.bind_all('<MouseWheel>', Show_canvas_mouseWheel_function)

            # -- Bind Up arrow Direction function
            Showextension_List_canvas.bind_all('<Up>', Up_direction_function)

            # -- Bind Down arrow arrow function
            Showextension_List_canvas.bind_all('<Down>', Down_direction_function)

        Mainfilefunction_frame.bind('<Enter>', Canvas_enter_function)

        # Leave event function
        def Canvas_leave_function(event):
            """ Leave event function """
            Showextension_List_canvas.unbind_all('<MouseWheel>')

            Showextension_List_canvas.unbind_all('<Up>')

            Showextension_List_canvas.unbind_all('<Down>')

        Mainfilefunction_frame.bind('<Leave>', Canvas_leave_function)

        """ --- FUNCTION FOR HOVER AND DEHOVER EFFECT --- """

        # Hover effect function
        def Canvas_hover_function(event):
            """ Hover event function """

            Main_widget = event.widget
            Main_widget.config(bg='#4f5156')

            for Sub_widget in Main_widget.winfo_children():
                Sub_widget.config(bg='#4f5156', activebackground='#4f5156')

        # Dehover effect function
        def Canvas_dehover_function(event):

            Main_widget = event.widget
            Main_widget.config(bg=Color_list['Base_color'])

            for sub_widget in Main_widget.winfo_children():
                sub_widget.config(bg=Color_list['Base_color'],
                                  activebackground=Color_list['Base_color'])

        """ ----------- CREATE BASE FOR SHOW EXTENSION LIST OF PARTICULAR FILE --------------- """

        # Base main frame
        ExtensionList_f1 = Frame(Setting_canvas, height=Height,
                                 width=Width - 236,
                                 bg=Color_list['Base_color'], bd=0)

        # Base canvas
        Showextension_List_canvas_1 = Canvas(ExtensionList_f1, width=Width - 236,
                                             height=Height,
                                             bg=Color_list['Base_color'], highlightthickness=0, bd=0)
        Showextension_List_canvas_1.pack(side="left")

        # Base scrolling frame
        ExtensionList_function_frame = Frame(Showextension_List_canvas_1, bg=Color_list['Base_color'], height=Height)
        Showextension_List_canvas_1.create_window((0, 0), window=ExtensionList_function_frame, anchor='nw')

        # Create scrolling function
        def Scroll_function(event):
            Showextension_List_canvas_1.configure(scrollregion=Showextension_List_canvas_1.bbox("all"))

        ExtensionList_function_frame.bind("<Configure>", Scroll_function)

        """ ---------- MOUSEWHEEL SCROLLING FUNCTION -----------"""

        def Extensionlist_mousewheel_function(event):
            """ Function for mouse wheel event """
            Showextension_List_canvas_1.yview_scroll(int(-1 * (event.delta / 120)), 'units')

        def Extension_up_direction(event):
            Showextension_List_canvas_1.yview_scroll(-1, 'unit')

        def Extension_down_direction(event):
            """ Down direction event function """
            Showextension_List_canvas_1.yview_scroll(1, 'unit')

            """ Up direction event function """

        """ ------------- BIND SCROLLING FUNCTION OF ENTER AND LEAVE EVENT WITH FRAME --------------- """

        # Enter event function
        def Extension_enter_function(event):

            Showextension_List_canvas_1.bind_all('<MouseWheel>', Extensionlist_mousewheel_function)
            Showextension_List_canvas_1.bind_all('<Up>', Extension_up_direction)
            Showextension_List_canvas_1.bind_all("<Down>", Extension_down_direction)

        ExtensionList_function_frame.bind('<Enter>', Extension_enter_function)

        # Leave event function
        def Extension_leave_function(event):

            Showextension_List_canvas_1.unbind_all('<MouseWheel>')
            Showextension_List_canvas_1.unbind_all('<Up>')
            Showextension_List_canvas_1.unbind_all('<Down>')

        ExtensionList_function_frame.bind("<Leave>", Extension_leave_function)

        """ -------------- HOVER AND DEHOVER FUNCTION FOR EXTENSION NAME FRAME ------------------ """

        # Hover effect function
        def Extension_hover_function(event):
            """ Function for hover effect """

            Main_widget = event.widget
            Main_widget.config(bg='#4f5156')

            for sub_widget in Main_widget.winfo_children():
                sub_widget.config(bg='#4f5156', activebackground='#4f5156')

        # Dehover effect function
        def Extension_dehover_function(event):
            """ Function for dehover effect """

            Main_widget = event.widget
            Main_widget.config(bg=Color_list['Base_color'])

            for sub_widget in Main_widget.winfo_children():
                sub_widget.config(bg=Color_list['Base_color'],
                                  activebackground=Color_list['Base_color'])

        """ ---- DELETE FILE DATA AND DELETE EXTENSION DATA FUNCTION ---- """

        # Function which delete main file data
        def Delete_main_file_function(filename):
            """ Function for Delete Main file data in Extension.pkl and Folderdata.pkl file """

            Answer = messagebox.askquestion('Lion manager', 'Are you sure you want to delete this file data ?')

            if Answer == 'yes':

                """ -- Delete in extension.pkl file -- """

                # -- Create Dic for store data
                Data = {}

                # -- Open Extension List pickle file for delete data

                Extension = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
                Read_data = pickle.load(Extension)
                Data.update(Read_data)
                Extension.close()

                # -- Clear This file data
                del Data[filename]

                # -- Write data in file\
                Extension = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'wb')
                pickle.dump(Data, Extension)
                Extension.close()

                # -- Clear dic
                Data.clear()

                """ -- Delete in Folderdata pickle file -- """

                Folder_data = {}

                Folder_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'rb')
                Read_data = pickle.load(Folder_file)

                # -- Clear Folder data dic
                Folder_data.clear()

                Folder_data.update(Read_data)
                Folder_file.close()

                # -- Delete file data
                del Folder_data[filename]

                # -- Write in Folder data pickle file
                Folder_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'wb')
                pickle.dump(Folder_data, Folder_file)
                Folder_file.close()

                # -- Clear Folder data dic
                Folder_data.clear()

                # -- Call Setting screen function
                Set_show_extension()

                # -- Call Mainscreen function

                for widget in Extension_Frame.winfo_children():
                    widget.destroy()
                Main_extension_set_function()

            else:
                pass

        # Function which delete extension data of particular file data
        def Delete_extension_value_function(filename, extension_value):
            """ Function for Delete particular extension """

            """ Function is delete particular extension in Extension file data """

            Answer = messagebox.askquestion('Lion manager', 'Are you sure you want to delete this extension ? \n'
                                                            f'{extension_value}')

            if Answer == 'yes':

                # -- Create Data dic for store data
                Data = {}

                # -- Open Extension data pickle file
                Extension = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
                Read_data = pickle.load(Extension)
                Data.update(Read_data)
                Extension.close()

                # -- Get File data
                Last_data = Data[filename]

                # -- Delete extension
                Last_data.remove(extension_value)

                if len(Last_data) == 0:
                    messagebox.showinfo('Lion manager', 'You can not delete this extension because every\n'
                                                        'file require at least one extension')
                else:

                    # -- Remove Last file data in dic
                    del Data[filename]

                    # -- Add New data
                    Add_data = {filename: Last_data}

                    # -- Update Add_data dic
                    Add_data.update(Data)

                    # -- Write Extension data pickle file

                    Extension = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'wb')
                    pickle.dump(Add_data, Extension)
                    Extension.close()

                    # -- Clear Data dic
                    Data.clear()

                    # -- Clear Add data dic
                    Add_data.clear()

                    # -- Call function
                    Function_for_set_extensionList(filename, Last_data)

                    # -- Call Main screen function
                    for widget in Extension_Frame.winfo_children():
                        widget.destroy()

                    Main_extension_set_function()

        """ -- Open Back button image -- """

        Back_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Back button\\Mainframe_back.ico')
        Back_image = ImageTk.PhotoImage(Back_image, master=ExtensionList_function_frame)

        """ ---- RENAME FILE NAME AND RENAME EXTENSION NAME FUNCTION ---- """

        # Function for rename file name
        def Rename_file_name_function(lastfilename):
            """ Function for Rename File name """

            def Change_file_name_main_function():
                """ Function is Rename file name in database """

                if Rename_entry.get() == '':
                    messagebox.showinfo('Lion manager', 'Please,Enter filename in entry widget ')

                else:

                    """ -- Update Extension.pkl file data -- """

                    Extension_data_1 = {}

                    File = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
                    Read_data = pickle.load(File)

                    # -- Update data
                    Extension_data_1.update(Read_data)

                    # -- Close file
                    File.close()

                    # -- Get Filename
                    New_file_name = Rename_entry.get()

                    if New_file_name in Extension_data_1.items():
                        messagebox.showinfo('Lion manager', 'You already set this file name')

                    else:

                        # -- Change File name
                        Extension_data_1[New_file_name] = Extension_data_1.pop(lastfilename)

                        # -- Write in Extension data pickle file
                        File = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'wb')
                        pickle.dump(Extension_data_1, File)
                        File.close()

                        # -- Clear Extension data
                        Extension_data_1.clear()

                        """ -- Update Folder data pickle file -- """

                        Folder_data = {}

                        # -- Read file
                        Folder_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'rb')
                        Folder_data.update(pickle.load(Folder_file))
                        Folder_file.close()

                        # -- Change data
                        Folder_data[New_file_name] = Folder_data.pop(lastfilename)

                        # -- Write in Folder data file
                        Folder_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Folderdata.pkl', 'wb')
                        pickle.dump(Folder_data, Folder_file)
                        Folder_file.close()

                        # -- Clear Folder data dic
                        Folder_data.clear()

                        # -- Call Set data frame function
                        Set_show_extension()

                        # -- Call Main screen function
                        for widget in Extension_Frame.winfo_children():
                            widget.destroy()

                        Main_extension_set_function()
                """ Function for change file name in database """

            """ -- Set setup for Change file name -- """

            # -- Clear all widget in Mainfile frame
            for widget in ExtensionList_function_frame.winfo_children():
                widget.destroy()

            Infor_frame = Frame(ExtensionList_function_frame, height=40, width=Showframe_f1.winfo_screenwidth() - 615,
                                bg='#3b404a',
                                bd=0, highlightbackground='#777778', highlightthickness=1)
            Infor_frame.grid(row=0, column=0, padx=6, pady=5)

            # -- Create Back Button
            Back_button = Button(Infor_frame, image=Back_image, bg='#3b404a', activebackground='#3b404a', bd=0,
                                 command=Set_show_extension)

            Back_button.place(x=8, y=5)
            Back_button.image = Back_image

            # -- Create Filename information label

            File_name_information = Label(Infor_frame, text=f' | {lastfilename}', bg='#3b404a', fg='white',
                                          font=('calibri', 12), bd=0)
            File_name_information.place(x=39, y=7)

            """ -- Create Rename entry content widget -- """

            Rename_frame = Frame(ExtensionList_function_frame, height=250, width=Showframe_f1.winfo_screenwidth() - 615,
                                 bg=Color_list['Base_color'],
                                 bd=0)
            Rename_frame.grid(row=1, column=0, padx=6, pady=5)

            # -- Create Rename file information label
            Rename_information = Label(Rename_frame, text='Enter new Filename', bg=Color_list['Base_color'],
                                       bd=0, fg='white', font=('calibri', 12))
            Rename_information.place(x=5, y=10)

            # -- Create Filename entry widget

            Rename_entry = Entry(Rename_frame, width=25, bg=Color_list['Base_color'],
                                 highlightbackground=Color_list['Entry_color'],
                                 highlightthickness=1, highlightcolor=Color_list['Entry_color'],
                                 insertbackground='white',
                                 fg='white', font=('calibri', 12), bd=0)
            Rename_entry.place(x=5, y=45)
            Rename_entry.focus_set()

            # -- Create Change button
            # -- For set new filename

            Change_frame = Frame(Rename_frame, height=32, width=80, bg=Color_list['Base_color'],
                                 bd=0, highlightbackground=Color_list['Button_background'], highlightthickness=1,
                                 highlightcolor=Color_list['Button_background'])
            Change_frame.place(x=5, y=85)

            Change_button = Button(Change_frame, text='Change', bg=Color_list['Base_color'],
                                   activebackground=Color_list['Base_color'],
                                   fg=Color_list['Button_background'], activeforeground=Color_list['Button_background'],
                                   font=('calibri', 12), bd=0,
                                   command=Change_file_name_main_function)
            Change_button.place(x=9, y=3, relheight=0.80)

        # Function for rename extension name
        def Rename_extension_name_function(last_extension, filename, ex_list):
            """ Function for Rename extension in File data """

            def Rename_extension_name_main_function():
                """ Function which rename extension name in database """

                if Rename_entry.get() == '':
                    messagebox.showinfo('Lion manager', 'Please,Enter new extension in entry widget')

                else:

                    if str(Rename_entry.get())[0:1] != '.':
                        messagebox.showinfo('Lion manager', 'Please,Enter correct extension.\n'
                                                            'Extension format .extension_name')
                    else:

                        # -- Change extension

                        """ -- Open Extension.pkl file -- """

                        Extension_data = {}

                        # -- Read file
                        Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
                        Extension_data.update(pickle.load(Extension_file))
                        Extension_file.close()

                        # -- Get File data
                        File_data = Extension_data[filename]

                        # -- Remove past extension
                        File_data.remove(last_extension)

                        # -- Add new extension
                        File_data.append(Rename_entry.get())

                        # -- Write in file

                        Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'wb')
                        pickle.dump(Extension_data, Extension_file)
                        Extension_file.close()

                        # -- Call Set Extension list function
                        Function_for_set_extensionList(filename, File_data)

                        # -- Call Main screen function
                        for widget in Extension_Frame.winfo_children():
                            widget.destroy()

                        Main_extension_set_function()

            """ -- Set Setup for Rename Extension """

            # -- Clear all widget in Mainfile frame

            for widget in ExtensionList_function_frame.winfo_children():
                widget.destroy()

            Infor_frame = Frame(ExtensionList_function_frame, height=40, width=Showframe_f1.winfo_screenwidth() - 615,
                                bg='#3b404a',
                                bd=0, highlightbackground='#777778', highlightthickness=1)
            Infor_frame.grid(row=0, column=0, padx=6, pady=5)

            # -- Create Back Button
            Back_button = Button(Infor_frame, image=Back_image, bg='#3b404a', activebackground='#3b404a', bd=0,
                                 command=lambda file=filename, list=ex_list: Function_for_set_extensionList(filename,
                                                                                                            list))
            Back_button.place(x=8, y=5)
            Back_button.image = Back_image

            # -- Create Filename information label

            File_name_information = Label(Infor_frame, text=f' | {last_extension}', bg='#3b404a', fg='white',
                                          font=('calibri', 12), bd=0)
            File_name_information.place(x=39, y=7)

            """ -- Create Rename entry content widget -- """

            Rename_frame = Frame(ExtensionList_function_frame, height=250, width=Showframe_f1.winfo_screenwidth() - 615,
                                 bg=Color_list['Base_color'],
                                 bd=0)
            Rename_frame.grid(row=1, column=0, padx=6, pady=5)

            # -- Create Rename file information label
            Rename_information = Label(Rename_frame, text='Enter new extension name (.extension)',
                                       bg=Color_list['Base_color'],
                                       bd=0, fg='white', font=('calibri', 12))
            Rename_information.place(x=5, y=10)

            # -- Create Filename entry widget

            Rename_entry = Entry(Rename_frame, width=25, bg=Color_list['Base_color'],
                                 highlightbackground=Color_list['Entry_color'],
                                 highlightthickness=1, highlightcolor=Color_list['Entry_color'],
                                 insertbackground='white',
                                 fg='white', font=('calibri', 12), bd=0)
            Rename_entry.place(x=5, y=45)
            Rename_entry.focus_set()

            # -- Create Change button
            # -- For set new filename

            Change_frame = Frame(Rename_frame, height=32, width=80, bg=Color_list['Base_color'],
                                 bd=0, highlightbackground=Color_list['Button_background'], highlightthickness=1,
                                 highlightcolor=Color_list['Button_background'])
            Change_frame.place(x=5, y=85)

            Change_button = Button(Change_frame, text='Change', bg=Color_list['Base_color'],
                                   activebackground=Color_list['Base_color'],
                                   fg=Color_list['Button_background'], activeforeground=Color_list['Button_background'],
                                   font=('calibri', 12), bd=0,
                                   command=Rename_extension_name_main_function)
            Change_button.place(x=9, y=3, relheight=0.80)

        """ ---- FUNCTION WHICH SET EXTENSION LIST DATA FRAME ---- """

        def Function_for_set_extensionList(filename, extensionlist):

            """ Function for Set Extension list of particular file
            """

            # -- Disable Main frame
            Showframe_f1.place_forget()

            # -- Set Extension frame
            ExtensionList_f1.place(x=232, y=0)

            for widget in ExtensionList_function_frame.winfo_children():
                widget.destroy()

            # -- Create Information frame

            Infor_frame = Frame(ExtensionList_function_frame, height=40, width=Showframe_f1.winfo_screenwidth() - 615,
                                bg='#3b404a',
                                bd=0, highlightbackground='#777778', highlightthickness=1)
            Infor_frame.grid(row=0, column=0, padx=6, pady=5)

            # -- Create Back Button
            Back_button = Button(Infor_frame, image=Back_image, bg='#3b404a', activebackground='#3b404a', bd=0,
                                 command=Set_show_extension)
            Back_button.place(x=8, y=5)
            Back_button.image = Back_image

            # -- Create Filename information label

            File_name_information = Button(Infor_frame, text=f' | Rename -- {filename}', bg='#3b404a', fg='white',
                                           font=('calibri', 12), bd=0, activebackground='#3b404a',
                                           activeforeground='white',
                                           command=lambda file_name=filename: Rename_file_name_function(file_name))
            File_name_information.place(x=39, y=3)

            List_row = 1

            """ -- Set extension list -- """

            for extension in extensionlist:

                # -- Create Show Extension Frame

                Show_extension = Frame(ExtensionList_function_frame, height=38,
                                       width=Showframe_f1.winfo_screenwidth() - 615,
                                       bg=Color_list['Base_color'],
                                       bd=0, highlightthickness=1)
                Show_extension.grid(row=List_row, column=0, padx=6, pady=5)

                # -- Bind Enter event function
                Show_extension.bind('<Enter>', Extension_hover_function)

                # -- Bind Leave event function
                Show_extension.bind('<Leave>', Extension_dehover_function)

                # -- Create extension value delete button

                Delete_button = Button(Show_extension, image=Delete_image, bd=0, bg=Color_list['Base_color'],
                                       activebackground=Color_list['Base_color'],
                                       command=lambda file_name=filename, list=extension:
                                       Delete_extension_value_function(file_name, list))
                Delete_button.place(x=5, y=7)
                Delete_button.image = Delete_image

                # -- Create Extension name label
                Extension_label = Button(Show_extension, text=extension, fg='white', bg=Color_list['Base_color'],
                                         font=('calibri', 12), activeforeground='white',
                                         bd=0, activebackground=Color_list['Base_color'],
                                         command=lambda lastextension=extension, file_name=filename, list=extensionlist:
                                         Rename_extension_name_function(lastextension, file_name, list))
                Extension_label.place(x=35, y=9, relheight=0.50)

                # -- Set Frame Border color
                if List_row % 2 == 0:
                    Show_extension.config(highlightbackground='#3fc1c9')

                else:
                    Show_extension.config(highlightbackground='#fce38a')

                # -- Update Row value
                List_row = List_row + 1

        """ ---- FUNCTION WHICH ADD ANOTHER EXTENSION IN FILE DATA FUNCTION ---- """

        def Another_extension_function(file_name, extension_list):

            def Another_extension_add_main_function():

                """ Function which add new extension in database """

                # -- Create dic for store data
                Data_dic = {}

                # -- Open extension pickle file
                Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
                Read_data = pickle.load(Extension_file)

                # -- Clear data dic
                Data_dic.clear()
                Data_dic.update(Read_data)

                Extension_file.close()

                if Extension_entry.get() == '':
                    messagebox.showinfo('Lion manager', 'Please,add new extension in entry widget')

                elif Extension_entry.get() in extension_list:
                    messagebox.showinfo('Lion manager', 'You already add this extension in this file data')

                else:

                    if str(Extension_entry.get())[0:1] != '.':
                        messagebox.showinfo('Lion manager', 'Please,Enter correct extension.\n'
                                                            'Extension format .extension_name')
                    else:

                        # -- Add new extension in extension list
                        extension_list.append(Extension_entry.get())

                        # -- Add new data
                        Data_dic[file_name] = extension_list

                        # -- Write data in file
                        Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'wb')
                        pickle.dump(Data_dic, Extension_file)
                        Extension_file.close()

                        # -- Clear Data dic
                        Data_dic.clear()

                        # -- Call Main screen function
                        Set_show_extension()

                        # -- Call Main screen function
                        for widget in Extension_Frame.winfo_children():
                            widget.destroy()

                        Main_extension_set_function()

            """ Function for add another extension in file data """

            """ -- Set Setup for add another extension -- """

            # -- Clear all widget in Main file frame
            for widget in Mainfilefunction_frame.winfo_children():
                widget.destroy()

            # -- Create Back button frame

            Infor_frame = Frame(Mainfilefunction_frame, height=40, width=Showframe_f1.winfo_screenwidth() - 615,
                                bg='#3b404a',
                                bd=0, highlightbackground='#777778', highlightthickness=1)
            Infor_frame.grid(row=0, column=0, padx=6, pady=5)

            # -- Create Back Button
            Back_button = Button(Infor_frame, image=Back_image, bg='#3b404a', activebackground='#3b404a', bd=0,
                                 command=Set_show_extension)
            Back_button.place(x=8, y=5)
            Back_button.image = Back_image

            # -- Create Filename information label

            File_name_information = Label(Infor_frame, text=f' | {file_name}', bg='#3b404a', fg='white',
                                          font=('calibri', 12), bd=0)
            File_name_information.place(x=39, y=7)

            # -- Create Add new extension frame

            New_extension = Frame(Mainfilefunction_frame, heigh=300, width=Showframe_f1.winfo_screenwidth() - 615,
                                  bg=Color_list['Base_color'], bd=0)
            New_extension.grid(row=1, column=0, pady=5, padx=6)

            # -- Create Add another extension name label

            Another_extension_label = Label(New_extension, text='Enter another extension', bg=Color_list['Base_color'],
                                            fg='#9c9c9c', font=('calibri', 12), bd=0)
            Another_extension_label.place(x=5, y=10)

            # -- Create Entry widget

            Extension_entry = Entry(New_extension, bg=Color_list['Base_color'],
                                    highlightbackground=Color_list['Entry_color'],
                                    highlightcolor=Color_list['Entry_color'], highlightthickness=1,
                                    fg='white', insertbackground='white', font=('calibri', 12), bd=0, width=25)
            Extension_entry.focus_set()
            Extension_entry.place(x=5, y=40)

            # -- Add extension button frame
            Add_extension_button_frame = Frame(New_extension, height=32, width=130, bg=Color_list['Base_color'],
                                               bd=0, highlightbackground=Color_list['Button_background'],
                                               highlightthickness=1,
                                               highlightcolor=Color_list['Button_background'])
            Add_extension_button_frame.place(x=5, y=78)

            # -- Create Add extension button
            Add_extension_button = Button(Add_extension_button_frame, text='Add extension', bg=Color_list['Base_color'],
                                          activebackground=Color_list['Base_color'], fg=Color_list['Button_background'],
                                          activeforeground=Color_list['Button_background'], font=('calibri', 12), bd=0,
                                          command=Another_extension_add_main_function)
            Add_extension_button.place(x=10, y=5, relheight=0.60)

        """ ----- FUNCTION WHICH SET ALL FILE FRAME IN MAINSCREEN ----- """

        def Set_show_extension():

            """ Function is set file name list in Show extension canvas """

            # -- Disable Extension list frame
            ExtensionList_f1.place_forget()

            # -- Set Show extension frame
            Showframe_f1.place(x=232, y=0)

            # -- Create dic for store Extension list data
            Extension_data = {}

            # -- Open Extension list pickle file
            Extension_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Extension.pkl', 'rb')
            Read_data = pickle.load(Extension_file)

            # -- Clear Extension data dic
            Extension_data.clear()

            # -- Update dic
            Extension_data.update(Read_data)

            # -- Close File
            Extension_file.close()

            """ -- Clear all widget -- """
            for widget in Mainfilefunction_frame.winfo_children():
                widget.destroy()

            # -- Create Var for Row value
            Show_row_value = 0

            for Extension_name, Extension_list in Extension_data.items():

                # -- Create Show Extension Frame

                Show_extension = Frame(Mainfilefunction_frame, height=38, width=Showframe_f1.winfo_screenwidth() - 615,
                                       bg=Color_list['Base_color'],
                                       bd=0, highlightthickness=1)
                Show_extension.grid(row=Show_row_value, column=0, padx=6, pady=5)

                # -- Bind Enter event function with frame
                Show_extension.bind('<Enter>', Canvas_hover_function)

                # -- Bind Leave event function with frame
                Show_extension.bind('<Leave>', Canvas_dehover_function)
                # -- Create Delete Button
                Delete_button = Button(Show_extension, image=Delete_image, bd=0, bg=Color_list['Base_color'],
                                       activebackground=Color_list['Base_color'],
                                       command=lambda filename=Extension_name: Delete_main_file_function(filename))
                Delete_button.place(x=5, y=7)
                Delete_button.image = Delete_image

                # -- Create Plus button
                # -- For Adding New extension

                Add_extension_button = Button(Show_extension, text='+ ', bg=Color_list['Base_color'],
                                              activebackground=Color_list['Base_color'], font=('calibri', 15), bd=0,
                                              fg='#ffaa00', activeforeground='#ffaa00',
                                              command=lambda filename=Extension_name,
                                                             list=Extension_list: Another_extension_function(filename,
                                                                                                             list))
                Add_extension_button.place(x=35, y=8, relheight=0.50)

                # -- Create First character button
                Extension_name_first = Button(Show_extension, text=Extension_name, bg=Color_list['Base_color'],
                                              activebackground=Color_list['Base_color'], font=('calibri', 11), bd=0,
                                              fg='white', activeforeground='white',
                                              command=lambda filenmae=Extension_name, list=Extension_list:
                                              Function_for_set_extensionList(filenmae, list))
                Extension_name_first.place(x=63, y=9, relheight=0.50)

                # -- Set Frame Border color
                if Show_row_value % 2 == 0:

                    Show_extension.config(highlightbackground='#3fc1c9')

                else:
                    Show_extension.config(highlightbackground='#fce38a')

                # -- Update Row value
                Show_row_value = Show_row_value + 1

            # -- CLear Extension data dic
            Extension_data.clear()

        Set_show_extension()

    """ --- FUNCTION FOR MAIN OPTION BUTTON HOVER AND DEHOVER EFFECT --- """

    def Option_button_hover(event):
        """ Function is set Hover effect of Option button in Setting_frame """

        Widget = event.widget

        Widget.config(fg='#8cfffb', activeforeground='#8cfffb')

    def Option_button_unhover(event):
        """ Function is disable unhover effect of Option button in Setting_frame """

        Widget = event.widget

        Widget.config(fg='#9c9c9c', activeforeground='#9c9c9c')

    Setting_screen = Toplevel(Mainwindow)

    # -- Set screen height and width
    Height = 650
    Width = 1000
    Setting_x = Setting_screen.winfo_screenwidth() // 2 - (Width // 2)
    Setting_y = Setting_screen.winfo_screenheight() // 2 - (Height // 2) - 40

    # Set title
    Setting_screen.title('Setting')

    # -- Set screen geometry
    Setting_screen.geometry('{}x{}+{}+{}'.format(Width, Height, Setting_x, Setting_y))

    # Set resizable off
    Setting_screen.resizable(False, False)

    Setting_screen.wm_protocol('WM_DELETE_WINDOW', Close_Setting_screen_function)

    # -- Add Screen name in List
    Setting_screen_name.clear()
    Setting_screen_name.append(Setting_screen)

    # -- Set screen background color
    Setting_screen.config(bg=Color_list['Base_color'], highlightthickness=1, highlightbackground='#9c9c9c',
                          highlightcolor='#9c9c9c')

    # Set screen logo
    Setting_screen.iconbitmap(r'Logo.ico')

    # -- Create Setting canvas
    Setting_canvas = Canvas(Setting_screen, height=Height - 3,
                            width=Width - 3,
                            bd=0, highlightthickness=1, bg=Color_list['Base_color']
                            , highlightbackground='#9c9c9c', highlightcolor='#9c9c9c')
    Setting_canvas.place(x=0, y=0)

    # -- Create Setting frame
    Setting_frame = Frame(Setting_canvas, width=230, height=Height - 3, bd=0,
                          bg=Color_list['Main_color'])
    Setting_frame.place(x=0, y=0)

    # -- Create Division line
    Setting_canvas.create_line(231, 0, 231, Setting_canvas.winfo_screenheight(), fill='#414141')

    # Delete and rename file data option button

    Show_extension = Button(Setting_frame, text='DELETE | RENAME FILE DATA', bg=Color_list['Main_color'],
                            activebackground=Color_list['Main_color'], bd=0, font=('Calibri', 12), fg='#9c9c9c',
                            activeforeground='#9c9c9c', command=Show_extension_button_function)
    Show_extension.place(x=5, y=8)
    Show_extension.bind('<Enter>', Option_button_hover)
    Show_extension.bind('<Leave>', Option_button_unhover)

    # Add extension in file data option button
    Add_another_extension_button = Button(Setting_frame, text='ADD EXTENSION IN FILE DATA', bg=Color_list['Main_color'],
                                          activebackground=Color_list['Main_color'], fg='#9c9c9c',
                                          activeforeground='#9c9c9c', font=('calibri', 12), bd=0,
                                          command=Show_extension_button_function)
    Add_another_extension_button.place(x=5, y=35)
    Add_another_extension_button.bind('<Enter>', Option_button_hover)
    Add_another_extension_button.bind('<Leave>', Option_button_unhover)

    # Help button function
    Help_button = Button(Setting_frame, text='HELP', bg=Color_list['Main_color'],
                         activebackground=Color_list['Main_color'],
                         fg='#9c9c9c', activeforeground='#9c9c9c', font=('calibri', 13), bd=0)
    Help_button.place(x=5, y=62)
    Help_button.bind('<Enter>', Option_button_hover)
    Help_button.bind('<Leave>', Option_button_unhover)

    """ -- Create Setting screen animation -- """

    Setting_animation_frame = Frame(Setting_canvas, height=75, width=400, bg=Color_list['Base_color'], bd=0)
    Setting_animation_frame.place(x=260, y=15)

    # -- Create Setting label
    Setting_label = Label(Setting_animation_frame, text='Setting....', bg=Color_list['Base_color'],
                          fg='#676767', font=('calibri', 33), bd=0)
    Setting_label.place(x=5, y=2)

    # -- Create List for Setting animation dot value
    Animation_dot_value = [4]

    def Setting_animation():
        """ Function is set animation in setting screen """

        try:

            # -- Update dot value
            Value = int(Animation_dot_value[0])
            Value = Value - 1
            Animation_dot_value.clear()
            Animation_dot_value.append(Value)

            if int(Animation_dot_value[0]) == 0:

                Animation_dot_value.clear()
                Animation_dot_value.append(4)
                Setting_label.config(fg='#1be0dd')

            else:

                Setting_label.config(fg='#676767')

            Dot_text = int(Animation_dot_value[0]) * '.'

            Setting_label.config(text=f'Setting{Dot_text}')

            Call_animation = Timer(1.5, Setting_animation)
            Call_animation.start()
        except:
            pass

    Call_animation = Timer(1.5, Setting_animation)
    Call_animation.start()

    Setting_screen.mainloop()


""" -------------------- MAIN SCREEN FRAME FUNCTION LIST -------------------------- """

""" ------ COPY PATH BUTTON FUNCTION ------ """

# -- Create List for store current copy button name
Current_button = []

# create list for store copied button name
Copied_button = []


# Function which reset all copied button text to Copy path
def Call_function():
    """ Function for set Copied button text to COPY PATH
    after 5 second"""

    try:
        for item in Copied_button:
            item.config(fg='#b6b6b6',
                        text='COPY PATH')
        Copied_button.clear()
    except:
        pass


# Function which add click button name in Current button name list
# This is event button function
def Copy_path_event_function(event):
    """ Function is add Current copy button name in Current_button list """

    Widget = event.widget

    # -- Add button name
    Current_button.clear()
    Current_button.append(Widget)


# Function which copy path and call reset button text function
def Copy_path_function(filepath):
    """ Function for copy path and set button name
    COPY PATH to Copied text """

    Current_button[0].config(fg='#ffae63',
                             text='Copied')

    Path = os.path.normpath(filepath)
    pyperclip.copy(Path)

    # -- Add this button name in Copied _button
    Copied_button.append(Current_button[0])

    Time = Timer(3, Call_function)
    Time.start()


""" --- OPEN FILE FUNCTION --- """


def Open_file(filepath):
    """ Function which open file in window """

    os.startfile(filepath)


""" --- DELETE FILE FUNCTION --- """


# Function for Delete phase 1 searching file
def Delete_file(filepath):
    """ Function for delete file in main machine """

    answer = messagebox.askquestion('Delete file',
                                    'Are you sure you want to delete file ? \n'
                                    f'{filepath}')

    if answer == 'yes':

        # -- Remove from system

        os.remove(filepath)

        # -- Delete all widget in Mainfile frame

        for widget in Mainfile_frame.winfo_children():
            widget.destroy()

        # -- Get Folder name
        Path = os.path.dirname(filepath)

        # -- Get File name
        File_name = os.path.basename(filepath)

        # -- Remove this data from Dir data
        Dir_data[Path].remove(File_name)

        # -- Call Function Option Frame function
        Set_option_frame_function()

        # -- Call Set_main_file_data_function
        Set_main_file_data_function(Main_width - 28)

    else:
        pass


# Function for delete phase 2 searching file
def Delete_folder_file(filepath):
    """ Function is delete folder file """

    answer = messagebox.askquestion('Delete file',
                                    'Are you sure you want to delete file ? \n'
                                    f'{filepath}')

    if answer == 'yes':

        # -- Remove this file
        os.remove(filepath)

        # -- Clear all widget
        for widget in Mainfile_frame.winfo_children():
            widget.destroy()

        # -- Get Folder name
        Path = os.path.dirname(filepath)

        # --Get File name
        File_name = os.path.basename(filepath)

        # -- Remove Data from Dic
        Folder_data[Path].remove(File_name)

        """ -- Call Main screen function -- """
        Set_option_frame_function()

        Set_main_file_data_function(Main_width - 28)

        Set_folder_file_in_main_canvas(Main_width - 28)
    else:
        pass


""" ----- FUNCTION FOR STORE FILE IN SOFTWARE DATABASE ----- """

# -- Create List for Store Current Store File button name
Store_current_button = []

# -- Create List for change store file button value
Active_store_button = []


# Function which reset all store file button text
def Reset_store_file_button():
    """ Function is reset store file button """

    try:
        for item in Active_store_button:
            item.config(fg='#b579ff', activeforeground='#b579ff',
                        text='Store file')

        Active_store_button.clear()
    except:
        pass


# Function which store file in out database
# Main button function
def Store_file_function(filepath):
    """ Function for store file in Storefile json file """

    # -- Create list for store file
    Store_data = []

    # -- Open store file json file

    Storefile = open('C:\\Users\\asd\\Lion manager\\Store\\Storefile.json', 'r')
    Read_data = json.load(Storefile)

    for item in Read_data:
        Store_data.append(item)

    # -- Close file
    Storefile.close()

    if filepath in Store_data:
        pass
    else:
        Store_data.append(filepath)

        # -- Change button text

    # -- Write Store data in json file

    Storefile = open('C:\\Users\\asd\\Lion manager\\Store\\Storefile.json', 'w')
    json.dump(Store_data, Storefile)
    Storefile.close()

    # -- Clear Store data list
    Store_data.clear()

    # -- Change button attributes
    Store_current_button[0].config(text='Store', fg='#ffc400', activeforeground='#ffc400')

    # -- Add this button name Active button name list
    Active_store_button.append(Store_current_button[0])

    # -- Call Timer function
    Reset_store_button = Timer(5, Reset_store_file_button)
    Reset_store_button.start()


# Function which store clicked button name Store current button name llist
def Store_file_event_function(event):
    """ Function is event function of Store file whcih add current store file button
    name in list """

    Widget = event.widget

    # -- Add button name in list
    Store_current_button.clear()
    Store_current_button.append(Widget)


""" --------------- FUNCTION FOR FOLDER FRAME HOVER AND DEHOVER EFFECT ------ """


def Open_folder(path):
    """ Function for open folder in system """

    os.startfile(path)


def folder_frame_hover(event):
    Widget = event.widget
    Widget.config(bg='#43434a')

    for sub_widget in Widget.winfo_children():
        sub_widget.config(bg='#43434a', activebackground='#43434a')


def folder_frame_dehover(event):
    Widget = event.widget
    Widget.config(bg=Color_list['File_show_canvas_color'])

    for sub_widget in Widget.winfo_children():
        sub_widget.config(bg=Color_list['File_show_canvas_color'],
                          activebackground=Color_list['File_show_canvas_color'])


""" -- Main canvas scrolling function -- """


# 1 -- MouseWheel function

def Main_mousewheel_function(event):
    """ Mouse wheel function """

    Mainfile_List_canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')


# 2 -- Up arrow key function
def Up_arrow_function(event):
    """ -- Up arrow key function -- """
    Mainfile_List_canvas.yview_scroll(-1, 'unit')


def Down_arrow_function(event):
    """ Down arrow key function """
    Mainfile_List_canvas.yview_scroll(1, 'unit')


""" -- Extension frame scroll function -- """


def Extension_frame_scroll_function(event):
    """ Extension frame MouseWheel function """

    Extension_List_canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')


""" -- Extension canvas key function -- """

Value = [0]


def extension_up_key(event):
    Extension_List_canvas.yview_scroll(-1, 'unit')


def extension_down_key(event):
    Extension_List_canvas.yview_scroll(1, 'unit')


""" ----------- Enter and Leave event function for Extension frame for scrolling ----------------  """


# Bind all Mousewheel function
def Enter_extension_frame(event):
    # -- Bind MouseWheel event
    Extension_List_canvas.bind_all('<MouseWheel>', Extension_frame_scroll_function)

    # -- Bind up | w | W key for going on Up direction
    Extension_List_canvas.bind_all('<Up>', extension_up_key)
    Extension_List_canvas.bind_all('<W>', extension_up_key)
    Extension_List_canvas.bind_all('<w>', extension_up_key)

    # -- Bind Down | s | S key for going on down direction
    Extension_List_canvas.bind_all('<Down>', extension_down_key)
    Extension_List_canvas.bind_all('<S>', extension_down_key)
    Extension_List_canvas.bind_all('<s>', extension_down_key)


# Unbind all Mousewheel function
def Leave_extension_frame(event):
    # -- Unbind MouseWheel event
    Extension_List_canvas.unbind_all('<MouseWheel>')

    # -- Unbind Up | w | W key for going on Up direction
    Extension_List_canvas.unbind_all('<Up>')
    Extension_List_canvas.unbind_all('<w>')
    Extension_List_canvas.unbind_all('<W>')

    # -- Unbind Down | s | S key for going on Down direction
    Extension_List_canvas.unbind_all('<Down>')
    Extension_List_canvas.unbind_all('<s>')
    Extension_List_canvas.unbind_all('<S>')


""" ---------- Function for search entry in Extension list frame ----------- """


# Function which active search entry state on cursor enter event
def Set_search_entry_function(event):
    """ Enter event function for Search entry widget """

    # -- Set Search entry widget State active
    Search_entry.config(state=NORMAL)


# Function which disable search entry state on cursor leave event
def Reset_search_entry_function(event):
    """ Leave event function for search entry widget """

    # -- Set Search entry widget State Disable
    Search_entry.config(state=DISABLED)


""" -- Enter and Leave event function for Main file frame -- """


def Enter_main_file_frame(event):
    # -- Bind MouseWheel event
    Mainfile_List_canvas.bind_all('<MouseWheel>', Main_mousewheel_function)

    # -- Bind Up | w | W event for going on up direction
    Mainfile_List_canvas.bind_all('<Up>', Up_arrow_function)
    Mainfile_List_canvas.bind_all('<W>', Up_arrow_function)
    Mainfile_List_canvas.bind_all('<w>', Up_arrow_function)

    # -- Bind Down | s | Sf for going on Down direction
    Mainfile_List_canvas.bind_all('<Down>', Down_arrow_function)
    Mainfile_List_canvas.bind_all('<s>', Down_arrow_function)
    Mainfile_List_canvas.bind_all("<S>", Down_arrow_function)


def Leave_main_file_frame(event):
    # -- Unbind MouseWheel event
    Mainfile_List_canvas.unbind_all('<MouseWheel>')

    # -- Unbind Up | w | W key for going on Up direction
    Mainfile_List_canvas.unbind_all('<Up>')
    Mainfile_List_canvas.unbind_all('<w>')
    Mainfile_List_canvas.unbind_all('<W>')

    # -- Unbind down direction event
    Mainfile_List_canvas.unbind_all('<Down>')
    Mainfile_List_canvas.unbind_all('<s>')
    Mainfile_List_canvas.unbind_all('<S>')


""" -- Enter and Leave function for Enable path list frame -- """


def Enter_enable_path_frame(event):
    Enable_List_canvas.bind_all('<MouseWheel>', Enable_path_mousewheel_function)


def Leave_enable_path_frame(event):
    Enable_List_canvas.unbind_all('<MouseWheel>')


""" -- Function for Set Hover effect of Main file Frame -- """


def Main_file_frame_hover_effect(event):
    """ Function is set Mainfile frame Hover effect """

    Widget = event.widget
    Widget.config(bg='#43434a')

    var = 0
    for sub_widget in Widget.winfo_children():

        if var == 0:
            var = 1
        else:
            sub_widget.config(bg='#43434a', activebackground='#43434a')


def Main_file_frame_unhover_effect(event):
    """ Function is set dehover effect of Mainfile frame """

    Widget = event.widget
    Widget.config(bg=Color_list['File_show_canvas_color'])

    var = 0

    for sub_widget in Widget.winfo_children():

        if var == 0:
            var = 1

        else:
            sub_widget.config(bg=Color_list['File_show_canvas_color'],
                              activebackground=Color_list['File_show_canvas_color'])


def Animation_code_function():
    Animation_screen = Tk()

    # -- Set Screen height and width
    Height = 300
    Width = 650
    X = (Animation_screen.winfo_screenwidth() // 2) - (Width // 2)
    Y = (Animation_screen.winfo_screenheight() // 2) - (Height // 2)

    # -- Set Geometry of Animation screen
    Animation_screen.geometry('{}x{}+{}+{}'.format(Width, Height, X, Y))

    # -- Close Title bar
    Animation_screen.overrideredirect(1)

    # -- Set Screen background color and Highlight color
    Animation_screen.config(bg='#202225')

    # -- Create Lion manager Label frame
    Lion_manager = Canvas(Animation_screen, height=350, width=Width, bg='#202225', highlightthickness=0)
    Lion_manager.pack(fill=BOTH)

    # -- Open Lion manger logo image
    Logo_image = Image.open('lion-128 (1).ico')
    Logo_image = Logo_image.resize((85, 85))
    Logo_image = ImageTk.PhotoImage(Logo_image)

    # -- Place Logo image label
    Logo_image_label = Label(Lion_manager, image=Logo_image, bg='#202225', bd=0)
    Logo_image_label.place(x=140, y=100)

    # -- Create Lion manager text label
    Logo_image_text = Label(Lion_manager, text='Lion manager', bg='#202225', fg='#9c9c9c', font=('calibri', 30), bd=0)
    Logo_image_text.place(x=239, y=102)

    # -- Create Version name information label
    Version_name = Label(Lion_manager, text=' version 2021.1.0', bg='#202225', fg='#757575', font=('calibri', 15), bd=0)
    Version_name.place(x=239, y=150)

    def Close_animation_screen_function():
        """ Function which close animation function """

        Animation_screen.destroy()

    Animation_screen.update()
    time.sleep(5)
    Close_animation_screen_function()

    Animation_screen.mainloop()


def Give_call_animation_screen():
    # -- Open Animation data pickle file
    Animation_file = open(f'C:\\Users\\{Main_username}\\Lion manager\\Store\\Animation.pkl', 'rb')
    Read_data = pickle.load(Animation_file)

    if Read_data[0] == 0:
        Animation_code_function()
    else:
        pass


Give_call_animation_screen()

# -- Color List for Extension value
Extension_color = ['#ff7818', '#f8980a', '#f8d40a', '#98f80a', '#40ff0c', '#0cff6d', '#0cff9d', '#0cffce', '#0c8dff',
                   '#0c20ff', '#a10cff', '#f20cff', '#ff0c65', '#ff0c0c']

# -- Create Dic for Color list
Color_list = {
    'close_button_text': '#66686b',
    'Base_color': '#36393F',
    'Main_color': '#2f3136',
    'Extension': '#202225',
    'Option_menu': '#36393f',
    'Option_menu_hover': '#717275',
    'Main_extension_label': '#ffca18',
    'Extension_frame_hover': '#5a5a5b',
    'Show_extension_frame': '#151515',
    'Show_extension_text': '#eaeaea',
    'Show_extension_hover': '#1ce882',
    'Title': '#00fff6',
    'Entry_color': '#00ffa6',
    'Button_background': '#ffbb00',
    'Button_hover': '#fff6dc',
    'Screen_information': '#ff830f',
    'File_show_canvas_color': '#393c42',
}

""" ----- Mainwindow start ---- 
    ----- License information Apache License, Version 2.0 ---- """

Mainwindow = Tk()

# Set zoomed status
Mainwindow.state('zoomed')

# Set Title and Logo
Mainwindow.title("Lion manager")
Mainwindow.iconbitmap(r'Logo.ico')

# Set Minimize screen size
Mainwindow.minsize(850, 600)

# Set Mainwindow background color and other attributes
Mainwindow.config(bd=0, highlightthickness=1, highlightbackground='#9c9c9c', highlightcolor='#9c9c9c')

""" -------------------- CREATE MAINWINDOW CANVAS ----------------------- """

Mainwindow_canvas = Canvas(Mainwindow, bg=Color_list['File_show_canvas_color'], height=Mainwindow.winfo_screenheight(),
                           width=Mainwindow.winfo_screenwidth(), highlightthickness=0)
Mainwindow_canvas.pack(fill=BOTH)

""" ----- Extension list main frame ----- """

# Extension list main frame
Main_extension = Frame(Mainwindow_canvas, height=Mainwindow.winfo_screenheight(), width=275, bg=Color_list['Extension'],
                       )
Main_extension.place(x=0, y=0)

# Function which set active state of search entry in Extension list frame on cursor enter
Main_extension.bind('<Enter>', Set_search_entry_function)

# Function which set disable state of search entry in Extension list frame on leave cursor
Main_extension.bind('<Leave>', Reset_search_entry_function)

""" --- Extension list canvas base --- """

# Base-main-frame
Extension_frame = Frame(Mainwindow_canvas, width=275, height=Mainwindow.winfo_screenheight() - 140, bd=0,
                        bg=Color_list['Extension'], cursor='arrow')
Extension_frame.place(x=0, y=75)

# Base-canvas
Extension_List_canvas = Canvas(Extension_frame, width=275, height=Mainwindow.winfo_screenheight() - 142,
                               highlightthickness=0, bd=0,
                               bg=Color_list['Extension'], cursor='arrow')
Extension_List_canvas.pack(side=LEFT)

# Base-scrolling-frame
Extension_Frame = Frame(Extension_List_canvas, bg=Color_list['Extension'], height=Mainwindow.winfo_screenheight() - 100,
                        cursor='arrow')

Extension_List_canvas.create_window((0, 0), window=Extension_Frame, anchor='nw')


# Scrolling function
def Scroll_function(event):
    Extension_List_canvas.configure(scrollregion=Extension_List_canvas.bbox("all"))


Extension_Frame.bind("<Configure>", Scroll_function)

# Enter event function for Bind all mousewheel function
Extension_Frame.bind('<Enter>', Enter_extension_frame)

# Leave event function for unbind all mousewheel function
Extension_Frame.bind('<Leave>', Leave_extension_frame)

""" ---- Main extension frame information label ---- """

MAIN_LABEL_EXTENSION = Label(Main_extension, text='EXTENSION LIST', bg=Color_list['Extension'],
                             fg=Color_list['Main_extension_label'],
                             font=('calibri', 13), bd=0)
MAIN_LABEL_EXTENSION.place(x=80, y=10)

""" --------- EXTENSION LIST SEARCH BAR FRAME ---------  """

# Search button image
Search_image_main = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Search.ico')
Search_image = ImageTk.PhotoImage(Search_image_main)
Search_image_main.close()

# Back button image
Extension_back_image_main = Image.open(
    f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Back button\\Extension_back.ico')
Extension_back_image = ImageTk.PhotoImage(Extension_back_image_main)
Extension_back_image_main.close()

# Create Search bar frame
Search_frame = Canvas(Main_extension, height=40, width=273, bg=Color_list['Extension'], bd=0, highlightthickness=0)
Search_frame.place(x=0, y=40)

# Create Extension back button
Extension_back_button = Button(Search_frame, image=Extension_back_image, bg=Color_list['Extension'],
                               activebackground=Color_list['Extension'], bd=0,
                               command=Extension_back_button_function)
Extension_back_button.place(x=10, y=5)
Search_frame.create_line(35, 5, 35, 25, fill='#4f4f4f')

# Create Search button
Search_button = Button(Search_frame, image=Search_image, bg=Color_list['Extension'],
                       activebackground=Color_list['Extension'],
                       bd=0, command=Extension_search_button_function)
Search_button.place(x=45, y=5)
Search_frame.create_line(70, 5, 70, 25, fill='#4f4f4f')

""" -------- SEARCH ENTRY WIDGET -------  """

Search_entry = Entry(Search_frame, bg=Color_list['Extension'], bd=0, highlightbackground='#34373a',
                     highlightthickness=1, highlightcolor='#34373a', fg='#9c9c9c', font=('calibri', 12),
                     width=23, insertbackground='#9c9c9c', disabledbackground=Color_list['Extension'])
Search_entry.focus_set()
Search_entry.place(x=75, y=3)

# Open Eye image
Eye_image_main = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Extension_eye.ico')
Eye_image = ImageTk.PhotoImage(Eye_image_main)
Eye_image_main.close()

""" ------- FUNCTION WHICH SET EXTENSION LIST DATA IN FRAME --------- """


def Main_extension_set_function():
    """ This function is set extension list in Mainwindow extension list frame """

    # Thia process for use search button in Extension frame
    if Extension_call[0] == 'Active':

        # Function which update all Extension file data in dic
        Open_extension_file_function()

    else:
        pass

    # Create variable for update raw value
    Extension_row = 0

    for filename, extension in Extension_data.items():
        # -- Get First character for filename
        First_character = str(filename[0:1]).upper()

        # -- Get Foreground color
        FG = random.choice(Extension_color)

        # -- Create Extension shown frame
        Show_frame = Frame(Extension_Frame, height=35, width=257, bg=Color_list['Extension'], bd=0)
        Show_frame.grid(row=Extension_row, column=0, padx=10, pady=5)

        # Hover effect function
        Show_frame.bind('<Enter>', lambda event, widget=Show_frame: Enter_frame(event, widget))

        # Dehover effect
        Show_frame.bind('<Leave>', lambda event, widget=Show_frame: Unhover_frame(event, widget))

        # Function which call Finding file data function same work as file name button
        Show_frame.bind('<Button-1>',
                        lambda event, file_name=filename, list=extension: Extension_frame_function(event, file_name,
                                                                                                   list))
        # -- Create Main short button

        Main_short = Button(Show_frame, text=First_character, fg=FG, activeforeground=FG, bg=Color_list['Extension'],
                            activebackground=Color_list['Extension'], font=('calibri', 12), bd=0,
                            command=lambda filename=filename, extension=extension: Set_extension_list(filename,
                                                                                                      extension)
                            )
        Main_short.place(x=5, y=3)

        # -- Create Full extension filename  button
        Main_full = Button(Show_frame, text=filename, bg=Color_list['Extension'],
                           activebackground=Color_list['Extension'],
                           fg='white', activeforeground='white', font=('calibri', 12), bd=0,
                           command=lambda filename=filename, extension=extension: Set_extension_list(filename,
                                                                                                     extension))
        Main_full.place(x=30, y=4)

        # Eye image
        # For Show Folder in | Folder show functionality active or disable

        Extension_show = Label(Show_frame, image=Eye_image, bd=0, bg=Color_list['Extension'])
        Extension_show.image = Eye_image
        Extension_show.place(x=225, y=8)

        # Function which call set extension frame function for set extension frame
        Extension_show.bind('<Button-1>',
                            lambda event, file=filename: Call_file_data_screen_function(event, file))

        # -- Update Extension row value
        Extension_row = Extension_row + 1


Main_extension_set_function()

# Frame for show Folder in | Folder show functionality of particular file data

Show_extension = Frame(Mainwindow, width=15, bg=Color_list['Show_extension_frame'], bd=0)

""" --- Option menu --- 
    --- Content --> Setting, Add extension, Enable/Disable path, Help """

Option_canvas = Canvas(Mainwindow_canvas, height=45, width=Mainwindow.winfo_screenwidth() - 275,
                       bg=Color_list['Option_menu'],
                       highlightthickness=0)
Option_canvas.place(x=276, y=0)
Option_canvas.create_line(0, 44, Option_canvas.winfo_screenwidth(), 44, fill='#2b2b2b')

""" --- Setting button --- """

# Open setting image
Setting_icon = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Setting.ico')
Setting_image = ImageTk.PhotoImage(Setting_icon)
Setting_icon.close()

# Setting image label
Setting_label = Label(Option_canvas, image=Setting_image, bd=0, bg=Color_list['Option_menu'])
Setting_label.place(x=10, y=9)

# Setting button
Setting_button = Button(Option_canvas, text='Setting', bg=Color_list['Option_menu'],
                        activebackground=Color_list['Option_menu'],
                        fg='#08ddc1', activeforeground='#08ddc1', font=('calibri', 13), bd=0,
                        command=Main_setting_button_function)
Setting_button.place(x=40, y=5)

""" --- Account button --- """
Account_option = Button(Option_canvas, text='Account', bg=Color_list['Option_menu'],
                        activebackground=Color_list['Option_menu'],
                        fg='white', activeforeground='white', font=('calibri', 13), bd=0)
Account_option.place(x=100, y=11, relheight=0.50)

""" -- ADD EXTENSION BUTTON -- """

Add_extension = Button(Option_canvas, text='Add extension', bg=Color_list['Option_menu'],
                       fg=Color_list['Show_extension_text'], font=('calibri', 13), bd=0,
                       command=Add_extension_button)
Add_extension.place(x=170, y=11, relheight=0.50)

# Hover effect
Add_extension.bind('<Enter>',
                   lambda event, widget=Add_extension: widget.config(bg=Color_list['Option_menu_hover'], fg='white',
                                                                     activebackground=Color_list['Option_menu_hover'],
                                                                     activeforeground='white'))

# Dehover effect
Add_extension.bind('<Leave>', lambda event, widget=Add_extension: widget.config(bg=Color_list['Option_menu'],
                                                                                fg=Color_list['Show_extension_text'],
                                                                                activebackground=Color_list[
                                                                                    'Option_menu'],
                                                                                activeforeground=Color_list[
                                                                                    'Show_extension_text']))

""" -- ENABLE | DISABLE PATH -- """

Enable_path = Button(Option_canvas, text='Enable path', bg=Color_list['Option_menu'],
                     fg=Color_list['Show_extension_text'], font=('calibri', 13), bd=0,
                     command=Add_enable_disable_path_button)
Enable_path.place(x=280, y=11, relheight=0.50)

# Hover effect
Enable_path.bind('<Enter>',
                 lambda event, widget=Enable_path: widget.config(bg=Color_list['Option_menu_hover'], fg='white',
                                                                 activebackground=Color_list['Option_menu_hover'],
                                                                 activeforeground='white'))

# Dehover effect
Enable_path.bind('<Leave>', lambda event, widget=Enable_path: widget.config(bg=Color_list['Option_menu'],
                                                                            fg=Color_list['Show_extension_text'],
                                                                            activebackground=Color_list[
                                                                                'Option_menu'],
                                                                            activeforeground=Color_list[
                                                                                'Show_extension_text']))

""" -- STORE FILE -- """

Store_file = Button(Option_canvas, text='Store file', bg='#556f6a', fg='#00ffcc',
                    bd=0, font=('calibri', 12), activebackground='#556f6a', activeforeground='#00ffcc',
                    command=Store_file_main_button_function)
Store_file.place(x=380, y=11, relheight=0.50)

""" --- Help button ---  """

Help_button = Button(Option_canvas, text='Help', bg=Color_list['Option_menu'],
                     activebackground=Color_list['Option_menu'],
                     fg='#ffc71e', activeforeground='#ffc71e', font=('calibri', 12), bd=0)
Help_button.place(x=450, y=11, relheight=0.50)

Close_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Close.ico')
Close_image = ImageTk.PhotoImage(Close_image)

""" ------- ADD EXTENSION FILE DATA CANVAS START -------- """

Add_details = Canvas(Mainwindow, height=Mainwindow.winfo_screenheight(), width=Mainwindow.winfo_screenwidth(),
                     bg=Color_list['Base_color'], highlightthickness=0)

""" --- TITLE BAR ---  """

Title_frame = Frame(Add_details, height=Add_details.winfo_screenheight(), bg=Color_list['Main_color'],
                    width=250)
Title_frame.place(x=0, y=0)

# Close button

Close_button = Button(Title_frame, image=Close_image, bd=0, bg=Color_list['Main_color'],
                      activebackground=Color_list['Main_color'],
                      command=Main_close_button)
Close_button.place(x=100, y=30)

# Escape information label

Close_label = Label(Title_frame, text='ESC', bg=Color_list['Main_color'], fg=Color_list['close_button_text'],
                    font=('calibri', 12), bd=0)
Close_label.place(x=104, y=65)

# Title information label

Add_title = Label(Add_details, text='ADD EXTENSION', fg=Color_list['Title'], bd=0, bg=Color_list['Main_color'],
                  font=('calibri', 13))
Add_title.place(x=60, y=105)

""" --- DATA ENTRY FRAME --- """

Entry_frame = Frame(Add_details, height=Add_details.winfo_screenheight(), bg=Color_list['Base_color'], bd=0,
                    width=Add_details.winfo_screenwidth() - 250)
Entry_frame.place(x=251, y=0)

""" -- File name entry widget -- """

File_name = Label(Entry_frame, text='File name :', bg=Color_list['Base_color'], fg='white', font=('calibri', 13), bd=0)
File_name.place(x=10, y=107)

File_name_entry = Entry(Entry_frame, highlightthickness=1, highlightbackground=Color_list['Entry_color'],
                        highlightcolor=Color_list['Entry_color'], width=35, insertbackground='white',
                        fg='white', font=('calibri', 12), bd=0, bg=Color_list['Base_color'])
File_name_entry.place(x=95, y=107)
File_name_entry.focus_set()

""" --- Extension name entry widget --- """

Extension_name = Label(Entry_frame, text='Extension :', bg=Color_list['Base_color'], fg='white',
                       font=('calibri', 13), bd=0)
Extension_name.place(x=10, y=145)

Extension_name_entry = Entry(Entry_frame, highlightthickness=1, highlightbackground=Color_list['Entry_color'],
                             highlightcolor=Color_list['Entry_color'], width=35, insertbackground='white',
                             fg='white', font=('calibri', 12), bd=0, bg=Color_list['Base_color'])
Extension_name_entry.place(x=95, y=145)

""" --- SET FILE DATA BUTTON --- """

Set_frame = Frame(Entry_frame, width=130, height=30, bg=Color_list['Base_color'], highlightthickness=1,
                  highlightbackground=Color_list['Button_background'])
Set_frame.place(x=10, y=190)

# Set data button
Set_extension = Button(Set_frame, text='Set data', bg=Color_list['Base_color'], fg=Color_list['Button_background'],
                       activeforeground=Color_list['Button_background'], font=('calibri', 13), bd=0,
                       activebackground=Color_list['Base_color'],
                       command=Set_extension_button_function)
Set_extension.place(x=27, y=7, relheight=0.50)

""" -------------------------------- ENABLE PATH | DISABLE PATH CANVAS --------------------------------- """

Enable_path_canvas = Canvas(Mainwindow, height=Mainwindow.winfo_screenheight(), width=Mainwindow.winfo_screenwidth(),
                            bg=Color_list['Base_color'], highlightthickness=0)

""" --- TITLE BAR --- """

Enable_title = Frame(Enable_path_canvas, height=Mainwindow.winfo_screenheight(), width=250,
                     bg=Color_list['Main_color'])
Enable_title.place(x=0, y=0)

# Close button

Close_button = Button(Enable_title, image=Close_image, bd=0, bg=Color_list['Main_color'],
                      activebackground=Color_list['Main_color'],
                      command=Main_close_button)
Close_button.place(x=100, y=30)

# ESC key information label

Close_label = Label(Enable_title, text='ESC', bg=Color_list['Main_color'], fg=Color_list['close_button_text'],
                    font=('calibri', 12), bd=0)
Close_label.place(x=104, y=65)

""" --- Enable/ Disable canvas option --- 
    --- Option 1 = Enable/Disable path 
    --- Option 2 = Add new path option """

# Option 1

Enable_title_1 = Button(Enable_title, text='Enable / Disable path', bg=Color_list['Main_color'], fg=Color_list['Title'],
                        font=('calibri', 13), bd=0, activebackground=Color_list['Main_color'],
                        command=Set_enable_path_list)
Enable_title_1.place(x=45, y=103)

# Option 2

Enable_add_path = Button(Enable_title, text='Add new path', bg=Color_list['Main_color'],
                         activebackground=Color_list['Main_color'],
                         fg=Color_list['Title'], activeforeground=Color_list['Title'], font=('calibri', 13), bd=0,
                         command=Enable_add_new_path)
Enable_add_path.place(x=45, y=135)

""" --- CREATE CANVAS BASE ---  """

# Set height and width
Enable_width = Mainwindow.winfo_screenwidth() - 250
Enable_Height = Mainwindow.winfo_screenheight()

# Base-main-frame
Enable_F1 = Frame(Enable_path_canvas, width=Enable_width, height=Enable_Height, bd=0,
                  bg=Color_list['File_show_canvas_color'])
Enable_F1.place(x=256, y=0)

# Base-canvas
Enable_List_canvas = Canvas(Enable_F1, width=Enable_width, height=Enable_Height,
                            bg=Color_list['File_show_canvas_color'],
                            highlightthickness=0, bd=0)
Enable_List_canvas.pack(side="left")

# Base-scroll-frame
Enable_frame = Frame(Enable_List_canvas, bg=Color_list['File_show_canvas_color'], height=Enable_Height)
Enable_List_canvas.create_window((0, 0), window=Enable_frame, anchor='nw')


# Create scrolling function
def Scroll_function(event):
    Enable_List_canvas.configure(scrollregion=Enable_List_canvas.bbox("all"))


Enable_frame.bind("<Configure>", Scroll_function)

# Bind enter event function for active scrolling function
Enable_frame.bind('<Enter>', Enter_enable_path_frame)

# Bind leave event function for disable scrolling function
Enable_frame.bind('<Leave>', Leave_enable_path_frame)

""" ----------------------------- CREATE MAINWINDOW CANVAS BASE ----------------------------------- """

# Set height and width
Height = Mainwindow.winfo_screenheight() - 44
Main_width = Mainwindow.winfo_screenwidth() - 275

""" -- Start canvas base -- """

# Base-main-frame
Mainfile_F1 = Frame(Mainwindow_canvas, width=Main_width, height=Height, bd=0, bg=Color_list['File_show_canvas_color'])
Mainfile_F1.place(x=276, y=86)

# Base-canvas
Mainfile_List_canvas = Canvas(Mainfile_F1, width=Main_width, height=Height - 107,
                              bg=Color_list['File_show_canvas_color'],
                              highlightthickness=0, bd=0)
Mainfile_List_canvas.pack(side="left")

# Base-scroll-frame
Mainfile_frame = Frame(Mainfile_List_canvas, bg=Color_list['File_show_canvas_color'], height=Height)
Mainfile_List_canvas.create_window((0, 0), window=Mainfile_frame, anchor='nw')


# Create scrolling function
def Scroll_function(event):
    Mainfile_List_canvas.configure(scrollregion=Mainfile_List_canvas.bbox("all"))


Mainfile_frame.bind("<Configure>", Scroll_function)

# Bind enter event function for active scrolling function
Mainfile_frame.bind('<Enter>', Enter_main_file_frame)

# Bind leave event function for disable scrolling function
Mainfile_frame.bind('<Leave>', Leave_main_file_frame)

""" --------------------------------- MAIN SCREEN FUNCTION ------------------------------ """

""" --- Open delete image icon --- """

Delete_image_main = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Delete.ico')
Delete_image_main = Delete_image_main.resize((18, 18))
Delete_image = ImageTk.PhotoImage(Delete_image_main)
Delete_image_main.close()

# Create var for raw value
List_raw_value = [0]


# Function which set Option frame

def Set_option_frame_function():
    """ Function is set Option Frame """

    """ --- Content -- Folder in option, Folder show option, Back button option """

    def Folder_in_function():
        """ Function is set only Folder in file data in Main screen """

        # -- Clear All widget in Mainfile frame
        for widget in Mainfile_frame.winfo_children():
            widget.destroy()

        if Select_filename_function_data[0] == 'ACTIVE':

            # -- Update List raw list value
            List_raw_value.clear()
            List_raw_value.append(0)

            if len(Folder_data) == 0:

                # If not found any file in particular folder than this functionality run

                # -- Create Notification frame
                Notification_frame = Frame(Mainfile_frame, height=30, width=Main_width - 28,
                                           bg=Color_list['File_show_canvas_color'],
                                           bd=0)
                Notification_frame.grid(row=0, column=0, pady=7, padx=8)

                # -- Create Information label
                Information_label = Label(Notification_frame, text='NOT FOUND ANY DATA IN FOLDER',
                                          bg=Color_list['File_show_canvas_color'],
                                          font=('calibri', 13), bd=0, fg='#ffa200')
                Information_label.place(x=5, y=5)

                # -- Update All frame
                Mainfile_F1.update()
                Mainfile_List_canvas.update()
                Mainfile_frame.update()

            else:

                # If find data in particular folder than call main screen function

                # -- Call set folder file function
                Set_folder_file_in_main_canvas(Main_width - 28)

        else:

            # -- Create Notification frame
            Notification_frame = Frame(Mainfile_frame, height=30, width=Main_width - 28,
                                       bg=Color_list['File_show_canvas_color'],
                                       bd=0)
            Notification_frame.grid(row=0, column=0, pady=7, padx=8)

            # -- Create Information label
            Information_label = Label(Notification_frame, text='YOU DISABLE THIS OPTION',
                                      bg=Color_list['File_show_canvas_color'],
                                      font=('calibri', 13), bd=0, fg='#ffa200')
            Information_label.place(x=5, y=5)

            # -- Update All frame
            Mainfile_F1.update()
            Mainfile_List_canvas.update()
            Mainfile_frame.update()

    """ --- FOLDER SHOW BUTTON FUNCTION --- """

    def Folder_Show_function():
        """ Function is set only main file in Main window """

        # -- Clear all widget
        for widget in Mainfile_frame.winfo_children():
            widget.destroy()

        # -- Set List raw value
        List_raw_value.clear()
        List_raw_value.append(0)

        if Select_filename_function_data[1] == 'ACTIVE':

            if len(Folder_list) == 0:

                # -- Set Not found any folder frame

                Notification_frame = Frame(Mainfile_frame, height=30, width=Main_width - 28,
                                           bg=Color_list['File_show_canvas_color'],
                                           bd=0)
                Notification_frame.grid(row=0, column=0, pady=7, padx=8)

                # -- Create Information label
                Information_label = Label(Notification_frame, text='YOU DISABLE THIS OPTION',
                                          bg=Color_list['File_show_canvas_color'],
                                          font=('calibri', 13), bd=0, fg='#ffa200')
                Information_label.place(x=5, y=5)

                # -- Update all frame
                Mainfile_F1.update()
                Mainfile_List_canvas.update()
                Mainfile_frame.update()

            else:

                # -- Call function
                Set_folder_data(Main_width - 28)

        else:

            # -- Create Notification frame
            Notification_frame = Frame(Mainfile_frame, height=30, width=Main_width - 28,
                                       bg=Color_list['File_show_canvas_color'],
                                       bd=0)
            Notification_frame.grid(row=0, column=0, pady=7, padx=8)

            # -- Create Information label
            Information_label = Label(Notification_frame, text='YOU DISABLE THIS OPTION',
                                      bg=Color_list['File_show_canvas_color'],
                                      font=('calibri', 13), bd=0, fg='#ffa200')
            Information_label.place(x=5, y=5)

            # -- Update all frame
            Mainfile_F1.update()
            Mainfile_List_canvas.update()
            Mainfile_frame.update()

    """ --- BACK BUTTON FUNCTION --- """

    def Back_button_function():
        """ Function is set Back all file in screen """

        # -- Clear all widget
        for widget in Mainfile_frame.winfo_children():
            widget.destroy()

        # -- Call to Function
        Set_main_file_data_function(Main_width - 28)

        if Select_filename_function_data[0] == 'ACTIVE':
            Set_folder_file_in_main_canvas(Main_width - 28)
        else:
            pass

    # -- Create Option frame
    Information_frame = Canvas(Mainwindow_canvas, height=40, width=Mainwindow.winfo_screenwidth() - 275,
                               bg=Color_list['Option_menu'], highlightthickness=0
                               )
    Information_frame.place(x=276, y=46)
    Information_frame.create_line(0, 39, Information_frame.winfo_screenwidth(), 39, fill='#2b2b2b')

    # -- Open Back button image
    Back = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Back button\\Mainframe_back.ico')
    Back_image = ImageTk.PhotoImage(Back)

    # -- Create Back button
    File_back_button = Button(Information_frame, image=Back_image, bd=0, bg=Color_list['Option_menu'],
                              activebackground=Color_list['Option_menu'],
                              command=Back_button_function)
    File_back_button.place(x=10, y=8)
    File_back_button.image = Back_image

    # -- Create Line 1
    Information_frame.create_line(50, 8, 50, 35, fill='#5e5e5f')

    # -- Create Folder in Button
    Folder_in_button = Button(Information_frame, text='FILE IN FOLDER', font=('calibri', 12), bd=0,
                              fg='#03f5b4', activeforeground='#03f5b4', bg=Color_list['Option_menu'],
                              activebackground=Color_list['Option_menu'],
                              command=Folder_in_function)
    Folder_in_button.place(x=61, y=8, relheight=0.60)

    # -- Create Line 2
    Information_frame.create_line(180, 8, 180, 35, fill='#5e5e5f')

    # -- Create Folder show button
    Folder_show = Button(Information_frame, text='FOLDER SHOW',
                         fg='#f5c803', activeforeground='#03f5b4', font=('calibri', 12), bd=0,
                         bg=Color_list['Option_menu'], activebackground=Color_list['Option_menu'],
                         command=Folder_Show_function)
    Folder_show.place(x=188, y=8, relheight=0.60)

    """ --- Create Function of Hover and Unhover effect of Folder in and Folder show button --- """

    """ -- Start Folder in button effect -- """

    # -- Bind hover effect of Folder in button
    def Folder_in_hover(event):
        Folder_in_button.config(bg=Color_list['Extension_frame_hover'],
                                activebackground=Color_list['Extension_frame_hover'])

    Folder_in_button.bind('<Enter>', Folder_in_hover)

    # -- Bind dehover effect with Folder in button
    def Folder_in_dehover(event):
        Folder_in_button.config(bg=Color_list['Option_menu'], activebackground=Color_list['Option_menu'])

    Folder_in_button.bind('<Leave>', Folder_in_dehover)

    """ -- Start Folder show button effect -- """

    # -- Bind hover effect with Folder show button
    def Folder_show_hover(event):
        Folder_show.config(bg=Color_list['Extension_frame_hover'],
                           activebackground=Color_list['Extension_frame_hover'])

    Folder_show.bind('<Enter>', Folder_show_hover)

    # -- Bind dehover effect with folder show button
    def Folder_show_dehover(event):
        Folder_show.config(bg=Color_list['Option_menu'], activebackground=Color_list['Option_menu'])

    Folder_show.bind('<Leave>', Folder_show_dehover)


# Function which set searching phase 1 data in screen
# Main data
def Set_main_file_data_function(x):
    """ Function is set File data in Main screen which Find by particular function """

    # -- Clear all widget in Mainfile frame

    for widget in Mainfile_frame.winfo_children():
        widget.destroy()

    Mainfile_List_canvas.yview_moveto(0)

    """ -- Set List raw value to --> 0 """

    List_raw_value.clear()
    List_raw_value.append(0)

    """ -- Set File data -- """

    for Folder_name, File_data in Dir_data.items():

        if len(File_data) == 0:
            pass
        else:
            """ -- Create Folder name label -- """

            # -- Folder label information
            # -- Background color = #38544c
            # -- Foreground color = #43b581

            # -- Get Folder name
            Main_folder_name = os.path.basename(Folder_name)

            Folder_label = Label(Mainfile_frame, text=Main_folder_name, bg='#38524C',
                                 fg='#43B581', font=('calibri', 12))
            Folder_label.grid(row=int(List_raw_value[0]), column=0, pady=5)

            # -- Update List raw value
            Value = int(List_raw_value[0])
            Value = Value + 1
            List_raw_value.clear()
            List_raw_value.append(Value)

            """ -- Read File_data and create File name frame -- """

            for file_name in File_data:

                """ -- Start File Frame -- 
                                                    -- Content 1 Short file name
                                                               2 Full file name
                                                               3 Copy path button
                                                               4 Store file button
                                                               5 Folder name button
                                                               6 Delete file button """

                # -- Create First character
                First = str(file_name).upper()[0:1]

                # -- Get Background color

                global BG

                try:
                    BG = Character_color[First]
                except:
                    BG = random.choice(Extension_color)

                # 1 -- Create Shown frame
                Shown_frame = Canvas(Mainfile_frame, height=60, width=x, bg=Color_list['File_show_canvas_color'],
                                     bd=0,
                                     highlightbackground='#9c9c9c', highlightthickness=1)
                Shown_frame.grid(row=int(List_raw_value[0]), column=0, pady=7, padx=8)

                # -- Bind Enter event with shown frame
                # -- For active hover effect
                Shown_frame.bind('<Enter>', Main_file_frame_hover_effect)

                # -- Bind leave event with shown frame
                # -- For Disable hover effect
                Shown_frame.bind('<Leave>', Main_file_frame_unhover_effect)

                # 2 -- Create Short file name button
                Main_button = Button(Shown_frame, text=First, bg=BG, font=('calibri', 15), bd=0,
                                     width=6, height=1, activebackground=BG,
                                     command=lambda filepath=f'{Folder_name}//{file_name}': Open_file(filepath))
                Main_button.place(x=5, y=11)

                # 3 -- Create Full file name button

                File_name = Button(Shown_frame, text=file_name, bg=Color_list['File_show_canvas_color'],
                                   font=('calibri', 13), fg='#8cfffb', bd=0, width=70, anchor='nw',
                                   activebackground=Color_list['File_show_canvas_color'],
                                   activeforeground='#8cfffb',
                                   command=lambda filepath=f'{Folder_name}\\{file_name}': Open_file(filepath))
                File_name.place(x=85, y=2)

                # 4  -- Create Copy path button
                File_path = Button(Shown_frame, text='COPY PATH', bg=Color_list['File_show_canvas_color'], bd=0,
                                   activebackground=Color_list['File_show_canvas_color'], fg='#b6b6b6',
                                   activeforeground='#ffae63', font=('calibri', 11),
                                   command=lambda filepath=f'{Folder_name}\\{file_name}': Copy_path_function(
                                       filepath))
                File_path.place(x=85, y=28)

                # -- Bind Button-1 event with Copy path button
                File_path.bind('<Button-1>', Copy_path_event_function)

                # -- Create Line 1
                Shown_frame.create_line(195, 30, 195, 55, fill='#9c9c9c')

                # 5 -- Create Delete file button
                Delete_button = Button(Shown_frame, image=Delete_image, bg=Color_list['File_show_canvas_color'],
                                       activebackground=Color_list['File_show_canvas_color'], bd=0,
                                       command=lambda filepath=f'{Folder_name}\\{file_name}': Delete_file(filepath))
                Delete_button.place(x=200, y=32)
                Delete_button.image = Delete_image

                # -- Create Line 2
                Shown_frame.create_line(225, 30, 225, 55, fill='#9c9c9c')

                # 6 -- Create Store file button
                Store_file_button = Button(Shown_frame, text='Store file', bg=Color_list['File_show_canvas_color'],
                                           activebackground=Color_list['File_show_canvas_color'], fg='#b579ff',
                                           activeforeground='#b579ff', font=('calibri', 12), bd=0,
                                           command=lambda
                                               filepath=f'{Folder_name}\\{file_name}': Store_file_function(
                                               filepath))
                Store_file_button.place(x=228, y=29)

                # -- Bind Button-1 event with Store file button
                Store_file_button.bind('<Button-1>', Store_file_event_function)

                # -- Create Line 3
                Shown_frame.create_line(295, 30, 295, 55, fill='#9c9c9c')

                # 7 -- Create Folder name information label
                Folder_NAME = Button(Shown_frame, text=f'Folder =  {Main_folder_name}',
                                     bg=Color_list['File_show_canvas_color'],
                                     fg='#ff8c8c',
                                     font=('calibri', 12), anchor='nw', bd=0,
                                     activebackground=Color_list['File_show_canvas_color'],
                                     activeforeground='#ff8c8c',
                                     command=lambda filepath=Folder_name: Open_file(filepath))
                Folder_NAME.place(x=300, y=32)

                # -- Update List raw value
                Value = int(List_raw_value[0])
                Value = Value + 1
                List_raw_value.clear()
                List_raw_value.append(Value)


# Function which set searching phase 2 data in screen
# Folder in data
def Set_folder_file_in_main_canvas(x):
    """ Function is set folder data in """

    for folder_name, file_data in Folder_data.items():

        """ -- Create Folder name label -- """

        # -- Get folder name using folder_name
        folder_1 = os.path.basename(folder_name)

        # -- Update List row value
        Value = List_raw_value[0]
        Value = Value + 1
        List_raw_value.clear()
        List_raw_value.append(Value)

        # -- Create Folder information label
        # -- Background color = #38524C
        # -- Foreground color = #43B581

        Folder_info = Label(Mainfile_frame, text=folder_1, font=('calibri', 13), bd=0,
                            bg='#38524C', fg='#43B581')
        Folder_info.grid(row=List_raw_value[0], column=0, pady=5)

        # -- Update List raw value
        Value = List_raw_value[0]
        Value = Value + 1
        List_raw_value.clear()
        List_raw_value.append(Value)

        """ -- Start to Set Folder file frame  -- """

        for folder_list in file_data:

            """ Frame content """

            # -- Get First character of file name
            First = str(folder_list[0:1]).upper()

            # -- Get Background color

            global BG_Color

            try:
                BG_Color = Character_color[First]
            except:
                BG_Color = random.choice(Extension_color)

            """ --- Create  File shown frame """

            Shown_frame = Canvas(Mainfile_frame, height=60, width=x, bg=Color_list['File_show_canvas_color'], bd=0,
                                 highlightbackground='#9c9c9c', highlightthickness=1)
            Shown_frame.grid(row=List_raw_value[0], column=0, pady=7, padx=8)

            # -- Bind Enter effect with Shown frame
            # -- For Active hover effect
            Shown_frame.bind('<Enter>', Main_file_frame_hover_effect)

            # -- Bind leave effect with shown frame
            # -- For Disable hover effect
            Shown_frame.bind('<Leave>', Main_file_frame_unhover_effect)

            # -- Create Main button

            Main_button = Button(Shown_frame, text=First, bg=BG_Color, font=('calibri', 15), bd=0,
                                 width=6, height=1, activebackground=BG_Color,
                                 command=lambda filepath=f'{folder_name}//{folder_list}': Open_file(filepath))
            Main_button.place(x=5, y=11)

            # -- Create Full file name button

            File_name = Button(Shown_frame, text=folder_list, bg=Color_list['File_show_canvas_color'],
                               font=('calibri', 13), fg='#8cfffb', bd=0, width=50, anchor='nw',
                               activebackground=Color_list['File_show_canvas_color'], activeforeground='#8cfffb',
                               command=lambda filepath=f'{folder_name}//{folder_list}': Open_file(filepath))
            File_name.place(x=85, y=2)

            # -- Create path shown button

            File_path = Button(Shown_frame, text='COPY PATH', bg=Color_list['File_show_canvas_color'], bd=0,
                               activebackground=Color_list['File_show_canvas_color'], fg='#b6b6b6',
                               activeforeground='#ffae63', font=('calibri', 11),
                               command=lambda path=f'{folder_name}\\{folder_list}': Copy_path_function(path))
            File_path.place(x=85, y=28)

            # -- Bind button-1 event with Copy Path button
            File_path.bind('<Button-1>', Copy_path_event_function)

            # -- Create Line 1
            Shown_frame.create_line(195, 30, 195, 55, fill='#9c9c9c')

            # -- Create delete button

            Delete_button = Button(Shown_frame, image=Delete_image, bg=Color_list['File_show_canvas_color'],
                                   activebackground=Color_list['File_show_canvas_color'], bd=0,
                                   command=lambda filepath=f'{folder_name}\\{folder_list}': Delete_folder_file(
                                       filepath))
            Delete_button.place(x=200, y=32)
            Delete_button.image = Delete_image

            # -- Create Line 2
            Shown_frame.create_line(225, 30, 225, 55, fill='#9c9c9c')

            # -- Create Store file button

            Store_file_button = Button(Shown_frame, text='Store file', bg=Color_list['File_show_canvas_color'],
                                       activebackground=Color_list['File_show_canvas_color'], fg='#b579ff',
                                       activeforeground='#b579ff', font=('calibri', 12), bd=0,
                                       command=lambda path=f'{folder_name}\\{folder_list}': Store_file_function(path))
            Store_file_button.place(x=228, y=29)

            # -- Bind Button-1 function with Store file button
            Store_file_button.bind('<Button-1>', Store_file_event_function)

            # -- Create Line 3
            Shown_frame.create_line(295, 30, 295, 55, fill='#9c9c9c')

            # -- Create folder name label

            Folder_name = Button(Shown_frame, text=f'Folder =  {folder_1}', bg=Color_list['File_show_canvas_color'],
                                 fg='#ff8c8c',
                                 font=('calibri', 12), anchor='nw', bd=0,
                                 activebackground=Color_list['File_show_canvas_color'],
                                 activeforeground='#ff8c8c',
                                 command=lambda filepath=f'{folder_name}': Open_file(filepath))
            Folder_name.place(x=300, y=32)

            # -- Update List row value
            Value = List_raw_value[0]
            Value = Value + 1
            List_raw_value.clear()
            List_raw_value.append(Value)


# Open Folder image

F_folder = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Other\\Folder.ico')
F_folder = F_folder.resize((20, 20))
F_folder_image = ImageTk.PhotoImage(F_folder)


# Function which set Folder in Main screen
def Set_folder_data(x):
    for folder_name in Folder_list:

        # -- Folder name

        Folder = os.path.basename(folder_name)

        # -- Get First character
        First = str(Folder[0:1]).upper()

        # -- Get Background color

        global Folder_color

        try:
            Folder_color = Color_list[First]
        except:
            Folder_color = random.choice(Extension_color)

        """ -- Create Folder information shown frame """

        Shown_frame = Canvas(Mainfile_frame, height=40, width=x, bg=Color_list['File_show_canvas_color'], bd=0,
                             highlightthickness=1)
        Shown_frame.grid(row=List_raw_value[0], column=0, pady=7, padx=8)

        # Bind Hover effect
        Shown_frame.bind('<Enter>', folder_frame_hover)

        # Bind Dehover effect
        Shown_frame.bind('<Leave>', folder_frame_dehover)

        # -- Create Main character button
        Folder_button = Button(Shown_frame, image=F_folder_image, bd=0, bg=Color_list['File_show_canvas_color'],
                               activebackground=Color_list['File_show_canvas_color'],
                               command=lambda path=folder_name: Open_folder(path))

        Folder_button.place(x=10, y=10)
        Folder_button.image = F_folder_image

        # -- Create Folder name button
        Folder_name = Button(Shown_frame, text=Folder, bg=Color_list['File_show_canvas_color'],
                             activebackground=Color_list['File_show_canvas_color'], font=('calibri', 13), bd=0,
                             command=lambda path=folder_name: Open_folder(path))
        Folder_name.place(x=40, y=3)

        # -- Update List canvas value

        Value = List_raw_value[0]
        Value = Value + 1

        # -- Clear List canvas list

        List_raw_value.clear()
        List_raw_value.append(Value)

        # -- Set Frame Highlight background color

        if int(List_raw_value[0]) % 2 == 0:
            Shown_frame.config(highlightbackground='#7cdda5', highlightthickness=1)
            Folder_name.config(fg='#7cdda5', activeforeground='#7cdda5')
        else:
            Shown_frame.config(highlightbackground='#e7c661', highlightthickness=1)
            Folder_name.config(fg='#e7c661', activeforeground='#e7c661')


""" -- Start Main screen animation -- """

# -- Create animation frame
Main_animation_frame = Frame(Mainfile_frame, height=250, width=650, bg=Color_list['File_show_canvas_color'], bd=0)
Main_animation_frame.grid(row=0, column=0, pady=7, padx=10)

# -- Open Logo image
# -- Layer 1
# -- Foreground color = #00FFEE

Logo_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Animation\\Main_logo.ico')
Logo_image = Logo_image.resize((80, 80))
Logo_image = ImageTk.PhotoImage(Logo_image)

# -- Open Layer 2 image
# -- Foreground color = #3CC1B8

Layer2_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Animation\\Layer2.ico')
Layer2_image = Layer2_image.resize((80, 80))
Layer2_image = ImageTk.PhotoImage(Layer2_image)

# -- Open Layer 3 image
# -- Foreground color = #53948F

Layer3_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Animation\\Layer3.ico')
Layer3_image = Layer3_image.resize((80, 80))
Layer3_image = ImageTk.PhotoImage(Layer3_image)

# -- Open Layer 4 image
# -- Foreground color = #4E5A59

Layer4_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Animation\\Layer4.ico')
Layer4_image = Layer4_image.resize((80, 80))
Layer4_image = ImageTk.PhotoImage(Layer4_image)

# -- Open Layer 5 image
# -- Foreground color = #393C42

Layer5_image = Image.open(f'C:\\Users\\{Main_username}\\Lion manager\\Image\\Animation\\Layer5.ico')
Layer5_image = Layer5_image.resize((80, 80))
Layer5_image = ImageTk.PhotoImage(Layer5_image)

""" -- Create Logo image label -- """

Logo_image_label = Label(Main_animation_frame, image=Logo_image, bg=Color_list['File_show_canvas_color'], bd=0)
Logo_image_label.place(x=30, y=10)

""" -- Create Software name label  -- """
Software_name = Label(Main_animation_frame, text='Lion manager', bg=Color_list['File_show_canvas_color'], bd=0,
                      font=('calibri', 28))
Software_name.place(x=120, y=25)

# -- Create List for update Image one by one
Animation_value = [1]

# -- Create List for Call forward and reverse image
# -- 0 for go 1 to 5
# -- 1 for go 5 to 1

Forward_reverse_value = [0]

""" -------------- MAIN SCREEN ANIMATION FUNCTION -------------- """


def Main_animation_function():
    try:
        # -- Set Image one by one

        if Animation_value[0] == 1:

            # -- Set Image
            Logo_image_label.config(image=Logo_image)
            Logo_image_label.image = Logo_image

            # -- Set label of fg
            Software_name.config(fg='#00FFEE')

        elif Animation_value[0] == 2:

            Logo_image_label.config(image=Layer2_image)
            Logo_image_label.image = Layer2_image

            Software_name.config(fg='#3CC1B8')

        elif Animation_value[0] == 3:

            Logo_image_label.config(image=Layer3_image)
            Logo_image_label.image = Layer3_image

            Software_name.config(fg='#53948F')

        elif Animation_value[0] == 4:

            Logo_image_label.config(image=Layer4_image)
            Logo_image_label.image = Layer4_image

            Software_name.config(fg='#4E5A59')

        else:

            Logo_image_label.config(image=Layer5_image)
            Logo_image_label.image = Layer5_image

            Software_name.config(fg='#393C42')
        # -- Check Animation value 5 or not

        if int(Animation_value[0]) == 5:

            # -- Update Animation value
            Animation_value.clear()
            Animation_value.append(5)

            # -- Update Forward animation value
            Forward_reverse_value.clear()
            Forward_reverse_value.append(1)

        elif int(Animation_value[0]) == 0:

            # -- Update Animation value
            Animation_value.clear()
            Animation_value.append(0)

            # -- Update Forward animation value
            Forward_reverse_value.clear()
            Forward_reverse_value.append(0)
        else:
            pass

        # -- Update Animation value

        if int(Forward_reverse_value[0]) == 0:

            # -- Update Animation value
            Value = int(Animation_value[0])
            Value = Value + 1
            Animation_value.clear()
            Animation_value.append(Value)

        else:

            # -- Update Animation value
            Value = int(Animation_value[0])
            Value = Value - 1
            Animation_value.clear()
            Animation_value.append(Value)

        # -- Call Animation function again
        Call_animation = Timer(2, Main_animation_function)
        Call_animation.start()

    except:
        pass


Call_animation = Timer(0, Main_animation_function)
Call_animation.start()

""" --------------- MAINWINDOW BINDING FUNCTION -------------- """

Mainwindow.bind('<Escape>', Escape_function)

# Binding Button-3 event function for disable File data functionality frame
Mainwindow.bind('<Button-3>', Disable_show_extension)


def Map_event_function(event):
    """ Function for map event for mainwindow """

    try:

        if len(Setting_screen_name) == 1:
            Setting_screen_name[0].deiconify()
        else:
            pass

        if len(Storage_screen_name) == 1:
            Storage_screen_name[0].deiconify()
        else:
            pass
    except:
        pass


Mainwindow.bind('<Map>', Map_event_function)


def Unmap_event_function(event):
    """ Unmap event function """

    try:

        if len(Setting_screen_name) == 1:
            Setting_screen_name[0].iconify()
        else:
            pass

        if len(Storage_screen_name) == 1:

            Storage_screen_name[0].iconify()
        else:
            pass
    except:
        pass


Mainwindow.bind('<Unmap>', Unmap_event_function)
Mainwindow.overrideredirect(1)
Mainwindow.overrideredirect(0)

Mainwindow.mainloop()

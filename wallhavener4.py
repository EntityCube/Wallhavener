# A Wallpaper downloader app using wallhaven api

# imports
import os
import ctypes
import platform
import requests
import time
import random
from pprint import pprint
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from threading import Thread
import pdb  # for debugging
from tkinter import Message

# --- Program Functions ---

# function to set categoryArr
categoryArr = [1, 0, 0]  # general, anime, people


def set_category(toggle):
    global categoryArr

    if (toggle == 'general'):
        toggle_category(0)
    elif (toggle == 'anime'):
        toggle_category(1)
    elif (toggle == 'people'):
        toggle_category(2)

    toggle_category_color()


def toggle_category(pos):
    global categoryArr

    if (categoryArr[pos] == 0):
        categoryArr[pos] = 1
    else:
        categoryArr[pos] = 0
        if not(1 in categoryArr):
            categoryArr[pos] = 1

    # print(categoryArr)


def toggle_category_color():
    if (categoryArr[0] == 0):
        generalBT.configure(style='Inactive.TButton')
    else:
        generalBT.configure(style='Active.TButton')

    if (categoryArr[1] == 0):
        animeBT.configure(style='Inactive.TButton')
    else:
        animeBT.configure(style='Active.TButton')

    if (categoryArr[2] == 0):
        peopleBT.configure(style='Inactive.TButton')
    else:
        peopleBT.configure(style='Active.TButton')


# function to set purtiy
purityArr = [1, 0, 0]  # sfw, sketchy, nsfw


def set_purity(toggle):
    global purityArr

    if (toggle == 'sfw'):
        toggle_purity(0)
    elif (toggle == 'sketchy'):
        toggle_purity(1)
    elif (toggle == 'nsfw'):
        toggle_purity(2)

    toggle_purity_color()


def toggle_purity(pos):
    global purityArr

    if (purityArr[pos] == 0):
        purityArr[pos] = 1
    else:
        purityArr[pos] = 0
        if not(1 in purityArr):
            purityArr[pos] = 1

    # print(purityArr)


def toggle_purity_color():
    if (purityArr[0] == 0):
        sfwBT.configure(style='Inactive.TButton')
    else:
        sfwBT.configure(style='Active.TButton')

    if (purityArr[1] == 0):
        sketchyBT.configure(style='Inactive.TButton')
    else:
        sketchyBT.configure(style='Active.TButton')

    if (purityArr[2] == 0):
        # nsfwBT.configure(style='Inactive.TButton')
        # apikeyLB.place_forget()  # hide api label
        # apikeyEN.place_forget()  # hide api entry
        # apikeyEN.configure(state='disabled')
        pass

    else:
<<<<<<< HEAD
        nsfwBT.configure(style='Active.TButton')
        # apikeyLB.place(relx=0.01, rely=0.25, relwidth=0.17)  # show api label
        # apikeyEN.place(relx=0.22, rely=0.25, relwidth=0.7)  # show api entry
        apikeyEN.configure(state='enabled')
=======
        pass
        # nsfwBT.configure(style='Active.TButton')
        # apikeyLB.place(relx=0.01, rely=0.25, relwidth=0.17)  # show api label
        # apikeyEN.place(relx=0.22, rely=0.25, relwidth=0.7)  # show api entry
        # apikeyEN.configure(state='enabled')
>>>>>>> 5b03881f0fb3f5b8753a432a677a7a439456907e

        # api_cache()


# function to set api cache
def api_cache():
    global run
    global apikey

    getapi = 'get your api from: https://wallhaven.cc/settings/account'
    apiEntryState = str(apikeyEN.cget('state'))

    if os.path.exists('.apicache.ini'):
        # print('api cache exists')
        with open('.apicache.ini', 'r') as api_cache:
            api_cached_key = api_cache.read()

            if (api_cached_key):
                if apiEntryState == 'disabled':
                    apikeyEN.config(state='enabled')
                    apikeyEN.delete(0, END)
                    apikeyEN.insert(0, api_cached_key)
                    apikeyEN.config(state='disabled')
                else:
                    apikeyEN.delete(0, END)
                    apikeyEN.insert(0, api_cached_key)

                apikey = api_cached_key

            else:
                # print('no api found!')
                # print(apikeyEN.cget('state'))
                if apiEntryState == 'disabled':
                    apikeyEN.config(state='enabled')
                    apikeyEN.delete(0, END)
                    apikeyEN.insert(0, getapi)
                    apikeyEN.config(state='disabled')
                else:
                    apikeyEN.delete(0, END)
                    apikeyEN.insert(0, getapi)

    else:
        if apiEntryState == 'disabled':
            apikeyEN.config(state='enabled')
            apikeyEN.delete(0, END)
            apikeyEN.insert(0, getapi)
            apikeyEN.config(state='disabled')
        else:
            apikeyEN.delete(0, END)
            apikeyEN.insert(0, getapi)


# function for api input
apikey = ''


def on_apikey_input(event):
    entry = apikeyEN.get()
    set_apikey(entry)


def set_apikey(value):
    global apikey
    apikey = value
    # print(apikey)


# function for setting sorting
sorting = 'date_added'


def on_sorting_selected(event):
    global topRange
    selected_sorting = sortingCB.get()
    set_sorting(selected_sorting)

    if (selected_sorting == 'toplist' or selected_sorting == 'toplist-beta'):
        topRange = '1M'
        topRangeCB.place(relx=0.75, rely=0.27, relwidth=0.2)
    else:
        topRangeCB.place_forget()
        topRange = ''


def set_sorting(value):
    global sorting
    sorting = value
    # print(sorting)


# function for setting toprange
topRange = '1M'


def on_top_range_selected(event):
    selected_top_range = topRangeCB.get()
    set_top_range(selected_top_range)


def set_top_range(value):
    global topRange
    topRange = value
    # print(topRange)


# function for setting order
order = 'desc'


def set_order():
    order = sortingOrderVar.get()
    # print(order)


# function for setting resolution
atleast = ''
resolutions = ''


def on_resolution_selected(event):
    global ratios
    selected_resolution = resolutionCB.get()
    set_resolution(selected_resolution)

    if (selected_resolution != 'Any' and resolutionVar.get() == 'exact'):
        ratioCB.current(0)
        ratios = ''
        ratioCB.place_forget()
        ratioLB.place_forget()
    else:
        ratioCB.place(relx=0.65, rely=0.4, relwidth=0.2)
        ratioLB.place(relx=0.53, rely=0.415, relwidth=0.1)


def set_resolution(value):
    global atleast
    global resolutions

    if (value == 'Any'):
        resolutions = ''
        atleast = ''
    elif(resolutionVar.get() == 'atleast'):
        resolutions = ''
        atleast = value
    elif(resolutionVar.get() == 'exact'):
        resolutions = value
        atleast = ''

    # print('res', resolutions)
    # print('atl', atleast)


# function for setting exact and atleast
def on_exact_or_atleast():
    selected_resolution = resolutionCB.get()
    set_resolution(selected_resolution)

    if (selected_resolution != 'Any' and resolutionVar.get() == 'exact'):
        ratioCB.place_forget()
        ratioLB.place_forget()
    else:
        ratioCB.place(relx=0.65, rely=0.4, relwidth=0.2)
        ratioLB.place(relx=0.53, rely=0.415, relwidth=0.1)


# function for setting ratio
ratios = ''
ratios_list = ['Any', '16x9', '32x9', '9x16']


def on_ratio_selected(even):
    selected_ratio = ratioCB.get()
    set_ratio(selected_ratio)


def set_ratio(value):
    global ratios
    if (value == 'Any'):
        ratios = ''
    else:
        ratios = value


# function to set page
page = ''


def on_page_selected(event):
    selected_page = pageCB.get()
    set_page(selected_page)


def set_page(value):
    global page
    if (value == 'Any'):
        page = ''
    else:
        page = value

    # print(page)


# function for timeout entry
timeout = 0


def on_timeout_input(event):
    entry = timeoutEN.get()
    if(validate_timeout_input(entry)):
        set_timeout(entry)


def set_timeout(value):
    global timeout
    timeout = int(value)
    # print(timeout)


def validate_timeout_input(value):
    if value:
        try:
            if (value != 0):
                int(value)
            

            # print(value)
            return True
        except ValueError:
            timeoutEN.delete(0, END)
            # print('deleted')
            return False
    else:
        return False


# function for run toggle
run = False


def toggle_running():
    global run

    set_settings()  # set parameters
    if (run is False):
        runBT.configure(text='Stop')
        run = True
        toggle_setting_widgets(True)
    elif (run is True):
        runBT.configure(text='Run')
        run = False
        toggle_setting_widgets(False)
        statusVar.set('Not Running')
    # connecting to real functions
    main()


def toggle_setting_widgets(running):
    global runBTcolor
    if running:
        runBTcolor = '#FF5722'
        gui_style()
    else:
        runBTcolor = '#00C853'
        gui_style()


def StartThread():
    thread = Thread(target=loop)
    thread.daemon = True
    thread.start()

# ****** PROGRAM REAL FUNCTIONS ********
# from multiprocessing import Process


def main():
    global run
    # print(run)
    # if run:
    # print('Starting')
    # else:
    # print('Stopping')


def set_apicache():
    # print('saving api key', apikey)
    with open('.apicache.ini', 'w') as apicache:
        apicache.write(apikey)


def loop():
    global statusVar
    global loopTimeout
    global run

    while 1:
        while run:
            # print('looping x')
            fetch()

            for i in range(loopTimeout, 0, -1):
                if not run:
                    break
                else:
                    time.sleep(1)
                    statusVar.set(i-1)
                    # print(i)

        time.sleep(1)

# functions for collecting walls
# variabels


# starting thread and run loop function
# this runs in background and check for run and stop
StartThread()
url = 'https://wallhaven.cc/api/v1/search'


def fetch():
    set_params()
    global params
    # print(params)
    global lastpage
    global response
    global run
    global lastSetWallpaper

    response_code = 0
    try:
        if run:
            # print('sending api----------------------')
            print(params)
            statusVar.set('sending api request')
            response = requests.get(url, params=params)
            response_code = response.status_code
    except Exception:
        # print('No internet Error')
        statusVar.set('Network Error')
        toggle_running()

    # print(response_code)
    if (run and validate_response_code(response_code)):
        set_lastpage()

        wallpaper_list = filter_wall_urls(response)

        if (wallpaper_list and run):
            chosen_wallpaper = random.choice(wallpaper_list)
            lastSetWallpaper = chosen_wallpaper

            # pprint(chosen_wallpaper)
            chosen_wallpaper = chosen_wallpaper['path']
            if(download_wall(chosen_wallpaper) and run):
                currentPlatform = platform.system()
                # print(currentPlatform)
                set_wallpaper(currentPlatform)

        else:
            statusVar.set('wallpapers no match found with current parameters')
            # print('no wallpapers recieved')
            toggle_running()


def set_wallpaper(platform):  # need more compatibility
    global run

    if (platform == 'Linux'):
        set_wall_on_linux()

    elif (platform == 'Windows'):
        set_wall_on_windows()

    elif (platform == 'Darwin'):
        toggle_running()
        statusVar.set('This app is not supported in mac now')

    else:
        statusVar.set('This platform not supported now')


def set_lastpage():
    global page
    global response
    global lastpage

    lastpage = response.json()['meta']['last_page']

    if (page == ''):
        lastpage = response.json()['meta']['last_page']
    elif (page == '1'):
        lastpage = 1
    elif(int(page.split('-')[0]) <= lastpage):
        lastpage = int(page.split('-')[1])

    # print(lastpage, '= lastpage')


def set_wall_on_windows():
    statusVar.set('setting wallpaper')
    global wallpath

    if (saveVar.get()):

        dirpath = os.getcwd()
        imgpath = wallpath
        wallpath = os.path.join(dirpath, imgpath)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpath, 3)

        statusVar.set(f'{wallpath} wallpaper set and saved')
    else:
        dirpath = os.getcwd()
        imgpath = '.wallpaper.jpg'
        wallpath = os.path.join(dirpath, imgpath)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpath, 3)

        statusVar.set('wallpaper set')
        # print('wallpaper applied')


def set_wall_on_linux():  # need more methods for all linux
    set_wall_method_feh()


def set_wall_method_feh():
    statusVar.set('setting wallpaper using feh')
    global wallpath
    if (saveVar.get()):
        os.system(f'feh {wallpath} --bg-fill')
        statusVar.set(f'{wallpath} wallpaper set and saved')
    else:
        os.system('feh .wallpaper.jpg --bg-fill')
        statusVar.set('wallpaper set')
        # print('wallpaper applied')


def download_wall(url):
    global wallpath
    global run

    # test if already downloaded
    wallname = url.split('/')[-1].split('?')[0]
    wallpath = f'Wallpapers/{wallname}'

    if os.path.isfile(wallpath):
        # print("Image found in cache")
        # statusVar.set('Wallaper found in saved')
        return True

    if (saveVar.get()):
        # print(wallpath)
        newpath = r'Wallpapers'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
    else:
        wallpath = '.wallpaper.jpg'

    try:
        if run:
            statusVar.set(f'downloading: {url}')
            response = requests.get(url, allow_redirects=True)
            open(wallpath, 'wb').write(response.content)
            # print('Wallpaper downloaded')
            return True
    except:
        statusVar.set(f'error downloading: {url}')
        # print('Error downloading wallpaper')
        toggle_running()
        return False


lastSetWallpaper = {'path': ''}


def filter_wall_urls(response):
    global lastSetWallpaper

    statusVar.set('filtering urls')
    response_json = response.json()
    response_list = response_json['data']
    collected_wall_urls = []
    for item in response_list:
        # filter the new list from last set wallpaper to avoid duplication
        if(item['path'] != lastSetWallpaper['path']):
            collected_wall_urls.append(item)

    return collected_wall_urls


def validate_response_code(code):
    global purityArr

    statusVar.set('validating response code')
    if (code == 200):
        statusVar.set('response code okay')

        set_apicache()  # set api key cache
        return True

    else:

        statusVar.set(f'bad response code {code}')

        if (code == 401):
            toggle_running()
            statusVar.set('invalid apikey')
            apikeyEN.delete(0, END)
            getapi = 'get your api from: https://wallhaven.cc/settings/account'
            apikeyEN.insert(0, getapi)

        return False


lastpage = 1


def set_settings():
    global apikey

    global reqApikey
    global reqCategories
    global reqPurity
    global reqSorting
    global reqOrder
    global reqTopRange
    global reqAtleast
    global reqResolutions
    global reqRatios
    global reqTags

    global timeout
    global loopTimeout

    category = concatenate_list_data(categoryArr)
    purity = concatenate_list_data(purityArr)

    reqCategories = category
    reqPurity = purity
    
    tags = tagsEN.get()

    # dont use api key if nsfw purity is off
    if (purityArr[2] != 0):
        reqApikey = apikey
    else:
        reqApikey = ''

    reqSorting = sorting
    reqOrder = order
    reqTopRange = topRange
    reqAtleast = atleast
    reqResolutions = resolutions
    reqRatios = ratios
    reqTags = tags

    loopTimeout = timeout


def set_params():  # This function is called everytime when requesting for new wallpaper

    global params
    global lastpage
    global categoryArr
    global purityArr

    global reqApikey
    global reqCategories
    global reqPurity
    global reqSorting
    global reqOrder
    global reqTopRange
    global reqAtleast
    global reqResolutions
    global reqRatios
    global reqTags

    random_page = random.randint(1, lastpage)

    params = {'apikey': reqApikey,
              'categories': reqCategories,
              'purity': reqPurity,
              'sorting': reqSorting,
              'order': reqOrder,
              'topRange': reqTopRange,
              'atleast': reqAtleast,
              'resolutions': reqResolutions,
              'ratios': reqRatios,
              'q': reqTags,

              # random page needs will be 1 on first api call
              # on 1st request we get lastpage number
              # after 1st request everything will be random according to settings
              'page': random_page
              }


def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result


#  *********** GUI ****************
WIDTH = 450
HEIGHT = 650

# COLORS
# bg
canvasbg = '#212121'
framebg = '#3F51B5'
redbg = '#f44336'
greenbg = '#4CAF50'
# fg
whitefg = '#FFF'

runBTcolor = '#00C853'

root = ThemedTk(theme='equilux')
# root.resizable(False, False)
root.minsize(WIDTH, HEIGHT)
root.title('Wallhavener')
root.attributes("-alpha", 0.93)

# root.update_idletasks()
# root.overrideredirect(True)
# root.wait_visibility(root)
# root.attributes('-type', 'normal')
# root.attributes('-alpha', 0.8)

# Styling * ---- *


def gui_style():

    root.configure(background=canvasbg)

    style = ttk.Style()

    style.configure('TRadiobutton', foreground='white', background=canvasbg)
    # configure label
    style.configure('TLabel', background=canvasbg, foreground=whitefg)

    # configure buttons

    style.configure('Inactive.TButton',
                    background='#37474F', foreground=whitefg)
    style.configure('Active.TButton', background='#039BE5', foreground=whitefg)

    # bakcground fix
    style.configure('TButton', background=canvasbg, foreground=whitefg)
    style.configure('TCombobox', background=canvasbg)
    style.configure('TEntry', background=canvasbg, foreground=whitefg)
    style.configure('TCheckbutton', background=canvasbg, foreground=whitefg)

    style.configure('Run.TButton', background=runBTcolor, foreground=whitefg)
    # hidden
    # entry button
    style.map("TEntry", background=[("disabled", '#37474F')])
    canvas.configure(bg=canvasbg)

    # * --------------- *


# Main Canvas
canvas = Canvas(root, bd=0, bg=canvasbg, highlightthickness=0)
canvas.pack()


gui_style()

# Categories
categoryLB = ttk.Label(root, text='Category:', anchor='e', width=8)
categoryLB.place(relx=0.01, rely=0.03, relwidth=0.17)

generalBT = ttk.Button(text='General', width=6, style='Active.TButton',
                       command=lambda: set_category('general'))
generalBT.place(relx=0.22, rely=0.03, relwidth=0.2)

animeBT = ttk.Button(text='Anime', width=6, style='Inactive.TButton',
                     command=lambda: set_category('anime'))
animeBT.place(relx=0.47, rely=0.03, relwidth=0.2)

peopleBT = ttk.Button(text='People', width=6, style='Inactive.TButton',
                      command=lambda: set_category('people'))
peopleBT.place(relx=0.72, rely=0.03, relwidth=0.2)
# ----------

# Purity label and 3 buttons
purtiyLB = ttk.Label(root, text='Purity:', anchor='e', width=8)
purtiyLB.place(relx=0.01, rely=0.09, relwidth=0.17)

sfwBT = ttk.Button(text='SFW', width=6, style='Active.TButton',
                   command=lambda: set_purity('sfw'))
sfwBT.place(relx=0.22, rely=0.09, relwidth=0.2)

sketchyBT = ttk.Button(text='Sketchy', width=6,
                       style='Inactive.TButton', command=lambda: set_purity('sketchy'))
sketchyBT.place(relx=0.47, rely=0.09, relwidth=0.2)

<<<<<<< HEAD
nsfwBT = ttk.Button(text='NSFW', width=6, style='Inactive.TButton',
                    command=lambda: set_purity('nsfw'))
nsfwBT.place(relx=0.72, rely=0.09, relwidth=0.2)

# Api entry
apikeyLB = ttk.Label(root, text='Api key:', anchor='e', width=8)
apikeyLB.place(relx=0.01, rely=0.15, relwidth=0.17)
# apikeyLB.place_forget()

apikeyEN = ttk.Entry(root, width=30, state='disabled')
apikeyEN.place(relx=0.22, rely=0.15, relwidth=0.7)
=======
# nsfwBT = ttk.Button(text='NSFW', width=6, style='Inactive.TButton',
                    # command=lambda: set_purity('nsfw'))
# nsfwBT.place(relx=0.72, rely=0.15, relwidth=0.2)

# Api entry
# apikeyLB = ttk.Label(root, text='Api key:', anchor='e', width=8)
# apikeyLB.place(relx=0.01, rely=0.25, relwidth=0.17)
# apikeyLB.place_forget()

# apikeyEN = ttk.Entry(root, width=30, state='disabled')
# apikeyEN.place(relx=0.22, rely=0.25, relwidth=0.7)
>>>>>>> 5b03881f0fb3f5b8753a432a677a7a439456907e
# apikeyEN.place_forget()
# apikeyEN.bind('<KeyRelease>', on_apikey_input)
# apikeyEN.bind('<FocusOut>', on_apikey_input)


# Tags
tagsLB = ttk.Label(root, text='Tags:', anchor='e', width=8)
tagsLB.place(relx=0.01, rely=0.21, relwidth=0.17)

tagsEN = ttk.Entry(root, width=30)
tagsEN.place(relx=0.22, rely=0.21, relwidth=0.7)


# sorting methods
sortingLB = ttk.Label(root, text='Sort By:', anchor='e', width=8)
sortingLB.place(relx=0.01, rely=0.28, relwidth=0.17)

sortingMethodList = ['date_added', 'relevance', 'random',
                     'views', 'favorites', 'toplist', 'toplist-beta']
sortingCB = ttk.Combobox(root, values=sortingMethodList,
                         width=10, state='readonly')
sortingCB.current(0)
sortingCB.place(relx=0.22, rely=0.27, relwidth=0.5)
sortingCB.bind('<<ComboboxSelected>>', on_sorting_selected)
# ---------------

# top range ! show only when sorting method is toplist
topRangeList = ['1d', '3d', '1w', '1M', '3M', '6M', '1y']
topRangeCB = ttk.Combobox(root, values=topRangeList, width=3, state='readonly')
topRangeCB.current(3)
topRangeCB.place(relx=0.75, rely=0.27, relwidth=0.2)
topRangeCB.place_forget()
topRangeCB.bind('<<ComboboxSelected>>', on_top_range_selected)
# -------------

# sorting order
# asc
sortingOrderVar = StringVar()
ascRB = ttk.Radiobutton(
    root, text='Asc', variable=sortingOrderVar, value='asc', command=set_order)
ascRB.place(relx=0.22, rely=0.33)
# desc
descRB = ttk.Radiobutton(
    root, text='Desc', variable=sortingOrderVar, value='desc', command=set_order)
descRB.place(relx=0.4, rely=0.33)
descRB.invoke()
# -------------

# Resolution
resolutionLB = ttk.Label(root, text='Resolution:', anchor='e', width=8)
resolutionLB.place(relx=0.01, rely=0.415, relwidth=0.19)

resolutionList = ['Any', '1280x720', '1600x900',
                  '1920x1080', '2560x1440', '3840x2160']
resolutionCB = ttk.Combobox(
    root, values=resolutionList, width=10, state='readonly')
resolutionCB.place(relx=0.22, rely=0.4, relwidth=0.3)
resolutionCB.bind('<<ComboboxSelected>>', on_resolution_selected)
resolutionCB.current(0)

# Ratio
ratioLB = ttk.Label(root, text='Ratio:', anchor='e', width=4)
ratioLB.place(relx=0.53, rely=0.415, relwidth=0.1)

ratioCB = ttk.Combobox(root, values=ratios_list, width=4, state='readonly')
ratioCB.place(relx=0.65, rely=0.4, relwidth=0.2)
ratioCB.bind('<<ComboboxSelected>>', on_ratio_selected)
ratioCB.current(0)

# radio buttons exact, atleast
resolutionVar = StringVar()
exactRB = ttk.Radiobutton(root, text='Exact', variable=resolutionVar,
                          value='exact', command=on_exact_or_atleast)
exactRB.place(relx=0.22, rely=0.46)

atleastRB = ttk.Radiobutton(root, text='Atleast', variable=resolutionVar,
                            value='atleast', command=on_exact_or_atleast)
atleastRB.place(relx=0.4, rely=0.46)
atleastRB.invoke()

# Page
pageLB = ttk.Label(root, text='Page:', anchor='e', width=8)
pageLB.place(relx=0.01, rely=0.54, relwidth=0.19)

pagelist = ['Any', '1', '1-3', '1-5', '1-10', '1-15', '1-20']
pageLB = ttk.Label(root, text='Page:')
pageCB = ttk.Combobox(root, values=pagelist, width=10, state='readonly')
pageCB.place(relx=0.22, rely=0.53, relwidth=0.18)
pageCB.bind('<<ComboboxSelected>>', on_page_selected)
pageCB.current(0)

# Save locally
saveLocallyLB = ttk.Label(root, text='Save Img:', anchor='e', width=8)
saveLocallyLB.place(relx=0.01, rely=0.62, relwidth=0.19)

saveVar = IntVar()
saveCB = ttk.Checkbutton(root, variable=saveVar, onvalue=1, offvalue=0)
saveCB.place(relx=0.22, rely=0.612)

# timeout
timeoutLB = ttk.Label(root, text='Interval:', anchor='e', width=8)
timeoutLB.place(relx=0.01, rely=0.672, relwidth=0.19)

timeoutEN = ttk.Entry(root, width=5)
timeoutEN.place(relx=0.22, rely=0.67, relwidth=0.2)
timeoutEN.bind('<KeyRelease>', on_timeout_input)

# countdown and status
statusLB = ttk.Label(root, text='status:', anchor='e', width=8)
statusLB.place(relx=0.01, rely=0.73, relwidth=0.19)

statusVar = StringVar()
statusVar.set('Not Running')
statusLB2 = Message(root, textvariable=statusVar, anchor='nw', justify='left', fg=whitefg, bg=canvasbg, width=380)
statusLB2.place(relx=0.22, rely=0.728)

# Run button
runBT = ttk.Button(root, text='Run', command=toggle_running,
                   width=5, style='Run.TButton')
runBT.place(relx=0.7, rely=0.9, relwidth=0.23)


# api_cache()  # set apikey if its found in cache

# tkinter loop
root.mainloop()


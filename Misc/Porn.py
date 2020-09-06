import pyautogui as pg

#Opening This Pc
pg.doubleClick(70,35,duration=0.5)

#Opening Folder using mouse
#pg.doubleClick(1435,480,duration=0.25)
#pg.doubleClick(875,250,duration=0.25)
#pg.doubleClick(303,300,duration=0.25)

#Opening Folder Using keyboard
pg.click(260,195,duration=0.25)
pg.typewrite('F:\Program Videos\On Going',interval=0.05)
pg.press('enter')

#Using Video Tools
pg.doubleClick(340,47,duration=0.5)
pg.doubleClick(74,115,duration=0.5)

import pyautogui as pg

#Opening This Pc
pg.doubleClick(70,35,duration=0.5)

#Opening Folder Using keyboard
pg.click(260,195,duration=0.25)
pg.typewrite('G:\\ProgramStudy\\Us',interval=0.05)
pg.press('enter')


#Using Video Tools
pg.doubleClick(340,47,duration=0.25)
pg.doubleClick(140,115,duration=0.25)

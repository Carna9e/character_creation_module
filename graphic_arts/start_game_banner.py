от   аскииматики  .   рендереры   импортируют   FigletText  ,  Fire 
от   аскииматики  .   рендереры   импортируют   SpeechBubble 
от   аскииматики  .  сцен    импорт   Сцены 
от   аскииматики  .   Экран   импорта   экрана 
от   аскииматики  .  эффектов    импорт   Печать 
от   аскииматики  .  исключений    импорт   ResizeScreenError 
из   pyfiglet   импорта   Figlet 
импорт   системы 


анимация определения   (  экран  ) screen : 
    сцены   =  [] 

    text   =   Figlet  (  font  =  "banner"  ,  width  =  200  ).   renderText  (  "НАЧАТЬ ИГРУ"  ) 
    распечатать  (  текст  ) 
    эффекты   =  [ 
        Распечатать  (  экран  , 
              Огонь  (  скрин  .  высота  ,  80  ,  текст  ,  0.4  ,  40  ,  скрин  .  цвета  ), 
              0 , 
              скорость  =  1  , 
              прозрачный  =  Ложь  , 
              ), 
        Распечатать  (  экран  , 
              FigletText  (  "Реальная практическая игра"  ,  "баннер"  ), 
              экран  .   высота   -   15  , 
              цвет  =  экран  .   ЦВЕТ_БЕЛЫЙ  , 
              бг  =  Экран  .   ЦВЕТ_БЕЛЫЙ  , 
              скорость  =  1  ), 
        Распечатать  (  экран  , 
              SpeechBubble  (  "Пожалуйста, нажмите X - начать игру"  ), 
              экран  .   высота  -  5  , 
              скорость  =  1  ,  прозрачность  =  ложь  ) 

    ] 
    сцены  .   добавить  (  Сцена  (  эффекты  ,  -  1  )) 

    экран  .   играть  (  сцены  ,  stop_on_resize  =  True  ) 


 (  защита run_screensaver  ): 
    Экран  .   обертка  (  анимация  ) 


если   __name__   ==   "__main__"  : 
    запустить_скринсейвер  () 
    сис  .   выход  (  0  ) 

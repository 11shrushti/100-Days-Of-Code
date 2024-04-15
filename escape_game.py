# This is the fun and amazing escape game .....

print(''' o _
                                   ___|\_
                                _____/_\-_
                            _____________
              ,--.      _____________________
            mmm-. \ _________________________
           ((\     )____________________________
            )6(\    )__________________________
            \ _`)    )____________________________
            _ =o= ) ))__________________________
           ( (__/)  ) )______________________
         _/ ( (   \  \ ______________________
        _(=.|\    |)=.|____________________
      ___\  \ )   /   |______________________
     ____|   /  /     |____________________
    _____|_,/  (`;-.  |\ ___________________
   _______ /    |\  `'   \______  _,/)_____
  _______ /     ' `       \ ____/_/)/_________
 _______ /                  \
 _______/                    \ ________________
______ /                       \
______/                          \ ______________
__   /                   `.       . \
____;                      \       \  )____________
    /                   `   \        \ )
___;    '                `    \       )________________
   /   :                  ;  ,-.    ,'
___;__,-.     ;   .   .     /"""`-='_______________
gpyy   /_,`-=-.___,.__,-=-''"""'`
_____________________________________________
   ''')

print('''welcome to "Escape to Freedom: Cinderella's Enchanted Challenge"...
      Cinderella will get a magical message to way her out .''')
#challenge 1
choice_1=input(" You are in a room full of old books.you needed to find a secret code to open a hidden door.Type 'look on the shelves' or 'read the old paper'\n " ).lower()
if choice_1=="look on the shelves":
    print(" You have got a little mouse to open a locked door")
    #challeenge2
    choice_2=input("But oh no! Her mean stepmom set traps.Type  'walk quiet' or 'sing a song'to help Cinderella get past them without being caught.\n").lower()
    if choice_2=="walk quiet":
        print("Congratulations!!  You have entered a pretty garden")
        #challenge three
        choice_3=input(" Cinderella had to get through a maze without her stepmom catching her. type' go around the roses' or  'use the magic key .'\n").lower()
        if choice_3=="use the magic key ":
            print("Cindrella had went through the magic door you won the game.")
        else:
            print("Sorry , Cindrella was caught by her step mom.")    
        
    else:
        print("You have been caught by the step mom.. game over")    

    

else:
    print("You have not found any clue . Game over.")    

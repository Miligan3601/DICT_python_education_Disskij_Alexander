print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")
camel = r"""
The camel habitat...
___.-''''-.
/___ @ |
',,,,. | _.'''''''._
' | / \
| \ _.-' \
| '.-' '-.
| ',
| '',
',,-, ':;
',,| ;,, ,' ;;
! ; !'',,,',',,,,'! ; ;:
: ; ! ! ! ! ; ; :;
; ; ! ! ! ! ; ; ;,
; ; ! ! ! ! ; ;
; ; ! ! ! ! ; ;
;,, !,! !,! ;,;
/_I L_I L_I /_I
Look at that!"""
lion = r"""
The lion habitat...
,w.
,YWMMw ,M ,
_.---.._ __..---._.'MMMMMw,wMWmW,
_.-"" ''' YP"WMMMMMMMMMb,
.-' __.' .' MMMMW^WMMMM;
_, .'.-'"; `, /` .--"" :MMM[==MWMW^;
,mM^" ,-'.' / ; ; / , MMMMb_wMW" @\
,MM:. .'.-' .' ; `\ ; `, MMMMMMMW `"=./`-,
WMMm__,-'.' / _.\ F'''-+,, ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-' ,-' _.--"" `-, ; \ ; ;MMMMMMMMMMW^``; __|
/ .' ; ; ) )`{ \ `"^W^`, \ :
/ .' / ( .' / Ww._ `. `"
/ Y, `, `-,=,_{ ; MMMP`""-, `-._.-,
(--, ) `,_ / `) \/"") ^" `-, -;"\:
The lion is roaring!"""
deer = r"""
The deer habitat...
/| |\
`__\\ //__'
|| ||
\__`\ |'__/
`_\\ //_'
_.,:---;,._
\_: :_/
|@. .@|
| |
,\.-./ \
;;`-' `---__________-----.-.
;;; \_\
';;; |
; | ;
\ \ \ | /
\_, \ / \ |\
|';| |,,,,,,,,/ \ \ \_
| | | \ / |
\ \ | | / \ |
| || | | | | |
| || | | | | |
| || | | | | |
|_||_| |_| |_|

/_//_/ /_/ /_/
Pretty good!"""
goose = r"""
The goose habitat...

_
,-"" "".
,' ____ `.
,' ,' `. `._
(`. _..--.._ ,' ,' \ \
(`-.\ .-"" ""' / ( d _b
(`._ `-"" ,._ ( `-( \
<_ ` ( <`< \ `-._\
<`- (__< < :
(__ (_<_< ;
`------------------------------------------
Beautiful!"""
bat = r"""
The bat habitat...
_________________ _________________
~-. \ |\___/| / .-~
~-. \ / o o \ / .-~
> \\ W // <
/ /~---~\ \
/_ | | _\
~-. | | .-~
; \ / i
/___ /\ /\ ___\
~-. / \_/ \ .-~
V V
It's doing fine."""

rabbit = r"""
The rabbit habitat...
,
/| __
/ | ,-~ /
Y :| // /
| jj /( .^
>-"~"-v"
/ Y
jo o |
( ~T~ j
>._-' _./
/ "~" |
Y _, |
/| ;-"~ _ l
/ l/ ,-"~ \
\//\/ .- \
Y / Y
l I !
]\ _\ /"\
(" ~----( ~ Y. )
It looks fine!"""
animals = [camel, lion, deer, goose, bat, rabbit]
user_input = input("Please enter the number of the habitat you would like to view: ")
user_input = int(user_input)
if 1 <= user_input <= len(animals):
    print(animals[user_input - 1])
else:
    print("Invalid input. Please enter a valid number.")
print("You've reached the end of the program.")
while True:
    user_input = input("Please enter the number of the habitat you would like to view or type 'exit' to quit: > ")
    if user_input == 'exit':
        break
    if user_input.isdigit():
        animal_number = int(user_input)
        if 1 <= animal_number <= len(animals):
            print(animals[animal_number - 1])
        else:
            print("Invalid habitat number!")
    else:
        print("Invalid input. Please enter a number or type 'exit' to quit.")
print("See you later!")
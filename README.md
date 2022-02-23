# Requirements

<code>
 conda create -n translate python=3.9<br>
 conda activate translate<br>
 pip install deep-translator
</code>

For more information go to: https://pypi.org/project/deep-translator/

# About
<section>
       ....
   .xH888888Hx.
 .H8888888888888:                           .d``
 888*"""?""*88888X        .u         .u     @8Ne.   .u
'f     d8x.   ^%88k    ud8888.    ud8888.   %8888:u@88N
'>    <88888X   '?8  :888'8888. :888'8888.   `888I  888.
 `:..:`888888>    8> d888 '88%" d888 '88%"    888I  888I
        `"*88     X  8888.+"    8888.+"       888I  888I
   .xHHhx.."      !  8888L      8888L       uW888L  888'
  X88888888hx. ..!   '8888c. .+ '8888c. .+ '*88888Nu88P
 !   "*888888888"     "88888%    "88888%   ~ '88888F`
        ^"***"`         "YP'       "YP'       888 ^
     s                                        *8E   .x+=:.         ..                  s
    :8                                        '8>  z`    ^%  x .d88"                  :8
   .88       .u    .                  u.    u. "  z` .   <k  5888R                  .88           u.      .u    .   
  :888ooo  .d88B :@8c        u      x@88k u@88c.    .@8Ned8"  '888R         u       :888ooo  ...ue888b   .d88B :@8c  
-*8888888 ="8888f8888r    us888u.  ^"8888""8888"  .@^%8888"    888R      us888u.  -*8888888  888R Y888r ="8888f8888r 
  8888      4888>'88"  .@88 "8888"   8888  888R  x88:  `)8b.   888R   .@88 "8888"   8888     888R I888>   4888>'88"  
  8888      4888> '    9888  9888    8888  888R  8888N=*8888   888R   9888  9888    8888     888R I888>   4888> '    
  8888      4888>      9888  9888    8888  888R   %8"    R88   888R   9888  9888    8888     888R I888>   4888>      
 .8888Lu=  .d888L .+   9888  9888    8888  888R    @8Wou 9%    888R   9888  9888   .8888Lu= u8888cJ888   .d888L .+   
 ^%888*    ^"8888*"    9888  9888   "*88*" 8888" .888888P`    .888B . 9888  9888   ^%888*    "*888*P"    ^"8888*"    
   'Y"        "Y"      "888*""888"    ""   'Y"   `   ^"F      ^*888%  "888*""888"    'Y"       'Y"          "Y"      
                        ^Y"   ^Y'                               "%     ^Y"   ^Y'

usage: TranslateText.py [-h] [-s S] [-d D] [-t T] [-o O] [--compact [COMPACT]]

optional arguments:
  -h, --help           show this help message and exit
  -s S                 Source language for translate file
  -d D                 Destination language to saving file
  -t T                 Source file for translation
  -o O                 Output file translated
  --compact [COMPACT]  Compact text for reduce number of requests for most big files
(testransl) hmd@DESKTOP-R48RN54:~/translate/translate-text-file$

example: $ python TranslateText.py -s en -d ro -t text_needs_translation.txt
 
</section>

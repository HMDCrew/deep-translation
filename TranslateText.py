import asyncio
import os
import argparse
from pprint import pprint
import sys

from deep_translator import GoogleTranslator

class Translation:
    '''The script will translate the text file from one language to the next language.
    Example of command to run the script: python TranslateText.py fr sq
    The "fr en" means to translate a French text into Albanian.
    For more information on googletrans go to: http://py-googletrans.readthedocs.io/en/latest/
    Note: type print(googletrans.LANGUAGES) to see supported languages
    Example of language codes: 'fr' = French; 'sq' = Albanian; 'en' = English
    '''
    def __init__(self, *a):
        self.from_language = args['s']
        self.to_language = args['d']
        self.extract_file = extract_file
        self.translate_file = translate_file
        self.rows = list( open(extract_file, "r").read().splitlines())

    def clean_text(self):
        text = open(self.extract_file, 'r').read()
        text = text.replace('\n', '\n ')
        text = text.replace('\n', '')
        text = text.replace('.', '.\n')
        text = text.replace('!', '!\n')
        text = text.replace('?', '?\n')
        self.rows = list(text.splitlines())

    ## Translite line
    async def translate_line(self, line):
        if( len(line.strip()) > 0 ):
            return GoogleTranslator(source=self.from_language, target=self.to_language).translate(line.strip())
        else:
            return ""

    ## Requests
    async def requests_six(self, one, tow, three, four, five, six):
        return await asyncio.gather(
            self.translate_line(one),
            self.translate_line(tow),
            self.translate_line(three),
            self.translate_line(four),
            self.translate_line(five),
            self.translate_line(six)
        )
    async def requests_three(self, one, tow, three):
        return await asyncio.gather(
            self.translate_line(one),
            self.translate_line(tow),
            self.translate_line(three)
        )
    async def requests_one(self, one):
        return await asyncio.gather( self.translate_line(one) )

    ## Main Requests
    def write_translation(self):
        translated = []
        rows_length = len(self.rows) - 1
        rows_ter, columns_ter = os.popen('stty size', 'r').read().split()

        ## Async requests
        i = 0
        while(i <= rows_length):
            if( (rows_length - i) >= 6 ):
                translated += asyncio.run(self.requests_six(
                    self.rows[i].strip(), 
                    self.rows[i+1].strip(), 
                    self.rows[i+2].strip(),
                    self.rows[i+3].strip(), 
                    self.rows[i+4].strip(), 
                    self.rows[i+5].strip()
                ))
                i += 6
            else:
                if( (rows_length - i) >= 3 ):
                    translated += asyncio.run( self.requests_three(self.rows[i].strip(), self.rows[i+1].strip(), self.rows[i+2].strip()) )
                    i += 3
                else:
                    translated += asyncio.run( self.requests_one(self.rows[i].strip()) )
                    i += 1

            ## Print terminal progress
            title = "Translation progress"
            end_row = '[%d / %d]'%(i, len(self.rows))
            n_spaces = int(columns_ter)-len(title)-len(end_row)-2

            spaces = ""
            for h in range(0, n_spaces):
                spaces += " "

            print( '\r%s %s %s'%(title, spaces, end_row), end="" )


        ## Write output
        print("\nWritting file")
        with open(self.translate_file, 'w') as f:
            for i in translated:
                f.write( str(i)+ '\n')
        f.close()

if __name__ == "__main__":

    print("       ....                                                                                                          ")
    print("   .xH888888Hx.                                                                                                      ")
    print(" .H8888888888888:                           .d``                                                                     ")
    print(" 888*\"\"\"?\"\"*88888X        .u         .u     @8Ne.   .u                                                               ")
    print("'f     d8x.   ^%88k    ud8888.    ud8888.   %8888:u@88N                                                              ")
    print("'>    <88888X   '?8  :888'8888. :888'8888.   `888I  888.                                                             ")
    print(" `:..:`888888>    8> d888 '88%\" d888 '88%\"    888I  888I                                                             ")
    print("        `\"*88     X  8888.+\"    8888.+\"       888I  888I                                                             ")
    print("   .xHHhx..\"      !  8888L      8888L       uW888L  888'                                                             ")
    print("  X88888888hx. ..!   '8888c. .+ '8888c. .+ '*88888Nu88P                                                              ")
    print(" !   \"*888888888\"     \"88888%    \"88888%   ~ '88888F`                                                                ")
    print("        ^\"***\"`         \"YP'       \"YP'       888 ^                                                                  ")
    print("     s                                        *8E   .x+=:.         ..                  s                             ")
    print("    :8                                        '8>  z`    ^%  x .d88\"                  :8                            ")
    print("   .88       .u    .                  u.    u. \"  z` .   <k  5888R                  .88           u.      .u    .   ")
    print("  :888ooo  .d88B :@8c        u      x@88k u@88c.    .@8Ned8\"  '888R         u       :888ooo  ...ue888b   .d88B :@8c  ")
    print("-*8888888 =\"8888f8888r    us888u.  ^\"8888\"\"8888\"  .@^%8888\"    888R      us888u.  -*8888888  888R Y888r =\"8888f8888r ")
    print("  8888      4888>'88\"  .@88 \"8888\"   8888  888R  x88:  `)8b.   888R   .@88 \"8888\"   8888     888R I888>   4888>'88\"  ")
    print("  8888      4888> '    9888  9888    8888  888R  8888N=*8888   888R   9888  9888    8888     888R I888>   4888> '    ")
    print("  8888      4888>      9888  9888    8888  888R   %8\"    R88   888R   9888  9888    8888     888R I888>   4888>      ")
    print(" .8888Lu=  .d888L .+   9888  9888    8888  888R    @8Wou 9%    888R   9888  9888   .8888Lu= u8888cJ888   .d888L .+   ")
    print(" ^%888*    ^\"8888*\"    9888  9888   \"*88*\" 8888\" .888888P`    .888B . 9888  9888   ^%888*    \"*888*P\"    ^\"8888*\"    ")
    print("   'Y\"        \"Y\"      \"888*\"\"888\"    \"\"   'Y\"   `   ^\"F      ^*888%  \"888*\"\"888\"    'Y\"       'Y\"          \"Y\"      ")
    print("                        ^Y\"   ^Y'                               \"%     ^Y\"   ^Y'                                     ")
    print("                                                                                                              ")


    argparser = argparse.ArgumentParser()
    argparser.add_argument('-s', help = 'Source language for translate file')
    argparser.add_argument('-d', help = 'Destination language to saving file')
    argparser.add_argument('-t', help = 'Source file for translation')
    argparser.add_argument('-o', help = 'Output file translated')
    argparser.add_argument('--compact', nargs='?', default="false", const="true", help = 'Compact text for reduce number of requests for most big files' )

    args = vars(argparser.parse_args())

    extract_file = "{}".format(args['t'])
    translate_file = "translated_{}_{}_{}.txt".format(args['s'], args['d'], os.path.splitext(args['t'])[0])

    if( args['o'] != None ) :
        translate_file = args['o']

    t=Translation()
    if( args['compact'] == "true" ) :
        t.clean_text()
    t.write_translation()
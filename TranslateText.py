import asyncio
import os
import argparse
from pprint import pprint

from deep_translator import GoogleTranslator

def remove_old_translated():
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.startswith("translated"):
            os.remove(f)
            
def remove_old_temps():
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.startswith("temp"):
            os.remove(f)

class Translation:
    '''The script will translate the text file from one language to the next language.
    Example of command to run the script: python TranslateText.py fr sq
    The "fr en" means to translate a French text into Albanian.
    For more information on googletrans go to: http://py-googletrans.readthedocs.io/en/latest/
    Note: type print(googletrans.LANGUAGES) to see supported languages
    Example of language codes: 'fr' = French; 'sq' = Albanian; 'en' = English
    '''
    def __init__(self, *a):
        self.from_language = args.from_language
        self.to_language = args.to_language
        self.extract_file = extract_file
        self.translate_file = translate_file
        self.transformed_file = transformed_file
        with open(self.extract_file, 'a') as f:
            f.write('\n')

    def clean_text(self):
        text = open(self.extract_file, 'r').read()
        text = text.replace('\n', '\n ')
        text = text.replace('\n', '')
        text = text.replace('.', '.\n')
        text = text.replace('!', '!\n')
        text = text.replace('?', '?\n')

        self.transformed_file = list(text.splitlines())

        #f = open(self.transformed_file, 'w')
        #f.write(text)
    
    async def translate_line(self, line):
        if( len(line.strip()) > 0 ):
            return GoogleTranslator(source=self.from_language, target=self.to_language).translate(line.strip())
        else:
            return ""

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

    def write_translation(self):

        rows =  self.transformed_file
        translated = []

        #for i, line in enumerate(rows):
        #    translation = self.translate_line(line)
        #    print('\r\rTranslation progress [%d / %d]'%(i, len(rows)), end="")
        #    translated.append(translation)
        #lis = [1, 2, 3, 4, 5]


        
        
        rows_length = len(rows) - 1
        i = 0
        while(i <= rows_length):

            if( (rows_length - i) >= 6 ):
                translated += asyncio.run(self.requests_six(
                    rows[i].strip(), 
                    rows[i+1].strip(), 
                    rows[i+2].strip(),
                    rows[i+3].strip(), 
                    rows[i+4].strip(), 
                    rows[i+5].strip()
                ))
                i += 6
            else:
                if( (rows_length - i) >= 3 ):
                    translated += asyncio.run( self.requests_three(rows[i].strip(), rows[i+1].strip(), rows[i+2].strip()) )
                    i += 3
                else:
                    translated += asyncio.run( self.requests_one(rows[i].strip()) )
                    i += 1

            # print( "\n%s \n%s \n%s" %(rows[i], rows[i+1], rows[i+2]) )
            # print( "\n" )

            print( '\r\rTranslation progress [%d / %d]'%(i, len(rows)), end="" )
        
        print("\n")
        
        with open(self.translate_file, 'w') as f:
            for i in translated:
                f.write( str(i)+ '\n')
        f.close()



if __name__ == "__main__":
    remove_old_translated()
    mypath =  os.path.dirname(os.path.abspath(__file__))
    for f in os.listdir(mypath):
        if f.endswith(".txt"):
            argparser = argparse.ArgumentParser()
            argparser.add_argument('from_language',help = 'Example of command to run: python TranslateText.py fr en')
            argparser.add_argument('to_language',help = 'Example of command to run: python TranslateText.py fr en')
            args = argparser.parse_args()
            extract_file = "{}.txt".format(os.path.splitext(f)[0])
            transformed_file = "temp_{}.txt".format(os.path.splitext(f)[0])
            translate_file = "translated_{}_{}_{}.txt".format(args.from_language, args.to_language, os.path.splitext(f)[0])
            t=Translation()
            t.clean_text()
            t.write_translation()
            remove_old_temps()
            print('translation complete - check text file that starts with translated')
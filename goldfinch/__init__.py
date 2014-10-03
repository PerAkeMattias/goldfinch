import string
import sys
import unicodedata

def validFileName(inputName, space="underscore", initCap=True, ascii=True):
    """
    Use to remove invalid filename characters like '<>:"/\|?*'
    inputName = string or unicode object.
    space = 'underscore', 'remove',or 'keep'.
    initCap = True or False
    ascii= True or False
    """
    try:
        if space not in ('remove','underscore','keep'):
            print("Warning:  the only valid argument values for space is either 'remove', 'underscore', or 'keep'."
                  "Default value 'remove' will be used instead of the '{}' you passed".format(space))
            space = 'remove'
        if initCap not in (True,False):
            print("Warning: The only valid argument values for initCap is either True or False. "
                  "Default value True will be used instead of the '{}' you passed".format(initCap))
            initCap=True
        if ascii not in (True,False):
            print("Warning: The only valid argument values for ascii is either True or False. "
                  "Default value True will be used instead of the '{}' you passed".format(ascii))
            strict=False
       
    
        if sys.version_info[0] == 2:
            if isinstance(inputName, unicode) == True or isinstance(inputName, str) == True:
                if isinstance(inputName, str) == True:
                    inputName = inputName.decode('UTF-8')
            else:
                raise TypeError
                
            characters = ''.join(unichr(i) for i in xrange(255))
            reservedCharacters = '<>:"/\|?*'
            for character in reservedCharacters: 
                characters = characters.replace(character, "")
                    
        if sys.version_info[0] == 3:
            if isinstance(inputName, str) == True:
                pass
            else:
                raise TypeError
                
            characters = ''.join(chr(i) for i in range(255))
            print(characters)
            reservedCharacters = '<>:"/\|?*'
            for character in reservedCharacters: 
                characters = characters.replace(character, "")
            
        validName = ''.join(char for char in inputName if char in characters)
        
        if ascii == True:
            validName = unicodedata.normalize('NFKD', validName).encode('ascii','ignore')
        elif ascii == False:
            pass
        
        if initCap == True:
            validName = string.capwords(validName)
        elif initCap == False:
            pass
        
        if space == 'remove':
            validName = validName.replace(' ','')
        elif space == 'underscore':
            validName = validName.replace(' ','_')
        elif space == 'keep':
            pass
        
        return validName
    except TypeError:
        errMsg = 'Accepted input is str or unicode, you passed a {}'.format(type(inputName))
        print(errMsg)
        return


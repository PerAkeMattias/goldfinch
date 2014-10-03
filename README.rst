**About** 
 
goldfinch is simple package which removes invalid filename characters from a filename.  Pass in a string or unicode (with or without invalid characters) and get valid filename returned (as unicode).  

In general, goldfinch will remove invalid filename characters like <>:"/\|?* and characters above the 0-255 character set.  The default is is to attempt to convert to ascii characters using _unicodedata_. 

**Why use goldfinch**
  
The only real usecase for this package is when one creates filenames on the fly and there is no way of knowing what exactly will be passed as the filename.  I find it particularly useful when I scrape websites.  

So, instead of this happening:: 
	>>> fileName = 'this is a filename with some invalid characters in it <>:"/\|?*'
	>>> file = open(fileName,"w")
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	IOError: [Errno 2] No such file or directory: 'this is a filename with some invalid characters in it <>:"/\\|?*'  

Do this:: 
	>>> from goldfinch import validFileName as vfn
	>>> fileName = 'this is a filename with some invalid characters in it <>:"/\|?*' 
	>>> file = open(vfn(fileName),"w")  

**Examples**  
  
There are three (space, initCap, and ascii) options available when normalizing a filename.  
The default is 'space="underscore", initCap=True, ascii=True'.  
- For space the options are underscore, remove, and keep.  The default is underscore which will replace a space with an underscore (_).
- initCap is a True & False option.  True which is the default will convert the first character in a word to cap and leave all others lowercase.  
- ascii is also a True & False option.  Once again True is the default which will convert something like this ÅåÄäÖ to this AaAaO. False will leave characters as-is.  

Use default setting:
	>>> fileName = 'THIS IS a filename with ÅåÄäÖ some characters that will not work like these: <>:"/\|?*'
	>>> vfn(fileName)
	'This_Is_A_Filename_With_Aaaao_Some_Characters_That_Will_Not_Work_Like_These'  

Default with unicode input: 
	>>> fileName = u'THIS IS a filename with ÅåÄäÖ some characters that will not work like these: <>:"/\|?*'
	>>> vfn(fileName)  
	'This_Is_A_Filename_With_Aaaao_Some_Characters_That_Will_Not_Work_Like_These'  

With initCap = False: 
	>>> vfn(fileName, initCap = False)  
	'THIS_IS_a_filename_with_AaAaO_some_characters_that_will_not_work_like_these_' 

With space = 'remove': 
	>>> vfn(fileName, space = 'remove')   
	'ThisIsAFilenameWithAaaaoSomeCharactersThatWillNotWorkLikeThese'

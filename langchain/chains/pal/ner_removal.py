prompt = '''

Please take the below paragraph of text beginning with "TEXT:", and you should return back that same paragraph with the following named entity changes:

- any named entities referring to people (singular or plural) or animal(s) should be replaced with the token <PERSON>.  
- an inanimate object(s), plant(s), items of food etc., should be replaced with the token <OBJECT>.  
- any named entities referring to geographical locations should be replaced with the token <PLACE>. 
- any numbers should be replaced with the token <NUM>.

All named entities matching the above list in the paragraph should be changed.

Any references to times, days of the week, months of the year, hours of the day etc. should be unchanged and not replaced with other tokens.

Your response consist only of the token "OUTPUT:" followed by the text with the named entity changes. 

For example, the following would be an accurate response:

TEXT: John took a book to the local park, and on the way he met Jill, who was eating an apple.
OUTPUT: <PERSON> took a <OBJECT> to <PLACE>, and on the way he met <PERSON> who was eating an <OBJECT>.

TEXT:
{TEXT}
'''

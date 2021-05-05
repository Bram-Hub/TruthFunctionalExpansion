# TruthFunctionalExpansion
## Authors:
2021:
Cole Feuer and David Wiser

## About:
The TruthFunctionalExpansion tool takes given First order logic statement as well as a universe of discourse, and then produces a proposition logic expression than can be validate using a short truth tree.  This method specifically can be used to prove FO invalidity

How to use:
![Interface](/InterfaceImage.png)


## Planned Changes:
- Implement validation of expanded expressions
- Fix backspace and reset 
- Fix unicode conversion

## Installation:
### Windows
- Download the repository
- Double click on LogicExpander1.6.py and you should see the application interface.

### Mac
- Download the repository
- Open LogicExpander1.6.py with any python compiler and then run and you should see the application interface.

## Known Issues:
- certain sybmols from the character representation back into the unicode logic symbols yeilded strange results. Specifically, the or, if, and exists. You can find that the associated lines in the conv_str2Log function are commented out and thus remain as the internal character representation. This does not impede the functionality of the code however reduces the readability and forces the user to refrence the documentaion on what the symbold represent.
- the backspace and reset buttons were causing problems as the tkinter labels were not able to be destroyed visually although there variables do in fact change. A band-aid solution was applied which over write a blank string on top however there can still be dots in the background. Again, this is a purely a user expereince issue but doesnt mess up the functionality.
- the parenhesis and x, y, z shortcuts can conflict with the entry box. If any of these symbols are typed into the entry box the will automatically be added to the expression causing it to double.
- extra parenthesis are sometimes added which doesnt impact the logic but makes the output much harder to read. 

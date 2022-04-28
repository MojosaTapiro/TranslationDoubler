# TranslationDoubler
A software to facilitate Jackbox translation projects with double folder structure

Two programs, so far for the translation of QuiplashXL from Jackbox PartyPack 2. To make them work, they need to be in the same folder as the folder containing all Quiplash game files. 

Quiplash_translationChecker checks if all prompts in the QuiplashQuestion.jet correspond with the prompts in the data.jet files in the QuiplashQuestion folder. It prints the prompt ID and prompt of all prompts that differ from each other. 
Quiplash_translationDoubler replaces all prompts in the individual data.jet files with the corresponding prompt in QuiplashQuestion.jet.

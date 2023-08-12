![图片](https://github.com/JinyinZha/Secondary_Structure_Painter/assets/44738533/56957417-efff-4bcd-b529-41c7622dc098)# Secondary_Structure_Painter
Secondary Structure Painter (SSP) is a tool for plotting amino acid sequence of a protein with their seconday structure. SSP requires no installation on Windows and especially, outputs in a pptx format so that it could be further modified. 

# Brief Introduction
The secondary structure diagram of the protein sequence is a common way to demonstrate protein structures. The current tool (SSP) offers you an easy way to create these diagrams. Using a PDB file, PDB ID or Uniprot ID of the intersted protein as input, SSP could plot the diagrams in seconds. Importantly, the output style of SSP is in pptx format, suggesting that users could perform further modifications, based on their individual requirements, and is not limited by DPIs. Besides, SSP itself has also integrated many options to meet different requirements. SSP on windows is developed as a user-friendly GUI program requires no installation. It could also be used on other systems as long as you are familiar with Python.

![1](https://github.com/JinyinZha/Secondary_Structure_Painter/assets/44738533/f06a5839-0b63-4b45-ab0d-7e97025ceea9)



# Usage
## 1, GUI on Windows
The easiest way to use SSP is to use the GUI program. Download "SSP_V1.rar" and unwrap it, in which you could find "SSP.exe". Double click the program to open it. You will first see a window for mode selection.

In "PDB ID Mode", the protein structure is assigned by offering a valid PDB ID. The chain ID of the PDB structure should also be assigned because the secondary structure diagram is usually reasonable for discribing a single chain of the protein. Besides, the user should also select the output directory and offer the name of the output pptx file. Note that an automatic pptx name will be formed when PDB ID and chain ID is given. After offering those basic inputs, you could press "submit" to create the diagram. The program would download protein structure from RSCB Protein Data Bank, analyze it with DSSP, and visualize secondary structures with objects in PPT. Missing residues will be detected and drawn as "?". You could find your pptx file in the output directory assigned. If you want to use another mode, press "back" to the mode selection page.

The usage of "PDB File Mode" and "AlphaFold Mode" is almost same to that of "PDB ID mode". The only differences are in assignment of protein structures. in "PDB File Mode", the structure is to be selected as a PDB file in your computer. "AlphaFold Mode" is made for situations where protein structures are unavaliable in RSCB Protein Data Bank. Thus, we could use structures in AlphaFold Database by supporting the Uniprot ID of the interested protein. It has to be demonstrated that since disordered region are usually in low confidence in AlphaFold, we highly recommend to restric the range of residue IDs in the "Additional Settings".

Below basic inputs are several "Additional Settings" where you could DIY your diagram, including the length of the diagram, the size of the residue chars in diagram, range of residues IDs in diagram (suggesting that you could only plot a fragment of the protein), color of secondary structures and color of all residues. The last setting is done by pressing the "Residue Color Map" button and a new window will be formed. You could edit RGB values for each residue, or you can edit or use two templates at the bottom (by pressing "Apply This Map"). Press "OK" to save the map or "Back" to cancel. 

![3](https://github.com/JinyinZha/Secondary_Structure_Painter/assets/44738533/db112174-c7f9-47b3-9653-ecd4236a1dab)

Let's make an example. We want to make a scondary structure diagram of β-tubulin. We enter the PDB ID model. β-tubulin could be fetched as chain B of PDB ID 1JFF. We save the output file in D:/. Then we applied some additional settings. Note that these settings are optional. As long as you have filled basic inputs, you could click "submit" to plot your diagram. Here, we click "residue color map" and click "Apply this Map" in "Positive/Negative Map". Color settings of residues are automatically changed, where positive reisdues are red while negative residues are blue. Click "Save" to save the color map. Then we click "submit" to plot the diagram. When the plotting succeeds, a window would pops up to show. Finally, we go to the output folder (set as D:/ here, and obviously could be elsewhere) and open the pptx file. It could be seen that the C-terminal of β-tubulin is very negative. More modifications could be done to this pptx file.

![4](https://github.com/JinyinZha/Secondary_Structure_Painter/assets/44738533/2ca879f5-ce16-44e8-82be-b8b50cb1fc43)

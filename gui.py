# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:55:25 2023

@author: 15308
"""
import os
import tkinter as tk
from tkinter import filedialog
from aasequence import AASequence
from parameters import paras
paras0 = paras.copy()
my_dir = os.getcwd()


def gui_main():
    global paras,paras0
    top_w = 300
    top_h = 200
    paras = paras0.copy()
    top = tk.Tk()
    top.title("SSP")
    top.geometry('%dx%d'%(top_w,top_h))
    top.resizable(False, False)
    top.iconbitmap("%s/icon.ico"%(my_dir))
    
    label1 = tk.Label(top, text="Please select a mode",font=('Times New Roman',16, 'bold'))
    label1.pack()
    pdbID_button = tk.Button(top,text="PDB ID Mode",font=('Times New Roman',12, 'bold'),
                              command=lambda:(top.destroy(),pdb_id_mode()))
    pdbID_button.pack(pady=5)
    pdbf_button = tk.Button(top,text="PDB File Mode",font=('Times New Roman',12, 'bold'),command=lambda:(top.destroy(),pdb_file_mode()))
    pdbf_button.pack(pady=5)
    af_button = tk.Button(top,text="AlphaFold Mode",font=('Times New Roman',12, 'bold'),command=lambda:(top.destroy(),AF_mode()))
    af_button.pack(pady=5)
    top.mainloop()    
    
def pdb_id_mode():
    top_w = 580
    top_h = 460
    top = tk.Tk()
    top.title("PDB ID Mode")
    top.geometry('%dx%d'%(top_w,top_h))
    top.resizable(False, False)
    top.iconbitmap("%s/icon.ico"%(my_dir))
    
    PDBID = tk.StringVar()
    chain = tk.StringVar()
    min_resid = tk.StringVar()
    max_resid = tk.StringVar()
    pptx = tk.StringVar()
    folder = tk.StringVar()
    fig_width = tk.StringVar()
    char_size = tk.StringVar()
    helix_color_r = tk.StringVar()
    helix_color_g = tk.StringVar()
    helix_color_b = tk.StringVar()
    sheet_color_r = tk.StringVar()
    sheet_color_g = tk.StringVar()
    sheet_color_b = tk.StringVar()
    loop_color_r = tk.StringVar()
    loop_color_g = tk.StringVar()
    loop_color_b = tk.StringVar()
    
    fig_width.set(paras["fig_width"])
    char_size.set(paras["char_size"])
    helix_color_r.set(str(paras["helix_color_r"]))
    helix_color_g.set(str(paras["helix_color_g"]))
    helix_color_b.set(str(paras["helix_color_b"]))
    sheet_color_r.set(str(paras["sheet_color_r"]))
    sheet_color_g.set(str(paras["sheet_color_g"]))
    sheet_color_b.set(str(paras["sheet_color_b"]))
    loop_color_r.set(str(paras["loop_color_r"]))
    loop_color_g.set(str(paras["loop_color_g"]))
    loop_color_b.set(str(paras["loop_color_b"]))
    folder.set("Browse...")
    min_resid.set("None")
    max_resid.set("None")
        
    n_row = 0
    #Row 1
    label1 = tk.Label(top, text="Basic Input",font=('Times New Roman',12, 'bold'), )
    label1.grid(row=n_row,column=0,columnspan=4)
    n_row += 1
    #Row 2
    PDBID_label = tk.Label(top, text="PDB ID:")
    PDBID_label.grid(row=n_row,column=0,pady=5)
    pdbID_box = tk.Entry(top,textvariable=PDBID,validate='key',
                         vcmd=lambda:auto_pptx(PDBID,chain,pptx))
    pdbID_box.grid(row=n_row,column=1,pady=5)
    
    chain_label = tk.Label(top, text="Chain:")
    chain_label.grid(row=n_row,column=2,)
    chain_box = tk.Entry(top,textvariable=chain,validate='all',
                         vcmd=lambda:auto_pptx(PDBID,chain,pptx))
    chain_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 3
    folder_label = tk.Label(top, text="Output Folder:" )
    folder_label.grid(row=n_row,column=0,pady=5)
    folder_button = tk.Button(top,textvariable=folder,width=20,bg="#FFD347",
                              command=lambda:(folder.set(filedialog.askdirectory()),
                                              folder.set("Browse..." if folder.get()=="" else folder.get())))
    folder_button.grid(row=n_row,column=1,pady=5,columnspan=3,sticky=tk.E+tk.W)
    n_row += 1
    #Row 4
    filename_label = tk.Label(top, text="Output PPTX:" )
    filename_label.grid(row=n_row,column=0,pady=5)
    filename_box = tk.Entry(top,textvariable=pptx)
    filename_box.grid(row=n_row,column=1,pady=5,columnspan=3,sticky=tk.E+tk.W)
    n_row += 1
    #Row 5
    submit_button = tk.Button(top,text="Submit",width=20,bg="#FF8F8F",
                              command=lambda:(
                                  tk.messagebox.showinfo("Result",main(p2v(paras),folder))))
    submit_button.grid(row=n_row,column=1,pady=20)
    back_button = tk.Button(top,text="Back",width=20,bg="#9090E0",
                          command=lambda:(top.destroy(),gui_main()))
    back_button.grid(row=n_row,column=3,pady=20,)
    n_row += 1
    #Row 6
    label1 = tk.Label(top, text="Additional Settings",font=('Times New Roman',12, 'bold') )
    label1.grid(row=n_row,column=0,columnspan=4)
    n_row += 1
    #Row 7
    figwidth_label = tk.Label(top, text="Figure Width (cm)")
    figwidth_label.grid(row=n_row,column=0,pady=5)
    figwidth_box = tk.Entry(top,textvariable=fig_width)
    figwidth_box.grid(row=n_row,column=1,pady=5)
    charsize_label = tk.Label(top, text="Char. Size (pt)")
    charsize_label.grid(row=n_row,column=2,pady=5)
    charsize_box = tk.Entry(top,textvariable=char_size)
    charsize_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 8
    min_resid_label = tk.Label(top, text="Min. ResID:")
    min_resid_label.grid(row=n_row,column=0,pady=5)
    min_resid_box = tk.Entry(top,textvariable=min_resid)
    min_resid_box.grid(row=n_row,column=1,pady=5)
    min_resid_label = tk.Label(top, text="Max. ResID:")
    min_resid_label.grid(row=n_row,column=2,)
    min_resid_box = tk.Entry(top,textvariable=max_resid)
    min_resid_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 9
    label = tk.Label(top, text="R")
    label.grid(row=n_row,column=1)
    label = tk.Label(top, text="G")
    label.grid(row=n_row,column=2)
    label = tk.Label(top, text="B")
    label.grid(row=n_row,column=3)
    n_row += 1
    #Row 10
    helix_color_label = tk.Label(top, text="α-Helix Color:")
    helix_color_label.grid(row=n_row,column=0,pady=5)
    helix_color_boxr = tk.Entry(top,textvariable=helix_color_r)
    helix_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    helix_color_boxg = tk.Entry(top,textvariable=helix_color_g)
    helix_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    helix_color_boxb = tk.Entry(top,textvariable=helix_color_b)
    helix_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 11
    sheet_color_label = tk.Label(top, text="β-Sheet Color:")
    sheet_color_label.grid(row=n_row,column=0,pady=5)
    sheet_color_boxr = tk.Entry(top,textvariable=sheet_color_r)
    sheet_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    sheet_color_boxg = tk.Entry(top,textvariable=sheet_color_g)
    sheet_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    sheet_color_boxb = tk.Entry(top,textvariable=sheet_color_b)
    sheet_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 12
    loop_color_label = tk.Label(top, text="Loop Color:")
    loop_color_label.grid(row=n_row,column=0,pady=5)
    loop_color_boxr = tk.Entry(top,textvariable=loop_color_r)
    loop_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    loop_color_boxg = tk.Entry(top,textvariable=loop_color_g)
    loop_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    loop_color_boxb = tk.Entry(top,textvariable=loop_color_b)
    loop_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 13
    res_color_button = tk.Button(top,text="Residue Color Map",bg="#DDFFDD",
                              command=lambda:(#top.attributes("-disabled", 1),
                                              res_color_window(top),))
    res_color_button.grid(row=n_row,column=0,pady=5,padx=5,columnspan=4,sticky=tk.E+tk.W)
    n_row += 1
    #Link
    paras["protein"] = {"type":"PDB ID","PDB ID":PDBID,"chain":chain,
                        "max_resid":max_resid,"min_resid":min_resid}
    paras["pptx"] = pptx
    paras["fig_width"] = fig_width
    paras["char_size"] = char_size
    paras["helix_color_r"] = helix_color_r
    paras["helix_color_g"] = helix_color_g
    paras["helix_color_b"] = helix_color_b
    paras["sheet_color_r"] = sheet_color_r
    paras["sheet_color_g"] = sheet_color_g
    paras["sheet_color_b"] = sheet_color_b
    paras["loop_color_r"] = loop_color_r
    paras["loop_color_g"] = loop_color_g
    paras["loop_color_b"] = loop_color_b
    top.mainloop()
    
def pdb_file_mode():
    top_w = 580
    top_h = 470
    top = tk.Tk()
    top.title("PDB File Mode")
    top.geometry('%dx%d'%(top_w,top_h))
    top.resizable(False, False)
    top.iconbitmap("%s/icon.ico"%(my_dir))
    
    pdb_file = tk.StringVar()
    chain = tk.StringVar()
    min_resid = tk.StringVar()
    max_resid = tk.StringVar()
    pptx = tk.StringVar()
    folder = tk.StringVar()
    fig_width = tk.StringVar()
    char_size = tk.StringVar()
    helix_color_r = tk.StringVar()
    helix_color_g = tk.StringVar()
    helix_color_b = tk.StringVar()
    sheet_color_r = tk.StringVar()
    sheet_color_g = tk.StringVar()
    sheet_color_b = tk.StringVar()
    loop_color_r = tk.StringVar()
    loop_color_g = tk.StringVar()
    loop_color_b = tk.StringVar()
    
    pdb_file.set("Browse...")
    fig_width.set(paras["fig_width"])
    char_size.set(paras["char_size"])
    helix_color_r.set(str(paras["helix_color_r"]))
    helix_color_g.set(str(paras["helix_color_g"]))
    helix_color_b.set(str(paras["helix_color_b"]))
    sheet_color_r.set(str(paras["sheet_color_r"]))
    sheet_color_g.set(str(paras["sheet_color_g"]))
    sheet_color_b.set(str(paras["sheet_color_b"]))
    loop_color_r.set(str(paras["loop_color_r"]))
    loop_color_g.set(str(paras["loop_color_g"]))
    loop_color_b.set(str(paras["loop_color_b"]))
    folder.set("Browse...")
    min_resid.set("None")
    max_resid.set("None")
        
    n_row = 0
    #Row 1
    label1 = tk.Label(top, text="Basic Input",font=('Times New Roman',12, 'bold'), )
    label1.grid(row=n_row,column=0,columnspan=4)
    n_row += 1
    #Row 2
    file_label = tk.Label(top, text="PDB File:" )
    file_label.grid(row=n_row,column=0,pady=5)
    file_button = tk.Button(top,textvariable=pdb_file,width=20,bg="#FFD347",
                              command=lambda:(pdb_file.set(filedialog.askopenfilename()),
                                              pdb_file.set("Browse..." if pdb_file.get()=="" else pdb_file.get())))
    file_button.grid(row=n_row,column=1,pady=5,columnspan=3,sticky=tk.E+tk.W)
    n_row += 1
    #Row 3
    folder_label = tk.Label(top, text="Output Folder:" )
    folder_label.grid(row=n_row,column=0,pady=5)
    folder_button = tk.Button(top,textvariable=folder,width=20,bg="#FFD347",
                              command=lambda:(folder.set(filedialog.askdirectory()),
                                              folder.set("Browse..." if folder.get()=="" else folder.get())))
    folder_button.grid(row=n_row,column=1,pady=5,columnspan=3,sticky=tk.E+tk.W)
    n_row += 1
    #Row 4
    chain_label = tk.Label(top, text="Chain:")
    chain_label.grid(row=n_row,column=0,)
    chain_box = tk.Entry(top,textvariable=chain,validate='all',
                         vcmd=lambda:auto_pptx(pdb_file,chain,pptx))
    chain_box.grid(row=n_row,column=1,pady=5)
    filename_label = tk.Label(top, text="Output PPTX:" )
    filename_label.grid(row=n_row,column=2,pady=5)
    filename_box = tk.Entry(top,textvariable=pptx)
    filename_box.grid(row=n_row,column=3,pady=5,sticky=tk.E+tk.W)
    n_row += 1
    #Row 5
    submit_button = tk.Button(top,text="Submit",width=20,bg="#FF8F8F",
                              command=lambda:(
                                  tk.messagebox.showinfo("Result",main(p2v(paras),folder))))
    submit_button.grid(row=n_row,column=1,pady=20)
    back_button = tk.Button(top,text="Back",width=20,bg="#9090E0",
                          command=lambda:(top.destroy(),gui_main()))
    back_button.grid(row=n_row,column=3,pady=20,)
    n_row += 1
    #Row 6
    label1 = tk.Label(top, text="Additional Settings",font=('Times New Roman',12, 'bold') )
    label1.grid(row=n_row,column=0,columnspan=4)
    n_row += 1
    #Row 7
    figwidth_label = tk.Label(top, text="Figure Width (cm)")
    figwidth_label.grid(row=n_row,column=0,pady=5)
    figwidth_box = tk.Entry(top,textvariable=fig_width)
    figwidth_box.grid(row=n_row,column=1,pady=5)
    charsize_label = tk.Label(top, text="Char. Size (pt)")
    charsize_label.grid(row=n_row,column=2,pady=5)
    charsize_box = tk.Entry(top,textvariable=char_size)
    charsize_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 8
    min_resid_label = tk.Label(top, text="Min. ResID:")
    min_resid_label.grid(row=n_row,column=0,pady=5)
    min_resid_box = tk.Entry(top,textvariable=min_resid)
    min_resid_box.grid(row=n_row,column=1,pady=5)
    min_resid_label = tk.Label(top, text="Max. ResID:")
    min_resid_label.grid(row=n_row,column=2,)
    min_resid_box = tk.Entry(top,textvariable=max_resid)
    min_resid_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 9
    label = tk.Label(top, text="R")
    label.grid(row=n_row,column=1)
    label = tk.Label(top, text="G")
    label.grid(row=n_row,column=2)
    label = tk.Label(top, text="B")
    label.grid(row=n_row,column=3)
    n_row += 1
    #Row 10
    helix_color_label = tk.Label(top, text="α-Helix Color:")
    helix_color_label.grid(row=n_row,column=0,pady=5)
    helix_color_boxr = tk.Entry(top,textvariable=helix_color_r)
    helix_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    helix_color_boxg = tk.Entry(top,textvariable=helix_color_g)
    helix_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    helix_color_boxb = tk.Entry(top,textvariable=helix_color_b)
    helix_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 11
    sheet_color_label = tk.Label(top, text="β-Sheet Color:")
    sheet_color_label.grid(row=n_row,column=0,pady=5)
    sheet_color_boxr = tk.Entry(top,textvariable=sheet_color_r)
    sheet_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    sheet_color_boxg = tk.Entry(top,textvariable=sheet_color_g)
    sheet_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    sheet_color_boxb = tk.Entry(top,textvariable=sheet_color_b)
    sheet_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 12
    loop_color_label = tk.Label(top, text="Loop Color:")
    loop_color_label.grid(row=n_row,column=0,pady=5)
    loop_color_boxr = tk.Entry(top,textvariable=loop_color_r)
    loop_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    loop_color_boxg = tk.Entry(top,textvariable=loop_color_g)
    loop_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    loop_color_boxb = tk.Entry(top,textvariable=loop_color_b)
    loop_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 13
    res_color_button = tk.Button(top,text="Residue Color Map",bg="#DDFFDD",
                              command=lambda:(#top.attributes("-disabled", 1),
                                              res_color_window(top),))
    res_color_button.grid(row=n_row,column=0,pady=5,padx=5,columnspan=4,sticky=tk.E+tk.W)
    n_row += 1
    #Link
    paras["protein"] = {"type":"PDB File","PDB File Name":pdb_file,"chain":chain,
                        "max_resid":max_resid,"min_resid":min_resid}
    paras["pptx"] = pptx
    paras["fig_width"] = fig_width
    paras["char_size"] = char_size
    paras["helix_color_r"] = helix_color_r
    paras["helix_color_g"] = helix_color_g
    paras["helix_color_b"] = helix_color_b
    paras["sheet_color_r"] = sheet_color_r
    paras["sheet_color_g"] = sheet_color_g
    paras["sheet_color_b"] = sheet_color_b
    paras["loop_color_r"] = loop_color_r
    paras["loop_color_g"] = loop_color_g
    paras["loop_color_b"] = loop_color_b
    top.mainloop()
    
def AF_mode():
    top_w = 580
    top_h = 460
    top = tk.Tk()
    top.title("AlphaFold Mode")
    top.geometry('%dx%d'%(top_w,top_h))
    top.resizable(False, False)
    top.iconbitmap("%s/icon.ico"%(my_dir))
    
    UNPID = tk.StringVar()
    chain = tk.StringVar()
    min_resid = tk.StringVar()
    max_resid = tk.StringVar()
    pptx = tk.StringVar()
    folder = tk.StringVar()
    fig_width = tk.StringVar()
    char_size = tk.StringVar()
    helix_color_r = tk.StringVar()
    helix_color_g = tk.StringVar()
    helix_color_b = tk.StringVar()
    sheet_color_r = tk.StringVar()
    sheet_color_g = tk.StringVar()
    sheet_color_b = tk.StringVar()
    loop_color_r = tk.StringVar()
    loop_color_g = tk.StringVar()
    loop_color_b = tk.StringVar()
    
    chain.set("A")
    fig_width.set(paras["fig_width"])
    char_size.set(paras["char_size"])
    helix_color_r.set(str(paras["helix_color_r"]))
    helix_color_g.set(str(paras["helix_color_g"]))
    helix_color_b.set(str(paras["helix_color_b"]))
    sheet_color_r.set(str(paras["sheet_color_r"]))
    sheet_color_g.set(str(paras["sheet_color_g"]))
    sheet_color_b.set(str(paras["sheet_color_b"]))
    loop_color_r.set(str(paras["loop_color_r"]))
    loop_color_g.set(str(paras["loop_color_g"]))
    loop_color_b.set(str(paras["loop_color_b"]))
    folder.set("Browse...")
    min_resid.set("None")
    max_resid.set("None")
        
    n_row = 0
    #Row 1
    label1 = tk.Label(top, text="Basic Input",font=('Times New Roman',12, 'bold'), )
    label1.grid(row=n_row,column=0,columnspan=4)
    n_row += 1
    #Row 2
    UNPID_label = tk.Label(top, text="Uniprot ID:")
    UNPID_label.grid(row=n_row,column=0,pady=5)
    unpID_box = tk.Entry(top,textvariable=UNPID,validate='key',
                         vcmd=lambda:auto_pptx(UNPID,chain,pptx))
    unpID_box.grid(row=n_row,column=1,pady=5)
    filename_label = tk.Label(top, text="Output PPTX:" )
    filename_label.grid(row=n_row,column=2,pady=5)
    filename_box = tk.Entry(top,textvariable=pptx)
    filename_box.grid(row=n_row,column=3,pady=5,sticky=tk.E+tk.W)
    n_row += 1
    #Row 3
    folder_label = tk.Label(top, text="Output Folder:" )
    folder_label.grid(row=n_row,column=0,pady=5)
    folder_button = tk.Button(top,textvariable=folder,width=20,bg="#FFD347",
                              command=lambda:(folder.set(filedialog.askdirectory()),
                                              folder.set("Browse..." if folder.get()=="" else folder.get())))
    folder_button.grid(row=n_row,column=1,pady=5,columnspan=3,sticky=tk.E+tk.W)
    n_row += 1
    #Row 5
    submit_button = tk.Button(top,text="Submit",width=20,bg="#FF8F8F",
                              command=lambda:(
                                  tk.messagebox.showinfo("Result",main(p2v(paras),folder))))
    submit_button.grid(row=n_row,column=1,pady=20)
    back_button = tk.Button(top,text="Back",width=20,bg="#9090E0",
                          command=lambda:(top.destroy(),gui_main()))
    back_button.grid(row=n_row,column=3,pady=20,)
    n_row += 1
    #Row 6
    label1 = tk.Label(top, text="Additional Settings",font=('Times New Roman',12, 'bold') )
    label1.grid(row=n_row,column=0,columnspan=4)
    n_row += 1
    #Row 7
    figwidth_label = tk.Label(top, text="Figure Width (cm)")
    figwidth_label.grid(row=n_row,column=0,pady=5)
    figwidth_box = tk.Entry(top,textvariable=fig_width)
    figwidth_box.grid(row=n_row,column=1,pady=5)
    charsize_label = tk.Label(top, text="Char. Size (pt)")
    charsize_label.grid(row=n_row,column=2,pady=5)
    charsize_box = tk.Entry(top,textvariable=char_size)
    charsize_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 8
    min_resid_label = tk.Label(top, text="Min. ResID:")
    min_resid_label.grid(row=n_row,column=0,pady=5)
    min_resid_box = tk.Entry(top,textvariable=min_resid)
    min_resid_box.grid(row=n_row,column=1,pady=5)
    min_resid_label = tk.Label(top, text="Max. ResID:")
    min_resid_label.grid(row=n_row,column=2,)
    min_resid_box = tk.Entry(top,textvariable=max_resid)
    min_resid_box.grid(row=n_row,column=3,pady=5)
    n_row += 1
    #Row 9
    label = tk.Label(top, text="R")
    label.grid(row=n_row,column=1)
    label = tk.Label(top, text="G")
    label.grid(row=n_row,column=2)
    label = tk.Label(top, text="B")
    label.grid(row=n_row,column=3)
    n_row += 1
    #Row 10
    helix_color_label = tk.Label(top, text="α-Helix Color:")
    helix_color_label.grid(row=n_row,column=0,pady=5)
    helix_color_boxr = tk.Entry(top,textvariable=helix_color_r)
    helix_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    helix_color_boxg = tk.Entry(top,textvariable=helix_color_g)
    helix_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    helix_color_boxb = tk.Entry(top,textvariable=helix_color_b)
    helix_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 11
    sheet_color_label = tk.Label(top, text="β-Sheet Color:")
    sheet_color_label.grid(row=n_row,column=0,pady=5)
    sheet_color_boxr = tk.Entry(top,textvariable=sheet_color_r)
    sheet_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    sheet_color_boxg = tk.Entry(top,textvariable=sheet_color_g)
    sheet_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    sheet_color_boxb = tk.Entry(top,textvariable=sheet_color_b)
    sheet_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 12
    loop_color_label = tk.Label(top, text="Loop Color:")
    loop_color_label.grid(row=n_row,column=0,pady=5)
    loop_color_boxr = tk.Entry(top,textvariable=loop_color_r)
    loop_color_boxr.grid(row=n_row,column=1,pady=5,padx=5)
    loop_color_boxg = tk.Entry(top,textvariable=loop_color_g)
    loop_color_boxg.grid(row=n_row,column=2,pady=5,padx=5)
    loop_color_boxb = tk.Entry(top,textvariable=loop_color_b)
    loop_color_boxb.grid(row=n_row,column=3,pady=5,padx=5)
    n_row += 1
    #Row 13
    res_color_button = tk.Button(top,text="Residue Color Map",bg="#DDFFDD",
                              command=lambda:(#top.attributes("-disabled", 1),
                                              res_color_window(top),))
    res_color_button.grid(row=n_row,column=0,pady=5,padx=5,columnspan=4,sticky=tk.E+tk.W)
    n_row += 1
    #Link
    paras["protein"] = {"type":"AF","UNP ID":UNPID,"chain":"A",
                        "max_resid":max_resid,"min_resid":min_resid}
    paras["pptx"] = pptx
    paras["fig_width"] = fig_width
    paras["char_size"] = char_size
    paras["helix_color_r"] = helix_color_r
    paras["helix_color_g"] = helix_color_g
    paras["helix_color_b"] = helix_color_b
    paras["sheet_color_r"] = sheet_color_r
    paras["sheet_color_g"] = sheet_color_g
    paras["sheet_color_b"] = sheet_color_b
    paras["loop_color_r"] = loop_color_r
    paras["loop_color_g"] = loop_color_g
    paras["loop_color_b"] = loop_color_b
    top.mainloop()    
    
    
def res_color_window(top0):
    top_w = 1050
    top_h = 650
    top = tk.Toplevel(top0)
    top.title("Residue Color Map")
    top.geometry('%dx%d'%(top_w,top_h))
    top.resizable(False, False)
    #Row 1
    label1 = tk.Label(top, text="RGB Colors of Residues",font=('Times New Roman',12, 'bold') )
    label1.grid(row=0,column=0,columnspan=8)
    #Row2
    label = tk.Label(top, text="R",font=('Times New Roman',10, 'bold') )
    label.grid(row=1,column=1)
    label = tk.Label(top, text="G",font=('Times New Roman',10, 'bold') )
    label.grid(row=1,column=2)
    label = tk.Label(top, text="B",font=('Times New Roman',10, 'bold') )
    label.grid(row=1,column=3)
    label = tk.Label(top, text="R",font=('Times New Roman',10, 'bold') )
    label.grid(row=1,column=5)
    label = tk.Label(top, text="G",font=('Times New Roman',10, 'bold') )
    label.grid(row=1,column=6)
    label = tk.Label(top, text="B",font=('Times New Roman',10, 'bold') )
    label.grid(row=1,column=7)
    #Row 3
    aas = "ARNDCQEGHILKMFPSTWYV?"
    color_vars = dict()
    for n,aa in enumerate(aas):
        label = tk.Label(top, text="%s:"%(aa))
        label.grid(row=n//2+2,column=0+n%2*4,pady=5)
        color_vars[aa] = []
        for i in range(3):
            tmp = tk.StringVar()
            tmp.set(str(paras["res_color"][aa][i]))
            box = tk.Entry(top,textvariable=tmp)
            box.grid(row=n//2+2,column=i+1+n%2*4,pady=5,padx=5)
            color_vars[aa].append(tmp)
    n_row = n//2 + 3
    #Speciail Maps0
    pos_r = tk.StringVar()
    pos_g = tk.StringVar()
    pos_b = tk.StringVar()
    pos_r.set("255")
    pos_g.set("0")
    pos_b.set("0")
    neg_r = tk.StringVar()
    neg_g = tk.StringVar()
    neg_b = tk.StringVar()
    neg_r.set("0")
    neg_g.set("0")
    neg_b.set("255")
    neu_r = tk.StringVar()
    neu_g = tk.StringVar()
    neu_b = tk.StringVar()
    neu_r.set("0")
    neu_g.set("0")
    neu_b.set("0")
    label = tk.Label(top, text="Positive/Negative Map")
    label.grid(row=n_row,column=0,pady=5,columnspan=4)
    label = tk.Label(top, text="Positive:")
    label.grid(row=n_row+1,column=0,pady=5)
    pos_boxr = tk.Entry(top,textvariable=pos_r)
    pos_boxr.grid(row=n_row+1,column=1,pady=5,padx=5)
    pos_boxg = tk.Entry(top,textvariable=pos_g)
    pos_boxg.grid(row=n_row+1,column=2,pady=5,padx=5)
    pos_boxb = tk.Entry(top,textvariable=pos_b)
    pos_boxb.grid(row=n_row+1,column=3,pady=5,padx=5)
    label = tk.Label(top, text="Negative:")
    label.grid(row=n_row+2,column=0,pady=5)
    neg_boxr = tk.Entry(top,textvariable=neg_r)
    neg_boxr.grid(row=n_row+2,column=1,pady=5,padx=5)
    neg_boxg = tk.Entry(top,textvariable=neg_g)
    neg_boxg.grid(row=n_row+2,column=2,pady=5,padx=5)
    neg_boxb = tk.Entry(top,textvariable=neg_b)
    neg_boxb.grid(row=n_row+2,column=3,pady=5,padx=5)
    label = tk.Label(top, text="Neutral:")
    label.grid(row=n_row+3,column=0,pady=5)
    neu_boxr = tk.Entry(top,textvariable=neu_r)
    neu_boxr.grid(row=n_row+3,column=1,pady=5,padx=5)
    neu_boxg = tk.Entry(top,textvariable=neu_g)
    neu_boxg.grid(row=n_row+3,column=2,pady=5,padx=5)
    neu_boxb = tk.Entry(top,textvariable=neu_b)
    neu_boxb.grid(row=n_row+3,column=3,pady=5,padx=5)
    button = tk.Button(top,text="Apply This Map",bg="#FFD347",
                              command=lambda:(set_residue_color(color_vars,aas,neu_r,neu_g,neu_b),
                                              set_residue_color(color_vars,"KRH",pos_r,pos_g,pos_b),
                                              set_residue_color(color_vars,"DE",neg_r,neg_g,neg_b),))
    button.grid(row=n_row+4,column=0,pady=5,padx=5,columnspan=4,sticky=tk.E+tk.W)
    #Speciail Maps1
    pol_r = tk.StringVar()
    pol_g = tk.StringVar()
    pol_b = tk.StringVar()
    pol_r.set("255")
    pol_g.set("0")
    pol_b.set("0")
    npol_r = tk.StringVar()
    npol_g = tk.StringVar()
    npol_b = tk.StringVar()
    npol_r.set("0")
    npol_g.set("0")
    npol_b.set("255")
    label = tk.Label(top, text="Polar/Nonpolar Map")
    label.grid(row=n_row,column=5,pady=5,columnspan=4)
    label = tk.Label(top, text="Polar:")
    label.grid(row=n_row+1,column=4,pady=5)
    pol_boxr = tk.Entry(top,textvariable=pol_r)
    pol_boxr.grid(row=n_row+1,column=5,pady=5,padx=5)
    pol_boxg = tk.Entry(top,textvariable=pol_g)
    pol_boxg.grid(row=n_row+1,column=6,pady=5,padx=5)
    pol_boxb = tk.Entry(top,textvariable=pol_b)
    pol_boxb.grid(row=n_row+1,column=7,pady=5,padx=5)
    label = tk.Label(top, text="Nonpolar:")
    label.grid(row=n_row+2,column=4,pady=5)
    npol_boxr = tk.Entry(top,textvariable=npol_r)
    npol_boxr.grid(row=n_row+2,column=5,pady=5,padx=5)
    npol_boxg = tk.Entry(top,textvariable=npol_g)
    npol_boxg.grid(row=n_row+2,column=6,pady=5,padx=5)
    npol_boxb = tk.Entry(top,textvariable=npol_b)
    npol_boxb.grid(row=n_row+2,column=7,pady=5,padx=5)
    button = tk.Button(top,text="Apply This Map",bg="#FFD347",
                              command=lambda:(set_residue_color(color_vars,"DEKRHNQSTY",pol_r,pol_g,pol_b),
                                              set_residue_color(color_vars,"AGVLIPFMWC?",npol_r,npol_g,npol_b),))
    button.grid(row=n_row+4,column=4,pady=5,padx=5,columnspan=4,sticky=tk.E+tk.W)
    n_row += 5
    button = tk.Button(top,text="Save",bg="#FF8F8F",
                              command=lambda:(save_residue_color(color_vars),top.destroy()))
    button.grid(row=n_row+4,column=0,pady=20,padx=5,columnspan=4,sticky=tk.E+tk.W)
    button = tk.Button(top,text="Exit",bg="#9090E0",
                              command=lambda:(top.destroy()))
    button.grid(row=n_row+4,column=4,pady=20,padx=5,columnspan=4,sticky=tk.E+tk.W)
    top.mainloop()


    
def auto_pptx(PDBID,chain,pptx):
    if PDBID.get() and chain.get():
        pptx.set("%s_%s.pptx"%(PDBID.get().split("/")[-1].split(".pdb")[0],chain.get()))
    return True

def p2v(d0):
    d = dict()
    for k in d0.keys():
        if type(d0[k]) == type(tk.StringVar()):
            d[k] = d0[k].get()
        elif type(d0[k]) == type(dict()):
            d[k] = p2v(d0[k])
        else:
            d[k] = d0[k]
    return d

def set_residue_color(d,reses,r,g,b):
    for aa in reses:
        d[aa][0].set(r.get())
        d[aa][1].set(g.get())
        d[aa][2].set(b.get())

def save_residue_color(d):
    tmp = dict()
    for aa in d.keys():
        try:
            tmp[aa] = [int(d[aa][0].get()),int(d[aa][1].get()),int(d[aa][2].get())]
        except:
            tk.messagebox.showinfo("Error","Invalid color in %s"%(aa))
            return
        if max(tmp[aa])>255 or min(tmp[aa])<0:
            tk.messagebox.showinfo("Error","Invalid color in %s!\nRGB values should be 0~255!"%(aa))
            return
    paras["res_color"] = tmp
    
    
def main(paras,folder):   
    print(paras)
    #Check paras validity
    if paras["protein"]["type"] == "PDB ID":
        if len(paras["protein"]["PDB ID"]) != 4:
            return "Please input a valid PDB ID!"
    elif paras["protein"]["type"] == "PDB File":
        if paras["protein"]["PDB File Name"] == "Browse...":
            return "Please select a PDB file!"
        if not os.path.exists(paras["protein"]["PDB File Name"]):
            return "PDB file does not exist!"
    elif paras["protein"]["type"] == "AF":
        if len(paras["protein"]["UNP ID"]) == 0:
            return "Please input a valid Uniprot ID!"
    if paras["protein"]["chain"] == "":
        return "Please input a valid chain ID!"
    if folder.get() == "Browse...":
        return "Please select an output folder!"
    if not os.path.exists(folder.get()):
        return "Folder does not exists!"
    os.chdir(folder.get())
    print(os.getcwd())
    if paras["pptx"] == "":
        return "Please input a name for the output file!"
    try:
        float(paras["fig_width"])
    except:
        return "Please input a valid Figure Width!"
    try:
        float(paras["char_size"])
    except:
        return "Please input a valid Char Size!"
    try:
        if paras["protein"]["min_resid"] != "None":
            int(paras["min_resid"])
        if paras["protein"]["max_resid"] != "None":
            int(paras["max_resid"])
    except:
        return "Please input a valid range of residue IDs!"
    for k in paras.keys():
        if "color" in k and k!= "res_color":
            try:
                int(paras[k])
            except:
                return "Please input a valid %s!"%(" ".join(k.split("_")[0:2]))
            if int(paras[k]) < 0 or int(paras[k]) > 255:
                return "Please input a valid %s!\nRGB values should be 0~255!"%(" ".join(k.split("_")[0:2]))
    
    a = AASequence(paras)
    if a.error:
        return a.error
    a.run()
    if a.error:
        return a.error
    return "Done!" 
    
gui_main()

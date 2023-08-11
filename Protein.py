# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:09:38 2023

@author: 15308
"""
import requests
import os
my_dir = os.getcwd()

class Protein():
    def __init__(self,info):
        self.error = ""
        self.residue_dict = dict()
        if info["min_resid"] == "None":
            self.min_resid = -999999999999999999999999999999999999999999999
        else:
            self.min_resid = int(info["min_resid"])
        if info["max_resid"] == "None":
            self.max_resid = 999999999999999999999999999999999999999999999
        else:
            self.max_resid = int(info["max_resid"])
            
        if info["type"] == "PDB ID":
            self.fetch_from_RSCB(info["PDB ID"],info["chain"])
        elif info["type"] == "PDB File":
            self.fetch_from_PDBFile(info["PDB File Name"],info["chain"])
        elif info["type"] == "AF":
            self.fetch_from_AF(info["UNP ID"],info["chain"])
            
    def fetch_from_RSCB(self,pdb_id,chain):
        res = requests.get("https://files.rcsb.org/download/%s.pdb"%(pdb_id))
        if res.status_code == 200:
            pdb_file = "%s.pdb"%(pdb_id)
            f = open(pdb_file,"w")
            f.write(res.text)
            f.close()
            self.fetch_from_PDBFile(pdb_file,chain)
        else:
            res = requests.get("https://files.rcsb.org/download/11BG.pdb")
            if res.status_code == 200:
                self.error = "Invalid PDB ID!"
                return
            else:
                self.error = "Network Error!"
                return
    
    def fetch_from_AF(self,unp_id,chain):
        res = requests.get("https://alphafold.ebi.ac.uk/files/AF-%s-F1-model_v4.pdb"%(unp_id))
        if res.status_code == 200:
            pdb_file = "AF-%s-F1-model_v4.pdb"%(unp_id)
            f = open(pdb_file,"w")
            f.write(res.text)
            f.close()
            self.fetch_from_PDBFile(pdb_file,chain)
        else:
            res = requests.get("https://alphafold.ebi.ac.uk/files/AF-P05067-F1-model_v4.pdb")
            if res.status_code == 200:
                self.error = "Invalid UniProt ID!\n Or this protein does not exist in AlphaFold Database!"
                return
            else:
                self.error = "Network Error!"
                return
    
    def fetch_from_PDBFile(self,pdb_file,chain):
        #1, Use DSSP
        dssp_file = pdb_file.split("/")[-1].split(".pdb")[0]+".dssp"
        print("%s/mkdssp.exe -i %s -o %s"%(my_dir,pdb_file,dssp_file))
        os.system("%s/mkdssp.exe -i %s -o %s"%(my_dir,pdb_file,dssp_file))
        if not os.path.exists(dssp_file):
            self.error = "Error in calculating secondary structure!\nPlease check your PDB file!"
            return
        #2, Read DSSP File
        f = open(dssp_file)
        fli = f.read().split("\n")
        f.close()
        j = 0
        while fli[j].replace(" ","")[0:8] != "#RESIDUE":
            j += 1
        for i in range(j+1,len(fli)):
            if len(fli[i]) < 17:
                continue
            if "!*" not in fli[i] and fli[i][10:12].strip().upper() == chain.upper():
                res_id = int(fli[i][5:10])
                if res_id > self.max_resid or res_id < self.min_resid:
                    continue
                single_name = fli[i][13]
                if fli[i][16] in "HGIP":
                    ss = "H"
                elif fli[i][16] in "BE":
                    ss = "S"
                else:
                    ss = ""
                self.residue_dict[res_id] = [single_name,ss]
        #3, Check missing
        res_ids = list(self.residue_dict.keys())
        if len(res_ids) == 0:
            self.error = "No residue is found in chain %s of the protein!"%(chain)
            return
        res_ids.sort()
        for i in range(min(res_ids),max(res_ids)+1):
            if i not in res_ids:
                self.residue_dict[i] = ["?",""]
        
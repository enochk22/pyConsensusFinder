#!/usr/bin/python
import _mypath
import CF

HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

configfile = HOME+"/config/config.cfg"
defaults = {
            'File_Name' : "None",
            'Email' : "None",
            'Maximum_Sequences' : "2000",
            'Blast_E_Value' : "1e-3",
            'Consensus_Threshold' : "0",#need to check if zero will give desired results. Might need to be 1
            'Consensus_Ratio' : "7",
            'Use_Complete_sequences' : "True",
            'Alignment_Iterations' : "1",
            'Maximum_Redundancy_Threshold' : "0.9",
            'Logging' : "False",
            'Keep_Temp_Files' : "False",
            'Chain' : 'A',
            'Angstrom' : "1",
            'Residue' : "0",
            'PDB_Name' : "None",
            'Blast_binary' : HOME+"/binaries/blastp",
            'CDHIT_binary' : HOME+"/binaries/cd-hit",
            'ClustalO_binary' : HOME+"/binaries/clustalo-1.2.4-Ubuntu-x86_64",
            }
            
MainProgram=CF.CF(defaults,configfile,write=False)
Mutations=MainProgram.mutations

MutationsNotinActiveSite=[]

for i in Mutations:
    print(i.res) #residue number
    print(i.wt) #wildtype residue id
    print(i.sug) #suggested mutation id
    if i (test if i is in active site):
        MutationsNotinActiveSite.append(i)
settings.PDB
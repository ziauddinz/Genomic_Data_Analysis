import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
import openpyxl
import pandas as pd


def getCGoe(sequence):

   
    sequence = sequence.upper()
    CG = sequence.count("CG")
    TG = sequence.count("TG")
    C = sequence.count("C")
    G = sequence.count("G")
    A = sequence.count('A')      
    T = sequence.count('T')
    try:
        cpgoe = (CG/(C*G))*len(sequence)    
    except ZeroDivisionError:
        cpgoe=0
    try:
        tpgoe = (TG/(T*G))*len(sequence)

    except ZeroDivisionError:
        tpgoe=0
        
    try:
        GCcontent = (C+G)/(A+T+G+C)*100
    except ZeroDivisionError:
        GCcontent=0       
    return [cpgoe,tpgoe,A,T,C,G,CG,TG,GCcontent]


    # return oe
# print(getCGoe(A))

def getOEByWindow(seq, window, step):

    """
    例：
    window size=100
    step size = 100
    计算oe
    """

    seq = seq.upper()
    start = 0
    results = {}  #
    count_end = [] #
    for end in range(window-1, len(seq), step):
        count_end.append(end)     # 
        getSeq = seq[start:end+1] # 
        getSeq = getSeq.upper()
        try:
            CpGoe = getCGoe(getSeq)[0]   #
        except TypeError:
            CpGoe = 0

        try:
            TpGoe = getCGoe(getSeq)[1]
        except TypeError:
            TpGoe = 0

        try:
            Acount = getCGoe(getSeq)[2]     #
        except TypeError:
            Acount = 0
        try:
            Tcount = getCGoe(getSeq)[3]
        except TypeError:
            Tcount = 0
        try:
            Ccount = getCGoe(getSeq)[4]
        except TypeError:
            Ccount = 0
        try:
            Gcount = getCGoe(getSeq)[5]
        except TypeError:
            Gcount = 0
        try:
            CGcount = getCGoe(getSeq)[6]
        except TypeError:
            CGcount = 0
        try:
            TGcount = getCGoe(getSeq)[7]
        except TypeError:
            TGcount = 0
        try:
            GCcontent = getCGoe(getSeq)[8]
        except TypeError:
            GCcontent = 0

        startkb = start+1         # 
        endkb = end+1             # 
        results[f'{startkb}-{endkb}'] = [CpGoe,TpGoe,Acount,Tcount,Ccount,Gcount,CGcount,TGcount,GCcontent]  # 输出结果字典
        start += step
    # print(count_end)
    # print(len(seq))
    if (len(seq)-count_end[-1]-1) == 0:      # 
        print("The sliding window is complete.")
    else:
        remain_seq = seq[count_end[-1]+1:len(seq)+1]   
        try:
            re_Acount = getCGoe(remain_seq)[2]     # 
            re_Tcount = getCGoe(remain_seq)[3]
            re_Ccount = getCGoe(remain_seq)[4]
            re_Gcount = getCGoe(remain_seq)[5]
            re_CGcount = getCGoe(remain_seq)[6]
            re_TGcount = getCGoe(remain_seq)[7]
            re_GCcontent = getCGoe(remain_seq)[8]
        except:
            re_Acount = 0     # 
            re_Ccount = 0
            re_Gcount = 0
            re_CGcount = 0
            re_TGcount = 0
            re_GCcontent = 0         

        try:
            remain_CpGoe = getCGoe(remain_seq)[0]
        except TypeError:
            remain_CpGoe = 0          

        try:
            remain_TpGoe = getCGoe(remain_seq)[1]
        except TypeError:
            remain_TpGoe = 0

        rem_startkb = count_end[-1]+1+1        
        results[f'{rem_startkb}-{len(seq)}'] = [remain_CpGoe,remain_TpGoe,re_Acount,re_Tcount,re_Ccount,re_Gcount,re_CGcount,re_TGcount,re_GCcontent]
    for key,value in list(results.items()):  # 
        if value.count(0) > 8:               # 
    return results



def main(input_file, output_file):
   
    file_exists = os.path.isfile(output_file)    
    
    # fasta
    for fastaseq in SeqIO.parse(input_file, "fasta"):
        
        out_end2 = pd.DataFrame()
        Seq_id = fastaseq.id 
        ca_seq = fastaseq.seq  # 
        CpGoe = getOEByWindow(ca_seq, len(ca_seq), len(ca_seq))
        out_end = pd.DataFrame(CpGoe)
        out_end2 = out_end.T  # 
        out_end2.insert(loc=9, value=Seq_id, column='Seq_id')  #

        header = ['CpGoe', 'TpGoe', 'Acount', 'Tcount', 'Ccount', 'Gcount', 'CGcount', 'TGcount', 'GCcontent', 'Seq_id']
        
        if file_exists:
            out_end2.to_csv(output_file, header=False, mode='a')  
        else:
            out_end2.to_csv(output_file, header=header, mode='w')  #
            file_exists = True  
if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Calculate gene CpG observed/expected ratio and save results to CSV.")
    parser.add_argument("input_file", help="Path to input FASTA file.")
    parser.add_argument("output_file", help="Path to output CSV file.")


    args = parser.parse_args()
    main(args.input_file, args.output_file)

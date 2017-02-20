#encoding:utf-8

import os
import numpy as np
from scipy import stats
import warnings
import string
import re

try:
    import cPickle as pickle
except ImportError:
    import pickle

warnings.filterwarnings('error')

class Matrix(object):

    def __init__(self):

        self.normal_gene = []
        self.tumor_gene = []
        self.union_NT = []
        self.gene_go_data = {}
        self.node_weight_connect = {}


    def get_matrix(self):

        raw_normal =  {}
        for gene in open('BRCA-Normal-GeneExp.txt', 'r'):
            gene = gene.split()
            gene_name = gene[0]
            self.normal_gene.append(gene_name)
            raw_normal[gene_name] = []

            for i in range(1, len(gene)):
                raw_normal[gene_name].append(float(gene[i]))

        raw_tumor = {}
        for gene in open('BRCA-Tumor-GeneExp.txt', 'r'):
            gene = gene.split()
            gene_name = gene[0]
            self.tumor_gene.append(gene_name)
            raw_tumor[gene_name] = []

            for i in range(1, len(gene)):
                raw_tumor[gene_name].append(float(gene[i]))

        raw_ppi = [x.strip() for x in open('HPRD-PPI.txt', 'r')]
        normal_matrix = []
        tumor_matrix = []
        cc = 0
        for single_ppi in raw_ppi:

            normal_sign = False
            tumor_sign = False
            single_ppi = single_ppi.strip()

            first_p, second_p = single_ppi.split('#')

            if first_p in normal_gene and second_p in normal_gene:
                x_normal = raw_normal[first_p]
                y_normal = raw_normal[second_p]
                
                try:
                    cor, p_value = stats.spearmanr(x_normal, y_normal)
                    if abs(cor) >= 0.8:
                        normal_matrix.append(single_ppi)
                except Exception, e:
                    cc += 1
                    # print e
                    pass

            if first_p in tumor_gene and second_p in tumor_gene:
                x_tumor = raw_tumor[first_p]
                y_tumor = raw_tumor[second_p]
                
                try:
                    cor, p_value = stats.spearmanr(x_tumor, y_tumor)
                    if abs(cor) >= 0.8:
                        tumor_matrix.append(single_ppi)
                except Exception, e:
                    # print 'error'
                    # print e
                    pass
            
        print '#' * 100
        print 'N-T:'
        # N - T
        N_T = list(set(normal_matrix).difference(set(tumor_matrix)))
        print N_T
        print '#' * 100
        print 'T-N:'
        # T - N
        T_N = list(set(tumor_matrix).difference(set(normal_matrix)))
        print T_N
        # (N - T) U (T - N)
        print '#' * 100
        self.union_NT = list(set(N_T).union(set(T_N)))
        print 'union:'
        print self.union_NT
        serial_union = pickle.dumps(union_NT)
        fp = open('serial_union.tmp', 'w')
        fp.write(serial_union)
        fp.close()


    def count_node_weight(self):

        union_NT = pickle.load(open('serial_union.tmp', 'rb'))
        # check repeat
        for value in union_NT:
            first, second = value.split('#')
            # print first, second
            swap_value = second + '#' + first
            if swap_value in union_NT:
                print '!' * 100
        
        for go_data in open('GO-Human-2.txt', 'r'):
            gene = go_data.strip().split('#')[0]
            pattern = re.compile(r'GO:(\d+)')
            match_result = pattern.findall(go_data)
            self.gene_go_data[gene] = match_result
        
        # print gene_go_data
        # raw_input('wait...')

        for value in union_NT:
            gene_first, gene_second = value.split('#')
            self.gene_go_data
            if test:
                pass

            for gene in value.split('#'):
                if gene not in gene_connect_count:
                    gene_count
                    for _ in union_NT:
                        if string.find(_, gene) != -1:
                            gene_count
           

def main():
    # get_matrix()
    # next_handle()
    martrix = Matrix()
    martrix.count_node_weight()


if __name__ == '__main__':
    os.system('clear')
    main()

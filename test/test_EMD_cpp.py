#
# test_EMD_cpp.py
# unit tests for the crayon EMD C++ methods
#
# Copyright (c) 2018 Wesley Reinhart.
# This file is part of the crayon project, released under the Modified BSD License.

from __future__ import print_function

import numpy as np

import os
test_path = os.path.abspath(os.path.dirname(__file__))
build_path = os.getcwd()

import sys
sys.path.insert(0,build_path)
import _crayon

sys.path.insert(0,test_path)
from validation_emd import *

from emd import emd

import unittest

class ValidateEMD(unittest.TestCase):
    # run this every time
    def setUp(self):
        pass

    def testGPU(self):
        _crayon.gpuAdd(10)
        pass

    def testValidationEMD(self):

        n = len(gdvList)
        crayon_emd = np.zeros((n,n))
        crayon_emd_gpu = np.zeros((n,n))
        py_emd = np.zeros((n,n))
        for i, P in enumerate(gdvList):
            for j, Q in enumerate(gdvList):
                if i == j:
                    continue
                crayon_emd[i,j] = _crayon.emd(P,Q)
                crayon_emd_gpu[i,j] = _crayon.emdGPU(P,Q)
                py_emd[i,j] = emd(P,Q)
                print(i,j,':',crayon_emd[i,j],crayon_emd_gpu[i,j],py_emd[i,j])
                break
            break

        np.testing.assert_array_almost_equal(crayon_emd,py_emd)

        # d = _crayon.emd_dists(gdvList[0],gdvList[1])
        # np.testing.assert_array_almost_equal(d,distAB)
        # d = _crayon.emd(gdvList[0],gdvList[1])
        # self.assertAlmostEqual(d,2.660116954218473,10)
        #
        # d = _crayon.emd_dists(gdvList[2],gdvList[3])
        # np.testing.assert_array_almost_equal(d,distCD)
        # d = _crayon.emd(gdvList[2],gdvList[3])
        # self.assertAlmostEqual(d,0.467100676478769,10)

        # n = len(gdvList)
        # myemds = np.zeros((n,n))
        # pyemds = np.zeros((n,n))
        # for i in range(n):
        #     print(i,end=': ')
        #     for j in range(n):
        #         print(j,end=' ')
        #         myemds[i,j] = _crayon.emd(gdvList[i],gdvList[j])
        #         pyemds[i,j] = emd(gdvList[i],gdvList[j])
        #     print('')

        # print('done')

        # print(myemds)
        # print(pyemds)

if __name__ == "__main__":
    unittest.main(argv = ['test.py', '-v'])

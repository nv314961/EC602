# Copyright 2017 nv314961@bu.edu
import unittest
import subprocess
import string

#please change this to valid author emails
#AUTHORS = ['?@bu.edu', '??@bu.edu', '???@bu.edu']

# make test cases for:
# make sure precision of data is consistent from input to output

AUTHORS = ['nv314961@bu.edu']
PROGRAM_TO_TEST = "cfiles/collisionc_27"

def runprogram(program, args, inputstr):
    coll_run = subprocess.run(
        [program, *args],
        input=inputstr.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout = 1 # if program takes > 1 sec to complete, count as error
		)

    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)

def replaceTrailingZeros(out):
    outLines = out.split('\n')
    del outLines[-1] # empty \n element was appearing at the end of outLines
    newOut = ""
    for i in outLines:
        try:
            i = '{:g}'.format(float(i)) # the magic: remove trailing zeros
            newOut += (i + '\n') # construct new string, include \n
        except ValueError: # when we don't get a string with just a number (time), just pass it as is to the new string
            newOut += (i + '\n')
            continue
    return newOut
	
class CollisionTestCase(unittest.TestCase):		
    def test_invalid_input(self):
        strin = " two \n one 0 0 5 -1 1"
        correct_out = ""
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        out = replaceTrailingZeros(out)
        self.assertEqual(rc,1) # should return 1 since coords invalid
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")		

    def test_times_notInOrder(self):
        strin = "one 0 0 1 1"
        correct_out = "1\none 1 1 1 1\n3\none 3 3 1 1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3","1"],strin)
        out = replaceTrailingZeros(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_identical_labels(self):
        strin = "one 20 10 1 0\n one 0 0 -1 -1"
        correct_out = "5\none 25 10 1 0\none -5 -5 -1 -1\n"
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        out = replaceTrailingZeros(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

    def test_sparse_timeInputs(self):
        strin = "one 10 10 -1 -1\ntwo 0 0 1 1"
        correct_out = ("1\n" +
        "one 9 9 -1 -1\n" +
        "two 1 1 1 1\n" +
        "2\n" +
        "one 9.0710678 9.0710678 1 1\n" +
        "two 0.92893219 0.92893219 -1 -1\n" +
        "100\n" +
        "one 107.07107 107.07107 1 1\n" +
        "two -97.071068 -97.071068 -1 -1\n" +
        "10000\n" +
        "one 10007.071 10007.071 1 1\n" +
        "two -9997.0711 -9997.0711 -1 -1\n" +
        "100000\n" +
        "one 100007.07 100007.07 1 1\n" +
        "two -99997.071 -99997.071 -1 -1\n")
        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1", "2", "100", "10000", "100000"],strin)
        out = replaceTrailingZeros(out)        
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")							

    def test_complex_moreThanTen(self):
        strin = ("2MU133 -34.94 -69.13 0.468 -0.900\n" +
        "0WI913 -43.08 92.12 -0.811 -0.958\n" +
        "6UP738  2.97 -66.25 -0.077 0.074\n" +
        "1IA244 72.94 -86.02 -0.665 -0.283\n" +
        "8RT773 -32.25 -2.63 -0.797 0.628\n" +
        "0HV350 -103.97 24.21 0.960 -0.870\n" +
        "0DU118 -82.09 44.95 0.661 -0.343\n" +
        "4FA522 -18.20 72.32 0.734 -0.990\n" +
        "1WR684 31.71 68.89 -0.509 -0.706\n" +
        "7SW673 41.29 42.68 0.549 -0.012\n" +
        "eleven -71.97 21.21 0.960 4.870\n" +
        "twelve -92.09 49.95 0.661 -3.344\n" +
        "thirteen -180.20 82.32 3.734 -3.990\n" +
        "fourteen 800.04 1.25 -100 0.283" )
		
        correct_out = ("300\n" +
        "2MU133 -18.116664 -641.34782 -0.033420867 -2.1262697\n" +
        "0WI913 1011.105 2910.8912 3.6933555 9.9219018\n" +
        "6UP738 -20.13 -44.05 -0.077 0.074\n" +
        "1IA244 -126.56 -170.92 -0.665 -0.283\n" +
        "8RT773 -28918.97 -2751.975 -99.002647 -9.4427547\n" +
        "0HV350 1053.5239 -628.83255 4.1039501 -2.2500316\n" +
        "0DU118 116.21 -57.95 0.661 -0.343\n" +
        "4FA522 34.084844 -356.55524 0.1031531 -1.4854472\n" +
        "1WR684 46.925156 -11.034758 0.1218469 -0.21055284\n" +
        "7SW673 205.99 39.08 0.549 -0.012\n" +
        "eleven -883.95847 885.69825 -2.8507926 2.8034487\n" +
        "twelve 559.40172 -513.94277 2.2945428 -1.6468721\n" +
        "thirteen -259.10891 -859.72686 -0.54207201 -3.0808265\n" +
        "fourteen -749.83708 514.23551 -2.4879158 1.5404041\n")

        (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["300"],strin)
        out = replaceTrailingZeros(out)
        self.assertEqual(rc,0)
        self.assertEqual(out,correct_out)
        self.assertEqual(errs,"")

		
    def test_programname(self):
        self.assertTrue(PROGRAM_TO_TEST.startswith('cfiles/col'),"wrong program name")

def main():
    unittest.main()

if __name__ == '__main__':
    main()


	
"""    # def test_one_xy_velocity_frac(self):
        # strin = "one 20 10 -1.1 1.1"
        # correct_out = "3\none 16.7 13.3 -1.1 1.1\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["3"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_time_neg(self):
        # strin = "one 20 10 -1.1 1.1"
        # correct_out = ""
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["-6"],strin)
        # self.assertEqual(rc,2) # should return 2 since time is neg
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_time_NaN(self):
        # strin = "one 20 10 -1 1"
        # correct_out = ""
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["t"],strin)
        # print(out)
        # self.assertEqual(rc,2) # should return 2 since time is invalid
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_one_x(self):
        # strin = "one 20 10 1 0"
        # correct_out = "5\none 25 10 1 0\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")

    # def test_one_y(self):
        # strin = "one 20 10 0 -2"
        # correct_out = "5\none 20 0 0 -2\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")

    # def test_neg_pos(self):
        # strin = "one -10 -10 1 0"
        # correct_out = "5\none -5 -10 1 0\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_one_stationary(self):
        # strin = "one 1 1 0 0"
        # correct_out = "9\none 1 1 0 0\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["9"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_one_move_one_still(self):
        # strin = "one 0 0 0 0\ntwo 20 0 1 1"
        # correct_out = "5\none 0 0 0 0\ntwo 25 5 1 1\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        # print(PROGRAM_TO_TEST)
        # print(out)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_two_parallel(self):
        # strin = "one 0 0 1 1\ntwo 20 0 1 1"
        # correct_out = "5\none 5 5 1 1\ntwo 25 5 1 1\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["5"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_two_time_inputs(self):
        # strin = "one 0 0 1 1"
        # correct_out = "1\none 1 1 1 1\n3\none 3 3 1 1\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["1","3"],strin)
        # print(out)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
		
    # def test_two_headoncol(self):
        # strin = "one 0 20 5 0\ntwo 20 20 -5 0"
        # correct_out = "2\none 0 20 -5 0\ntwo 20 20 5 0\n"
        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")

    # def test_complex_collision(self):
        # strin = ("2MU133 -34.94 -69.13 0.468 -0.900\n" +
        # "0WI913 -43.08 92.12 -0.811 -0.958\n" +
        # "6UP738  2.97 -66.25 -0.077 0.074\n" +
        # "1IA244 72.94 -86.02 -0.665 -0.283\n" +
        # "8RT773 -32.25 -2.63 -0.797 0.628\n" +
        # "0HV350 -73.97 24.21 0.960 -0.870\n" +
        # "0DU118 -82.09 44.95 0.661 -0.343\n" +
        # "4FA522 -18.20 72.32 0.734 -0.990\n" +
        # "1WR684 31.71 68.89 -0.509 -0.706\n" +
        # "7SW673 41.29 42.68 0.549 -0.012\n" )
        # correct_out = ("2000\n" +
        # "2MU133 901.06 -1869.13 0.468 -0.9\n" +
        # "0WI913 -1665.08 -1823.88 -0.811 -0.958\n" +
        # "6UP738 -151.03 81.75 -0.077 0.074\n" +
        # "1IA244 -1257.06 -652.02 -0.665 -0.283\n" +
        # "8RT773 1793.4177 1323.8136 0.92840971 0.66354266\n" +
        # "0HV350 -1573.6377 -1786.2336 -0.76540971 -0.90554266\n" +
        # "0DU118 1239.91 -641.05 0.661 -0.343\n" +
        # "4FA522 209.44512 -2881.8154 0.1031531 -1.4854472\n" +
        # "1WR684 254.06488 -368.97458 0.1218469 -0.21055284\n" +
        # "7SW673 1139.29 18.68 0.549 -0.012\n")

        # (rc,out,errs) = runprogram(PROGRAM_TO_TEST,["2000"],strin)
        # self.assertEqual(rc,0)
        # self.assertEqual(out,correct_out)
        # self.assertEqual(errs,"")
"""
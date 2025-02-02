#Checking if any given overlap is inside the polytope of classical overlaps of the graph K5

#Importing numpy and qutip
import numpy as np
import math
from qutip import *


#Put the vectors as quantum objects described by qutip
#Examples
A=Qobj([[1],[0],[0]])
B=(1/math.sqrt(3))*Qobj([[1],[1],[1]])
C=(1/math.sqrt(3))*Qobj([[-1],[1],[1]])
D=(1/math.sqrt(3))*Qobj([[1],[-1],[1]])
E=(1/math.sqrt(3))*Qobj([[1],[1],[-1]])

#Calculate out the overlaps
rAB = abs(A.overlap(B))**2
rAC = abs(A.overlap(C))**2
rAE = abs(A.overlap(E))**2
rAD = abs(A.overlap(D))**2
rBC = abs(B.overlap(C))**2
rBD = abs(B.overlap(D))**2
rBE = abs(B.overlap(E))**2
rCE = abs(C.overlap(E))**2
rDE = abs(D.overlap(E))**2
rCD = abs(C.overlap(D))**2

#Long list of check's for each single inequality defining the classical polytope
if	(-rAB<= 0) and (-rAC<= 0) and (-rAD<= 0) and (-rAE<= 0 ) and (-rBC<= 0 ) and (-rBD<= 0 ) and (-rBE<= 0 ) and (-rCD<= 0 ) and (-rCE<= 0 ) and (-rDE<= 0 ):
	print("POSITIVITY CHECK: YES")
else:
	print("POSITIVITY CHECK: NO")
if	(-rAB+rAE+rBE<= 1 ):
	print("(11): YES")
else:
	print("(11): NO")
if	(-rAB+rAD+rBD<= 1 ):
	print("(12): YES")
else:
	print("(12): NO")
if	(-rAB+rAC+rBC<= 1 ):
	print("(13): YES")
else:
	print("(13): NO")
if	(-rAC+rAE+rCE<= 1 ):
	print("(14): YES")
else:
	print("(14): NO")
if	(-rAC+rAD+rCD<= 1 ):
	print("(15): YES")
else:
	print("(15): NO")
if	(-rAD+rAE+rDE<= 1 ):
	print("(16): YES")
else:
	print("(16): NO")
if	(-rBC+rBE+rCE<= 1 ):
	print("(17): YES")
else:
	print("(17): NO")
if	(-rBC+rBD+rCD<= 1 ):
	print("(18): YES")
else:
	print("(18): NO")
if	(-rBD+rBE+rDE<= 1 ):
	print("(19): YES")
else:
	print("(19): NO")
if	(-rCD+rCE+rDE<= 1 ):
	print("(20): YES")
else:
	print("(20): NO")
if	(+rCD-rCE+rDE<= 1 ):
	print("(21): YES")
else:
	print("(21): NO")
if	(+rCD+rCE-rDE<= 1 ):
	print("(22): YES")
else:
	print("(22): NO")
if	(+rBD-rBE+rDE<= 1 ):
	print("(23): YES")
else:
	print("(23): NO")
if	(+rBD+rBE-rDE<= 1 ):
	print("(24): YES")
else:
	print("(24): NO")
if	(+rBC-rBD+rCD<= 1 ):
	print("(25): YES")
else:
	print("(25): NO")
if	(+rBC-rBE+rCE<= 1 ):
	print("(26): YES")
else:
	print("(26): NO")
if	(+rBC+rBE-rCE<= 1 ):
	print("(27): YES")
else:
	print("(27): NO")
if	(+rBC+rBD-rCD<= 1 ):
	print("(28): YES")
else:
	print("(28): NO")
if	(+rAD-rAE+rDE<= 1 ):
	print("(29): YES")
else:
	print("(29): NO")
if	(+rAD+rAE-rDE<= 1 ):
	print("(30): YES")
else:
	print("(30): NO")
if	(+rAC-rAD+rCD<= 1 ):
	print("(31): YES")
else:
	print("(31): NO")
if	(+rAC-rAE+rCE<= 1 ):
	print("(32): YES")
else:
	print("(32): NO")
if	(+rAC+rAE-rCE<= 1 ):
	print("(33): YES")
else:
	print("(33): NO")
if	(+rAC+rAD-rCD<= 1 ):
	print("(34): YES")
else:
	print("(34): NO")
if	(+rAB-rAC+rBC<= 1 ):
	print("(35): YES")
else:
	print("(35): NO")
if	(+rAB-rAD+rBD<= 1 ): 
	print("(36): YES")
else:
	print("(36): NO")
if	(+rAB-rAE+rBE<= 1 ):
	print("(37): YES")
else:
	print("(37): NO")
if	(+rAB+rAE-rBE<= 1 ):
	print("(38): YES")
else:
	print("(38): NO")
if	(+rAB+rAD-rBD<= 1 ):
	print("(39): YES")
else:
	print("(39): NO")
if	(+rAB+rAC-rBC<= 1 ):
	print("(40): YES")
else:
	print("(40): NO")
if	(-rAB-rAC+rAE-rBC+rBE+rCE<= 1):
	print("(41): YES")
else:
	print("(41): NO")
if	(-rAB-rAC+rAD-rBC+rBD+rCD<= 1):
	print("(42): YES")
else:
	print("(42): NO")
if	(-rAB-rAD+rAE-rBD+rBE+rDE<= 1):
	print("(43): YES")
else:
	print("(43): NO")
if	(-rAB+rAD-rAE+rBD-rBE+rDE<= 1):
	print("(44): YES")
else:
	print("(44): NO")
if	(-rAB+rAC-rAD+rBC-rBD+rCD<= 1):
	print("(45): YES")
else:
	print("(45): NO")
if	(-rAB+rAC-rAE+rBC-rBE+rCE<= 1):
	print("(46): YES")
else:
	print("(46): NO")
if	(-rAC-rAD+rAE-rCD+rCE+rDE<= 1):
	print("(47): YES")
else:
	print("(47): NO")
if	(-rAC+rAD-rAE+rCD-rCE+rDE<= 1):
	print("(48): YES")
else:
	print("(48): NO")
if	(-rBC-rBD+rBE-rCD+rCE+rDE<= 1):
	print("(49): YES")
else:
	print("(49): NO")
if	(-rBC+rBD-rBE+rCD-rCE+rDE<= 1):
	print("(50): YES")
else:
	print("(50): NO")
if	(+rBC-rBD-rBE+rCD+rCE-rDE<= 1):
	print("(51): YES")
else:
	print("(51): NO")
if	(+rBC+rBD+rBE-rCD-rCE-rDE<= 1):
	print("(52): YES")
else:
	print("(52): NO")
if	(+rAC-rAD-rAE+rCD+rCE-rDE<= 1):
	print("(53): YES")
else:
	print("(53): NO")
if	(+rAC+rAD+rAE-rCD-rCE-rDE<= 1):
	print("(54): YES")
else:
	print("(54): NO")
if	(+rAB-rAC-rAD+rBC+rBD-rCD<= 1):
	print("(55): YES")
else:
	print("(55): NO")
if	(+rAB-rAC-rAE+rBC+rBE-rCE<= 1):
	print("(56): YES")
else:
	print("(56): NO")
if	(+rAB-rAD-rAE+rBD+rBE-rDE<= 1):
	print("(57): YES")
else:
	print("(57): NO")
if	(+rAB+rAD+rAE-rBD-rBE-rDE<= 1):
	print("(58): YES")
else:
	print("(58): NO")
if	(+rAB+rAC+rAE-rBC-rBE-rCE<= 1):
	print("(59): YES")
else:
	print("(59): NO")
if	(+rAB+rAC+rAD-rBC-rBD-rCD<= 1):
	print("(60): YES")
else:
	print("(60): NO")
if	(-rAB-rAC-rAD+rAE-rBC-rBD+rBE-rCD+rCE+rDE<= 1):
	print("(61): YES")
else:
	print("(61): NO")
if	(-rAB-rAC+rAD-rAE-rBC+rBD-rBE+rCD-rCE+rDE<= 1):
	print("(62): YES")
else:
	print("(62): NO")
if	(-rAB+rAC-rAD-rAE+rBC-rBD-rBE+rCD+rCE-rDE<= 1):
	print("(63): YES")
else:
	print("(63): NO")
if	(+rAB-rAC-rAD-rAE+rBC+rBD+rBE-rCD-rCE-rDE<= 1):
	print("(64): YES")
else:
	print("(64): NO")
if	(+rAB+rAC+rAD+rAE-rBC-rBD-rBE-rCD-rCE-rDE<= 1):
	print("(65): YES")
else:
	print("(65): NO")
if	(-rAB-rAC+rAD+rAE-rBC+rBD+rBE+rCD+rCE-rDE<= 2):
	print("(66): YES")
else:
	print("(66): NO")
if	(-rAB+rAC-rAD+rAE+rBC-rBD+rBE+rCD-rCE+rDE<= 2):
	print("(67): YES")
else:
	print("(67): NO")
if	(-rAB+rAC+rAD-rAE+rBC+rBD-rBE-rCD+rCE+rDE<= 2):
	print("(68): YES")
else:
	print("(68): NO")
if	(-rAB+rAC+rAD+rAE+rBC+rBD+rBE-rCD-rCE-rDE<= 2):
	print("(69): YES")
else:
	print("(69): NO")
if	(+rAB-rAC-rAD+rAE+rBC+rBD-rBE-rCD+rCE+rDE<= 2):
	print("(70): YES")
else:
	print("(70): NO")
if	(+rAB-rAC+rAD-rAE+rBC-rBD+rBE+rCD-rCE+rDE<= 2):
	print("(71): YES")
else:
	print("(71): NO")
if	(+rAB-rAC+rAD+rAE+rBC-rBD-rBE+rCD+rCE-rDE<= 2):
	print("(72): YES")
else:
	print("(72): NO")
if	(+rAB+rAC-rAD-rAE-rBC+rBD+rBE+rCD+rCE-rDE<= 2):
	print("(73): YES")
else:
	print("(73): NO")
if	(+rAB+rAC-rAD+rAE-rBC+rBD-rBE+rCD-rCE+rDE<= 2):
	print("(74): YES")
else:
	print("(74): NO")
if	(+rAB+rAC+rAD-rAE-rBC-rBD+rBE-rCD+rCE+rDE<= 2):
	print("(75): YES")
else:
	print("(75): NO")
if	(-rAB-rAC+rAD+rAE+rBC-rBD+rBE+rCD-rCE-rDE<= 2):
	print("(76): YES")
else:
	print("(76): NO")
if	(-rAB-rAC+rAD+rAE+rBC+rBD-rBE-rCD+rCE-rDE<= 2):
	print("(77): YES")
else:
	print("(77): NO")
if	(-rAB+rAC-rAD+rAE-rBC+rBD+rBE+rCD-rCE-rDE<= 2):
	print("(78): YES")
else:
	print("(78): NO")
if	(-rAB+rAC-rAD+rAE+rBC+rBD-rBE-rCD-rCE+rDE<= 2):
	print("(79): YES")
else:
	print("(79): NO")
if	(-rAB+rAC+rAD-rAE-rBC+rBD+rBE-rCD+rCE-rDE<= 2):
	print("(80): YES")
else:
	print("(80): NO")
if	(-rAB+rAC+rAD-rAE+rBC-rBD+rBE-rCD-rCE+rDE<= 2):
	print("(81): YES")
else:
	print("(81): NO")
if	(+rAB-rAC-rAD+rAE-rBC+rBD-rBE+rCD+rCE-rDE<= 2):
	print("(82): YES")
else:
	print("(82): NO")
if	(+rAB-rAC-rAD+rAE+rBC-rBD-rBE+rCD-rCE+rDE<= 2):
	print("(83): YES")
else:
	print("(83): NO")
if	(+rAB-rAC+rAD-rAE-rBC-rBD+rBE+rCD+rCE-rDE<= 2):
	print("(84): YES")
else:
	print("(84): NO")
if	(+rAB-rAC+rAD-rAE+rBC-rBD-rBE-rCD+rCE+rDE<= 2):
	print("(85): YES")
else:
	print("(85): NO")
if	(+rAB+rAC-rAD-rAE-rBC-rBD+rBE+rCD-rCE+rDE<= 2):
	print("(86): YES")
else:
	print("(86): NO")
if	(+rAB+rAC-rAD-rAE-rBC+rBD-rBE-rCD+rCE+rDE<= 2):
	print("(87): YES")
else:
	print("(87): NO")
if	(-rAB-rAC-rAD+2*rAE-rBC-rBD+2*rBE-rCD+2*rCE+2*rDE<= 3):
	print("(88): YES")
else:
	print("(88): NO")
if	(-rAB-rAC+2*rAD-rAE-rBC+2*rBD-rBE+2*rCD-rCE+2*rDE<= 3):
	print("(89): YES")
else:
	print("(89): NO")
if	(-rAB+2*rAC-rAD-rAE+2*rBC-rBD-rBE+2*rCD+2*rCE-rDE<= 3):
	print("(90): YES")
else:
	print("(90): NO")
if	(+2*rAB-rAC-rAD-rAE+2*rBC+2*rBD+2*rBE-rCD-rCE-rDE<= 3):
	print("(91): YES")
else:
	print("(91): NO")
if	(+2*rAB+2*rAC+2*rAD+2*rAE-rBC-rBD-rBE-rCD-rCE-rDE<= 3):
	print("(92): YES")
else:
	print("(92): NO")
if	(-2*rAB-2*rAC+2*rAE-2*rBD+2*rBE+rCD+rCE+rDE<= 3):
	print("(93): YES")
else:
	print("(93): NO")
if	(-2*rAB-2*rAC+2*rAE+rBD+rBE-2*rCD+2*rCE+rDE<= 3):
	print("(94): YES")
else:
	print("(94): NO")
if	(-2*rAB-2*rAC+2*rAD+rBD+rBE+2*rCD-2*rCE+rDE<= 3):
	print("(95): YES")
else:
	print("(95): NO")
if	(-2*rAB-2*rAC+2*rAD+2*rBD-2*rBE+rCD+rCE+rDE<= 3):
	print("(96): YES")
else:
	print("(96): NO")
if	(-2*rAB-2*rAD+2*rAE-2*rBC+2*rBE+rCD+rCE+rDE<= 3):
	print("(97): YES")
else:
	print("(97): NO")
if	(-2*rAB-2*rAD+2*rAE+rBC+rBE-2*rCD+rCE+2*rDE<= 3):
	print("(98): YES")
else:
	print("(98): NO")
if	(-2*rAB+rAD+rAE-2*rBC+2*rBE-2*rCD+2*rCE+rDE<= 3):
	print("(99): YES")
else:
	print("(99): NO")
if	(-2*rAB+rAD+rAE-2*rBC+2*rBD+2*rCD-2*rCE+rDE<= 3):
	print("(100): YES")
else:
	print("(100): NO")
if	(-2*rAB+2*rAD-2*rAE-2*rBC+2*rBD+rCD+rCE+rDE<= 3):
	print("(101): YES")
else:
	print("(101): NO")
if	(-2*rAB+2*rAD-2*rAE+rBC+rBD+rCD-2*rCE+2*rDE<= 3):
	print("(102): YES")
else:
	print("(102): NO")
if	(-2*rAB+rAC+rAE-2*rBD+2*rBE-2*rCD+rCE+2*rDE<= 3):
	print("(103): YES")
else:
	print("(103): NO")
if	(-2*rAB+rAC+rAE+2*rBC-2*rBD+2*rCD+rCE-2*rDE<= 3):
	print("(104): YES")
else:
	print("(104): NO")
if	(-2*rAB+rAC+rAD+2*rBD-2*rBE+rCD-2*rCE+2*rDE<= 3):
	print("(105): YES")
else:
	print("(105): NO")
if	(-2*rAB+rAC+rAD+2*rBC-2*rBE+rCD+2*rCE-2*rDE<= 3):
	print("(106): YES")
else:
	print("(106): NO")
if	(-2*rAB+2*rAC-2*rAD+rBC+rBE+2*rCD+rCE-2*rDE<= 3):
	print("(107): YES")
else:
	print("(107): NO")
if	(-2*rAB+2*rAC-2*rAD+2*rBC-2*rBE+rCD+rCE+rDE<= 3):
	print("(108): YES")
else:
	print("(108): NO")
if	(-2*rAB+2*rAC-2*rAE+rBC+rBD+rCD+2*rCE-2*rDE<= 3):
	print("(109): YES")
else:
	print("(109): NO")
if	(-2*rAB+2*rAC-2*rAE+2*rBC-2*rBD+rCD+rCE+rDE<= 3):
	print("(110): YES")
else:
	print("(110): NO")
if	(-2*rAC-2*rAD+2*rAE-2*rBC+rBD+rBE+2*rCE+rDE<= 3):
	print("(111): YES")
else:
	print("(111): NO")
if	(-2*rAC-2*rAD+2*rAE+rBC-2*rBD+rBE+rCE+2*rDE<= 3):
	print("(112): YES")
else:
	print("(112): NO")
if	(-2*rAC+rAD+rAE-2*rBC-2*rBD+2*rBE+2*rCE+rDE<= 3):
	print("(113): YES")
else:
	print("(113): NO")
if	(-2*rAC+rAD+rAE-2*rBC+2*rBD-2*rBE+2*rCD+rDE<= 3):
	print("(114): YES")
else:
	print("(114): NO")
if	(-2*rAC+2*rAD-2*rAE-2*rBC+rBD+rBE+2*rCD+rDE<= 3):
	print("(115): YES")
else:
	print("(115): NO")
if	(-2*rAC+2*rAD-2*rAE+rBC+rBD-2*rBE+rCD+2*rDE<= 3):
	print("(116): YES")
else:
	print("(116): NO")
if	(+rAC-2*rAD+rAE-2*rBC-2*rBD+2*rBE+rCE+2*rDE<= 3):
	print("(117): YES")
else:
	print("(117): NO")
if	(+rAC-2*rAD+rAE+2*rBC-2*rBD-2*rBE+2*rCD+rCE<= 3):
	print("(118): YES")
else:
	print("(118): NO")
if	(+rAC+rAD-2*rAE-2*rBC+2*rBD-2*rBE+rCD+2*rDE<= 3):
	print("(119): YES")
else:
	print("(119): NO")
if	(+rAC+rAD-2*rAE+2*rBC-2*rBD-2*rBE+rCD+2*rCE<= 3):
	print("(120): YES")
else:
	print("(120): NO")
if	(+2*rAC-2*rAD-2*rAE+rBC-2*rBD+rBE+2*rCD+rCE<= 3):
	print("(121): YES")
else:
	print("(121): NO")
if	(+2*rAC-2*rAD-2*rAE+rBC+rBD-2*rBE+rCD+2*rCE<= 3):
	print("(122): YES")
else:
	print("(122): NO")
if	(+rAB-2*rAC+rAE-2*rBD+rBE-2*rCD+2*rCE+2*rDE<= 3):
	print("(123): YES")
else:
	print("(123): NO")
if	(+rAB-2*rAC+rAE+2*rBC+2*rBD+rBE-2*rCD-2*rDE<= 3):
	print("(124): YES")
else:
	print("(124): NO")
if	(+rAB-2*rAC+rAD+rBD-2*rBE+2*rCD-2*rCE+2*rDE<= 3):
	print("(125): YES")
else:
	print("(125): NO")
if	(+rAB-2*rAC+rAD+2*rBC+rBD+2*rBE-2*rCE-2*rDE<= 3):
	print("(126): YES")
else:
	print("(126): NO")
if	(+rAB-2*rAD+rAE-2*rBC+rBE-2*rCD+2*rCE+2*rDE<= 3):
	print("(127): YES")
else:
	print("(127): NO")
if	(+rAB-2*rAD+rAE+2*rBC+2*rBD+rBE-2*rCD-2*rCE<= 3):
	print("(128): YES")
else:
	print("(128): NO")
if	(+rAB+rAD-2*rAE-2*rBC+rBD+2*rCD-2*rCE+2*rDE<= 3):
	print("(129): YES")
else:
	print("(129): NO")
if	(+rAB+rAD-2*rAE+2*rBC+rBD+2*rBE-2*rCD-2*rCE<= 3):
	print("(130): YES")
else:
	print("(130): NO")
if	(+rAB+rAC-2*rAD+rBC-2*rBE+2*rCD+2*rCE-2*rDE<= 3):
	print("(131): YES")
else:
	print("(131): NO")
if	(+rAB+rAC-2*rAD+rBC+2*rBD+2*rBE-2*rCE-2*rDE<= 3):
	print("(132): YES")
else:
	print("(132): NO")
if	(+rAB+rAC-2*rAE+rBC-2*rBD+2*rCD+2*rCE-2*rDE<= 3):
	print("(133): YES")
else:
	print("(133): NO")
if	(+rAB+rAC-2*rAE+rBC+2*rBD+2*rBE-2*rCD-2*rDE<= 3):
	print("(134): YES")
else:
	print("(134): NO")
if	(+rAB+rAC+2*rAD+2*rAE+rBC-2*rBD-2*rCE-2*rDE<= 3):
	print("(135): YES")
else:
	print("(135): NO")
if	(+rAB+rAC+2*rAD+2*rAE+rBC-2*rBE-2*rCD-2*rDE<= 3):
	print("(136): YES")
else:
	print("(136): NO")
if	(+rAB+2*rAC+rAD+2*rAE-2*rBC+rBD-2*rCE-2*rDE<= 3):
	print("(137): YES")
else:
	print("(137): NO")
if	(+rAB+2*rAC+rAD+2*rAE+rBD-2*rBE-2*rCD-2*rCE<= 3):
	print("(138): YES")
else:
	print("(138): NO")
if	(+rAB+2*rAC+2*rAD+rAE-2*rBC+rBE-2*rCD-2*rDE<= 3):
	print("(139): YES")
else:
	print("(139): NO")
if	(+rAB+2*rAC+2*rAD+rAE-2*rBD+rBE-2*rCD-2*rCE<= 3):
	print("(140): YES")
else:
	print("(140): NO")
if	(+2*rAB-2*rAC-2*rAD+rBC+2*rBD+rBE+rCE-2*rDE<= 3):
	print("(141): YES")
else:
	print("(141): NO")
if	(+2*rAB-2*rAC-2*rAD+2*rBC+rBD+rBE-2*rCE+rDE<= 3):
	print("(142): YES")
else:
	print("(142): NO")
if	(+2*rAB-2*rAC-2*rAE+rBC+rBD+2*rBE+rCD-2*rDE<= 3):
	print("(143): YES")
else:
	print("(143): NO")
if	(+2*rAB-2*rAC-2*rAE+2*rBC+rBD+rBE-2*rCD+rDE<= 3):
	print("(144): YES")
else:
	print("(144): NO")
if	(+2*rAB-2*rAD-2*rAE+rBC+rBD+2*rBE+rCD-2*rCE<= 3):
	print("(145): YES")
else:
	print("(145): NO")
if	(+2*rAB-2*rAD-2*rAE+rBC+2*rBD+rBE-2*rCD+rCE<= 3):
	print("(146): YES")
else:
	print("(146): NO")
if	(+2*rAB+rAC+rAD+2*rAE-2*rBC-2*rBE+rCD-2*rDE<= 3):
	print("(147): YES")
else:
	print("(147): NO")
if	(+2*rAB+rAC+rAD+2*rAE-2*rBD-2*rBE+rCD-2*rCE<= 3):
	print("(148): YES")
else:
	print("(148): NO")
if	(+2*rAB+rAC+2*rAD+rAE-2*rBC-2*rBD+rCE-2*rDE<= 3):
	print("(149): YES")
else:
	print("(149): NO")
if	(+2*rAB+rAC+2*rAD+rAE-2*rBD-2*rBE-2*rCD+rCE<= 3):
	print("(150): YES")
else:
	print("(150): NO")
if	(+2*rAB+2*rAC+rAD+rAE-2*rBC-2*rBD-2*rCE+rDE<= 3):
	print("(151): YES")
else:
	print("(151): NO")
if	(+2*rAB+2*rAC+rAD+rAE-2*rBC-2*rBE-2*rCD+rDE<= 3):
	print("(152): YES")
else:
	print("(152): NO")
if	(-2*rAB-2*rAC+2*rAE-rBC+rBD+2*rBE+rCD+2*rCE-2*rDE<= 3):
	print("(153): YES")
else:
	print("(153): NO")
if	(-2*rAB-2*rAC+2*rAD-rBC+2*rBD+rBE+2*rCD+rCE-2*rDE<= 3):
	print("(154): YES")
else:
	print("(154): NO")
if	(-2*rAB-rAC+rAD+2*rAE-2*rBC+2*rBE+rCD+2*rCE-2*rDE<= 3):
	print("(155): YES")
else:
	print("(155): NO")
if	(-2*rAB-rAC+2*rAD+rAE-2*rBC+2*rBD+2*rCD+rCE-2*rDE<= 3):
	print("(156): YES")
else:
	print("(156): NO")
if	(-2*rAB-2*rAD+2*rAE+rBC-rBD+2*rBE+rCD-2*rCE+2*rDE<= 3):
	print("(157): YES")
else:
	print("(157): NO")
if	(-2*rAB+rAD+rAE+2*rBC+2*rBD+2*rBE-2*rCD-2*rCE-rDE<= 3):
	print("(158): YES")
else:
	print("(158): NO")
if	(-2*rAB+2*rAD-2*rAE+rBC+2*rBD-rBE-2*rCD+rCE+2*rDE<= 3):
	print("(159): YES")
else:
	print("(159): NO")
if	(-2*rAB+rAC-rAD+2*rAE-2*rBD+2*rBE+rCD-2*rCE+2*rDE<= 3):
	print("(160): YES")
else:
	print("(160): NO")
if	(-2*rAB+rAC+rAE+2*rBC+2*rBD+2*rBE-2*rCD-rCE-2*rDE<= 3):
	print("(161): YES")
else:
	print("(161): NO")
if	(-2*rAB+rAC+rAD+2*rBC+2*rBD+2*rBE-rCD-2*rCE-2*rDE<= 3):
	print("(162): YES")
else:
	print("(162): NO")
if	(-2*rAB+rAC+2*rAD-rAE+2*rBD-2*rBE-2*rCD+rCE+2*rDE<= 3):
	print("(163): YES")
else:
	print("(163): NO")
if	(-2*rAB+2*rAC-2*rAD+2*rBC-rBD+rBE+2*rCD-2*rCE+rDE<= 3):
	print("(164): YES")
else:
	print("(164): NO")
if	(-2*rAB+2*rAC-rAD+rAE+2*rBC-2*rBD+2*rCD-2*rCE+rDE<= 3):
	print("(165): YES")
else:
	print("(165): NO")
if	(-2*rAB+2*rAC-2*rAE+2*rBC+rBD-rBE-2*rCD+2*rCE+rDE<= 3):
	print("(166): YES")
else:
	print("(166): NO")
if	(-2*rAB+2*rAC+rAD-rAE+2*rBC-2*rBE-2*rCD+2*rCE+rDE<= 3):
	print("(167): YES")
else:
	print("(167): NO")
if	(-2*rAB+2*rAC+2*rAD+2*rAE+rBD+rBE-2*rCD-2*rCE-rDE<= 3):
	print("(168): YES")
else:
	print("(168): NO")
if	(-2*rAB+2*rAC+2*rAD+2*rAE+rBC+rBE-2*rCD-rCE-2*rDE<= 3):
	print("(169): YES")
else:
	print("(169): NO")
if	(-2*rAB+2*rAC+2*rAD+2*rAE+rBC+rBD-rCD-2*rCE-2*rDE<= 3):
	print("(170): YES")
else:
	print("(170): NO")
if	(-rAB-2*rAC+rAD+2*rAE-2*rBC+rBD+2*rBE+2*rCE-2*rDE<= 3):
	print("(171): YES")
else:
	print("(171): NO")
if	(-rAB-2*rAC+2*rAD+rAE-2*rBC+2*rBD+rBE+2*rCD-2*rDE<= 3):
	print("(172): YES")
else:
	print("(172): NO")
if	(-rAB+rAC-2*rAD+2*rAE+rBC-2*rBD+2*rBE-2*rCE+2*rDE<= 3):
	print("(173): YES")
else:
	print("(173): NO")
if	(-rAB+rAC+2*rAD-2*rAE+rBC+2*rBD-2*rBE-2*rCD+2*rDE<= 3):
	print("(174): YES")
else:
	print("(174): NO")
if	(-rAB+2*rAC-2*rAD+rAE+2*rBC-2*rBD+rBE+2*rCD-2*rCE<= 3):
	print("(175): YES")
else:
	print("(175): NO")
if	(-rAB+2*rAC+rAD-2*rAE+2*rBC+rBD-2*rBE-2*rCD+2*rCE<= 3):
	print("(176): YES")
else:
	print("(176): NO")
if	(-2*rAC-2*rAD+2*rAE+rBC+rBD-2*rBE-rCD+2*rCE+2*rDE<= 3):
	print("(177): YES")
else:
	print("(177): NO")
if	(-2*rAC+rAD+rAE+2*rBC-2*rBD-2*rBE+2*rCD+2*rCE-rDE<= 3):
	print("(178): YES")
else:
	print("(178): NO")
if	(-2*rAC+2*rAD-2*rAE+rBC-2*rBD+rBE+2*rCD-rCE+2*rDE<= 3):
	print("(179): YES")
else:
	print("(179): NO")
if	(+rAC-2*rAD+rAE-2*rBC+2*rBD-2*rBE+2*rCD-rCE+2*rDE<= 3):
	print("(180): YES")
else:
	print("(180): NO")
if	(+rAC+rAD-2*rAE-2*rBC-2*rBD+2*rBE-rCD+2*rCE+2*rDE<= 3):
	print("(181): YES")
else:
	print("(181): NO")
if	(+2*rAC-2*rAD-2*rAE-2*rBC+rBD+rBE+2*rCD+2*rCE-rDE<= 3):
	print("(182): YES")
else:
	print("(182): NO")
if	(+rAB-2*rAC-rAD+2*rAE+rBD-2*rBE-2*rCD+2*rCE+2*rDE<= 3):
	print("(183): YES")
else:
	print("(183): NO")
if	(+rAB-2*rAC+rAE+2*rBC-2*rBD-rBE+2*rCD+2*rCE-2*rDE<= 3):
	print("(184): YES")
else:
	print("(184): NO")
if	(+rAB-2*rAC+rAD+2*rBC-rBD-2*rBE+2*rCD+2*rCE-2*rDE<= 3):
	print("(185): YES")
else:
	print("(185): NO")
if	(+rAB-2*rAC+2*rAD-rAE-2*rBD+rBE+2*rCD-2*rCE+2*rDE<= 3):
	print("(186): YES")
else:
	print("(186): NO")
if	(+rAB-rAC-2*rAD+2*rAE+rBC-2*rBE-2*rCD+2*rCE+2*rDE<= 3):
	print("(187): YES")
else:
	print("(187): NO")
if	(+rAB-rAC+2*rAD-2*rAE+rBC-2*rBD+2*rCD-2*rCE+2*rDE<= 3):
	print("(188): YES")
else:
	print("(188): NO")
if	(+rAB-2*rAD+rAE-2*rBC+2*rBD-rBE+2*rCD-2*rCE+2*rDE<= 3):
	print("(189): YES")
else:
	print("(189): NO")
if	(+rAB+rAD-2*rAE-2*rBC-rBD+2*rBE-2*rCD+2*rCE+2*rDE<= 3):
	print("(190): YES")
else:
	print("(190): NO")
if	(+rAB+rAC-2*rAD-rBC+2*rBD-2*rBE+2*rCD-2*rCE+2*rDE<= 3):
	print("(191): YES")
else:
	print("(191): NO")
if	(+rAB+rAC-2*rAE-rBC-2*rBD+2*rBE-2*rCD+2*rCE+2*rDE<= 3):
	print("(192): YES")
else:
	print("(192): NO")
if	(+rAB+2*rAC-2*rAD-rAE-2*rBC+rBE+2*rCD+2*rCE-2*rDE<= 3):
	print("(193): YES")
else:
	print("(193): NO")
if	(+rAB+2*rAC-rAD-2*rAE-2*rBC+rBD+2*rCD+2*rCE-2*rDE<= 3):
	print("(194): YES")
else:
	print("(194): NO")
if	(+2*rAB-2*rAC-2*rAD+2*rBC+2*rBD-2*rBE-rCD+rCE+rDE<= 3):
	print("(195): YES")
else:
	print("(195): NO")
if	(+2*rAB-2*rAC-rAD+rAE+2*rBC+2*rBD-2*rBE-2*rCD+rDE<= 3):
	print("(196): YES")
else:
	print("(196): NO")
if	(+2*rAB-2*rAC-2*rAE+2*rBC-2*rBD+2*rBE+rCD-rCE+rDE<= 3):
	print("(197): YES")
else:
	print("(197): NO")
if	(+2*rAB-2*rAC+rAD-rAE+2*rBC-2*rBD+2*rBE-2*rCE+rDE<= 3):
	print("(198): YES")
else:
	print("(198): NO")
if	(+2*rAB-2*rAC+2*rAD+2*rAE-2*rBD-2*rBE+rCD+rCE-rDE<= 3):
	print("(199): YES")
else:
	print("(199): NO")
if	(+2*rAB-2*rAC+2*rAD+2*rAE+rBC-2*rBD-rBE+rCE-2*rDE<= 3):
	print("(200): YES")
else:
	print("(200): NO")
if	(+2*rAB-2*rAC+2*rAD+2*rAE+rBC-rBD-2*rBE+rCD-2*rDE<= 3):
	print("(201): YES")
else:
	print("(201): NO")
if	(+2*rAB-rAC-2*rAD+rAE+2*rBC+2*rBD-2*rBE-2*rCD+rCE<= 3):
	print("(202): YES")
else:
	print("(202): NO")
if	(+2*rAB-rAC+rAD-2*rAE+2*rBC-2*rBD+2*rBE+rCD-2*rCE<= 3):
	print("(203): YES")
else:
	print("(203): NO")
if	(+2*rAB-2*rAD-2*rAE-2*rBC+2*rBD+2*rBE+rCD+rCE-rDE<= 3):
	print("(204): YES")
else:
	print("(204): NO")
if	(+2*rAB+rAC-2*rAD-rAE-2*rBC+2*rBD+2*rBE+rCE-2*rDE<= 3):
	print("(205): YES")
else:
	print("(205): NO")
if	(+2*rAB+rAC-rAD-2*rAE-2*rBC+2*rBD+2*rBE+rCD-2*rDE<= 3):
	print("(206): YES")
else:
	print("(206): NO")
if	(+2*rAB+2*rAC-2*rAD+2*rAE-2*rBC-2*rBE+rCD-rCE+rDE<= 3):
	print("(207): YES")
else:
	print("(207): NO")
if	(+2*rAB+2*rAC-2*rAD+2*rAE-2*rBC+rBD-rBE-2*rCE+rDE<= 3):
	print("(208): YES")
else:
	print("(208): NO")
if	(+2*rAB+2*rAC-2*rAD+2*rAE-rBC+rBD-2*rBE+rCD-2*rCE<= 3):
	print("(209): YES")
else:
	print("(209): NO")
if	(+2*rAB+2*rAC+2*rAD-2*rAE-2*rBC-2*rBD-rCD+rCE+rDE<= 3):
	print("(210): YES")
else:
	print("(210): NO")
if	(+2*rAB+2*rAC+2*rAD-2*rAE-2*rBC-rBD+rBE-2*rCD+rDE<= 3):
	print("(211): YES")
else:
	print("(211): NO")
if	(+2*rAB+2*rAC+2*rAD-2*rAE-rBC-2*rBD+rBE-2*rCD+rCE<= 3):
	print("(212): YES")
else:
	print("(212): NO")
if	(-4*rAB-4*rAC+3*rAD+3*rAE-2*rBC+2*rBD+2*rBE+2*rCD+2*rCE-rDE<= 5):
	print("(213): YES")
else:
	print("(213): NO")
if	(-4*rAB-2*rAC+2*rAD+2*rAE-4*rBC+3*rBD+3*rBE+2*rCD+2*rCE-rDE<= 5):
	print("(214): YES")
else:
	print("(214): NO")
if	(-4*rAB+2*rAC-2*rAD+2*rAE+3*rBC-4*rBD+3*rBE+2*rCD-rCE+2*rDE<= 5):
	print("(215): YES")
else:
	print("(215): NO")
if	(-4*rAB+2*rAC+2*rAD-2*rAE+3*rBC+3*rBD-4*rBE-rCD+2*rCE+2*rDE<= 5):
	print("(216): YES")
else:
	print("(216): NO")
if	(-4*rAB+3*rAC-4*rAD+3*rAE+2*rBC-2*rBD+2*rBE+2*rCD-rCE+2*rDE<= 5):
	print("(217): YES")
else:
	print("(217): NO")
if	(-4*rAB+3*rAC+3*rAD-4*rAE+2*rBC+2*rBD-2*rBE-rCD+2*rCE+2*rDE<= 5):
	print("(218): YES")
else:
	print("(218): NO")
if	(-2*rAB-4*rAC+2*rAD+2*rAE-4*rBC+2*rBD+2*rBE+3*rCD+3*rCE-rDE<= 5):
	print("(219): YES")
else:
	print("(219): NO")
if	(-2*rAB+2*rAC-4*rAD+2*rAE+2*rBC-4*rBD+2*rBE+3*rCD-rCE+3*rDE<= 5):
	print("(220): YES")
else:
	print("(220): NO")
if	(-2*rAB+2*rAC+2*rAD-4*rAE+2*rBC+2*rBD-4*rBE-rCD+3*rCE+3*rDE<= 5):
	print("(221): YES")
else:
	print("(221): NO")
if	(-rAB+2*rAC+2*rAD+3*rAE+2*rBC+2*rBD+3*rBE-2*rCD-4*rCE-4*rDE<= 5):
	print("(222): YES")
else:
	print("(222): NO")
if	(-rAB+2*rAC+3*rAD+2*rAE+2*rBC+3*rBD+2*rBE-4*rCD-2*rCE-4*rDE<= 5):
	print("(223): YES")
else:
	print("(223): NO")
if	(-rAB+3*rAC+2*rAD+2*rAE+3*rBC+2*rBD+2*rBE-4*rCD-4*rCE-2*rDE<= 5):
	print("(224): YES")
else:
	print("(224): NO")
if	(+2*rAB-4*rAC-2*rAD+2*rAE+3*rBC+2*rBD-rBE-4*rCD+3*rCE+2*rDE<= 5):
	print("(225): YES")
else:
	print("(225): NO")
if	(+2*rAB-4*rAC+2*rAD-2*rAE+3*rBC-rBD+2*rBE+3*rCD-4*rCE+2*rDE<= 5):
	print("(226): YES")
else:
	print("(226): NO")
if	(+2*rAB-2*rAC-4*rAD+2*rAE+2*rBC+3*rBD-rBE-4*rCD+2*rCE+3*rDE<= 5):
	print("(227): YES")
else:
	print("(227): NO")
if	(+2*rAB-2*rAC+2*rAD-4*rAE+2*rBC-rBD+3*rBE+2*rCD-4*rCE+3*rDE<= 5):
	print("(228): YES")
else:
	print("(228): NO")
if	(+2*rAB-rAC+2*rAD+3*rAE+2*rBC-2*rBD-4*rBE+2*rCD+3*rCE-4*rDE<= 5):
	print("(229): YES")
else:
	print("(229): NO")
if	(+2*rAB-rAC+3*rAD+2*rAE+2*rBC-4*rBD-2*rBE+3*rCD+2*rCE-4*rDE<= 5):
	print("(230): YES")
else:
	print("(230): NO")
if	(+2*rAB+2*rAC-4*rAD-2*rAE-rBC+3*rBD+2*rBE+3*rCD+2*rCE-4*rDE<= 5):
	print("(231): YES")
else:
	print("(231): NO")
if	(+2*rAB+2*rAC-2*rAD-4*rAE-rBC+2*rBD+3*rBE+2*rCD+3*rCE-4*rDE<= 5):
	print("(232): YES")
else:
	print("(232): NO")
if	(+2*rAB+2*rAC-rAD+3*rAE-2*rBC+2*rBD-4*rBE+2*rCD-4*rCE+3*rDE<= 5):
	print("(233): YES")
else:
	print("(233): NO")
if	(+2*rAB+2*rAC+3*rAD-rAE-2*rBC-4*rBD+2*rBE-4*rCD+2*rCE+3*rDE<= 5):
	print("(234): YES")
else:
	print("(234): NO")
if	(+2*rAB+3*rAC-rAD+2*rAE-4*rBC+2*rBD-2*rBE+3*rCD-4*rCE+2*rDE<= 5):
	print("(235): YES")
else:
	print("(235): NO")
if	(+2*rAB+3*rAC+2*rAD-rAE-4*rBC-2*rBD+2*rBE-4*rCD+3*rCE+2*rDE<= 5):
	print("(236): YES")
else:
	print("(236): NO")
if	(+3*rAB-4*rAC-4*rAD+3*rAE+2*rBC+2*rBD-rBE-2*rCD+2*rCE+2*rDE<= 5):
	print("(237): YES")
else:
	print("(237): NO")
if	(+3*rAB-4*rAC+3*rAD-4*rAE+2*rBC-rBD+2*rBE+2*rCD-2*rCE+2*rDE<= 5):
	print("(238): YES")
else:
	print("(238): NO")
if	(+3*rAB-rAC+2*rAD+2*rAE+3*rBC-4*rBD-4*rBE+2*rCD+2*rCE-2*rDE<= 5):
	print("(239): YES")
else:
	print("(239): NO")
if	(+3*rAB+2*rAC-rAD+2*rAE-4*rBC+3*rBD-4*rBE+2*rCD-2*rCE+2*rDE<= 5):
	print("(240): YES")
else:
	print("(240): NO")
if	(+3*rAB+2*rAC+2*rAD-rAE-4*rBC-4*rBD+3*rBE-2*rCD+2*rCE+2*rDE<= 5):
	print("(241): YES")
else:
	print("(241): NO")
if	(+3*rAB+3*rAC-4*rAD-4*rAE-rBC+2*rBD+2*rBE+2*rCD+2*rCE-2*rDE<= 5):
	print("(242): YES")
else:
	print("(242): NO")

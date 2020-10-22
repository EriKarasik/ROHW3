from sympy import *

a1, a2, a3 = 1, 1, 1

def cross(a, b): return Matrix([a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])
def Tz(a): return Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, a], [0, 0, 0, 1]])
def Ty(a): return Matrix([[1, 0, 0, 0], [0, 1, 0, a], [0, 0, 1, 0], [0, 0, 0, 1]])
def Tx(a): return Matrix([[1, 0, 0, a], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def Tzd(): return Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
def Tyd(): return Matrix([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
def Txd(): return Matrix([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
def Rx(a): return Matrix([[1, 0, 0, 0], [0, cos(a), -sin(a), 0], [0, sin(a), cos(a), 0], [0, 0, 0, 1]])
def Ry(a): return Matrix([[cos(a), 0, sin(a), 0], [0, 1, 0, 0], [-sin(a), 0, cos(a), 0], [0, 0, 0, 1]])
def Rz(a): return Matrix([[cos(a), -sin(a), 0, 0], [sin(a), cos(a), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
def Rxd(a): return Matrix([[0,0,0,0],[0,-sin(a),-cos(a),0],[0,cos(a),-sin(a),0],[0,0,0,0]])
def Ryd(a): return Matrix([[-sin(a),0,cos(a),0],[0,0,0,0],[-cos(a),0,-sin(a),0],[0,0,0,0]])
def Rzd(a): return Matrix([[-sin(a),-cos(a),0,0],[cos(a),-sin(a),0,0],[0,0,0,0],[0,0,0,0]])
#def Rm1(q): return Matrix([[cos(q0),sin(q0),0,0],[-sin(q0)*cos(q1),cos(q0)*cos(q1),sin(q1),0], #R^-1
#                          [sin(q0)*sin(q1),-cos(q0)*sin(q1),cos(q1),0],[0,0,0,1]])

def FK(q): return Rz(q[0])*Tz(a1)*Ry(q[1])*Tx(a2)*Ry(q[2])*Tx(a3)
q0, q1, q2 = symbols('q0 q1 q2')

T00 = eye(4)
O0 = Matrix([[T00[0,3]],[T00[1,3]],[T00[2,3]]])
z0 = Matrix([[T00[0,2]],[T00[1,2]],[T00[2,2]]])
T01 = Rz(q0)*Tz(a1)
O1 = Matrix([[T01[0,3]],[T01[1,3]],[T01[2,3]]])
z1 = Matrix([[T01[0,0]],[T01[1,0]],[T01[2,0]]])
T02 = T01*Ry(q1)*Tx(a2)
O2 = Matrix([[T02[0,3]],[T02[1,3]],[T02[2,3]]])
z2 = Matrix([[T02[0,1]],[T02[1,1]],[T02[2,1]]])
T03 = T02*Ry(q2)*Tx(a3)
O3 = Matrix([[T03[0,3]],[T03[1,3]],[T03[2,3]]])
J1 = simplify(Matrix([cross(z0, O3-O0), z0]))
J2 = simplify(Matrix([cross(z1, O3-O1), z1]))
J3 = simplify(Matrix([cross(z2, O3-O2), z2]))
Jcb = J1.col_insert(1, J2.col_insert(1, J3))
print(Jcb)

result = Matrix([[-(cos(q1) + cos(q1 + q2))*sin(q0), -(sin(q1) + sin(q1 + q2))*sin(q0), -sin(q1 + q2)*cos(q0)],
                 [ (cos(q1) + cos(q1 + q2))*cos(q0),  (sin(q1) + sin(q1 + q2))*cos(q0), -sin(q0)*sin(q1 + q2)],
                 [                                0,                                 0,         -cos(q1 + q2)],
                 [                                0,                           cos(q0),              -sin(q0)],
                 [                                0,                           sin(q0),               cos(q0)],
                 [                                1,                                 0,                     0]])
v 20130925 2
C 40000 40000 0 0 0 title-B.sym
C 47000 43900 1 0 0 ground.sym
N 47200 46600 48500 46600 4
N 48500 45700 48500 45400 4
N 48500 44500 48500 44200 4
N 46300 44200 48500 44200 4
N 46300 44200 46300 46600 4
C 47200 46800 1 180 0 voltage-3.sym
{
T 47000 46100 5 8 0 0 180 0 1
device=VOLTAGE_SOURCE
T 46900 46300 5 10 1 1 180 0 1
refdes=V1
T 47200 46800 5 10 1 1 0 0 1
value=35.8
}
C 48600 45700 1 90 0 resistor-1.sym
{
T 48200 46000 5 10 0 0 90 0 1
device=RESISTOR
T 48300 45900 5 10 1 1 90 0 1
refdes=R1
T 48600 45700 5 10 1 1 0 0 1
value=6
}
C 48600 44500 1 90 0 resistor-1.sym
{
T 48200 44800 5 10 0 0 90 0 1
device=RESISTOR
T 48300 44700 5 10 1 1 90 0 1
refdes=R2
T 48600 44500 5 10 1 1 0 0 1
value=9
}

#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Kevin Armando Gonzalez Baeza
# No. Control: 19012313
# Calificación: XXX

x = 22
print ("x = {: >6b}". format ( x ) )
print ("x & 4 = {: >3d} = {: >6b}". format ( x & 4 , x & 4) )
print ("x | 1 = {: >3d} = {: >6b}". format ( x | 1 , x | 1) )
print ("x ^ 4 = {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )
print ("~x = {: >3d} = {: >6b}". format (~ x , ~ x ) )
print ("x << 1 = {: >3d} = {: >6b}". format ( x << 1 , x << 1) )
print ("x >> 2 = {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )
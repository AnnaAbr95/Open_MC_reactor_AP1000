# The OpenMC Monte Carlo Code 

import openmc
rod_position = 0.0

# Różne kasety zbudowane są z różnych materiałów, więc najpierw trzeba je zadeklarować
# KASETA A
uo2_A = openmc.Material()
uo2_A.add_nuclide('U235', 0.0074)
uo2_A.add_nuclide('U238', 0.9926)
uo2_A.add_element('O', 2.0)
uo2_A.set_density('g/cm3', 10.97)


# KASETA B
uo2_B = openmc.Material()
uo2_B.add_nuclide('U235', 0.0158)
uo2_B.add_nuclide('U238', 0.9842)
uo2_B.add_element('O', 2.0)
uo2_B.set_density('g/cm3', 10.96)


### KASETA C
uo2_C = openmc.Material()
uo2_C.add_nuclide('U235', 0.0320)
uo2_C.add_nuclide('U238', 0.968)
uo2_C.add_element('O', 2.0)
uo2_C.set_density('g/cm3', 10.94)

uo2_C_1 = openmc.Material()
uo2_C_1.add_nuclide('U235', 0.0158)
uo2_C_1.add_nuclide('U238', 0.9842)
uo2_C_1.add_element('O', 2.0)
uo2_C_1.set_density('g/cm3', 10.96)


### KASETA D
uo2_D_orange = openmc.Material()
uo2_D_orange.add_nuclide('U235', 0.0340)
uo2_D_orange.add_nuclide('U238', 0.966)
uo2_D_orange.add_element('O', 2.0)
uo2_D_orange.set_density('g/cm3', 10.97)

uo2_D_orange_1 = openmc.Material()
uo2_D_orange_1.add_nuclide('U235', 0.032)
uo2_D_orange_1.add_nuclide('U238', 0.968)
uo2_D_orange_1.add_element('O', 2.0)
uo2_D_orange_1.set_density('g/cm3', 10.97)

uo2_D_yellow = openmc.Material()
uo2_D_yellow.add_nuclide('U235', 0.042)
uo2_D_yellow.add_nuclide('U238', 0.958)
uo2_D_yellow.add_element('O', 2.0)
uo2_D_yellow.set_density('g/cm3', 10.97)

uo2_D_yellow_1 = openmc.Material()
uo2_D_yellow_1.add_nuclide('U235', 0.032)
uo2_D_yellow_1.add_nuclide('U238', 0.968)
uo2_D_yellow_1.add_element('O', 2.0)
uo2_D_yellow_1.set_density('g/cm3', 10.97)

uo2_D_green = openmc.Material()
uo2_D_green.add_nuclide('U235', 0.038)
uo2_D_green.add_nuclide('U238', 0.962)
uo2_D_green.add_element('O', 2.0)
uo2_D_green.set_density('g/cm3', 10.97)

uo2_D_green_1 = openmc.Material()
uo2_D_green_1.add_nuclide('U235', 0.032)
uo2_D_green_1.add_nuclide('U238', 0.968)
uo2_D_green_1.add_element('O', 2.0)
uo2_D_green_1.set_density('g/cm3', 10.97)


### KASETAA E1
### DOL I GORA
uo2_E1_orange_1 = openmc.Material()
uo2_E1_orange_1.add_nuclide('U235', 0.032)
uo2_E1_orange_1.add_nuclide('U238', 0.968)
uo2_E1_orange_1.add_element('O', 2.0)
uo2_E1_orange_1.set_density('g/cm3', 10.97)

uo2_E1_orange = openmc.Material()
uo2_E1_orange.add_nuclide('U235', 0.04)
uo2_E1_orange.add_nuclide('U238', 0.96)
uo2_E1_orange.add_element('O', 2.0)
uo2_E1_orange.set_density('g/cm3', 10.97)

uo2_E1_yellow = openmc.Material()
uo2_E1_yellow.add_nuclide('U235', 0.048)
uo2_E1_yellow.add_nuclide('U238', 0.952)
uo2_E1_yellow.add_element('O', 2.0)
uo2_E1_yellow.set_density('g/cm3', 10.97)

uo2_E1_yellow_1 = openmc.Material()
uo2_E1_yellow_1.add_nuclide('U235', 0.032)
uo2_E1_yellow_1.add_nuclide('U238', 0.968)
uo2_E1_yellow_1.add_element('O', 2.0)
uo2_E1_yellow_1.set_density('g/cm3', 10.97)

uo2_E1_green = openmc.Material()
uo2_E1_green.add_nuclide('U235', 0.044)
uo2_E1_green.add_nuclide('U238', 0.956)
uo2_E1_green.add_element('O', 2.0)
uo2_E1_green.set_density('g/cm3', 10.97)

uo2_E1_green_1 = openmc.Material()
uo2_E1_green_1.add_nuclide('U235', 0.032)
uo2_E1_green_1.add_nuclide('U238', 0.968)
uo2_E1_green_1.add_element('O', 2.0)
uo2_E1_green_1.set_density('g/cm3', 10.97)


### KASETA E2
uo2_E2_red = openmc.Material()
uo2_E2_red.add_nuclide('U235', 0.04)
uo2_E2_red.add_nuclide('U238', 0.96)
uo2_E2_red.add_element('O', 2.0)
uo2_E2_red.set_density('g/cm3', 10.97)

uo2_E2_greeen_IFBA = openmc.Material()
uo2_E2_greeen_IFBA.add_nuclide('U235', 0.044)
uo2_E2_greeen_IFBA.add_nuclide('U238', 0.956)
uo2_E2_greeen_IFBA.add_element('O', 2.0)
uo2_E2_greeen_IFBA.set_density('g/cm3', 10.97)

uo2_E2_yellow = openmc.Material()
uo2_E2_yellow.add_nuclide('U235', 0.048)
uo2_E2_yellow.add_nuclide('U238', 0.952)
uo2_E2_yellow.add_element('O', 2.0)
uo2_E2_yellow.set_density('g/cm3', 10.97)


### KASETA E3
#### UO2 BLANKET
uo2_blanket = openmc.Material()
uo2_blanket.add_nuclide('U235', 0.2320)
uo2_blanket.add_nuclide('U238', 0.768)
uo2_blanket.add_element('O', 2.0)
uo2_blanket.set_density('g/cm3', 10.97)


#### STANDARDOWA KOSZULKA
zr = openmc.Material()
zr.add_element('Zr', 1.0)
zr.set_density('g/cm3', 6.6)


### KOSZULKA IFDA
zrb2 = openmc.Material()
zrb2.add_element('Zr', 1.0)
zrb2.add_element('B', 2.0)
#zrb2.add_nuclide('b11', 0.205,'wo')
zrb2.set_density('g/cm3', 6.09)


####### WABA DŁUGI - 10B
WABA = openmc.Material()
WABA.add_nuclide('Al27',2.0)
WABA.add_nuclide('O16',3.0)
WABA.add_nuclide('B11',4.0)
#WABA.add_nuclide('b11',0.9762,'wo')
WABA.add_nuclide('C12',1.0)
WABA.set_density('g/cm3', 7.654)


###### WABA DŁUGIE BEZ 10B
WABA_l= openmc.Material()
WABA_l.add_nuclide('Al27',2.0)
WABA_l.add_nuclide('O16',3.0)
WABA_l.add_nuclide('B11',4.0)
WABA_l.add_nuclide('C12',1.0)
WABA_l.set_density('g/cm3', 7.654)


### WODA, KTÓRA OTACZA KOSZULKI
h2o = openmc.Material()
h2o.add_element('H', 2.0)
h2o.add_element('O', 1.0)
h2o.set_density('g/cm3', 1.0)

h2o.add_s_alpha_beta('c_H_in_H2O')

# PRĘT KONTROLNY
agincd = openmc.Material()
agincd.add_element('Ag', 0.8)
agincd.add_element('In', 0.15)
agincd.add_element('Cd', 0.05)
agincd.set_density('g/cm3', 10.17)


steel = openmc.Material()
steel.add_element('Ni',0.0925)
steel.add_element('Cr',0.19)
steel.add_element('Si',0.01)
steel.add_element('Fe',0.7075)
steel.set_density('g/cm3',8.03)


#PRET KONTROLNY
tungsten = openmc.Material()
tungsten.add_element('W', 1.0)
tungsten.set_density('g/cm3', 19.24)


#PRET KONTROLNY 1
alloy_718 = openmc.Material()
alloy_718.add_nuclide('Ni58',0.55)
alloy_718.add_nuclide('Cr52',0.21)
alloy_718.add_nuclide('Nb93',0.055)
alloy_718.add_nuclide('Mo98',0.033)
alloy_718.add_nuclide('Ti48',0.0115)
alloy_718.add_nuclide('Al27',0.008)
alloy_718.add_nuclide('Co59',0.01)
alloy_718.add_nuclide('C12',0.008)
alloy_718.add_nuclide('Mn55',0.0035)
alloy_718.add_nuclide('Fe56',0.111)
alloy_718.set_density('g/cm3',8.19)

materials = openmc.Materials([uo2_A, uo2_B, uo2_C, uo2_C_1, uo2_D_orange, uo2_D_orange_1, uo2_D_yellow, uo2_D_yellow_1, uo2_D_green, uo2_D_green_1, uo2_E1_orange, uo2_E1_orange_1, uo2_E1_yellow, uo2_E1_yellow_1, uo2_E1_green, uo2_E1_green_1, uo2_E2_red, uo2_E2_yellow, uo2_E2_greeen_IFBA, uo2_blanket, zr, zrb2, WABA, WABA_l, h2o, agincd, steel, alloy_718])
materials.export_to_xml()



# GEOMETRY CAŁEGO UKŁADU
colors = {h2o: 'blue',
          uo2_A: 'black',
          zr: 'violet',
          agincd: 'yellow'}


# PRET PALIWOWY

# KASETA A
fuel_cylinder_A = openmc.ZCylinder(R=0.409567)
gap_cylinder_A = openmc.ZCylinder(R=0.417822)
clad_cylinder_A = openmc.ZCylinder(R=0.4749705)

bot = openmc.ZPlane(z0=0, boundary_type='vacuum')
top = openmc.ZPlane(z0=426.7, boundary_type='vacuum')

fuel_A = openmc.Cell()
fuel_A.fill = uo2_A
fuel_A.region = -fuel_cylinder_A & +bot & -top

gap_A = openmc.Cell()
gap_A.region = +fuel_cylinder_A & -gap_cylinder_A & +bot & -top

clad_A = openmc.Cell()
clad_A.fill = zr
clad_A.region = +gap_cylinder_A & -clad_cylinder_A & +bot & -top

pitch = 1.259815
xm = openmc.XPlane(x0=-pitch / 2.0)
xp = openmc.XPlane(x0=pitch / 2.0)
ym = openmc.YPlane(y0=-pitch / 2.0)
yp = openmc.YPlane(y0=pitch / 2.0)

moderator_A = openmc.Cell()
moderator_A.fill = h2o
moderator_A.region = +xm & -xp & +ym & -yp & +clad_cylinder_A & +bot & -top

A = openmc.Universe(cells=[fuel_A, gap_A, clad_A, moderator_A])


# KASETA B
fuel_cylinder_B = openmc.ZCylinder(R=0.409567)
gap_cylinder_B = openmc.ZCylinder(R=0.417822)
clad_cylinder_B = openmc.ZCylinder(R=0.4749705)

fuel_B = openmc.Cell()
fuel_B.fill = uo2_B
fuel_B.region = -fuel_cylinder_B & +bot & -top

gap_B = openmc.Cell()
gap_B.region = +fuel_cylinder_B & -gap_cylinder_B & +bot & -top

clad_B = openmc.Cell()
clad_B.fill = zr
clad_B.region = +gap_cylinder_B & -clad_cylinder_B & +bot & -top

moderator_B = openmc.Cell()
moderator_B.fill = h2o
moderator_B.region = +xm & -xp & +ym & -yp & +clad_cylinder_B & +bot & -top

B = openmc.Universe(cells=[fuel_B, gap_B, clad_B, moderator_B])
#B.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


### KASETA C
fuel_cylinder_C = openmc.ZCylinder(R=0.409567)
fuel_cylinder_C_1 = openmc.ZCylinder(R=0.409567)
fuel_cylinder_C_2 = openmc.ZCylinder(R=0.409567)

gap_cylinder_C = openmc.ZCylinder(R=0.417822)


clad_cylinder_C = openmc.ZCylinder(R=0.4749705)


bot_C = openmc.ZPlane(z0=20.32, boundary_type="transmission")
top_C = openmc.ZPlane(z0=406.38, boundary_type="transmission")

fuel_C = openmc.Cell()
fuel_C.fill = uo2_C
fuel_C.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_C_1 = openmc.Cell()
fuel_C_1.fill = uo2_C_1
fuel_C_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_C_2 = openmc.Cell()
fuel_C_2.fill = uo2_C_1
fuel_C_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_C = openmc.Cell()
gap_C.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_C = openmc.Cell()
clad_C.fill = zr
clad_C.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_C = openmc.Cell()
moderator_C.fill = h2o
moderator_C.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


C = openmc.Universe(cells=[fuel_C, gap_C, clad_C, moderator_C,fuel_C_1,fuel_C_2])
#C.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


### KASETA D - orange
fuel_cylinder_D_orange = openmc.ZCylinder(R=0.409567)

gap_cylinder_D_orange= openmc.ZCylinder(R=0.417822)

clad_cylinder_D_orange = openmc.ZCylinder(R=0.4749705)

bot_D = openmc.ZPlane(z0=20.32, boundary_type="transmission")
top_D = openmc.ZPlane(z0=406.38, boundary_type="transmission")

fuel_D_orange = openmc.Cell()
fuel_D_orange.fill = uo2_D_orange
fuel_D_orange.region = -fuel_cylinder_D_orange & +bot_D & -top_D

fuel_D_orange_1 = openmc.Cell()
fuel_D_orange_1.fill = uo2_D_orange_1
fuel_D_orange_1.region = -fuel_cylinder_D_orange & +bot & -bot_D

fuel_D_orange_2 = openmc.Cell()
fuel_D_orange_2.fill = uo2_D_orange_1
fuel_D_orange_2.region = -fuel_cylinder_D_orange & +top_D & -top

gap_D_orange = openmc.Cell()
gap_D_orange.region = +fuel_cylinder_D_orange & -gap_cylinder_D_orange & +bot & -top


clad_D_orange = openmc.Cell()
clad_D_orange.fill = zr
clad_D_orange.region = +gap_cylinder_D_orange & -clad_cylinder_D_orange & +bot & -top


moderator_D_orange = openmc.Cell()
moderator_D_orange.fill = h2o
moderator_D_orange.region = +xm & -xp & +ym & -yp & +clad_cylinder_D_orange & +bot & -top



D_o = openmc.Universe(cells=[fuel_D_orange, gap_D_orange, clad_D_orange, moderator_D_orange,fuel_D_orange_1,fuel_D_orange_2,])

#D_o.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


### KASETA D - red
fuel_cylinder_D_red = openmc.ZCylinder(R=0.409567)

gap_cylinder_D_red= openmc.ZCylinder(R=0.417822)

clad_cylinder_D_red = openmc.ZCylinder(R=0.4749705)

#bot_D = openmc.ZPlane(z0=20.32, boundary_type="transmission")
#top_D = openmc.ZPlane(z0=406.38, boundary_type="transmission")

fuel_D_red = openmc.Cell()
fuel_D_red.fill = uo2_D_orange
fuel_D_red.region = -fuel_cylinder_D_red & +bot_D & -top_D

fuel_D_red_1 = openmc.Cell()
fuel_D_red_1.fill = uo2_blanket
fuel_D_red_1.region = -fuel_cylinder_D_red & +bot & -bot_D

fuel_D_red_2 = openmc.Cell()
fuel_D_red_2.fill = uo2_blanket
fuel_D_red_2.region = -fuel_cylinder_D_red & +top_D & -top

gap_D_red = openmc.Cell()
gap_D_red.region = +fuel_cylinder_D_red & -gap_cylinder_D_red & +bot & -top


clad_D_red = openmc.Cell()
clad_D_red.fill = zrb2
clad_D_red.region = +gap_cylinder_D_red & -clad_cylinder_D_red & +bot & -top


moderator_D_red = openmc.Cell()
moderator_D_red.fill = h2o
moderator_D_red.region = +xm & -xp & +ym & -yp & +clad_cylinder_D_red & +bot & -top



D_r = openmc.Universe(cells=[fuel_D_red, gap_D_red, clad_D_red, moderator_D_red,fuel_D_red_1,fuel_D_red_2])

#D_r.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


### KASETA D - brown
fuel_cylinder_D_red = openmc.ZCylinder(R=0.409567)

gap_cylinder_D_red= openmc.ZCylinder(R=0.417822)

clad_cylinder_D_red = openmc.ZCylinder(R=0.4749705)

#bot_D = openmc.ZPlane(z0=20.32, boundary_type="transmission")
#top_D = openmc.ZPlane(z0=406.38, boundary_type="transmission")

fuel_D_brown = openmc.Cell()
fuel_D_brown.fill = uo2_D_yellow
fuel_D_brown.region = -fuel_cylinder_D_red & +bot_D & -top_D

fuel_D_brown_1 = openmc.Cell()
fuel_D_brown_1.fill = uo2_blanket
fuel_D_brown_1.region = -fuel_cylinder_D_red & +bot & -bot_D

fuel_D_brown_2 = openmc.Cell()
fuel_D_brown_2.fill = uo2_blanket
fuel_D_brown_2.region = -fuel_cylinder_D_red & +top_D & -top

gap_D_brown = openmc.Cell()
gap_D_brown.region = +fuel_cylinder_D_red & -gap_cylinder_D_red & +bot & -top


clad_D_brown = openmc.Cell()
clad_D_brown.fill = zrb2
clad_D_brown.region = +gap_cylinder_D_red & -clad_cylinder_D_red & +bot & -top


moderator_D_brown = openmc.Cell()
moderator_D_brown.fill = h2o
moderator_D_brown.region = +xm & -xp & +ym & -yp & +clad_cylinder_D_red & +bot & -top



D_b = openmc.Universe(cells=[fuel_D_brown, gap_D_brown, clad_D_brown, moderator_D_brown,fuel_D_brown_1,fuel_D_brown_2])

#D_b.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


#### KASETA D - green
fuel_D_green = openmc.Cell()
fuel_D_green.fill = uo2_D_green
fuel_D_green.region = -fuel_cylinder_D_orange & +bot_D & -top_D

fuel_D_green_1 = openmc.Cell()
fuel_D_green_1.fill = uo2_D_green_1
fuel_D_green_1.region = -fuel_cylinder_D_orange & +bot & -bot_D

fuel_D_green_2 = openmc.Cell()
fuel_D_green_2.fill = uo2_D_green_1
fuel_D_green_2.region = -fuel_cylinder_D_orange & +top_D & -top

gap_D_orange = openmc.Cell()
gap_D_orange.region = +fuel_cylinder_D_orange & -gap_cylinder_D_orange & +bot & -top


clad_D_orange = openmc.Cell()
clad_D_orange.fill = zr
clad_D_orange.region = +gap_cylinder_D_orange & -clad_cylinder_D_orange & +bot & -top


moderator_D_orange = openmc.Cell()
moderator_D_orange.fill = h2o
moderator_D_orange.region = +xm & -xp & +ym & -yp & +clad_cylinder_D_orange & +bot & -top


D_g = openmc.Universe(cells=[fuel_D_green, gap_D_orange, clad_D_orange, moderator_D_orange,fuel_D_green_1,fuel_D_green_2,])

#D_g.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


#### KASETA D - green IFBA
fuel_D_green = openmc.Cell()
fuel_D_green.fill = uo2_D_green
fuel_D_green.region = -fuel_cylinder_D_orange & +bot_D & -top_D

fuel_D_green_1 = openmc.Cell()
fuel_D_green_1.fill = uo2_blanket
fuel_D_green_1.region = -fuel_cylinder_D_orange & +bot & -bot_D

fuel_D_green_2 = openmc.Cell()
fuel_D_green_2.fill = uo2_blanket
fuel_D_green_2.region = -fuel_cylinder_D_orange & +top_D & -top

gap_D_orange = openmc.Cell()
gap_D_orange.region = +fuel_cylinder_D_orange & -gap_cylinder_D_orange & +bot & -top


clad_D_orange = openmc.Cell()
clad_D_orange.fill = zrb2
clad_D_orange.region = +gap_cylinder_D_orange & -clad_cylinder_D_orange & +bot & -top


moderator_D_orange = openmc.Cell()
moderator_D_orange.fill = h2o
moderator_D_orange.region = +xm & -xp & +ym & -yp & +clad_cylinder_D_orange & +bot & -top



D_g_IFBA = openmc.Universe(cells=[fuel_D_green, gap_D_orange, clad_D_orange, moderator_D_orange,fuel_D_green_1,fuel_D_green_2])

#D_g_IFBA.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


#### KASETA D - yellow
fuel_D_yellow = openmc.Cell()
fuel_D_yellow.fill = uo2_D_yellow
fuel_D_yellow.region = -fuel_cylinder_D_orange & +bot_D & -top_D

fuel_D_yellow_1 = openmc.Cell()
fuel_D_yellow_1.fill = uo2_D_yellow_1
fuel_D_yellow_1.region = -fuel_cylinder_D_orange & +bot & -bot_D

fuel_D_yellow_2 = openmc.Cell()
fuel_D_yellow_2.fill = uo2_D_yellow_1
fuel_D_yellow_2.region = -fuel_cylinder_D_orange & +top_D & -top

gap_D_orange = openmc.Cell()
gap_D_orange.region = +fuel_cylinder_D_orange & -gap_cylinder_D_orange & +bot & -top


clad_D_orange = openmc.Cell()
clad_D_orange.fill = zr
clad_D_orange.region = +gap_cylinder_D_orange & -clad_cylinder_D_orange & +bot & -top


moderator_D_orange = openmc.Cell()
moderator_D_orange.fill = h2o
moderator_D_orange.region = +xm & -xp & +ym & -yp & +clad_cylinder_D_orange & +bot & -top



D_y = openmc.Universe(cells=[fuel_D_yellow, gap_D_orange, clad_D_orange, moderator_D_orange,fuel_D_yellow_1,fuel_D_yellow_2,])

#D_y.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


### KASETA E2 - red
#fuel_cylinder_C = openmc.ZCylinder(R=0.409567)
#fuel_cylinder_C_1 = openmc.ZCylinder(R=0.409567)
#fuel_cylinder_C_2 = openmc.ZCylinder(R=0.409567)
#gap_cylinder_C = openmc.ZCylinder(R=0.417822)


#clad_cylinder_C = openmc.ZCylinder(R=0.4749705)


#bot_C = openmc.ZPlane(z0=20.32, boundary_type="transmission")
#top_C = openmc.ZPlane(z0=406.38, boundary_type="transmission")

fuel_E2_red = openmc.Cell()
fuel_E2_red.fill = uo2_E2_red
fuel_E2_red.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_E2_red_1 = openmc.Cell()
fuel_E2_red_1.fill = uo2_blanket
fuel_E2_red_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_E2_red_2 = openmc.Cell()
fuel_E2_red_2.fill = uo2_blanket
fuel_E2_red_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_E2_red = openmc.Cell()
gap_E2_red.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_E2_red = openmc.Cell()
clad_E2_red.fill = zrb2
clad_E2_red.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_E2_red = openmc.Cell()
moderator_E2_red.fill = h2o
moderator_E2_red.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


E2_r = openmc.Universe(cells=[fuel_E2_red, gap_E2_red, clad_E2_red, moderator_E2_red,fuel_E2_red_1,fuel_E2_red_2])
#E2_r.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)
### KASETA E2 - orange

#fuel_cylinder_C = openmc.ZCylinder(R=0.409567)
#fuel_cylinder_C_1 = openmc.ZCylinder(R=0.409567)
#fuel_cylinder_C_2 = openmc.ZCylinder(R=0.409567)
#gap_cylinder_C = openmc.ZCylinder(R=0.417822)


#clad_cylinder_C = openmc.ZCylinder(R=0.4749705)


#bot_C = openmc.ZPlane(z0=20.32, boundary_type="transmission")
#top_C = openmc.ZPlane(z0=406.38, boundary_type="transmission")

fuel_E2_o = openmc.Cell()
fuel_E2_o.fill = uo2_E2_red
fuel_E2_o.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_E2_o_1 = openmc.Cell()
fuel_E2_o_1.fill = uo2_blanket
fuel_E2_o_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_E2_o_2 = openmc.Cell()
fuel_E2_o_2.fill = uo2_blanket
fuel_E2_o_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_E2_o = openmc.Cell()
gap_E2_o.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_E2_o = openmc.Cell()
clad_E2_o.fill = zr
clad_E2_o.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_E2_o = openmc.Cell()
moderator_E2_o.fill = h2o
moderator_E2_o.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


E2_o = openmc.Universe(cells=[fuel_E2_o, gap_E2_o, clad_E2_o, moderator_E2_o,fuel_E2_o_1,fuel_E2_o_2])



### KASETA E2 - green
fuel_E2_green = openmc.Cell()
fuel_E2_green.fill = uo2_E2_greeen_IFBA
fuel_E2_green.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_E2_green_1 = openmc.Cell()
fuel_E2_green_1.fill = uo2_blanket
fuel_E2_green_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_E2_green_2 = openmc.Cell()
fuel_E2_green_2.fill = uo2_blanket
fuel_E2_green_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_E2_green = openmc.Cell()
gap_E2_green.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_E2_green = openmc.Cell()
clad_E2_green.fill = zr
clad_E2_green.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_E2_green = openmc.Cell()
moderator_E2_green.fill = h2o
moderator_E2_green.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


E2_g = openmc.Universe(cells=[fuel_E2_green, gap_E2_green, clad_E2_green, moderator_E2_green,fuel_E2_green_1,fuel_E2_green_2])


### KASETA E2 - green IFBA
fuel_E2_green_IFBA = openmc.Cell()
fuel_E2_green_IFBA.fill = uo2_E2_greeen_IFBA
fuel_E2_green_IFBA.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_E2_green_IFBA_1 = openmc.Cell()
fuel_E2_green_IFBA_1.fill = uo2_blanket
fuel_E2_green_IFBA_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_E2_green_IFBA_2= openmc.Cell()
fuel_E2_green_IFBA_2.fill = uo2_blanket
fuel_E2_green_IFBA_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_E2_green_IFBA = openmc.Cell()
gap_E2_green_IFBA.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_E2_green_IFBA = openmc.Cell()
clad_E2_green_IFBA.fill = zrb2
clad_E2_green_IFBA.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_E2_green_IFBA = openmc.Cell()
moderator_E2_green_IFBA.fill = h2o
moderator_E2_green_IFBA.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


E2_g_IFBA = openmc.Universe(cells=[fuel_E2_green_IFBA, gap_E2_green_IFBA, clad_E2_green_IFBA, moderator_E2_green_IFBA,fuel_E2_green_IFBA_1,fuel_E2_green_IFBA_2])


### KASETA E2 - yellow
fuel_E2_yellow = openmc.Cell()
fuel_E2_yellow.fill = uo2_E2_yellow
fuel_E2_yellow.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_E2_yellow_1 = openmc.Cell()
fuel_E2_yellow_1.fill = uo2_blanket
fuel_E2_yellow_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_E2_yellow_2 = openmc.Cell()
fuel_E2_yellow_2.fill = uo2_blanket
fuel_E2_yellow_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_E2_yellow = openmc.Cell()
gap_E2_yellow.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_E2_yellow = openmc.Cell()
clad_E2_yellow.fill = zr
clad_E2_yellow.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_E2_yellow = openmc.Cell()
moderator_E2_yellow.fill = h2o
moderator_E2_yellow.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


E2_y = openmc.Universe(cells=[fuel_E2_yellow, gap_E2_yellow, clad_E2_yellow, moderator_E2_yellow,fuel_E2_yellow_1,fuel_E2_yellow_2])


### KASETA E2 - brown
fuel_E2_brown = openmc.Cell()
fuel_E2_brown.fill = uo2_E2_yellow
fuel_E2_brown.region = -fuel_cylinder_C & +bot_C & -top_C

fuel_E2_brown_1 = openmc.Cell()
fuel_E2_brown_1.fill = uo2_blanket
fuel_E2_brown_1.region = -fuel_cylinder_C_1 & +bot & -bot_C

fuel_E2_brown_2 = openmc.Cell()
fuel_E2_brown_2.fill = uo2_blanket
fuel_E2_brown_2.region = -fuel_cylinder_C_2 & +top_C & -top

gap_E2_brown = openmc.Cell()
gap_E2_brown.region = +fuel_cylinder_C & -gap_cylinder_C & +bot & -top


clad_E2_brown = openmc.Cell()
clad_E2_brown.fill = zrb2
clad_E2_brown.region = +gap_cylinder_C & -clad_cylinder_C & +bot & -top


moderator_E2_brown = openmc.Cell()
moderator_E2_brown.fill = h2o
moderator_E2_brown.region = +xm & -xp & +ym & -yp & +clad_cylinder_C & +bot & -top


E2_b = openmc.Universe(cells=[fuel_E2_brown, gap_E2_brown, clad_E2_brown, moderator_E2_brown,fuel_E2_brown_1,fuel_E2_brown_2])


### WABA DŁUGI
a_WABA = openmc.ZCylinder(R=0.29)

b_WABA = openmc.ZCylinder(R=0.34)

c_WABA = openmc.ZCylinder(R=0.35)

d_WABA = openmc.ZCylinder(R=0.40386)

e_WABA = openmc.ZCylinder(R=0.41783)

f_WABA = openmc.ZCylinder(R=0.48387)

g_WABA = openmc.ZCylinder(R=0.561329)

h_WABA = openmc.ZCylinder(R=0.612128)


bot_WABA = openmc.ZPlane(z0=20.32, boundary_type="transmission")
top_WABA = openmc.ZPlane(z0=406.38, boundary_type="transmission")


water_center_WABA = openmc.Cell()
water_center_WABA.fill = h2o
water_center_WABA.region = -a_WABA & +bot_WABA & -top

clad_center_WABA = openmc.Cell()
clad_center_WABA.fill = zr
clad_center_WABA.region = +a_WABA & -b_WABA & +bot_WABA & -top

gap_in_WABA = openmc.Cell()
gap_in_WABA.region = +b_WABA & -c_WABA & +bot_WABA & -top

absorber_WABA = openmc.Cell()
absorber_WABA.fill = WABA
absorber_WABA.region = +c_WABA & -d_WABA & +bot_WABA & -top_WABA


absorber_WABA_1 = openmc.Cell()
absorber_WABA_1.fill = WABA_l
absorber_WABA_1.region = +c_WABA & -d_WABA & +top_WABA & -top

gap_center_WABA = openmc.Cell()
gap_center_WABA.region = +d_WABA & -e_WABA & +bot_WABA & -top

clad_out_WABA = openmc.Cell()
clad_out_WABA.fill = zr
clad_out_WABA.region = +e_WABA & -f_WABA & +bot_WABA & -top

gap_out_WABA = openmc.Cell()
gap_out_WABA.region = +f_WABA & -g_WABA & +bot_WABA & -top

water_out_WABA = openmc.Cell()
water_out_WABA.fill = h2o
water_out_WABA.region = +h_WABA & +bot_WABA & -top

water = openmc.Cell()
water.fill = h2o
water.region = +bot & -bot_WABA


WABA = openmc.Universe(cells=[water,water_out_WABA,water_center_WABA,clad_out_WABA,clad_center_WABA,gap_out_WABA,gap_center_WABA,gap_in_WABA,absorber_WABA,absorber_WABA_1])
#WABA.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


### WABA ŚREDNI
#bot_WABA = openmc.ZPlane(z0=20.32, boundary_type="transmission")

bot_WABA_1 = openmc.ZPlane(z0=40.64, boundary_type="transmission")

top_WABA_1 = openmc.ZPlane(z0=335.3, boundary_type="transmission")


water_center_WABA = openmc.Cell()
water_center_WABA.fill = h2o
water_center_WABA.region = -a_WABA & +bot_WABA & -top

clad_center_WABA = openmc.Cell()
clad_center_WABA.fill = zr
clad_center_WABA.region = +a_WABA & -b_WABA & +bot_WABA & -top

gap_in_WABA = openmc.Cell()
gap_in_WABA.region = +b_WABA & -c_WABA & +bot_WABA & -top

absorber_WABA = openmc.Cell()
absorber_WABA.fill = WABA
absorber_WABA.region = +c_WABA & -d_WABA & +bot_WABA_1 & -top_WABA_1


absorber_WABA_1 = openmc.Cell()
absorber_WABA_1.fill = WABA_l
absorber_WABA_1.region = +c_WABA & -d_WABA & +top_WABA_1 & -top

gap_center_WABA = openmc.Cell()
gap_center_WABA.region = +d_WABA & -e_WABA & +bot_WABA & -top

clad_out_WABA = openmc.Cell()
clad_out_WABA.fill = zr
clad_out_WABA.region = +e_WABA & -f_WABA & +bot_WABA & -top

gap_out_WABA = openmc.Cell()
gap_out_WABA.region = +f_WABA & -g_WABA & +bot_WABA & -top

water_out_WABA = openmc.Cell()
water_out_WABA.fill = h2o
water_out_WABA.region = +h_WABA & +bot_WABA & -top

water = openmc.Cell()
water.fill = h2o
water.region = +bot & -bot_WABA


WABA_m = openmc.Universe(cells=[water,water_out_WABA,water_center_WABA,clad_out_WABA,clad_center_WABA,gap_out_WABA,gap_center_WABA,gap_in_WABA,absorber_WABA,absorber_WABA_1])

#WABA_m.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


# PRET KONTROLNY

#rod_cylinder = openmc.ZCylinder(R=0.484)
#bot_control = openmc.ZPlane(z0=rod_position, boundary_type="transmission")

#rod = openmc.Cell()
#rod.fill = agincd
#rod.region = -rod_cylinder & +bot_control & -top

#moderator_rod = openmc.Cell()
#moderator_rod.fill = h2o
#moderator_rod.region = +xm & -xp & +ym & -yp & +rod_cylinder & +bot_control & -top

# WODA POD WYSUNIETYM PRETEM
#moderator_under = openmc.Cell()
#moderator_under.fill = h2o
#moderator_under.region = +xm & -xp & +ym & -yp & +bot & -bot_control

#c = openmc.Universe(cells=[rod, moderator_rod, moderator_under])


### RURA WIODACA
rura_wiodaca = openmc.ZCylinder(R=0.417822)
clad_rura_wiodaca = openmc.ZCylinder(R=0.4749705)

rura_h2o = openmc.Cell()
rura_h2o.fill = h2o
rura_h2o.region = -rura_wiodaca & +bot & -top

clad_rura_h2o = openmc.Cell()
clad_rura_h2o.fill = zr
clad_rura_h2o.region = +rura_wiodaca & -clad_rura_wiodaca & +bot & -top

moderator_rura_wiodaca = openmc.Cell()
moderator_rura_wiodaca.fill = h2o
moderator_rura_wiodaca.region = +xm & -xp & +ym & -yp & +clad_rura_wiodaca & +bot & -top

W = openmc.Universe(cells=[rura_h2o, clad_rura_h2o,moderator_rura_wiodaca])


# PRET KONTROLNY
rod_cylinder = openmc.ZCylinder(R=0.44577)
rod_clad_in = openmc.ZCylinder(R=0.48387)
rod_clad_out = openmc.ZCylinder(R=0.507365)
bot_control = openmc.ZPlane(z0=rod_position, boundary_type="transmission")

rod = openmc.Cell()
rod.fill = agincd
rod.region = -rod_cylinder & +bot_control & -top

gap = openmc.Cell()
gap.region = +rod_cylinder & -rod_clad_in & +bot_control & -top

clad = openmc.Cell()
clad.fill = steel
clad.region = +rod_clad_in & -rod_clad_out & +bot_control & -top

moderator_rod = openmc.Cell()
moderator_rod.fill = h2o
moderator_rod.region = +xm & -xp & +ym & -yp & +rod_clad_out & +bot_control & -top


moderator_under = openmc.Cell()
moderator_under.fill = h2o
moderator_under.region = +xm & -xp & +ym & -yp & +bot & -bot_control


CON = openmc.Universe(cells=[rod, clad, moderator_rod, gap, moderator_under])
#CON.plot(width=(pitch * 1.2, pitch * 1.2), color_by='material', colors=colors)


### PRET KONTROLNY Z WOLFRANEM
wolfi_cylinder = openmc.ZCylinder(R=0.24892)
alloy_cylinder = openmc.ZCylinder(R=0.3937)
clad_in_cylinder = openmc.ZCylinder(R=0.48387)
clad_out_cylinder = openmc.ZCylinder(R=0.516255)

wolfi = openmc.Cell()
wolfi.fill = tungsten
wolfi.region = -wolfi_cylinder & +bot_control & -top

alloy = openmc.Cell()
alloy.fill = alloy_718
alloy.region = +wolfi_cylinder & -alloy_cylinder & +bot_control & -top


gap = openmc.Cell()
gap.region = +alloy_cylinder & -clad_in_cylinder & +bot_control & -top


clad = openmc.Cell()
clad.fill = steel
clad.region = +clad_in_cylinder & -clad_out_cylinder & +bot_control & -top

moderator_rod = openmc.Cell()
moderator_rod.fill = h2o
moderator_rod.region = +xm & -xp & +ym & -yp & +rod_clad_out & +bot_control & -top

moderator_under = openmc.Cell()
moderator_under.fill = h2o
moderator_under.region = +xm & -xp & +ym & -yp & +bot & -bot_control

CON_1 = openmc.Universe(cells=[wolfi, alloy, moderator_rod, gap, clad, moderator_under])


#CON_1.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)



# WODA POD WYSUNIETYM PRETEM
#moderator_under = openmc.Cell()
#moderator_under.fill = h2o
#moderator_under.region = +xm & -xp & +ym & -yp & +bot & -bot_control

#c = openmc.Universe(cells=[rod, moderator_rod, moderator_under])

#c.plot(width=(pitch * 1.2, pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)

#c.plot(width=(pitch * 1.2, pitch * 1.2), origin=(0, 0, 300), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW KONTROLNYMI
n_cells = 17
assembly_lattice_CON = openmc.RectLattice()
assembly_lattice_CON.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_CON.pitch = (pitch, pitch)
assembly_lattice_CON.universes = [
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
    [CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON, CON],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

CONN = openmc.Cell()
CONN.fill = assembly_lattice_CON
CONN.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

CONNN = openmc.Universe()
CONNN.add_cell(CONN)

#AAA.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)

#AAA.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 300), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW KONTROLNYMI WOLFI
n_cells = 17
assembly_lattice_CON_1 = openmc.RectLattice()
assembly_lattice_CON_1.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_CON_1.pitch = (pitch, pitch)
assembly_lattice_CON_1.universes = [
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
    [CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1, CON_1],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

CONN_1 = openmc.Cell()
CONN_1.fill = assembly_lattice_CON_1
CONN_1.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

CONNN_1 = openmc.Universe()
CONNN_1.add_cell(CONN_1)

CONNN_1.plot(width=(pitch * 1.2, pitch * 1, 2), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW A
n_cells = 17
assembly_lattice_A = openmc.RectLattice()
assembly_lattice_A.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_A.pitch = (pitch, pitch)
assembly_lattice_A.universes = [
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, A, A, A, W, A, A, W, A, A, W, A, A, A, A, A],
    [A, A, A, W, A, A, A, A, A, A, A, A, A, W, A, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, W, A, A, W, A, A, W, A, A, W, A, A, W, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, W, A, A, W, A, A, W, A, A, W, A, A, W, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, W, A, A, W, A, A, W, A, A, W, A, A, W, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, A, W, A, A, A, A, A, A, A, A, A, W, A, A, A],
    [A, A, A, A, A, W, A, A, W, A, A, W, A, A, A, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
    [A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A, A],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

AA = openmc.Cell()
AA.fill = assembly_lattice_A
AA.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

AAA = openmc.Universe()
AAA.add_cell(AA)

#AAA.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)

#AAA.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 300), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW B
n_cells = 17
assembly_lattice_B = openmc.RectLattice()
assembly_lattice_B.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_B.pitch = (pitch, pitch)
assembly_lattice_B.universes = [
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, W, B, B, W, B, B, W, B, B, B, B, B],
    [B, B, B, W, B, B, B, B, B, B, B, B, B, W, B, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, W, B, B, W, B, B, W, B, B, W, B, B, W, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, W, B, B, W, B, B, W, B, B, W, B, B, W, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, W, B, B, W, B, B, W, B, B, W, B, B, W, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, B, W, B, B, B, B, B, B, B, B, B, W, B, B, B],
    [B, B, B, B, B, W, B, B, W, B, B, W, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

BB = openmc.Cell()
BB.fill = assembly_lattice_B
BB.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

BBB = openmc.Universe()
BBB.add_cell(BB)

#BBB.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)

#BBB.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 300), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW C
n_cells = 17
assembly_lattice_C = openmc.RectLattice()
assembly_lattice_C.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_C.pitch = (pitch, pitch)
assembly_lattice_C.universes = [
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, C, C, C, W, C, C, W, C, C, W, C, C, C, C, C],
    [C, C, C, W, C, C, C, C, C, C, C, C, C, W, C, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, W, C, C, W, C, C, W, C, C, W, C, C, W, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, W, C, C, W, C, C, W, C, C, W, C, C, W, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, W, C, C, W, C, C, W, C, C, W, C, C, W, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, C, W, C, C, C, C, C, C, C, C, C, W, C, C, C],
    [C, C, C, C, C, W, C, C, W, C, C, W, C, C, C, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
    [C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

CC = openmc.Cell()
CC.fill = assembly_lattice_C
CC.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

CCC = openmc.Universe()
CCC.add_cell(BB)

#CCC.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)

#CCC.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 300), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW D
n_cells = 17
assembly_lattice_D = openmc.RectLattice()
assembly_lattice_D.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_D.pitch = (pitch, pitch)
assembly_lattice_D.universes = [
    [D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r],
    [D_o, D_g_IFBA, D_g, D_g, D_g, D_g_IFBA, D_g, D_g, D_g, D_g, D_g, D_g_IFBA, D_g, D_g, D_g, D_g_IFBA, D_o],
    [D_r, D_g, D_g, D_g, D_g, W, D_g, D_g, WABA, D_g, D_g, W, D_g, D_g, D_g, D_g, D_r],
    [D_o, D_g, D_g, WABA, D_g, D_g, D_b, D_y, D_g, D_y, D_b, D_g, D_g, WABA, D_g, D_g, D_o],
    [D_r, D_g, D_g, D_g, D_g, D_g, D_b, D_y, D_g, D_y, D_b, D_g, D_g, D_g, D_g, D_g, D_r],
    [D_o, D_g_IFBA, W, D_g, D_g, W, D_g, D_g, WABA, D_g, D_g, W, D_g, D_g, W, D_g_IFBA, D_o],
    [D_r, D_g, D_g, D_b, D_b, D_g, D_b, D_y, D_g, D_y, D_b, D_g, D_b, D_b, D_g, D_g, D_r],
    [D_o, D_g, D_g, D_y, D_y, D_g, D_y, D_b, D_g, D_b, D_y, D_g, D_y, D_y, D_g, D_g, D_o],
    [D_r, D_g, WABA, D_g, D_g, WABA, D_g, D_g, WABA, D_g, D_g, WABA, D_g, D_g, WABA, D_g, D_r],
    [D_o, D_g, D_g, D_y, D_y, D_g, D_y, D_b, D_g, D_b, D_y, D_g, D_y, D_y, D_g, D_g, D_o],
    [D_r, D_g, D_g, D_b, D_b, D_g, D_b, D_y, D_g, D_y, D_b, D_g, D_b, D_b, D_g, D_g, D_r],
    [D_o, D_g_IFBA, W, D_g, D_g, W, D_g, D_g, WABA, D_g, D_g, W, D_g, D_g, W, D_g_IFBA, D_o],
    [D_r, D_g, D_g, D_g, D_g, D_g, D_b, D_y, D_g, D_y, D_b, D_g, D_g, D_g, D_g, D_g, D_r],
    [D_o, D_g, D_g, WABA, D_g, D_g, D_b, D_y, D_g, D_y, D_b, D_g, D_g, WABA, D_g, D_g, D_o],
    [D_r, D_g, D_g, D_g, D_g, W, D_g, D_g, WABA, D_g, D_g, W, D_g, D_g, D_g, D_g, D_r],
    [D_o, D_g_IFBA, D_g, D_g, D_g, D_g_IFBA, D_g, D_g, D_g, D_g, D_g, D_g_IFBA, D_g, D_g, D_g, D_g_IFBA, D_o],
    [D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r, D_o, D_r],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

DD = openmc.Cell()
DD.fill = assembly_lattice_D
DD.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

DDD = openmc.Universe()
DDD.add_cell(DD)

#DDD.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)

#AAA.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 300), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW E1
n_cells = 17
assembly_lattice_E1 = openmc.RectLattice()
assembly_lattice_E1.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_E1.pitch = (pitch, pitch)
assembly_lattice_E1.universes = [
    [E2_o, E2_r, E2_o, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_o, E2_r, E2_o],
    [E2_r, E2_g, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g, E2_r],
    [E2_o, E2_g, E2_g, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, E2_g, E2_g, E2_o],
    [E2_r, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g, E2_g, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_g, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_b, E2_b, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_b, E2_b, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_b, E2_b, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_b, E2_b, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_g, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_g, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_r],
    [E2_o, E2_g, E2_g, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, E2_g, E2_g, E2_o],
    [E2_r, E2_g, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g, E2_r],
    [E2_o, E2_r, E2_o, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_o, E2_r, E2_o],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

E1 = openmc.Cell()
E1.fill = assembly_lattice_E1
E1.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

E11 = openmc.Universe()
E11.add_cell(E1)

#E11.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW E2
n_cells = 17
assembly_lattice_E2 = openmc.RectLattice()
assembly_lattice_E2.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_E2.pitch = (pitch, pitch)
assembly_lattice_E2.universes = [
    [E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_g, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_g, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g, W, E2_g, E2_g, E2_b, E2_b, E2_g, E2_b, E2_b, E2_g, E2_g, W, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g_IFBA, E2_g, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_b, E2_b, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_b, E2_b, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_b, E2_b, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_b, E2_b, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g_IFBA, E2_g, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g, E2_r],
    [E2_r, E2_g, E2_g, W, E2_g, E2_g, E2_b, E2_b, E2_g, E2_b, E2_b, E2_g, E2_g, W, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g, E2_g, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_g, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

E2 = openmc.Cell()
E2.fill = assembly_lattice_A
E2.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

E22 = openmc.Universe()
E22.add_cell(E2)

#E22.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)


# KONSTRUKCJA KASETY Z PRETOW E3
n_cells = 17
assembly_lattice_E3 = openmc.RectLattice()
assembly_lattice_E3.lower_left = (-n_cells / 2.0 * pitch, -n_cells / 2.0 * pitch)
assembly_lattice_E3.pitch = (pitch, pitch)
assembly_lattice_E3.universes = [
    [E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_g, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_g, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_b, E2_b, E2_g, E2_b, E2_b, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g_IFBA, E2_g, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, WABA_m, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_b, E2_b, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_b, E2_b, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, WABA_m, E2_g, E2_g, W, E2_g, E2_g, WABA_m, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_b, E2_b, E2_g, E2_y, E2_y, E2_g, E2_y, E2_y, E2_g, E2_b, E2_b, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, WABA_m, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_r],
    [E2_r, E2_g, E2_g_IFBA, E2_g, E2_g, E2_g, E2_b, E2_y, E2_g, E2_y, E2_b, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g, E2_r],
    [E2_r, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_b, E2_b, E2_g, E2_b, E2_b, E2_g, E2_g, WABA_m, E2_g, E2_g, E2_r],
    [E2_r, E2_g, E2_g, E2_g, E2_g_IFBA, W, E2_g, E2_g, W, E2_g, E2_g, W, E2_g_IFBA, E2_g, E2_g, E2_g, E2_r],
    [E2_r, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g, E2_g_IFBA, E2_g_IFBA, E2_g, E2_g, E2_g, E2_g_IFBA, E2_r],
    [E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r, E2_r],
]

assembly_pitch = n_cells * pitch
min_x = openmc.XPlane(x0=-assembly_pitch / 2.0)
max_x = openmc.XPlane(x0=assembly_pitch / 2.0)
min_y = openmc.YPlane(y0=-assembly_pitch / 2.0)
max_y = openmc.YPlane(y0=assembly_pitch / 2.0)

E3 = openmc.Cell()
E3.fill = assembly_lattice_A
E3.region = +min_x & -max_x & +min_y & -max_y & +bot & -top

E33 = openmc.Universe()
E33.add_cell(AA)
#E33.plot(width=(assembly_pitch * 1.2, assembly_pitch * 1.2), origin=(0, 0, 50), color_by='material', colors=colors)


# KONSTRUKCJA KASET Z WODA
cw = openmc.Cell()
cw.fill = h2o
cw.region = +min_x & -max_x & +min_y & -max_y & +bot & -top
uw = openmc.Universe()
uw.add_cell(cw)


 #KONSTRUKCJA REAKTORA Z KASET
n_main_cells = 17
main_lattice = openmc.RectLattice()
main_lattice.lower_left = (-n_main_cells / 2.0 * assembly_pitch,
                           -n_main_cells / 2.0 * assembly_pitch)

main_lattice.pitch = (assembly_pitch, assembly_pitch)
main_lattice.universes = [
    [uw, uw, uw, uw, uw, uw, uw, uw, uw, uw,uw,uw,uw,uw,uw,uw, uw],
    [uw, uw, uw, uw, uw, uw, uw, AAA, CCC, AAA,uw,uw,uw,uw,uw,uw, uw],
    [uw, uw, uw, uw, uw, AAA, CONNN, E11, CONNN_1, E11,CONNN,AAA,uw,uw,uw,uw, uw],
    [uw, uw, uw, uw,CCC, CONNN_1, E11, CONNN, DDD, CONNN,E11,CONNN_1,CCC,uw,uw,uw, uw],
    [uw, uw, uw,CCC,CONNN_1, E11, CONNN, DDD, CONNN_1, DDD, CONNN, E11, CONNN_1, CCC, uw,uw, uw],
    [uw, uw,  AAA, CONNN_1, E11, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, E11, CONNN_1, AAA, uw, uw],
    [uw, uw, CONNN,E11,CONNN,DDD,CONNN_1,DDD,CONNN_1,DDD,CONNN_1,DDD,CONNN,E11,CONNN,uw, uw],
    [uw, AAA, E11, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, E11, AAA, uw],
    [uw, CCC, CONNN_1, DDD, CONNN_1, DDD, CONNN_1, DDD, CONNN, DDD, CONNN_1, DDD, CONNN_1, DDD, CONNN_1, CCC, uw],
    [uw, AAA, E11, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, E11, AAA, uw],
    [uw, uw,  CONNN, E11, CONNN, DDD, CONNN_1, DDD, CONNN_1, DDD, CONNN_1, DDD, CONNN, E11, CONNN, uw, uw],
    [uw, uw,  AAA, CONNN_1, E11, CONNN, DDD, CONNN, DDD, CONNN, DDD, CONNN, E11, CONNN_1, AAA, uw, uw],
    [uw, uw,  uw, CCC, CONNN_1, E11, CONNN, DDD, CONNN_1, DDD, CONNN, E11, CONNN_1, CCC, uw,uw, uw],
    [uw, uw, uw , uw, CCC, CONNN_1, E11, CONNN, DDD, CONNN,E11,CONNN_1,CCC,uw,uw,uw, uw],
    [uw, uw, uw, uw , uw, AAA, CONNN, E11, CONNN_1, E11,CONNN,AAA,uw,uw,uw, uw ,uw],
    [uw, uw, uw, uw, uw, uw, uw, AAA, CCC, AAA, uw, uw, uw, uw, uw, uw, uw],
    [uw, uw, uw, uw, uw, uw, uw, uw, uw,uw,uw,uw,uw,uw,uw, uw, uw],

]

main_pitch = n_main_cells * assembly_pitch
barrel = openmc.ZCylinder(R=(main_pitch - assembly_pitch) / 2.0, boundary_type='reflective')

main_cell = openmc.Cell()
main_cell.fill = main_lattice
main_cell.region = -barrel & +bot & -top

root = openmc.Universe()
root.add_cell(main_cell)

geom = openmc.Geometry()
geom.root_universe = root
geom.export_to_xml()

root.plot(width=(main_pitch, main_pitch), color_by='material', colors=colors)



# SETTINGS
box = openmc.stats.Box((-main_pitch / 3.0, -main_pitch / 3.0, 0),
                       (main_pitch / 3.0, main_pitch / 3.0, 360))

src = openmc.Source(space=box)

settings = openmc.Settings()
settings.source = src
settings.batches = 40
settings.inactive = 8
settings.particles = 10000

settings.export_to_xml()

# MESH
mesh = openmc.Mesh()
n_mesh = 400
mesh.dimension = [n_mesh, n_mesh]
mesh.lower_left = [-main_pitch / 2.0, -main_pitch / 2.0]
mesh.upper_right = [main_pitch / 2.0, main_pitch / 2.0]

mesh_filter = openmc.MeshFilter(mesh)

# REJESTRY
tally = openmc.Tally()
tally.filters = [mesh_filter]
tally.scores = ['flux', 'fission', 'absorption', 'scatter']

tallies = openmc.Tallies()
tallies.append(tally)
tallies.export_to_xml()

# STARTUJEMY
openmc.run()

sp = openmc.StatePoint('statepoint.{}.h5'.format(settings.batches))

result = sp.get_tally(scores=['flux'])
flux = result.get_slice(scores=['flux'])
flux.mean.shape = (n_mesh, n_mesh)

result = sp.get_tally(scores=['fission'])
fission = result.get_slice(scores=['fission'])
fission.mean.shape = (n_mesh, n_mesh)

result = sp.get_tally(scores=['absorption'])
absorption = result.get_slice(scores=['absorption'])
absorption.mean.shape = (n_mesh, n_mesh)

result = sp.get_tally(scores=['scatter'])
scatter = result.get_slice(scores=['scatter'])
scatter.mean.shape = (n_mesh, n_mesh)

import matplotlib.pyplot as plt

plt.figure(1, (9, 6))

ax1 = plt.subplot(2, 2, 1)
ax1.set_title('Flux')
ax1.imshow(flux.mean)

ax2 = plt.subplot(2, 2, 2)
ax2.set_title('Fission')
ax2.imshow(fission.mean)

ax3 = plt.subplot(2, 2, 3)
ax3.set_title('Absorption')
ax3.imshow(absorption.mean)

ax4 = plt.subplot(2, 2, 4)
ax4.set_title('Scatter')
ax4.imshow(scatter.mean)

plt.tight_layout()
plt.show()

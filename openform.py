from string import Template

def build(parsed):
  tmpl = Template('''\
/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | foam-extend: Open Source CFD                    |
|  \\    /   O peration     | Version:     4.0                                |
|   \\  /    A nd           | Web:         http://www.foam-extend.org         |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    location    "system";
    object      transportProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

//mug mug [0 2 -1 0 0 0 0] 0;
//mul mul [0 2 -1 0 0 0 0] 1e-3;
mug mug [1 -1 -1 0 0 0 0] 0;
mul mul [1 -1 -1 0 0 0 0] 2.87e-3;

rhog rhog [ 1 -3  0 0 0 0 0 ] 1;
rhol rhol [ 1 -3  0 0 0 0 0 ] 1000;

sigma sigma [ 1 0 -2 0 0 0 0 ] 0.07;

h0 h0 [ 0 1 0 0 0 0 0] 1e-10;

Omega (0 0 52.36);
Oxyz     (0 0 0);

fCo   0;  //0.0125;

LapSwitch 0.;

//Nozzle initial location
Jxyz0	(0 0 0);

//nozzle velocity magnitude, i.e. the magnitude of velocity at which nozzle moves, do not confuse it with jet velocity
NozzleVel	0.1;

// unit tangential vector of nozzle motion path
NozzleMotionDir		(0.70710678 0.70710678 0);
	
JetR	$JetR;

hFixedVal	$hFixedVal;
UsMagFixedVal	$UsMagFixedVal;

// ************************************************************************* //
''')
  builded = tmpl.substitute(JetR=parsed['JetR'], hFixedVal=parsed['hFixedVal'], UsMagFixedVal=parsed['UsMagFixedVal'])
  return builded

  
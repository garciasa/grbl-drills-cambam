grbl-drills-cambam
==================

<p>Due to G81 gcode  is not supported by grbl, i did the script to convert G81 (produced for Cambam) to movements accepted by grbl to make drills.</p>
Usage:<br />
<code>
convertDrills.py -i inputfile -o outputfile [-m] <br />
<inputfile> File with cambam gcodes <br />
<outputfile> Outfile with drills converted <br />
-m Just mark the hole (the Z-axis just down 0.5mm) <br />
</code>
Example:<br />
<code>
python convertDrills.py -i test.nc -o test_modified.nc -m
</code>
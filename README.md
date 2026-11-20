# DBSproject
Database Systems Homework

The project uses Polynomial Rolling hash.
It takes modulo at each step to prevent the numbers from growing too large.
Since it's not meant for real usage and only used for demonstration, we don't need very advanced
functions that takes more time and space to evenly spread the data across buckets.
Hash function takes the order of the character, and multiplies by a power of 31 depending on its position.
The program first attempts to store the text in corresponding i.txt file. If not possible, it
creates a new file named "i-n.txt", where n is the overflow bucket number. I choose this format
to make it understandable at first glance. The name of the next overflow bucket(if exists) is
written at the top of the page and separated with '\n'. Although earlier version of the program
was using formula to guess the name of next overflow bucket, current version is following file
pointers(first line of the file) to traverse buckets like a linked list. As required, program
writes to the last bucket even if the ones before it may contain adequate space. The program has 
some additional commands like \getfile, \d, \end, \exists to mimic behavior of real DBMS. Empty
strings don't affect flow of the program and the ones too large to fit into one bucket are rejected.
No delimiter is used between stored strings.

command for running: python3 hash_app.py n s

No external libraries are used, only 2 built in modules(argparse, os)

the program does not perform re-hashing when restarted with a different n parameter.
Moreover, the program does not handle the cases of manual intervention(changing file names manually).
Next file pointers are ignored when calculating the number of characters in a bucket.
Characters are counted using python's native len() function, therefore follows python's rules.
The program can be exited by EoF(depends on OS), Ctrl+C(keyboard interruption), or simply by typing \end.
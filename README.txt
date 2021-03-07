"""
The first line in this file is the "shebang" line.  When you execute a file
from the shell, the shell tries to run the file using the command specified
on the shebang line.  The ! is called the "bang".  The # is not called the
"she", so sometimes the "shebang" line is also called the "hashbang".
The hash character is used because it defines a comment in most scripting
languages, so the shebang line will be ignored by the scripting language
by default.
The shebang line was invented because scripts are not compiled, so they are
not executable files, but people still want to "run" them.  The shebang
line specifies exactly how to run a script.  In other words, this shebang
line says that, when I type in ./basics.py, the shell will actuall run
  /usr/bin/env python basics.py
We use
  #!/usr/bin/env python
instead of
  #!/usr/bin/python
because we must specify an absolute path to a program, and /usr/bin/env
is a utility that uses the user's path to run an application (in this
case, python).  Thus, it's more portable.

More on shebang lines, including portability:
http://en.wikipedia.org/wiki/Shebang_(Unix)

If you don't like this basic walk through python, check out
http://docs.python.org/tutorial/
or
http://diveintopython.org/

In order to execute a python script without explicitly running python,
you need to add execute permissions to the file.  To do add execute permission
to basics.py, use
  chmod u+x basics.py

Beware that, while I have programmed in python, I am by no means an expert.
If anything in this file has bad style or is wrong, let me know!
Sam King <samking@cs.stanford.edu>
Made in Spring 2011 for CS1U at Stanford.
http://creativecommons.org/licenses/by/3.0/

This is a multiline string, which can also act as a mutliline comment.
"""

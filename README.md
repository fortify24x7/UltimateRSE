Ultimate Remote Shell Execution
===============================


***About***

URSE Toolkit is a specialized application for launching/executing remote shells and other shell/command based attacks!
URSE's main purpose is to help identify and prove exploitation vulnerabilities within a server or host during a penetration test (URSE & ALL EXPLOITS FOUND/LAUNCHED FROM URSE ARE NOT MADE FOR MALICIOUS USE, I AM NOT RESPONSIBLE FOR YOUR ACTIONS)! 


***Commands***

`show` - Shows variables set by URSE & the user. The command `show` by itself will give you the arguments you can run with it!

`search` - Query's both payloads and exploits for keywords: `search a;b,c d`! Search uses an auto splitting function so feel free to use any regular separation methods will typing in different keywords!

`set` - Sets variables that are used with URSE. Running `show args` will give you a list of variable that can be set!

`exploit|method` - Launches the exploit you have set! Running `show exploits` will give you a list of available exploits to set. To set an exploit run `set exploit #exploit_number` or `set exploit`!

`run|start` - Starts a service or combination service! To get a list of available services run `show servers` or `show combos` for combinations! To run a server in the background run `start server_type -t`! To select a custom port run `start server_type -p #port`[This can be mixed with `-t`]

`close` - Stopped all types of a set service. Usage: `close server_type`, to check if the server is still active run `show active`


***Servers/Services***

The main two services `http` and `socket` are used for shell uploads via local commands such as: `curl` or `wget`! These can also be used in combination with certain exploits `(combos)`! All these servers have dynamic files so you can keep the server threaded and change the payload as needed!


Ultra Edition
=============


***Commands***

`launch` - Executes options for running downloaded exploits.
`Variables:`

	-`launch` on its own will show the downloads you have available

  -`exploit exploit_number <arg> <arg> ....` will launch the exploit witu the args you set!

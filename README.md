# Julia vs Python Speed and Memory Tests

The purpose of this repository is to test the speed and memory allocations of 
python and julia to see if there are any meaningful gains in computation
time and efficiency that can be made by switching tooling from python to julia.

## Developing the code

To run this code in a development enviornment `docker-compose` should be used 
to make sure that versions and dependencies are correct across machines.

To open up an integrated terminal used to test scripts run the following 
shell command:
```bash
sudo docker-compose run dev
```

From here you can edit and modify files while still being able to run the scripts 
from an integrated shell.

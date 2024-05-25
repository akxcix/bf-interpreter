# brainfuck interpreter
barebones poc for a brainfuck interpreter

## running
programs can be run in following way
``` bash
python src/main.py <brainfuck-file> --data-size=<data-size> --print-end=<print-end>
```

### examples
``` bash
$ python3 src/main.py examples/adder.bf
2
2
4
```
``` bash
$ python3 src/main.py examples/helloworld.b --data-size=30000 --print-end=#
72#101#108#108#111#32#87#111#114#108#100#33#10#%                                                             
```

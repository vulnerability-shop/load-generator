# Load Generator

## Usage

### To run:
`python main.py <script file>`

### Example:
`python main.py .\scripts\webgoat_script.txt`

### To stop:
<kbd>Ctrl</kbd> + <kbd>C</kbd>

## Structure

```
load-generator
|  main.py    <- application's entry point
|  worker.py  <- Thread subclass with dynamic module importing
|  signals.py <- global var to stop worker threads
|
+--scripts    <- contains scripts which contain modules to load in a run
|  |  webgoat_script.py
|
+--scenarios  <- modules to run in looping threads
|  |  webgoat_sample.py
|
+--modules    <- resusable modules
|  |  etc.
```

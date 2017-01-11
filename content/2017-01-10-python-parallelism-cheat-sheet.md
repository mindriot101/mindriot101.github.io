title: Python parallelism cheat sheet
date: Tue Jan 10 22:53:24 GMT 2017
category: tech
tags: python
status: draft

I often get asked "how can I parallelise my Python code?". I've come up
with this simple cheat sheet to explain it. I will only explain the most
common method of parallel problems here: _embarassingly parallel problems_.

Throughout, we shall be referring to this code example. It's basic, but
illustrates the procedure:

```python
import numpy as np

a = np.arange(20)
b = np.random.uniform(0, 10, shape=20)
const = 100

results = []
for (avalue, bvalue) in zip(a, b):
    # pretend this computation is much more expensive
    results.append((avalue + bvalue) * const)
print(results)
```

### Step 1

_Find the part to parallelise._

In most of my applications, typically this is a single `for`-loop which
performs lots of work for each iteration. In the code example, it is the
loop over `a` and `b`:

```python
for (avalue, bvalue) in zip(a, b):
    results.append((avalue + bvalue) * const)
```

### Step 2

_Find out what data changes for each iteration of the loop_

Typically the loop iterates over _something_. It may be more than one
value. In the example, it's `avalue` and `bvalue`.

### Step 3

_Find out what data **does not** change for each iteration of the loop_

This data should ideally be read only. In the example it's `const`.

### Step 4

_Convert your loop into a function that takes a single argument of
things that vary, and other parameters of fixed data_

The way `python`'s multiprocessing works, it's generally easiest to use
`multiprocessing.Pool.map`, but this takes a function with a single
argument. We'll sort this out in the next step. **It's extremely important
to make sure your code works as before after this conversion. This is
the source of most errors.**

Applying this process to the example:

```python
import numpy as np


def worker_fn(changing_stuff, const_value):
    '''A function that takes as it's first parameter
    the values that change for each loop iteration, and
    the remaining parameters do not change with each
    loop iteration
    '''
    avalue, bvalue = changing_stuff
    return (avalue + bvalue) * const_value

a = np.arange(20)
b = np.random.uniform(0, 10, shape=20)
const = 100

results = []
for (avalue, bvalue) in zip(a, b):
    # call the new function
    result = worker_fn((avalue, bvalue), const)
    results.append(result)
print(results)
```

### Step 5

_Create a partially applied function_

This is how we get around the single argument problem, we "bake in" the
constant arguments into a new function which takes a single argument:

```python
from functools import partial
import numpy as np


def worker_fn(changing_stuff, const_value):
    '''A function that takes as it's first parameter
    the values that change for each loop iteration, and
    the remaining parameters do not change with each
    loop iteration
    '''
    avalue, bvalue = changing_stuff
    return (avalue + bvalue) * const_value


# ...
const = 100

# this function now takes only a single argument
fn = partial(worker_fn, const_value=const)

# ...
```

### Step 6

Now replace the for loop with the common pool set up:

```python
from functools import partial
from multiprocessing import Pool  # 1
import numpy as np


def worker_fn(changing_stuff, const_value):
    '''A function that takes as it's first parameter
    the values that change for each loop iteration, and
    the remaining parameters do not change with each
    loop iteration
    '''
    avalue, bvalue = changing_stuff
    return (avalue + bvalue) * const_value

a = np.arange(20)
b = np.random.uniform(0, 10, shape=20)
const = 100

fn = partial(worker_fn, const_value=const)

# this must be an `iterable`, so a list or generator
zipped_args = zip(a, b)  # 2

# Python 3
with Pool() as pool:  # 3
    results = pool.map(fn, zipped_args)  # 4

# or if you're stuck with Python 2:
pool = Pool()
results = pool.map(fn, zipped_args)  # 4
```

1. import the `Pool` object, which defaults to one process per cpu
2. create an iterable of your arguments which vary per loop iteration.
   This can either be a list or generator. Look up the [zip][1]
   documentation for more information.
3. Using the `Pool` as a context manager cleans up the processes after
   use
4. We call the `map` function, which applies a function taking one
   argument, to an iterable of things.

With these changes, your code should be parallelised! Of course things
may not be that easy. Here are some common gotchas:

* The biggest problem is with pickling. This is the process of
converting python code to a string, to give to the other processes
running your code. Lots of things can be pickled in Python, but some
important ones that can't are:
    * class instances, so you cannot use an instance method as your
    worker function
    * open files or sockets
    * if you find yourself with tracebacks that contain "pickle" then
    this is your problem
* Exceptions in processes cause wierd behaviour. Newer versions of
Python are better at this than older ones (*cough* python 2 *cough*),
but generally you cannot catch exceptions thrown from other processes.
Make your `worker_fn` bulletproof.
* A consequence of the previous point is that trying to Ctrl-C out of a
parallelised piece of code does not work, because the processes receive
the `KeyboardInterrupt` error, but they do not synchronise and exit
sanely. This is possibly fixed in Python 3.? but I don't quite know.

[1]: https://docs.python.org/3/library/functions.html#zip

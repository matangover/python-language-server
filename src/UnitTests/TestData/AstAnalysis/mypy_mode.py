### Fix 1
def greeting1():
    return 'hi'

b = greeting1()
# Before fix, 'b' is str. After, it's Any.
reveal_type(b) # In mypy it's Any.

### Fix2
def greeting2(name):
    # Before fix, 'name' is str. After, it's Any.
    reveal_type(name) # In mypy it's Any.

c = greeting2('hello')

### Fix3
def greeting3(name):
    # Before fix, 'a' is int. After, it's Any.
    a = 1337
    reveal_type(a) # In mypy it's Any.

def greeting4(name) -> None:
    # After and before fix, 'a' is int.
    a = 1337
    reveal_type(a) # In mypy it's int.

def greeting5(name: str):
    # After and before fix, 'a' is int.
    a = 1337

#### global scope
aa = 1233
reveal_type(aa)
def greeting6():
    reveal_type(aa) # mypy says Any
    # Before fix: aa is int, after fix: any
    # After fix: completion for 'aa.' doesn't work.

def greeting7() -> None:
    # Completion for 'aa.' works.
    reveal_type(aa)
    # Before fix: aa is int, after fix: int
    # After fix: completion for 'aa.' does work.


##### nested funcs
def dynamic():
    foo = 1
    reveal_type(foo)
    def static() -> None:
        bar = 'abc'
        reveal_type(bar)
        def dynamic2():
            baz = 123
            reveal_type(baz)
            blaz = foo
            reveal_type(blaz)
            def static2() -> None:
                beep = bar
                reveal_type(beep)

### Go to definition of undefined variable
bbb = hello()
bbb # Go to definition works only after fix


### Fix: don't scan module if stub available
import os # <-- does not cause huge scan of stdlib - only typeshed stubs
# os. <-- completion from stubs only (no docs unfortunately)

### Fix: Don't scan third party libs if untyped
import pytest # <-- error 'Untyped library import' [when installed, and stubs not installed]
pytest # <-- continues to function as unresolved module

### Fix: Do scan third party lib if has typing info
import coincurve # <--- pip install coincurve coincurve-stubs
coincurve.verify_signature(b'asf', b'asf', b'asf')
# No error, when coincurve-stubs is also installed. Completions are correct.

## TODO:
ccc = hello + 3
# mypy: ccc is any, vscode it's int
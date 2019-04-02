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
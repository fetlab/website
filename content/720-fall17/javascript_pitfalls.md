Title: Javascript Pitfalls and tips
Template: 720

#Javascript Pitfalls and Tips

##Type coercion
Javascript likes to be helpful. That means it wants to put bugs in
your code for you. One example is automatic type coercion: converting
values, if needed, to other types of objects. There are several
examples:

###`[]`
The `[]` operator (to access properties of an object) coerces strings:

```.javascript
> var a = ['hello', 'how', 'are', 'you']
> a[0]
hello
> a['0']
hello
```

###`+`
The `+` operator can add two numbers or concatenate two strings. It
depends on the types of the objects:

```.javascript
> 5 + 6
11
> '5' + '6'
'56'
> 5 + '6'
'56'
```


###Equality
Javascript has two kinds of equality operators: `==` and `===`. The
first kind, `==`, does some really weird stuff related to coercion, so
it's best to avoid it entirely. Always use `===` and, for testing
non-equality, `!==` (rather than `!=`). Read on for more details of
why this is good advice.

The `==` operator is bad because it coerces the values on either
side if they are of different types. For example, it might try to
interpret a string as an integer:

```.javascript
> 0 == '0'
true
```

The `===` operator leaves the types alone:

```.javascript
> 0 === '0'
false
```

##`var`
`var` defines the private variables for a function. For example, put
this into the left-hand window of your [repl.it](http://repl.it)
editor, then click the Run button:

```.javascript
x = "hello";
y = "goodbye";
var testA = function(j)
{
    var x = j;
    y = j;
    console.log("hello, x is ", x);
    console.log("hello, y is ", y);
}

var testB = function()
{
    console.log("hi, x is ", x);
    console.log("hi, y is ", y);
}
```

Now, in the right-hand console, run the two functions and think about
the results:

```.javascript
> testA(5)
hello, x is  5
hello, y is  5
> testB()
hi, x is  hello
hi, y is  5
```

What happened? Because they were declared outside of a function
definition, `x` and `y` are global variables. But when we use `var x`
inside of `testA`, `x` is a local variable for `testA`.

The lesson is to always declare all of your variables at the top of
the function.

##`NaN`
`NaN` (**N**ot **a** **N**umber) is a value that results from some invalid
computation. For example:

```.javascript
> 0/0
NaN
```

`NaN` is not equal to anything else, _including itself_:

```.javascript
> NaN === NaN
false
> NaN !== NaN
true
```

You can check if something is `Nan` with `isNan()`:

```.javascript
> x = NaN
> isNan(x)
true
```

##Truth and falseness
All values evaluate to `true` except for a few "falsy" ones. These
are:

- `false`
- `null`
- `undefined`
- `''` (the empty string)
- `0` (the number zero)
- `NaN`


##Decimals
Fractional numbers can act funny:

```.javascript
> .1 + .2
0.30000000000000004
> .1 + .2 === .3
false
```

##Default values
You can use the _logical or_ (`||`) operator to get default values out
of objects.  This works because Javascript returns `undefined` when
you ask for a property that doesn't exist, and because `undefined` is
a "falsy" value. Therefore:

```.javascript
> 3 || undefined
3
> undefined || 3
3
```

We can use this to get default values:

```.javascript
> options = {size: 'small', color: 'blue'}
> var size = options.size || 'medium'
> size
'small'
> var material = options.material || 'metal'
> material
'metal'
```

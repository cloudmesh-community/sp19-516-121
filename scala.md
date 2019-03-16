# Scala for Cloud Computing :o: :question:

Scala is a multi-paradigm programming language aiming to integrate the features
 of object oriented paradigm with that of functional programing. Scala is a statically typed 
 language. Scala and Java are interoprable in the sense that libraries written
  in either language can be used in Scala or Java.
  
## Language

### Install Scala

On macOS you can use Homebrew as follows:

```bash
brew update
brew install scala
```

For instructions on how to install Scala on other platforms please
vist the Scala website at https://www.scala-lang.org/download/.

### Hello World! in Scala

Open a terminal and run Scala:

```bash
scala
``` 

If Scala is installed on your machine you should get the following message:

```bash
Welcome to Scala 2.12.8 (Java HotSpot(TM) 64-Bit Server VM, Java 11.0.2).
Type in expressions for evaluation. Or try :help.

scala>

```
 
Now you can write and execute codes, for example:

```bash
println("hello world from scala!")
``` 
 
### Scala is object oriented!

#### how to define a class?

Let's define a class callled person:

```python
class Person(var firstName : String, var lastName : String){

override def toString : String = s"$firstName $lastName"

}

val fred = new Person("Fred", "Fredian")
println(fred)
```

Save the above script in a file named LearnTheLanguage.scala and run
the code as the following:
 ```python
scala LearnTheLanguage.scala 
```

The class Person has two fields and one method. The primary construcor is 
in the class signature. A class has one primary constructor (this is the constructor that 
you define in the signature of the class) and any (including none) number of auxiliary constructors.
An auxiliary constructor is defined using the keyword `this`. All auxiliary constructors must start 
with a call to a preceding auxiliary constructor or the primary constructor.

In the class `Person` above, we override the method toString. The method toString is
a method in the class AnyRef. The class AnyRef is the supertype of any refrence type. AnyRef is the 
equivalent of java.lang.Object.

The diagram below (taken from https://docs.scala-lang.org/tour/unified-types.html) shows a subset of 
the type hierarchy:

![A subset of the type hierarchy](images/unified-types-diagram.svg)

The top class `Any` has methods like `hashCode`, `isInstanceOf`, `asInstanceOf` , `toString` and the methods for 
equality (more on the class is availabe at https://www.scala-lang.org/api/2.12.1/scala/Any.html ). The class `AnyVal` does not add any methods. All value types
are derived from `AnyVal`. The class `AnyRef` adds some more methods: `wait`, `notify` and `synchronized` and `eq`. The method `eq` checks whether two refrences refer to the 
same object. If you want to compare two objects of a class by their values, you should override the `equals`. For example for the class `Person` defined 
above we should override `equals` as follows:
```python
final override def equals(other: Any) = {
val otherPerson = other.asInstanceOf[Person]
if (otherPerson == null) false
else firstName == otherPerson.firstName && lastName == otherPerson.lastName
}
```
Note that the method `equals` returns a boolean. In Scala, the type of the last statement in the body a method, is the 
return type of the method. Here we could make it implicit by declaring the return type as follows:
```python
final override def equals(other: Any) : Boolean = {
val otherPerson = other.asInstanceOf[Person]
if (otherPerson == null) false
else firstName == otherPerson.firstName && lastName == otherPerson.lastName
}
```
But Scala has type inferance capability and can infer the types whereever there are enough information for it to infer types.

Members of a class are `public` by default. You can use the access modifier `private` to limit access 
to the members. A `private` member can be accessed only within the class. In the example above, the members
`firstName` and `lastName` are public because they have been defined using `var`. In the primary constructor, any parameter that 
is defined using either `var` or `val` is public. Otherwise it is `private`. `var` indicates that the 
thing to be difined is mutable while `val` indicates that the thing to be defined is immutable.  

In Java we have the concept of `intefaces` where an `interface` contains only the signature of some methods.
`Traits` in Scala are similar to interfaces in Java.
Traits can not be instantiated but classes and objects (an `object` in Scala, which is defined by the kwyword `object` is just a singleton class) can extend traits.

Subtypying in Scala is simialr to that of Java. Let's modify our code and add the entity `Employee` as a subclass of `Person`:

```python
class Person(val firstName : String, val lastName : String){
override def toString : String = s"$firstName $lastName"
}

class Employee(firstName:String, lastName:String, val employeeId : String) extends Person(firstName, lastName){
var salary = 0.0
}

val fred = new Employee("Fred", "Fredian", "410")
println(fred)
```
Note that int the code above the primary constructor of `Employee` is calling the primary constructor of its supertype.
In Scala, only the primary constructor can call a superclass constructor.

Like Java, you can use the keyword `abstract` to define a class that cannot be instantiated.
In an abstract class, you can have methods or members that are not defined (that is, you can define a method without defining its body).


## Cloud computing with AWS Lambda and Scala

## Cloud computing with Spark and Scala

## Cloud computing with Scala and GridGain

 
 
 
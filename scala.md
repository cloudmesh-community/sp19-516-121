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
in the class signature. Here we override the method toString. The method toString is
a method in the class AnyRef. The class AnyRef is the supertype of any refrence type. AnyRef is the 
equivalent of java.lang.Object.

The diagram below (taken from https://docs.scala-lang.org/tour/unified-types.html) shows a subset of 
the type hierarchy:

![A subset of the type hierarchy](images/unified-types-diagram.svg)

The top class Any has methods like hashCode and toString (more on the class is availabe at https://www.scala-lang.org/api/2.12.1/scala/Any.html )
.


## Cloud computing with AWS Lambda and Scala

## Cloud computing with Spark and Scala

## Cloud computing with Scala and GridGain

 
 
 
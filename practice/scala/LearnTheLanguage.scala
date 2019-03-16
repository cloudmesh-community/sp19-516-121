class Person(var firstName : String, var lastName : String){

override def toString : String = s"$firstName $lastName"

}

val fred = new Person("Fred", "Fredian")
println(fred)

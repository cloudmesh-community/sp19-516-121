class Person(val firstName : String, val lastName : String){



override def toString : String = s"$firstName $lastName"
}

class Employee(firstName:String, lastName:String, val employeeId : String) extends Person(firstName, lastName){

var salary = 0.0
}

val fred = new Employee("Fred", "Fredian", "410")
println(fred)

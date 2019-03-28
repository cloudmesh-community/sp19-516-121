
package scala_example

import akka.actor.{Actor, ActorRef, ActorSystem, Props}

object Person {
  def props(name: String): Props = Props(new Person(name))

  case class MoneySent(amount: Double)

  case class MoneyRequested(amount: Double)

}

class Person(name: String) extends Actor {

  import Person._

  def receive = {

    case MoneySent(amount) => {
      println(name + " sent $" + amount)

    }
    case MoneyRequested(amount) => {
      println(name + " requested $" + amount)

    }
  }
}

object Main extends App {

  import Person._

  val system: ActorSystem = ActorSystem("helloAkka")
  val fred: ActorRef = system.actorOf(Person.props("fred"))
  val andi = system.actorOf(Person.props("andi"))
  fred ! new MoneyRequested(100)
  andi ! new MoneySent(100)

}
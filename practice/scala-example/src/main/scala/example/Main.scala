package example

// this example is based on the following tutorial:
// https://docs.scala-lang.org/getting-started-intellij-track/building-a-scala-project-with-intellij-and-sbt.html

object Main extends App{
  val ages = Seq(42, 75, 29, 64)
  println(s"The oldest person is ${ages.max}")

}

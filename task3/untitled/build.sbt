ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "3.3.0"

lazy val root = (project in file("."))
  .settings(
    name := "untitled"
  )

libraryDependencies += "org.apache.kafka" % "kafka-streams" % "3.4.0"
libraryDependencies += "org.apache.kafka" % "kafka-clients" % "3.4.0"
libraryDependencies += "org.apache.kafka" % "kafka-streams-scala_2.13" % "3.4.0"
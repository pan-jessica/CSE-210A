package Calculator

import scala.util.parsing.combinator._

abstract class Val {
  def eval():Double
}

case class Num(n: Double) extends Val {
  def eval():Double = n
}

case class Tail(op: String, v: Val)

case class Bin(op: String, v1: Val, v2: Val) extends Val {
  def eval():Double = op match {
    case "+" => v1.eval() + v2.eval()
    case "-" => v1.eval() - v2.eval()
    case "*" => v1.eval() * v2.eval()
    case "/" => v1.eval() / v2.eval()
  }
}

case class Parentheses(e: Val) extends Val {
  def eval():Double = e.eval()
}

case class Flform(v: Val, rest: List[Tail]) extends Val {
  def eval():Double = rest.foldLeft(v.eval()) {
    (r:Double, rest:Tail) => Bin(rest.op, Num(r), rest.v).eval()
  }
}

class Calculate extends JavaTokenParsers {
  def expr: Parser[Val] =
    term~rep(add_sub) ^^ { case f1~rest => Flform(f1, rest) }

  def term: Parser[Val] =
    factor~rep(mult_div) ^^ { case f1~rest => Flform(f1, rest) }

  def add_sub: Parser[Tail] =
    ("+"|"-")~term ^^ { case op~v => Tail(op, v) }

  def mult_div: Parser[Tail] =
    ("*"|"/")~factor ^^ { case op~v => Tail(op, v) }

  def factor: Parser[Val] = (
    floatingPointNumber ^^ { case n => Num(n.toDouble) }
      | "-"~>floatingPointNumber ^^ { case n => Num(n.toDouble * -1.0) }
      | "("~>expr<~")" ^^ { case e => Parentheses(e) }
    )

  def parse(e: String): Double = {
    parseAll(expr, e).get.eval
  }
}

object basicCalc extends App {
  val start = System.nanoTime
  val parser = new Calculate

  // ADDITION ---------------------------------------------
  if(parser.parse("2+3").round != 5){
    println("ERROR: add-1")
  } else if(parser.parse("3+92").round != 95){
    println("ERROR: add-2")
  } else if(parser.parse("100+0").round != 100){
    println("ERROR: add-3")
  } else if(parser.parse("-1 + -3").round != -4){
    println("ERROR: add-4")
  } else if(parser.parse("10 + -3").round != 7){
    println("ERROR: add-5")
  } else if(parser.parse("-1 + 0").round != -1){
    println("ERROR: add-6")
  } else if(parser.parse("99+3+12+2").round != 116){
    println("ERROR: add-7")
  } else if(parser.parse("2 + 3 + 4 + -1").round != 8){
    println("ERROR: add-8")
  } else if(parser.parse("-1 + -2 + 3").round != 0){
    println("ERROR: add-9")
  } else if(parser.parse("-1 + -5 + -1").round != -7){
    println("ERROR: add-10")
  }
  val add_duration = (System.nanoTime - start) / 1e9d
  println(add_duration + " seconds (ADD)")

  // SUBSTITUTION---------------------------------------------
  if(parser.parse("3-2").round != 1){
    println("ERROR: sub-1")
  } else if(parser.parse("5-3").round != 2){
    println("ERROR: sub-2")
  } else if(parser.parse("40-19").round != 21){
    println("ERROR: sub-3")
  } else if(parser.parse("-1 - 3").round != -4){
    println("ERROR: sub-4")
  } else if(parser.parse("3 - -7").round != 10){
    println("ERROR: sub-5")
  } else if(parser.parse("-19 - -20").round != 1){
    println("ERROR: sub-6")
  } else if(parser.parse("30-16-5").round != 9){
    println("ERROR: sub-7")
  } else if(parser.parse("-1 - -2-3").round != -2){
    println("ERROR: sub-8")
  } else if(parser.parse("100-25-50").round != 25){
    println("ERROR: sub-9")
  } else if(parser.parse("3-0-7").round != -4){
    println("ERROR: sub-10")
  }
  val sub_duration = (System.nanoTime - add_duration - start) / 1e9d
  println(sub_duration + " seconds (SUB)")

  // MULTIPLICATION ---------------------------------------------
  if(parser.parse("9*3").round != 27){
    println("ERROR: mult-1")
  } else if(parser.parse("-3*4").round != -12){
    println("ERROR: mult-2")
  } else if(parser.parse("0*2").round != 0){
    println("ERROR: mult-3")
  } else if(parser.parse("20*5").round != 100){
    println("ERROR: mult-4")
  } else if(parser.parse("0*2*5").round != 0){
    println("ERROR: mult-5")
  } else if(parser.parse("-2*-0").round != 0){
    println("ERROR: mult-6")
  } else if(parser.parse("2*3*4*1000").round != 24000){
    println("ERROR: mult-7")
  } else if(parser.parse("1*-2*3*-4").round != 24){
    println("ERROR: mult-8")
  } else if(parser.parse("9*2*99*999").round != 1780218){
    println("ERROR: mult-9")
  } else if(parser.parse("1*1*-1*1").round != -1){
    println("ERROR: mult-10")
  }
  val mult_duration = (System.nanoTime - sub_duration - add_duration - start) / 1e9d
  println(mult_duration + " seconds (MULT)")

  // DIVISION ---------------------------------------------
  if(parser.parse("9/3").round != 3){
    println("ERROR: div-1")
  } else if(parser.parse("-12/4").round != -3){
    println("ERROR: div-2")
  } else if(parser.parse("0/2").round != 0){
    println("ERROR: div-3")
  } else if(parser.parse("100/5").round != 20){
    println("ERROR: div-4")
  } else if(parser.parse("50/2").round != 25){
    println("ERROR: div-5")
  } else if(parser.parse("-0/-2").round != 0){
    println("ERROR: div-6")
  } else if(parser.parse("100/5/4").round != 5){
    println("ERROR: div-7")
  } else if(parser.parse("10/-2/5").round != -1){
    println("ERROR: div-8")
  } else if(parser.parse("1780218/9/99/999").round != 2){
    println("ERROR: div-9")
  } else if(parser.parse("1/1/-1/1").round != -1){
    println("ERROR: div-10")
  }
  val div_duration = (System.nanoTime - mult_duration - sub_duration - add_duration - start) / 1e9d
  println(div_duration + " seconds (DIV)")

  // PARENALL ---------------------------------------------
  if(parser.parse("( 8 - 2 ) * 5").round != 30){
    println("ERROR: div-1")
  } else if(parser.parse("( 2 + 9 ) * 9").round != 99){
    println("ERROR: div-2")
  } else if(parser.parse("5 * ( 4 - 3 )").round != 5){
    println("ERROR: div-3")
  } else if(parser.parse("( 5 + 5 ) / 5").round != 2){
    println("ERROR: div-4")
  } else if(parser.parse("( 7 + 9 - 6 ) * 5").round != 50){
    println("ERROR: div-5")
  } else if(parser.parse("( 1 + 4 ) * 2").round != 10){
    println("ERROR: div-6")
  } else if(parser.parse("( -12 - 4 ) / 4").round != -4){
    println("ERROR: div-7")
  } else if(parser.parse("( 4 - 9 ) + 2").round != -3){
    println("ERROR: div-8")
  } else if(parser.parse("( 4 * 3 ) - 2 / 2").round != 11){
    println("ERROR: div-9")
  } else if(parser.parse("( 49 - 3 ) * 2").round != 92){
    println("ERROR: div-10")
  }
  val parenall_duration = (System.nanoTime - div_duration - mult_duration - sub_duration - add_duration - start) / 1e9d
  println(parenall_duration + " seconds (PARENALL)")

  val total_duration = (System.nanoTime - start) / 1e9d
  println(total_duration + " seconds (TOTAL)")

}
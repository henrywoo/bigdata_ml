package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
    * Exercise 1
    */
  def pascal(c: Int, r: Int): Int = {
    if (c == 0 || c == r || r == 0) return 1
    pascal(c, r - 1) + pascal(c - 1, r - 1)
  }

  /**
    * Exercise 2
    */
  def balance(chars: List[Char]): Boolean = {
    def f(c: List[Char], n: Int): Boolean = {
      if (c.isEmpty)
        n == 0
      else {
        val h = c.head
        val m =
          if (h == '(') n + 1
          else if (h == ')') n - 1
          else n
        if (m >= 0) f(c.tail, m)
        else false
      }
    }

    f(chars, 0)
  }

  /**
    * Exercise 3
    */
  def countChange(money: Int, coins: List[Int]): Int = {
    def count(m: Int, c: List[Int]): Int = {
      if (c.isEmpty) 0
      else if (m - c.head == 0) 1
      else if (m - c.head < 0) 0
      else countChange(m - c.head, c) + countChange(m, c.tail)
    }

    count(money, coins.sorted)
  }

}

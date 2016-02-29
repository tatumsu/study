module Operator
  def add(a, b)
    return a + b
  end
end

class Calculator
  include Operator
end

c = Calculator.new
puts c.add(100, 234)

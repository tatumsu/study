module Operator
  def add(a, b)
    return a + b
  end

  def substract(a, b)
    return a - b
  end

  def multiple(a, b)
    return a * b
  end

  def divide(a, b)
    return a/b
  end

  module_function :add
end

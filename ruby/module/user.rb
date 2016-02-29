require './operator'
class User
  attr_accessor :name, :age, :email, :salary

  include Comparable 
  
  def initialize(name, age, email, salary)
    #puts self.to_s
    @name = name
    @age = age
    @email = email
    @salary = salary
  end

  def >= (other)
    @age <=> other.age
  end

  def to_s
    puts "User.to_s is invokded"
    return "Name=#{name}, Age=#{age}, Email=#{email}, Salary=#{salary}"
  end
end


tatum = User.new("tatum", 35, "tatum.su@augmentum.com", 24000)
aaron = User.new("aaron", 31, "aaron.zhang@microsoft.com", 25000)
puts tatum
puts aaron

p "tatum > aaron = #{tatum > aaron}"

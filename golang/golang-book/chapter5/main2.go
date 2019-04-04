package main 

import "fmt"

func main() {
	for i := 1; i <= 100; i++ {
		if i % 15 == 0 {
			fmt.Println("FizzBuzz")
		} else if i % 3 == 0 {
			fmt.Println("Fizz")
		} else if i % 5 == 0 {
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}

// This program prints Fizz for numbers divisible by 3 and Buzz for numbers divisible by 5, while printing the number for ones that are neither.

// I cannot figure out how to print FizzBuzz for numbers divisible by both 3 and 5. But need to include that. 

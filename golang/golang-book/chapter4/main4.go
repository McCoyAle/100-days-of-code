package main 

import "fmt"

// Convert Farenheit to CelciusC = (F-32) * 5/9

func main() {
	fmt.Println("Enter Farenheit degrees: ")
	var input float64
	fmt.Scanf("%f", &input)

	output := (input - 32) * 5/9

	fmt.Println(output)
}

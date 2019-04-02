package main 

import "fmt"

// Convert feet into meters = 1 ft = 0.3048 meters

func main() {
	fmt.Println("Enter measurement in feet: ")
	var feet float64
	fmt.Scanf("%f", &feet)

	output := feet * 0.3048

	fmt.Println(output)
}

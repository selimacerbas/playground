package main

import (
	"fmt"
	"sync"
)

func printSomething(s string, wg *sync.WaitGroup) {
	defer wg.Done() // This will actually simply decerement the operation execution by one.
	fmt.Println(s)
}
func main() {
	var wg sync.WaitGroup

	words := []string{
		"alpha",
		"beta",
		"delta",
		"gemma",
		"pi",
		"zeta",
		"eta",
		"theta",
		"epsilon",
	}

	wg.Add(9) // Which says add 9 opreation to be done.

	for i, x := range words {
		go printSomething(fmt.Sprintf("%d: %s", i, x), &wg)
	}
	wg.Wait()

	wg.Add(1)
	printSomething("Working too!", &wg)

}

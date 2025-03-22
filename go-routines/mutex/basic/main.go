package main

import (
	"fmt"
	"sync"
)

var msg string
var wg sync.WaitGroup

func UpdateMessage(s string, m *sync.Mutex) {
	defer wg.Done()

	m.Lock() // It locks the mutex so incoming other go routines will wait until it is opened.
	msg = s
	m.Unlock() // We are accesing data safely. There is no more Race condition.

}

func main() {
	msg = "Hello, world!"

	var mutex sync.Mutex

	wg.Add(2)
	go UpdateMessage("Hello, universe!", &mutex)
	go UpdateMessage("Hello, cosmos!", &mutex)
	wg.Wait()

	fmt.Println(msg)
}

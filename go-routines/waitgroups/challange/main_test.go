package main

import (
	"io"
	"os"
	"strings"
	"sync"
	"testing"
)

func TestPrintSomething(t *testing.T) {

	stdOut := os.Stdout

	r, w, _ := os.Pipe()
	os.Stdout = w

	var wg sync.WaitGroup

	wg.Add(2)
	go updateMessage("test", &wg)
	go printMessage(&wg)
	wg.Wait()

	_ = w.Close()

	result, _ := io.ReadAll(r)
	output := string(result)

	os.Stdout = stdOut

	if !strings.Contains(output, "test") {
		t.Errorf("Expected to find 'test', but it is not there")
	}
}

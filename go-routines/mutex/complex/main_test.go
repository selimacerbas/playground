package main

import (
	"io"
	"os"
	"strings"
	"testing"
)

func Test_main(t *testing.T) {
	stdOut := os.Stdout
	r, w, _ := os.Pipe()

	os.Stdout = w

	main()

	_ = w.Close()

	result, _ := io.ReadAll(r)
	outout := string(result)

	os.Stdout = stdOut

	if !strings.Contains(outout, "$34320.00") {
		t.Error("wrong balance returned")
	}

}

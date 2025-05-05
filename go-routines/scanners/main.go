package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("Enter multiple lines of text. Type 'END' to finish:")

	scanner := bufio.NewScanner(os.Stdin)
	var builder strings.Builder

	for scanner.Scan() {
		line := scanner.Text()
		if line == "END" {
			break
		}
		builder.WriteString(line)
		builder.WriteString("\n")
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input: %v\n", err)
		return
	}

	finalText := builder.String()
	fmt.Println("\nCollected Input:")
	fmt.Println(finalText)
}

package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

func main() {
	var s, sep string
	start := time.Now()
	sep = " "
	s += strings.Join(os.Args[1:], sep)
	fmt.Println(s)
	fmt.Printf("%.8fs elapsed\n", time.Since(start).Seconds())
}

package main

import (
	"cmp"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

func MustAtoi(str string) int {
	i, err := strconv.Atoi(str)
	if err != nil {
		log.Print(err)
		log.Fatalln("failed to convert string to int")
	}
	return i
}

func main() {
	// read and parse input
	stdin, err := io.ReadAll(os.Stdin)
	if err != nil {
		log.Fatal("failed to read input", err)
	}
	input := string(stdin)
	input = strings.TrimSuffix(input, "\n")
	lines := strings.Split(input, "\n")

	reports := make([][]int, len(lines))

	for j, line := range lines {
		levelsStr := strings.Split(line, " ")
		levels := make([]int, len(levelsStr))
		for i, el := range levelsStr {
			levels[i] = MustAtoi(el)
		}
		reports[j] = levels
	}

	safeReportCount(reports)
}

func safeReportCount(reports [][]int) {
	count := 0

	for _, report := range reports {
		if safeReport(report) {
			count += 1
		}
	}
	log.Print("safe reports count:", count)
}

func safeReport(report []int) bool {
	var goesUpOrDown int = cmp.Compare(report[1], report[0])
	var diff int = abs(report[1] - report[0])

	// diff should belong to [1,3]
	if goesUpOrDown == 0 || diff < 1 || diff > 3 {
		return false
	}

	for i := 2; i < len(report); i++ {
		diff = abs(report[i] - report[i-1])
		if cmp.Compare(report[i], report[i-1]) != goesUpOrDown || diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}
